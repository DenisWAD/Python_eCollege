class User :
    def __init__(self, name, age, address, mobile) :
        self.name = name
        self.age = age
        self.address = address
        self.mobile = mobile

    # def getAge() :
        

user1 = User("Denis Murray", 27, "Kilkenny", 353877838463)

# print(f"Name: {user1.name}\nAge: {user1.age}\nAddress: {user1.address}\nMobile: {user1.mobile}")
# print(user1.__dict__)


def getUserInfo() :
    return user1.__dict__


