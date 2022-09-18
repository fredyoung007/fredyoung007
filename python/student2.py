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
            if str(data[i])> str(data[position_largest]):
                position_largest = i
        data[position_largest], data[i] = data[i], data[position_largest]


def search_student(target, L):

    start = 0
    end = len(L) - 1
    i = 0
    while start <= end:
        middle = (start + end)// 2
        i += 1
        midpoint = L[middle]
        if midpoint.get_full_name() > target:
            end = middle - 1
        elif midpoint.get_full_name() < target:
            start = middle + 1
        else:
            return (True, i)
    return (False, i)

students = [Student('Fred', 'Fish', 'A'), Student('Michael', 'Hill', 'A'), Student('Sally', 'Jones', 'B'), Student('Liam', 'Pan', 'B'), Student('Olivia', 'Pan', 'C'), Student('Peter', 'Pan', 'C')]
selection_sort(students)

print("searching for Peter Pan", search_student('Pan Peter', students))
print("searching for Olivia Pan", search_student('Pan Olivia', students))
print("searching for Michael Hill", search_student('Hill Michael', students))
print("searching for Olivia Johnson", search_student('Johnson Olivia', students))