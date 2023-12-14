from models import *

# In-memory database
tasks = [
    Task(1, "Finish this tutorial", "Learn Flask basics"),
    Task(2, "Buy groceries", "Milk, eggs, bread"),
]

learning_profile = [
    LearningProfile(learning_profile_id=1,
                    student_id=1,
                    interests=['Science', 'Math'],
                    goals=['Graduate with honors'],
                    schedule=['Monday', 'Wednesday'],
                    commitments=['commitments 1', 'commitments 2']),

    LearningProfile(learning_profile_id=2,
                    student_id=2,
                    interests=['Science', 'English'],
                    goals=['Graduate with honors'],
                    schedule=['Monday', 'Thursday'],
                    commitments=['commitments 5', 'commitments 6'])
]

# inerit user class?
students = [
    Student(student_id=1,
            roll_no='21f1001051',
            learning_profile=learning_profile[0],
            cgpa=4,
            completed_courses=None, 
            pending_courses=None),

    Student(student_id=2,
            roll_no='21f1001051',
            learning_profile=learning_profile[1],
            cgpa=4.4,
            completed_courses=None, 
            pending_courses=None)           
]

courses = [
    Course(course_id=1,
           course_name='Course A',
           credits=3,
           fees=4,
           instructors='instructors A'),

    Course(course_id=2,
           course_name='Course B',
           credits=6,
           fees=23,
           instructors='instructors B'),
]
