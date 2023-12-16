from flask import jsonify, Blueprint, request, g, session, redirect
from database import *
import json
import random

api = Blueprint('api', __name__)

# auth
@api.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@api.route('/', methods=['POST'])
def login():
    # if request.method == 'GET':
    #     return jsonify({'message': 'User logged in'}), 200
    data = json.loads(request.data)
    session.pop('user', None)

    user = next((user for user in users if user.username == data['username']), None)
    if user is None:
        return jsonify({'message': 'No user found'}), 404
    else:
        if user.password != data['password']:
            return jsonify({'message': 'Incorrect password'}), 401
        else:
            session['user'] = data['username']
            return jsonify({'message': 'User logged in'}), 200

@api.route('/logout', methods=['GET'])
def logout():
    session.pop('user', None)
    return jsonify({'message': 'User logged out'}), 200

# *Get personalized learning path
# learning suggestion API: pick random courses from list of lists
@api.route('/api/students/learning_path', methods=['GET'])
def get_learning_path_recommendation():
    if g.user is None:
        return jsonify({'message': 'Not logged in'})
    
    learning_path = random.sample(courses, k=3)
    courses_list = []
    for course in learning_path:
        courses_list.append(course.__dict__)
    return jsonify(courses_list), 200


# *Get Course Details by id
@api.route('/api/course/<int:course_id>', methods=['GET'])
def get_course_by_id(course_id):
    if g.user is None:
        return jsonify({'message': 'Not logged in'})

    for course in courses:
        if course.course_id == course_id:
            return jsonify(course.__dict__), 200
    return jsonify({'message': 'No course found'}), 404
        
# Get all courses
@api.route('/api/courses', methods=['GET'])
def get_all_courses():
    if g.user is None:
        return jsonify({'message': 'Not logged in'})
    
    dumps = []
    for course in courses:
        dumps.append(course.__dict__)
    return jsonify(dumps), 200

# *Get student progress
# error when student_id=2
@api.route('/api/students/<int:student_id>/progress', methods=['GET'])
def get_student_progress(student_id):
    if g.user is None:
        return jsonify({'message': 'Not logged in'})
    
    dumps = {'completedCourses': None, 'pendingCourses': None}
    for student in users:
        if student.student_id == student_id:
            dumps['completedCourses'] = student.completed_courses
            dumps['pendingCourses'] = student.pending_courses
            return jsonify(dumps), 200
        else:
            return jsonify({'message': 'No student found'}), 404

# *Add feedback 
# needs data validation
@api.route('/api/students/<int:student_id>/feedback', methods=['POST'])
def post_student_feedback(student_id):
    if g.user is None:
        return jsonify({'message': 'Not logged in'})
    
    data = json.loads(request.data)

    new_feedback = Feedback(feedback_id=len(feedbacks)+1,
                            student_id=student_id,
                            course_id=next((course.course_id for course in courses if course.course_name == data['course']), None),
                            text=data['comment'],
                            ratings=data['rating'])
    
    feedbacks.append(new_feedback)
    return jsonify({'message': 'Successfull feedback submission'}), 204

# get all feedbacks
@api.route('/api/feedbacks', methods=['GET'])
def get_all_feedbacks():
    if g.user is None:
        return jsonify({'message': 'Not logged in'})
    
    dumps = []
    for feedback in feedbacks:
        dumps.append(feedback.__dict__)
    return jsonify(dumps), 200

# more stats?
@api.route('/api/administrator/degree_program_stats', methods=['GET'])
def degree_program_stats():
    if g.user is None:
        return jsonify({'message': 'Not logged in'})

    current_user = next((user for user in users if user.username == session['user']), None)
    if not current_user.is_admin:
        return jsonify({'message': 'Unauthorized'}), 403
    
    total_students = sum(not user.is_admin for user in users)
    instructors_available = len(set([course.instructor for course in courses]))
    
    dumps = {'totalStudents': total_students, 'instructorsAvailable': instructors_available, 'studentChurnRate': None}
    return jsonify(dumps), 200