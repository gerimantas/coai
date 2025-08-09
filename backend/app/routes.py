from flask import Blueprint, jsonify, request, abort
import os
import logging
from datetime import datetime
from .orchestrator import orchestrator
from .logger import coai_logger

bp = Blueprint("main", __name__)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@bp.route("/")
def index():
    return jsonify({"message": "Hello from COAI backend!", "version": "1.0.0"})

@bp.route("/status")
def status():
    """Enhanced status with orchestrator information"""
    orchestrator_status = orchestrator.get_orchestrator_status()
    return jsonify({
        "status": "ok", 
        "info": "COAI Backend is running with full orchestration.", 
        "orchestrator": orchestrator_status
    })


# --- Main chat endpoint using orchestrator ---
@bp.route("/api/chat", methods=["POST"])
def chat():
    """
    Main chat endpoint that uses the orchestrator for full request processing
    """
    try:
        data = request.get_json()
        message = data.get("message", "")
        project = data.get("project", "demo-project")
        file = data.get("file", "main.py")
        
        # Validate input
        if not message or not message.strip():
            return jsonify({"error": "Message cannot be empty"}), 400
        
        # Prepare context
        context = {
            "project": project,
            "file": file,
            "timestamp": datetime.now().isoformat(),
            "user_message": message,
            "endpoint": "/api/chat"
        }
        
        # Use orchestrator for full processing
        logger.info(f"Processing chat request through orchestrator - Project: {project}, File: {file}")
        response = orchestrator.process_chat_request(message, context)
        
        # Check if orchestrator returned an error
        if response.get("error"):
            return jsonify(response), 500
        
        # Log successful processing
        logger.info(f"Chat request {response.get('request_id')} completed successfully")
        
        return jsonify(response)
        
    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        return jsonify({
            "error": True,
            "message": "Internal server error",
            "details": str(e),
            "status": "endpoint_error"
        }), 500


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
    # Only allow reading files inside the project directory
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    file_path = os.path.abspath(os.path.join(base_dir, filename))
    if not file_path.startswith(base_dir):
        abort(403, description="Forbidden: invalid path")
    if not os.path.isfile(file_path):
        abort(404, description="File not found")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return jsonify({"filename": filename, "content": content})
    except Exception as e:
        abort(500, description=str(e))
@bp.route("/api/orchestrator/status", methods=["GET"])
def orchestrator_status():
    """Get detailed orchestrator status"""
    try:
        status_data = orchestrator.get_orchestrator_status()
        return jsonify(status_data)
    except Exception as e:
        logger.error(f"Error getting orchestrator status: {str(e)}")
        return jsonify({"error": "Failed to get orchestrator status"}), 500
