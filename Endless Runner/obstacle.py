'''
obstacle.py: Här är allt kopplat till obstacle

__author__  = "Viggo Öfors"
__version__ = "1.0.0"
__email__   = "viggo.ofors@elev.ga.ntig.se"
'''

from turtle import Turtle

class Obstacle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.shapesize(1, 1.5)
        self.left(90)  # För att spelaren ska stå upp
        self.penup()
        self.goto((300, -135))

    def move(self):
        self.goto(self.xcor() - 5, self.ycor())

        