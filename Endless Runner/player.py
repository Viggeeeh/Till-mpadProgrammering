'''
player.py: Här är allt med spelaren och dess funktioner

__author__  = "Viggo Öfors"
__version__ = "1.0.0"
__email__   = "viggo.ofors@elev.ga.ntig.se"
'''

from turtle import Turtle

class Player(Turtle):
    def __init__(self, position):
        super().__init__()  # Ärver klassen Turtle
        self.shape("square")
        self.color("white")
        self.shapesize(1, 2)
        self.left(90)  # För att spelaren ska stå upp
        self.penup()
        self.goto(position)

        self.is_jumping = False  # För att undvika flera hopp samtidigt
        self.start_y = position[1]

    def jump(self):
        if not self.is_jumping:  # Bara hoppa om spelaren inte redan är i luften
            self.is_jumping = True
            self.animate_jump(0)  # Börja hopp-animationen

    def animate_jump(self, step):
        jump_height = 50
        total_steps = 20  # Antalet steg för hopp-animationen

        if step <= total_steps:  # Uppåt-rörelse
            self.goto(self.xcor(), self.ycor() + jump_height / total_steps)
        elif step <= 2 * total_steps:  # Nedåt-rörelse
            self.goto(self.xcor(), self.ycor() - jump_height / total_steps)
        else:  # Slutför hoppet
            self.goto(self.xcor(), self.start_y)
            self.is_jumping = False
            return

        # Schemalägg nästa steg i animationen
        self.getscreen().ontimer(lambda: self.animate_jump(step + 1), 20)
