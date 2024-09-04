# class Car:
#     def __init__(self, name):
#         self.name = name


# car = Car("Audi")
# print(car.name)

import os

class Car:
    def __init__(self):
        self.car_details = {}

    def add_car(self, make, model):
        if make in self.car_details:
            self.car_details[make].append(model)
        else:
            self.car_details[make] = [model]
        

    def remove_car(self, make):
        self.car_details.pop(make)

    def list_cars(self):
            order = 1
            for make, model in self.car_details.items():
                if len(model) > 1:
                    for i in range(len(model)):
                        print(f"{order}) {make} - {model[i]}")
                        order += 1
                else:    
                    print(f"{order}) {make} - {model[0]}")
                order += 1


os.system("cls")

car = Car()
car.add_car("Ford", "Mustang")
car.add_car("Ferrari", "360")
car.add_car("Ferrari", "458")
car.add_car("Toyota", "Supra")
car.add_car("Ford", "GT")
car.add_car("Audi", "RS4")
car.add_car("Audi", "R8")
car.list_cars()
# car.remove_car("Ferrari")
# car.list_cars()

