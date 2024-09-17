class Pupil:
    def __init__(self, name, age, school):
        self.name : str = name
        self.age : int = age
        self.school : str = school
    
    def __str__(self):
        return f"{self.name} is {self.age} years old, and goes to {self.school}"
    
def add_pupil():
    name = input("Name? ")
    age = int(input("Age? "))
    school = input("School? ")
    pupils.append(Pupil(name, age, school))
    
pupils = []

while True:
    add_pupil()
    for pupil in pupils:
        print(pupil)