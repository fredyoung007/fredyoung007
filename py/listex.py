"""listex.py
"""
# slice [m:n:s]
list2 = list("123456789")
print(list2)
print(len(list2))
print(list2[0:6])   
print(list2[:6]) 
print(list2[6:])
print(list2[-1])
print(list2[::2])
print(list2[1::2])
print(list2[2:7:3])
print(list2[::-1])

# list.sort(reverse=True|False, key=func)
list2.sort(reverse=True)
print(list2)
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
# cars.reverse()
print(cars)

# String list
list1 = ["Maxine", "Marianne", "Athena"]
print(' '.join(list1))
print('-'.join(list1))

ss = "##".join(list1)
print(ss)
print(ss.split("##"))

# Remove duplicates
list1 = ["AB", "CD", "AB"]
print(list(set(list1)))

# Concatenaet lists
list1 = ["AB", "CD"]
list2 = ["EF", "GH"]
print(list1 + list2)
list1.append(list2)
print(list1)
