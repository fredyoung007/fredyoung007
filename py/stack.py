class Stack:
    
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            raise IndexError("ERROR: The stack is empty!")
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            raise IndexError("ERROR: The stack is empty!")
        return self.items[-1]
        
    def size(self):
        return len(self.items)

    def __str__(self):
        string = "["
        string += ', '.join(("'{}'" if type(item) is str else "{}").format(item) for item in self.items)
        string = string + " <-"
        return string

    def clear(self):
        self.items = []

    def multi_push(self, numbers, how_many):
        x = 0
        while x < how_many:
            self.items.extend(numbers)
            x += 1

    def multi_pop(self, number):
        pop_list = []
        start_index = len(self.items) - number
        if len(self.items) < number:
            raise IndexError("ERROR: Not enough elements")
        for item in range(start_index, len(self.items)):
            removed = self.items.pop()
            pop_list.append(removed)
        return pop_list

def zip_stack_list2(a_stack, a_list):
        stack_string = str(a_stack)[1:-3]
        stack_list = stack_string.split(",")
        stack_list = [int(x) for x in stack_list]
        
        new_list = []
        for item in a_list:
            new_list.append(stack_list[-1])
            stack_list.pop()
            new_list.append(item)
        
        s = Stack()
        for char in new_list:
            s.push(char)
        return s
        
def zip_stack_list3(a_stack, a_list):
    s = Stack()
    for item in a_list:
        s.push(a_stack.pop())
        s.push(item)
            
    return s

def zip_stack_list(a_stack, a_list):
    return [_ for _ in a_list for _ in (a_stack.pop(), _)]    

s1 = Stack()
for number in range(1, 5):
    s1.push(number)
q2 = [10, 20, 30, 40]
data = zip_stack_list(s1, q2)
print(data)
print(type(data))
print(s1.size())
