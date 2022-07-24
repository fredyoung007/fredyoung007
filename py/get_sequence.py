def get_sequence_number(n):
    if n == 0 or n ==1: 
        return 0

    elif n == 2:
        return 1

    else:
        return get_sequence_number(n-1) + get_sequence_number(n-2) + get_sequence_number(n-3)

term = int(input("Please enter a number: "))
print("Term", term, "of the sequence is", get_sequence_number(term))
