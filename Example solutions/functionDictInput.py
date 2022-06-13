#Funciton to Return as a function object
# def calculation(calc = "+") :
#     if calc == "+" :
#         return add
    
#     if calc == "-" :
#         return sub

#     if calc == "*" :
#         return mul

#     if calc == "/" :
#         return div

    
def add(a , b) :
    return a + b

def sub(a , b) :
    return a - b

def mul(a , b) :
    return a * b

def div(a , b) :
    return a / b


# Store in a dict
dict_calculations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}


print(dict_calculations["-"](15, 9))




# fn = calculation()

# print(fn(10 , 5))