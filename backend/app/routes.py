from flask import Blueprint, jsonify, request, abort, send_file
import os
import logging
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from app.progress_tracker import ProgressTracker
from app.orchestrator import COAIOrchestrator
from app.action_planner import ActionPlanner, TaskStatus, TaskPriority
from app.security_middleware import rate_limit, validate_security, cache_response

bp = Blueprint("app", __name__)

progress_tracker = ProgressTracker()
action_planner = ActionPlanner()

@bp.route("/api/debug/file-context", methods=["POST"])
def debug_file_context():
    """Debug endpoint to test file context functionality"""
    data = request.get_json() or {}
    message = data.get("message", "What files are in this project?")
    project = data.get("project", "demo-project")
    
    try:
        # Test file context manager directly
        from app.file_context_manager import file_context_manager
        should_include = file_context_manager.should_include_file_context(message)
        file_data = file_context_manager.get_project_file_listing(project)
        formatted = file_context_manager.format_file_context_for_ai(file_data)
        
        # Test preprocessor
        from app.preprocessor import preprocessor
        context = {"project": project, "file": "main.py"}
        processed = preprocessor.process_prompt(message, context)
        
        return jsonify({
            "message": message,
            "should_include_file_context": should_include,
            "file_data_status": file_data["status"],
            "total_files": file_data["file_summary"]["total_files"],
            "formatted_preview": formatted[:500],
            "enhanced_prompt_length": len(processed["enhanced_prompt"]),
            "has_file_info": "PROJECT FILE INFORMATION" in processed["enhanced_prompt"],
            "enhanced_prompt_preview": processed["enhanced_prompt"][:800]
        })
    except Exception as e:
        return jsonify({"error": str(e), "traceback": str(e.__traceback__)})

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
@rate_limit(limit=50, window=3600)  # 50 requests per hour
@validate_security()
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
@rate_limit(limit=10, window=3600)  # 10 rules reloads per hour
@validate_security()
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

# --- Usage Analytics Endpoints ---

@bp.route("/api/usage/summary", methods=["GET"])
def get_usage_summary():
    """Get daily usage summary"""
    try:
        from app.usage_tracker import usage_tracker
        
        # Get date from query params or use today
        target_date = request.args.get('date')
        summary = usage_tracker.get_daily_summary(target_date)
        
        if summary:
            return jsonify({
                "success": True,
                "summary": summary.__dict__
            })
        else:
            return jsonify({
                "success": False,
                "message": "No data available for the specified date"
            }), 404
            
    except Exception as e:
        logger.error(f"Error getting usage summary: {str(e)}")
        return jsonify({"error": "Failed to get usage summary"}), 500

@bp.route("/api/usage/stats", methods=["GET"])
@cache_response(ttl=60)  # Cache for 1 minute
@rate_limit(limit=200, window=3600)  # Higher limit for read operations
def get_usage_stats():
    """Get usage statistics for the last N days"""
    try:
        from app.usage_tracker import usage_tracker
        
        days = request.args.get('days', 7, type=int)
        if days < 1 or days > 90:  # Reasonable limits
            return jsonify({"error": "Days must be between 1 and 90"}), 400
        
        stats = usage_tracker.get_usage_stats(days)
        return jsonify({
            "success": True,
            "stats": stats
        })
        
    except Exception as e:
        logger.error(f"Error getting usage stats: {str(e)}")
        return jsonify({"error": "Failed to get usage stats"}), 500

@bp.route("/api/usage/export", methods=["POST"])
def export_usage_data():
    """Export usage data for a date range"""
    try:
        from app.usage_tracker import usage_tracker
        
        data = request.get_json()
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        format_type = data.get('format', 'json')
        
        if not start_date or not end_date:
            return jsonify({"error": "start_date and end_date are required"}), 400
        
        if format_type not in ['json', 'csv']:
            return jsonify({"error": "format must be 'json' or 'csv'"}), 400
        
        export_path = usage_tracker.export_usage_data(start_date, end_date, format_type)
        
        return jsonify({
            "success": True,
            "export_path": export_path,
            "download_url": f"/api/usage/download/{os.path.basename(export_path)}"
        })
        
    except Exception as e:
        logger.error(f"Error exporting usage data: {str(e)}")
        return jsonify({"error": "Failed to export usage data"}), 500

