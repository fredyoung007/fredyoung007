"""ex4.py
"""
alice = 1
beth = 200
day = 0
while alice <= beth*2:
    print(f"Day {day} - Alice: {alice}; Beth: {beth}")
    alice *= 2
    beth += 100
    day += 1
print("Alice's sweets will be more than double of Beth's sweets on day", day)