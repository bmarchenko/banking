from student import*
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

print "STUDENTS:"
for student in students:
    
    student.printDetails()
    print "Credit hours: ", len (student.courses)*3
