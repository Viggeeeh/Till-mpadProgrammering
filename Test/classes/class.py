import os

class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
    
    def view_car(self):
        return f"{self.make} - {self.model} ({self.color})"
    

os.system("cls")

cars = []

while True:
    for car in cars:
        print(car.view_car())
        
    car_make = input("Car make: ")
    car_model = input("Car model: ")
    car_color = input("Car color: ")

    cars.append(Car(car_make, car_model, car_color))
    os.system("cls")
