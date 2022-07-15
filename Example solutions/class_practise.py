class Car :
    num_wheels = 4
    drive = "manual"
    
    def __init__(self, brand, model, year, owner):
        self.brand = brand
        self.model = model
        self.year = year
        self.owner = owner

    def get_car_info (self):
        car_info = self.__dict__
        print(car_info)

    def change_owner(self, owner):
        self.owner = owner
        print(f"New owner: {owner}")
        print(self.__dict__)

    def delete_car_info (self):
        del self
        print(dir(Car))



if __name__ == "__main__":

    car1 = Car("Toyota", "Corolla", "2007", "Denis")
    #get_car_info(car1)
    #change_owner(car1, "Tom")
    #car1.change_owner()
    print(dir(Car))
    print()

    car1.get_car_info()
    car1.change_owner("Frank")
    car1.delete_car_info()