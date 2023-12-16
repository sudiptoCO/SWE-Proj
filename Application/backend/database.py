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
users = [
    Student(user_id=1,
            username='student1',
            fullname='student1',
            password='student1',
            email='student1@domain.com',
            dob='1/1/2000',
            roll_no='21f1001051',
            learning_profile=learning_profile[0],
            cgpa=4,
            completed_courses=['Math', 'Science'], 
            pending_courses=['Eng', 'Esp']),

    Student(user_id=2,
            username='student2',
            fullname='student2',
            password='student2',
            email='student2@domain.com',
            dob='1/1/2000',
            roll_no='21f1001052',
            learning_profile=learning_profile[1],
            cgpa=4,
            completed_courses=None, 
            pending_courses=None),

    Admin(user_id=3,
          username='admin1',
          fullname='admin1',
          password='admin1',
          email='admin1@domain.com',
          dob='1/1/2000')
]

courses = [
    Course(course_id=1,
           course_name='Course A',
           credits=3,
           fees=4,
           instructor='instructor A'),

    Course(course_id=2,
           course_name='Course B',
           credits=6,
           fees=23,
           instructor='instructor B'),
    
    Course(course_id=3,
           course_name='Course C',
           credits=6,
           fees=23,
           instructor='instructor B'),
    
    Course(course_id=4,
           course_name='Course D',
           credits=6,
           fees=23,
           instructor='instructor C'),
    
    Course(course_id=5,
           course_name='Course E',
           credits=6,
           fees=23,
           instructor='instructor B'),
]

feedbacks = [
    Feedback(feedback_id=1,
             course_id=1,
             student_id=1,
             text='Good',
             ratings=3),

    Feedback(feedback_id=2,
             course_id=1,
             student_id=2,
             text='Excellent',
             ratings=5)
]
