def function1(a, b):
    return function2(a + b)

def function2(a):
    b = a * 5

print(function1(2, 3))