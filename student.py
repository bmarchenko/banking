
class Student:
    'contains students, email, name ...'

    def __init__(self, name, courses, phone, email):
        self.name = name
        self.courses = courses
        self.phone = phone
        self.email = email
        print "Created a class instance for "+ name

    def printDetails(self):
        print "Name: ", self.name
        print "Courses: ", self.courses
        print "Phone: ", self.phone
        print "Email: ", self.email

    def enroll(self, course):
        self.courses.append(course)
