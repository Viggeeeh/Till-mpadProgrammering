import os
import time
from turtle import Screen
from player import Player

# Create a screen
screen_size_x = 750
screen_size_y = 325
screen = Screen()
screen.setup(screen_size_x, screen_size_y)
screen.bgcolor("black")
screen.title("Endless Runner - Tillämpad Programmering")
screen.tracer(0)

def main():
    player_xpos = -screen_size_x / 2 + 100  
    player_ypos = -screen_size_y / 2 + 30   

    player = Player((player_xpos, player_ypos))

    screen.listen()

    screen.onkeypress(player.jump, "space")
    #screen.onkeypress(quit(), "q")

    while True:
        screen.update()
        time.sleep(0.01)


if __name__ == "__main__":
    main()