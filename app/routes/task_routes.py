from flask import Blueprint, request , jsonify, abort 

task_bp = Blueprint("tasks", __name__, url_prefix="/tasks")

@task_bp.route("", methods=["GET"])
def get_tasks():
    return "all tasks"

@task_bp.route("", methods=["POST"])
def create_task():
    request_body = request.get_json()
    
    return "task created"

@task_bp.route("/<int:task_id>", methods=["GET"])
def get_task(task_id):
    return f"task {task_id}"

@task_bp.route("/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    return f"task {task_id} updated"

@task_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    return f"task {task_id} deleted"