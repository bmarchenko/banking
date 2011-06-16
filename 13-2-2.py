#!/usr/bin/env python

class Student:
    'contains students, email, name ...'

    def __init__(self, name, courses, phone, email, credit):
        self.name = name
        self.courses = courses
        self.phone = phone
        self.email = email
        self.credit = credit
        print "Created a class instance for "+ name

    def printDetails(self):
        print "Name: ", self.name
        print "Courses: ", self.courses
        print "Phone: ", self.phone
        print "Email: ", self.email
        print "Credit hours: ", self.credit

    def enroll(self, course):
        self.courses.append(course)

    credit = 0
    def addcredit (self):
        credit = credit + 3        

students = []
again = "yes"

while again != "no":
    name = raw_input ("Enter the student's name: ")
    phone = raw_input ("Enter the student's phone number: ")
    email = raw_input ("Enter the student's email: ")
    student = Student(name, [], phone, email, credit)
    students.append(student)

    print "Input the courses which", student.name, "is enrolled in."
    newcourse = raw_input ("Type the course number or 'stop' ")

    while newcourse != "stop":
        student.enroll(newcourse)
        print "Input the courses which", student.name, "is enrolled in."
        newcourse = raw_input ("Type the course number or 'stop' ")
        student.addcredit()
    again = raw_input ("Would you like to enter more students? ")


for student in students:
    student.printDetails()
