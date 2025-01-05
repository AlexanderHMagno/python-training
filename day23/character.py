from turtle import Turtle

class Character(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)   

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)