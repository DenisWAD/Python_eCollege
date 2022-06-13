# Create funciton that takes in a function as an argument along with any number of numbers for calculation

def fn_needed(calculation, *args) :
    return calculation(*args)
    

def add(*args) :
    total = 0
    
    for i in args :
        total += i

    return total


def subtract(*args) :
    total = 0

    for i in args :
        total -= i
    
    return total

def multiply(*args) :
    total = 1

    for i in args :
        total *= i

    return total


x = fn_needed(multiply, 10, 9, 5)
print(x)