class Student:
    def __init__(self, firstname, surname, grade = None):
        self.surname = surname
        self.firstname = firstname
        self.grade = grade
    def __str__(self):
        return '{} {}({})'.format(self.surname, self.firstname, self.grade)
    def get_full_name(self):
        return  "{} {}".format(self.surname, self.firstname)
    def get_grade(self):
        return self.grade

def selection_sort(data):	
    for num_iterations in range(len(data) - 1, 0, -1):
        position_largest = 0
        for i in range(1, num_iterations + 1):
            if data[i] > data[position_largest]:
                position_largest = i
        data[position_largest], data[i] = data[i], data[position_largest]

def selection_sort2(data):	
    for num_iterations in range(len(data) - 1, 0, -1):
        position_largest = 0
        for i in range(1, num_iterations + 1):
            if str(data[i])> str(data[position_largest]):
                position_largest = i
        data[position_largest], data[i] = data[i], data[position_largest]

s1 = Student('Dick', 'Smith', 'C')
s2 = Student('Sally', 'Jones', 'B')
s3 = Student('Michael', 'Hill', 'A')
s4 = Student('Peter', 'Pan', 'C')
s5 = Student('Olivia', 'Pan', 'C')
s6 = Student('Liam', 'Pan', 'B')
s7 = Student('Fred', 'Fish', 'A')
s8 = Student('Robert', 'Williams', 'B')
students = [s1, s2, s3, s4, s5, s6, s7, s8]
selection_sort2(students)
for s in students:
    print(s.surname)
