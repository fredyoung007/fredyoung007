"""recur.py
Recursion = base + self invocation
"""

from cgi import print_environ


def count_non_digits(word):
    if len(word) == 1:
        return 0 if word.isdigit() else 1

    return count_non_digits(word[1:]) + count_non_digits(word[0])  

def get_middle_letters(words):
    def mid(word):
        m = round(len(word) / 2)
        return word[m]
        
    if len(words) == 0:
        return ''
    if len(words) == 1:
        return mid(words[0])
    
    return get_middle_letters([words[0]]) + get_middle_letters(words[1:]) 

def get_sum_evens(numbers):
    if len(numbers) == 0:
        return (0,0)
    if len(numbers) == 1:
        number = numbers[0] if (numbers[0] % 2 == 0) else 0
        return (number,1)
    
    return tuple(map(sum, zip(get_sum_evens([numbers[0]]), get_sum_evens(numbers[1:]))))

def evaluate_m6(n):
    if (n<=0):
        return (3, 0)
    
    return tuple(map(sum, zip(evaluate_m6(n-1), (2,1))))

print(evaluate_m6(0))
print(evaluate_m6(1))
