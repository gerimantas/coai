from flask import Blueprint, jsonify, request, abort
import os
import logging
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from app.progress_tracker import ProgressTracker
from app.orchestrator import COAIOrchestrator

bp = Blueprint("app", __name__)

progress_tracker = ProgressTracker()

@bp.route('/')
def index():
    return 'COAI backend is running'

# Initialize the real orchestrator
logger = logging.getLogger("coai")

# Initialize orchestrator with fallback to stub if there are issues
try:
    orchestrator = COAIOrchestrator()
    logger.info("Real COAI Orchestrator initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize COAI Orchestrator: {e}")
    logger.info("Falling back to Orchestrator Stub")
    
    class OrchestratorStub:
        def process_chat_request(self, message, context):
            if len(message) > 10000:
                return {
                    "error": "Message too long (max 10000 characters)",
                    "status": "orchestrator_error"
                }
            return {
                "request_id": "stub",
                "reply": f"Echo: {message}",
                "original_message": message,
                "context": context,
                "metadata": {},
                "status": "completed",
                "error": False,
                "debug": {"stub": True}
            }
        def get_orchestrator_status(self):
            return {
                "orchestrator_status": "stub",
                "components": {"preprocessor": "ready", "logger": "ready", "ai_agents": "ready"},
                "version": "stub",
                "capabilities": ["chat_request_processing", "prompt_preprocessing", "request_logging", "ai_agent_integration"]
            }
    orchestrator = OrchestratorStub()
class CoaiLoggerStub:
    def get_chat_history(self, limit):
        return []
coai_logger = CoaiLoggerStub()

from app.rules_loader import load_agent_rules, RULES_PATH
from app.error_handler import (
    handle_api_errors, validate_chat_request, create_error_response,
    AIAgentError, ValidationError, log_error
)
import threading
rules_lock = threading.Lock()
current_agent_rules = load_agent_rules()

# --- Main chat endpoint using orchestrator ---
@bp.route("/api/chat", methods=["POST"])
@handle_api_errors
def chat():
    """
    Main chat endpoint that uses the orchestrator for full request processing
    Enhanced with comprehensive error handling
    """
    data = request.get_json()
    
    # Validate request data
    validate_chat_request(data)
    
    message = data.get("message", "").strip()
    project = data.get("project", "demo-project")
    file = data.get("file", "main.py")
    
    # Prepare context
    context = {
        "project": project,
        "file": file,
        "timestamp": datetime.now().isoformat(),
        "user_message": message,
        "endpoint": "/api/chat",
        "request_id": f"chat_{int(datetime.now().timestamp())}"
    }
    
    try:
        # Use orchestrator for full processing
        logger.info(f"Processing chat request through orchestrator - Project: {project}, File: {file}")
        
        # Inject current rules into context
        with rules_lock:
            context["global_rules"] = current_agent_rules.get('global', [])
            context["agent_rules"] = current_agent_rules.get('agents', {})
        
        response = orchestrator.process_chat_request(message, context)
        
        # Check if orchestrator returned an error
        if response.get("error"):
            # Convert orchestrator error to AI agent error for consistent handling
            raise AIAgentError(
                response.get("message", "Orchestrator processing failed"),
                agent_type=response.get("agent_type", "unknown")
            )
        
        # Log successful processing
        logger.info(f"Chat request {response.get('request_id')} completed successfully")
        
        return jsonify(response)
    
    except (AIAgentError, ValidationError):
        # These will be handled by the @handle_api_errors decorator
        raise
    except Exception as e:
        # Log unexpected errors and convert to AI agent error
        log_error(e, context)
        raise AIAgentError(f"Unexpected error during chat processing: {str(e)}")


    # --- Dynamic rules reload endpoint ---

