# def square_input(x) :
#   return x ** 2 

# output = square_input(10)

# print(output)

def get_names(*names) :
    """This function takes in whatever amount of names and prints out line for each name """
    for i in names :
        print("Hello there your name is", i)

#get_names("Denis", "Alan", "Derple", "Bob")

print(get_names.__doc__)