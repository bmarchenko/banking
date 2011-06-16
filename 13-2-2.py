#!/usr/bin/env python

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


students = []
again = "yes"

while again != "no":
    name = raw_input ("Enter the student's name: ")
    phone = raw_input ("Enter the student's phone number: ")
    email = raw_input ("Enter the student's email: ")
    student = Student(name, [], phone, email)
    students.append(student)

    print "Input the courses which", student.name, "is enrolled in."
    newcourse = raw_input ("Type the course number or 'stop' ")

    while newcourse != "stop":
        student.enroll(newcourse)
        print "Input the courses which", student.name, "is enrolled in."
        newcourse = raw_input ("Type the course number or 'stop' ")

    again = raw_input ("Would you like to enter more students? ")




class Employee:
    def __init__(self, name, position, phone, email):
        self.name = name
        self.position = position
        self.phone = phone
        self.email = email
        print "Created a class instance for "+ name

    def printDetails(self):
        print "Name: ", self.name
        print "Position: ", self.position
        print "Phone: ", self.phone
        print "Email: ", self.email


employees = []
again = "yes"

while again != "no":
    name = raw_input ("Enter employee's name: ")
    position = raw_input ("Enter employee's  position: ")
    phone = raw_input ("Enter employee's  phone number: ")
    email = raw_input ("Enter employee's email: ")
    employee = Employee(name, position, phone, email)
    employees.append(employee)
    again = raw_input ("Would you like to enter more employees? ")
print "STUDENTS:"
for student in students:
    
    student.printDetails()
    print "Credit hours: ", len (student.courses)*3

print "EMPLOYEES:"    
for employee in employees:
    employee.printDetails()
