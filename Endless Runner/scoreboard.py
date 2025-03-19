'''
scoreboard.py: Här hanteras scoreboarden

__author__  = "Viggo Öfors"
__version__ = "1.0.0"
__email__   = "viggo.ofors@elev.ga.ntig.se"
'''

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
POSITION = (0, 0)
ALIGNMENTMIDDLE = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(POSITION)
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def death_screen(self):
        self.clear()
        self.write(f"You died.. Score: {self.score}", align=ALIGNMENT, font=FONT)