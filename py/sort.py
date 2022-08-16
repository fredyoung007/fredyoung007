def selection_sort(data):
    check_list = []
    comp_count = len(data)
    for pass_num in range(len(data) - 1, 0, -1):
        position_largest = 0
        comp_count -= 1
        for i in range(1, pass_num + 1):
            new_list = []
            swap_count = 0
            if data[i] > data[position_largest]:
                position_largest = i
        swap_count +=1
        new_list.append(comp_count)
        new_list.append(swap_count)
        data[position_largest], data[i] = data[i], data[position_largest]
        check_list.append(new_list)
    return check_list

def selection_sort_fast(data):
    check_list = []
    comp_count = len(data)
    for pass_num in range(len(data) - 1, 0, -1):
        position_largest = 0
        comp_count -= 1
        for i in range(1, pass_num + 1):
            new_list = []
            swap_count = 0
            if data[i] > data[position_largest]:
                position_largest = i

        if position_largest != pass_num:
            data[position_largest], data[i] = data[i], data[position_largest]
            swap_count +=1
        new_list.append(comp_count)
        new_list.append(swap_count)
        check_list.append(new_list)
    return check_list
    
numbers1 = [76, 53, 48, 24, 12]
numbers2 = numbers1[:]
result1 = selection_sort(numbers1)
result2 = selection_sort_fast(numbers2)
print(result1)
print(result2)

numbers1 = [95, 55, 92, 9]
numbers2 = numbers1[:]
result1 = selection_sort(numbers1)
result2 = selection_sort_fast(numbers2)
print(result1)
print(result2)
