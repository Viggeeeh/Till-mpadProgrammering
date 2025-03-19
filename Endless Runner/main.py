'''
main.py: Här körs hela programmet

__author__  = "Viggo Öfors"
__version__ = "1.0.0"
__email__   = "viggo.ofors@elev.ga.ntig.se"
'''

import os
import time
from turtle import Screen
from player import Player
from obstacle import Obstacle
from scoreboard import Scoreboard

# Skapa en skärm
screen_size_x = 750
screen_size_y = 325
screen = Screen()
screen.setup(screen_size_x, screen_size_y)
screen.bgcolor("black")
screen.title("Endless Runner - Tillämpad Programmering")
screen.tracer(0)

def create_new_obstacle():
    return Obstacle()

def main():
    player_xpos = -screen_size_x / 2 + 100  
    player_ypos = -screen_size_y / 2 + 30   

    player = Player((player_xpos, player_ypos))
    scoreboard = Scoreboard()
    obstacles = [Obstacle()]

    player_name = screen.textinput("player name", "Enter your name")
    information = screen.textinput("Information", "Press space to jump, dodge the obstacles to gain score (Press OK to begin)")

    screen.listen()

    screen.onkeypress(player.jump, "space")

    while True:
        screen.update()

        # Flytta alla obstacles
        for obstacle in obstacles:
            obstacle.move()

        time.sleep(0.01)

        # Kolla om spelaren stöter i någon obstacle
        for obstacle in obstacles:
            if player.distance(obstacle) < 30:
                scoreboard.death_screen()
                screen.mainloop()   # Pausa skärmen
    
            # Spawna in nya obstacles
            if player.distance(obstacle) < 75 and not getattr(obstacle, "spawned", False):
                scoreboard.increase_score()
                obstacles.append(create_new_obstacle())
                obstacle.spawned = True


if __name__ == "__main__":
    main()