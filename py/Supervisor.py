class Supervisor:
    def __init__(self, name = ""):
        self.name = name
        self.students = []

    def add_student(self, student):
        check = isinstance(student, Student)
        if check == True:
            student.assign(self.name)
            self.students.append(student)
    
    def __str__(self):
        if len(self.students) == 0:
            message = "{} has 0 students.".format(self.name)
        elif len(self.students) == 1:
            message = "{} has 1 student.".format(self.name)
        else:
            message = "{} has {} students.".format(self.name, len(self.students))
        return message

    def remove_student(self, student):
            check = isinstance(student, Student)
            if check == True:
                student.unassign()
                self.students.remove(student)

    def print_names(self):
        if len(self.students) == 0:
            message = "No students."
        else:
            message = "Students:"
            for s in self.students:
                name_pr = "\n{}".format(s.name)
                message += name_pr
        print(message)


class Student:
    def __init__(self, name = "", supervisor_name = None):
        self.name = name
        self.supervisor_name = supervisor_name

    def assign(self, supervisor_name):
        self.supervisor_name = supervisor_name
    
    def unassign(self):
        self.supervisor_name = None
    
    def __str__(self):
        if self.supervisor_name == None:
            message = "{} is looking for a supervisor.".format(self.name)
        else:
            message = "{} has a supervisor.".format(self.name)
        return message

"""
student1 = Student("John")
staff = Supervisor("Michael")
print(staff)
staff.add_student(student1)
print(staff)
print(student1)

student1 = Student("Anna")
staff1 = Supervisor("Michael")
staff2 = Supervisor("Peter")
staff1.add_student(student1)
print(staff1 == staff2)
print(staff1)
print(staff2)

students = [Student("Anna"), Student("John"), Student("Peter")]
staff = Supervisor("Emma")
for s in students:
    staff.add_student(s)
print(staff)
print(students[0])
"""
students = [Student('Anna'), Student('John'), Student('Peter')]
staff = Supervisor("Michael")
for s in students:
    staff.add_student(s)
staff.print_names()

staff.remove_student(students[1])
print(staff)
print(students[0])
print(students[1])
staff.print_names()
