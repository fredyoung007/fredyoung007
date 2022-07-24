def validate_index(coins_list, position_number):
    if position_number in range(0, 9):
        if coins_list[int(position_number) - 1] == '$':
            return True

    return False

pos_num = int(input("Enter a number."))
coins_list = ['-', '$', '-', '-', '$', '-', '$', '$', '-']
print(validate_index(coins_list, pos_num))
