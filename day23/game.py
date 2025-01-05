from turtle import Screen
from character import Character
from car import Car
import random
import time

class TurtleCrossingGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Turtle Crossing Game")
        self.screen.tracer(0)
        self.character = Character()
        self.car = []


    def start_game(self):
        self.screen.listen()
        self.screen.onkey(self.character.move_up, "Up")
        self.screen.onkey(self.character.move_down, "Down")

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Car()
            self.car.append(new_car)

    def move_cars(self):
        for car in self.car:
            car.move()

    def check_collision(self):
        for car in self.car:
            if car.distance(self.character) < 20:
                return True
        return False

game = TurtleCrossingGame()
game.start_game()

while True:
    game.create_car()
    game.move_cars()
    game.screen.update()
    time.sleep(0.1)
    if game.check_collision():
        game.game_over()
        break

game.screen.exitonclick()