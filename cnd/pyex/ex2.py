"""ex2.py
"""
name = input("Please enter the name of a product: ")
unitPrice = float(input("Please enter the unit price of the product: "))
number = int(input("Please enter the number of the product: "))

import abc
import operator
totalPrice = unitPrice * number
print(operator.gt(int(totalPrice), len(name)))

import math
result = abs(operator.sub(unitPrice, math.sqrt(number)))
print(round(result, 2))
