# """ Creating simple classes and Objects. Manipulating the data in the seperate Objects"""

# class User :
#     """ The basic user for this app. Currently only only contains names, age, basic info. 
#     But soon will contain a stupid amount of info"""
#     def __init__(self, full_name, age ) :
#         name_pieces = full_name.split(" ")
        
#         self.first_name = name_pieces[0]
#         self.last_name = name_pieces[-1]
#         self.age = age

#     def getAge(self) :
#         return self.age

#     def getName(self) :
#         return self.first_name , self.last_name


# user1 = User("Denis Murray", 55)
# print(user1.getName())


try:
    n = int(input("How old are you?"))
    percent = round(n * 100/80, 1)
    print("You've gone through", percent, "% of your life!")
except ValueError:
    print("Oops, must enter a number.")
except ZeroDivisionError:
    print("Division by zero")
except:
    print("Something went very wrong")