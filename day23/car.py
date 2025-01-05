from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.goto(300, random.randint(-250, 250))
        self.setheading(180)
        self.level = 1
        self.move_distance_speed  = 20

    def move(self):
        self.forward(self.move_distance_speed)
        if self.xcor() < -340 and random.randint(1, 6) == 1:
            self.increase_speed()
            self.reset_position()

    def reset_position(self):
        self.goto(300, random.randint(-250, 250))
        self.setheading(180)

    def increase_speed(self):
        self.move_distance_speed += (1 * self.level)

