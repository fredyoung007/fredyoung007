"""ex7.py
"""
def validate(arg1, arg2, arg3):
    return (len(arg1) > 5) or (arg1 != "Surprise") or ((arg2%arg3) <= 4)   

print(validate("Surprise", 12, 7))
