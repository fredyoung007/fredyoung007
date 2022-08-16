"""ex3.py
"""
alice = 0
beth = 100
day = 0
while alice <= beth:
    print(f"Day {day} - Alice: {alice}; Beth: {beth}")
    alice += 1
    beth -= 2
    day += 1
print("Alice exceeds Beth on day", day)