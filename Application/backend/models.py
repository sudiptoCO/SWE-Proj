from Application.backend.database import db 

class Course(db.Model):
    __tablename__ = 'course'
    course_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    course_name = db.Column(db.String, unique=True, nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    fees = db.Column(db.Integer, nullable=False)
    instructors = db.Column(db.String, nullable=False)

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    user_name = db.Column(db.String, unique=True, nullable=False)
    fullname = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    dob = db.Column(db.String, nullable=False)

class Student(db.Model,User):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    roll_no = db.Column(db.String, unique=True, nullable=False)
    # learning_profile = db.Column(db.String, nullable=False)
    cgpa = db.Column(db.Integer, nullable=False)
    # completed_course = db.Column(db.String, nullable=False)
    # pending_courses = db.Column(db.String, nullable=False)

class LearningProfile(db.Model):
    __tablename__ = 'learning_profile'
    learning_profile_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    student_id = db.Column(db.Integer, unique=True, nullable=False)
    interests = db.Column(db.String, unique=True, nullable=False)
    schedule = db.Column(db.String, unique=True, nullable=False)
    goals = db.Column(db.String, unique=True, nullable=False)
    commitments = db.Column(db.String, unique=True, nullable=False)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    course_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    student_id = db.Column(db.Integer, unique=True, nullable=False)
    text = db.Column(db.String, unique=True, nullable=False)
    ratings = db.Column(db.Integer, unique=True, nullable=False)