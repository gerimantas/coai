from flask import Blueprint, jsonify, request
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
@bp.route("/api/orchestrator/status", methods=["GET"])
def orchestrator_status():
    """Get detailed orchestrator status"""
    try:
        status_data = orchestrator.get_orchestrator_status()
        return jsonify(status_data)
    except Exception as e:
        logger.error(f"Error getting orchestrator status: {str(e)}")
        return jsonify({"error": "Failed to get orchestrator status"}), 500
