with open("test.txt", "r") as inputf:
    for line in inputf:
       print(''.join(w[0].upper() for w in line.split(' ')))

