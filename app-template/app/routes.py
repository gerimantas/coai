from flask import Blueprint, jsonify

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return jsonify({"message": "Hello from the backend template!"})

@bp.route("/status")
def status():
    return jsonify({"status": "ok", "info": "Backend is running."})

# Example placeholder endpoints for future extension:
# @bp.route("/commands")
# def commands():
#     return jsonify({"commands": []})

# @bp.route("/server")
# def server_control():
#     return jsonify({"server": "control endpoint"})

# @bp.route("/git")
# def git_actions():
#     return jsonify({"git": "actions endpoint"})
