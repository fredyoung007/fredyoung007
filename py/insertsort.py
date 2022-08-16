def compare(value, item_to_insert, count_list):
    count_list[0] += 1
    return value > item_to_insert

def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        item_to_insert = a_list[index]
        i = index -1
        while i>=0 and a_list[i] > item_to_insert:
            a_list[i+1] = a_list[i]
            i -= 1
        a_list[i+1] = item_to_insert

def insert_sort(a_list):
    rc = []
    count_list = []
    sc = 0
    for index in range(1, len(a_list)):
        item_to_insert = a_list[index]
        i = index -1
        cc = 0
        # while i>=0 and a_list[i] > item_to_insert:
        while i>=0 and a_list[i] > item_to_insert:
            a_list[i+1] = a_list[i]
            i -= 1
            cc += 1
        a_list[i+1] = item_to_insert
        sc += 1        
        rc.append([cc, sc])
    return rc

def insert_sort2(a_list):
    rc = []
    for index in range(1, len(a_list)):
        item_to_insert = a_list[index]
        i = index -1
        count_list = [0, 0]
        while i>=0 and compare(a_list[i], item_to_insert, count_list):
            count_list[1] += 1
            a_list[i+1] = a_list[i]
            i -= 1
        a_list[i+1] = item_to_insert     
        rc.append([count_list[0], count_list[1]])
    return rc

numbers = [92,86,77,66,51,42,33,23]
numbers1 = [50,63,11,79,22,70,65,39,97,48]
result = insert_sort2(numbers1)
print(result)