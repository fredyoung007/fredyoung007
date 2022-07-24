def hello(*arg):
    """Hello world!"""
    print("Hello world")
    for name in arg:
        print(name)

def square(number):
    """This function returns the square of a given number"""
    return number ** 2


def double(number):
    """This function returns twice the value of a given number"""
    return number * 2

hello()
hello("Lolo", "Dodo","Joujou")
hello("Lolo", "Dodo","Joujou", "Cloclo", "Margot", "Froufrou" )
# help(hello) 