@bp.route("/api/usage/download/<filename>", methods=["GET"])
def download_usage_file(filename):
    """Download exported usage file"""
    try:
        from app.usage_tracker import usage_tracker
        
        file_path = usage_tracker.usage_dir / filename
        
        if not file_path.exists():
            return jsonify({"error": "File not found"}), 404
        
        # Security check - ensure file is in usage directory
        if not str(file_path).startswith(str(usage_tracker.usage_dir)):
            return jsonify({"error": "Access denied"}), 403
        
        return send_file(file_path, as_attachment=True)
        
    except Exception as e:
        logger.error(f"Error downloading usage file: {str(e)}")
        return jsonify({"error": "Failed to download file"}), 500

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

# Action Plan Endpoints

@bp.route('/api/plans', methods=['POST'])
def create_action_plan():
    """Generate a new action plan from user request"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        user_request = data.get('request', '').strip()
        if not user_request:
            return jsonify({"error": "Request text is required"}), 400
        
        project_context = data.get('project_context', {})
        
        # Generate action plan
        plan = action_planner.generate_plan(user_request, project_context)
        
        return jsonify({
            "success": True,
            "plan": {
                "id": plan.id,
                "title": plan.title,
                "description": plan.description,
                "total_tasks": len(plan.tasks),
                "estimated_time": plan.total_estimated_time,
                "tasks": [
                    {
                        "id": task.id,
                        "title": task.title,
                        "description": task.description,
                        "status": task.status.value,
                        "priority": task.priority.value,
                        "estimated_time": task.estimated_time,
                        "tags": task.tags
                    }
                    for task in plan.tasks
                ]
            }
        })
        
    except Exception as e:
        logger.error(f"Error creating action plan: {str(e)}")
        return jsonify({"error": "Failed to create action plan"}), 500

@bp.route('/api/plans', methods=['GET'])
@cache_response(ttl=120)  # Cache for 2 minutes
@rate_limit(limit=200, window=3600)
def list_action_plans():
    """List all action plans, optionally filtered by project"""
    try:
        project_path = request.args.get('project_path')
        plans = action_planner.list_plans(project_path)
        
        return jsonify({
            "success": True,
            "plans": plans
        })
        
    except Exception as e:
        logger.error(f"Error listing action plans: {str(e)}")
        return jsonify({"error": "Failed to list action plans"}), 500

@bp.route('/api/plans/<plan_id>', methods=['GET'])
def get_action_plan(plan_id):
    """Get detailed information about a specific action plan"""
    try:
        plan = action_planner.load_plan(plan_id)
        if not plan:
            return jsonify({"error": "Plan not found"}), 404
        
        return jsonify({
            "success": True,
            "plan": {
                "id": plan.id,
                "title": plan.title,
                "description": plan.description,
                "created_at": plan.created_at,
                "updated_at": plan.updated_at,
                "completion_percentage": plan.completion_percentage,
                "total_estimated_time": plan.total_estimated_time,
                "tasks": [
                    {
                        "id": task.id,
                        "title": task.title,
                        "description": task.description,
                        "status": task.status.value,
                        "priority": task.priority.value,
                        "estimated_time": task.estimated_time,
                        "dependencies": task.dependencies,
                        "tags": task.tags,
                        "created_at": task.created_at,
                        "completed_at": task.completed_at
                    }
                    for task in plan.tasks
                ]
            }
        })
        
    except Exception as e:
        logger.error(f"Error getting action plan: {str(e)}")
        return jsonify({"error": "Failed to get action plan"}), 500

@bp.route('/api/plans/<plan_id>/progress', methods=['GET'])
def get_plan_progress(plan_id):
    """Get progress information for a specific plan"""
    try:
        progress = action_planner.get_plan_progress(plan_id)
        if not progress:
            return jsonify({"error": "Plan not found"}), 404
        
        return jsonify({
            "success": True,
            "progress": progress
        })
        
    except Exception as e:
        logger.error(f"Error getting plan progress: {str(e)}")
        return jsonify({"error": "Failed to get plan progress"}), 500

@bp.route('/api/plans/<plan_id>/tasks/<task_id>/status', methods=['PUT'])
def update_task_status(plan_id, task_id):
    """Update the status of a specific task"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        new_status = data.get('status')
        if not new_status:
            return jsonify({"error": "Status is required"}), 400
        
        try:
            status_enum = TaskStatus(new_status)
        except ValueError:
            return jsonify({"error": "Invalid status value"}), 400
        
        success = action_planner.update_task_status(plan_id, task_id, status_enum)
        if not success:
            return jsonify({"error": "Plan or task not found"}), 404
        
        return jsonify({
            "success": True,
            "message": "Task status updated successfully"
        })
        
    except Exception as e:
        logger.error(f"Error updating task status: {str(e)}")
        return jsonify({"error": "Failed to update task status"}), 500
