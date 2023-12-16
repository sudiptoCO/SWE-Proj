class Course():
    def __init__(self, course_id, course_name, credits, fees, instructor):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
        self.fees = fees
        self.instructor = instructor

class User():
    def __init__(self, user_id, username, fullname, password, email, dob, is_admin):
        self.user_id = user_id
        self.username = username
        self.fullname = fullname
        self.password = password
        self.email = email
        self.dob = dob
        self.is_admin = is_admin


class LearningProfile():
    def __init__(self, learning_profile_id, student_id, interests, schedule, goals, commitments):
        self.learning_profile_id = learning_profile_id
        self.student_id = student_id
        self.interests = interests
        self.schedule = schedule
        self.goals = goals
        self.commitments = commitments

class Student(User):
    def __init__(self, user_id, username, fullname, password, email, dob, roll_no, learning_profile, cgpa, completed_courses, pending_courses):
        super().__init__(user_id, username, fullname, password, email, dob, is_admin=False)
        self.roll_no = roll_no
        self.learning_profile = learning_profile
        self.cgpa = cgpa
        self.completed_courses = completed_courses
        self.pending_courses = pending_courses   

class Admin(User):
    def __init__(self, user_id, username, fullname, password, email, dob):
        super().__init__(user_id, username, fullname, password, email, dob, is_admin=True)

# ?
# class Instructors(User):


class Feedback():
    def __init__(self, feedback_id, course_id, student_id, text, ratings):
        self.feedback_id = feedback_id
        self.course_id = course_id
        self.student_id = student_id
        self.text = text
        self.ratings = ratings



# class Dictionary():
#     def to_dict(self):
#         return {k:v for k,v in self.__dict__.items()}
    

class Task():
    def __init__(self, id, title, description, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "title": self.title,
    #         "description": self.description,
    #         "completed": self.completed,
    #     }

