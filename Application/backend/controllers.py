from flask import jsonify, Blueprint
from database import tasks, courses

api = Blueprint('api', __name__)
# learning suggestion API: pick random courses from list of lists

# *Get personalized learning path
@api.route('/api/students/<int:stundet_id>/learning_path', methods=['GET'])
def get_learning_path_recommendation(student_id):
    pass

# *Get Course Details by id
@api.route('/api/course/<int:course_id>', methods=['GET'])
def get_course_by_id(course_id):
    for course in courses:
        if course.course_id == course_id:
            return jsonify(course.__dict__), 200
    return jsonify({'message': 'No course found'}), 404
        
# Get all courses
@api.route('/api/courses', methods=['GET'])
def get_all_courses():
    dumps = []
    for course in courses:
        dumps.append(course.__dict__)
    return jsonify(dumps), 200
























# API endpoint to get all tasks
@api.route("/api/tasks", methods=["GET"])
def get_all_tasks():

    dumps=[]
    for i in tasks:
        dumps.append(i.__dict__)
    return jsonify(dumps), 200

# API endpoint to get a specific task
@api.route("/api/tasks/<int:task_id>", methods=["GET"])
def get_task_by_id(task_id):
    for task in tasks:
        if task.id == task_id:
            return jsonify(task.to_dict()), 200
    return jsonify({"error": "Task not found"}), 404

# # API endpoint to create a new task
# @app.route("/api/tasks", methods=["POST"])
# def create_task():
#     data = json.loads(request.data)
#     new_task = Task(id=len(tasks) + 1, title=data["title"], description=data.get("description"))
#     tasks.append(new_task)
#     return jsonify(new_task), 201

# # API endpoint to update a task
# @app.route("/api/tasks/<int:task_id>", methods=["PUT"])
# def update_task(task_id):
#     data = json.loads(request.data)
#     for i, task in enumerate(tasks):
#         if task.id == task_id:
#             tasks[i] = Task(id=task_id, title=data["title"], description=data.get("description"), completed=data.get("completed", task.completed))
#             return jsonify(tasks[i]), 200
#     return jsonify({"error": "Task not found"}), 404

# # API endpoint to delete a task
# @app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
# def delete_task(task_id):
#     for i, task in enumerate(tasks):
#         if task.id == task_id:
#             del tasks[i]
#             return jsonify({"message": "Task deleted successfully"}), 200
#     return jsonify({"error": "Task not found"}), 404