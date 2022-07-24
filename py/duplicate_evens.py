def duplicate_evens(numbers_list):
    lst = []
    for i in numbers_list:
        lst.append(i)
        if (i % 2) == 0:
             lst.append(i)
    numbers_list[:] = list(lst)

numbers = [1,2,3,4,5]
numbers2 = [11,3,9]
duplicate_evens(numbers)
print(numbers)