# --- Dynamic rules reload endpoint ---
@bp.route("/api/rules/reload", methods=["POST"])
def reload_agent_rules():
    """Reload agent rules from file and update in memory (no restart)"""
    global current_agent_rules
    try:
        with rules_lock:
            current_agent_rules = load_agent_rules()
        logger.info("Agent rules reloaded dynamically.")
        return jsonify({"success": True, "message": "Agent rules reloaded."})
    except Exception as e:
        logger.error(f"Failed to reload agent rules: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500


# --- Chat history endpoint ---
@bp.route("/api/chat/history", methods=["GET"])
def chat_history():
    """Get chat history from logger"""
    try:
        limit = request.args.get("limit", 50, type=int)
        history = coai_logger.get_chat_history(limit)
        return jsonify({"history": history, "count": len(history)})
    except Exception as e:
        logger.error(f"Error getting chat history: {str(e)}")
        return jsonify({"error": "Failed to get chat history"}), 500


# --- Orchestrator status endpoint ---

# --- File system access endpoint ---

@bp.route("/api/files/list", methods=["GET"])
def list_files():
    """Return a tree structure of files and folders in C:\ai_projects, lazy loading by path param"""
    base_dir = os.path.abspath("C:/ai_projects")
    rel_path = request.args.get("path", "")
    abs_path = os.path.abspath(os.path.join(base_dir, rel_path))
    # Saugumo patikra: turi būti C:/ai_projects viduje
    if not abs_path.startswith(base_dir):
        return jsonify({"error": "Forbidden"}), 403

    def build_tree(path):
        name = os.path.basename(path)
        if os.path.isdir(path):
            if name.startswith('.'):
                return None
            children = []
            for entry in sorted(os.listdir(path)):
                if entry.startswith('.'):
                    continue
                child_path = os.path.join(path, entry)
                if os.path.isdir(child_path):
                    children.append({"name": entry, "type": "dir"})
                else:
                    children.append({"name": entry, "type": "file", "path": os.path.relpath(child_path, base_dir)})
            return {"name": name, "type": "dir", "children": children, "path": os.path.relpath(path, base_dir)}
        else:
            if name.startswith('.'):
                return None
            rel_path = os.path.relpath(path, base_dir)
            return {"name": name, "type": "file", "path": rel_path}

    tree = build_tree(abs_path)
    # Jei ne root, grąžinti tik children masyvą
    if rel_path and tree and tree.get("children"):
        return jsonify({"children": tree["children"]})
    else:
        return jsonify({"tree": tree})
@bp.route("/api/files/<path:filename>", methods=["GET"])
def get_file(filename):
    """Safely read a file from the project directory (read-only)"""
    # Saugumo patikra
    if '..' in filename or filename.startswith('/'):
        return jsonify({'error': 'Neleistinas kelias'}), 400
    # Workspace root (vienas lygis aukščiau nei backend)
    workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    # Failo kelias turi būti reliatyvus workspace root
    file_path = os.path.abspath(os.path.join(workspace_root, filename))
    if not file_path.startswith(workspace_root):
        return jsonify({'error': 'Neleistinas kelias'}), 400
    if not os.path.isfile(file_path):
        return jsonify({'error': 'Failas nerastas'}), 404
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return jsonify({'content': content})
    except Exception:
        return jsonify({'error': 'Nepavyko perskaityti failo'}), 500
@bp.route("/api/orchestrator/status", methods=["GET"])
def orchestrator_status():
    """Get detailed orchestrator status"""
    try:
        status_data = orchestrator.get_orchestrator_status()
        return jsonify(status_data)
    except Exception as e:
        logger.error(f"Error getting orchestrator status: {str(e)}")
        return jsonify({"error": "Failed to get orchestrator status"}), 500

@bp.route("/api/health", methods=["GET"])
def health_check():
    """System health check endpoint"""
    try:
        from app.error_handler import check_system_health
        health_data = check_system_health()
        
        # Add orchestrator status
        try:
            orch_status = orchestrator.get_orchestrator_status()
            health_data["orchestrator"] = {
                "status": orch_status.get("orchestrator_status", "unknown"),
                "components": orch_status.get("components", {})
            }
        except:
            health_data["orchestrator"] = {"status": "error"}
        
        # Set HTTP status based on health
        http_status = 200
        if health_data["status"] == "unhealthy":
            http_status = 503
        elif health_data["status"] == "degraded":
            http_status = 200  # Still operational
        
        return jsonify(health_data), http_status
        
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }), 503

@bp.route('/api/progress/<task_id>', methods=['GET'])
def get_progress(task_id):
    status = progress_tracker.get_progress(task_id)
    return jsonify({"task_id": task_id, "status": status})

@bp.route('/api/progress/<task_id>', methods=['POST'])
def set_progress(task_id):
    data = request.get_json()
    status = data.get("status")
    if not status:
        abort(400, "Missing status")
    progress_tracker.set_progress(task_id, status)
    return jsonify({"task_id": task_id, "status": status})

@bp.route('/api/progress', methods=['GET'])
def get_all_progress():
    return jsonify(progress_tracker.get_all_progress())
