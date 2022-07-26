"""cph.py
Contianer comprehension 
Compare loop, comprehension, and map()
"""

# initialise list to 0
n = 6

lst = []
for _ in range(n):
    lst.append(0)
print(lst)

lst = [0 for _ in range(n)]
print(lst)

# initialise list to i
lst = []
for i in range(n):
    lst.append(i)
print(lst)
# print(lst.reverse()) # would not work because reverse returns nothing
lst.reverse()
print(lst)
print([i for i in range(n)])

# initilise in revesed order
lst = []
for i in range(n-1, -1, -1):
    lst.append(i)
print(lst)
print([i for i in range(n-1,-1, -1)])

# count word occurence
words = "hello well hello".split(' ')

woc = {}
for word in words:
    woc[word] = words.count(word)
print(woc)

woc = {word: words.count(word) for word in words}
print(woc)
