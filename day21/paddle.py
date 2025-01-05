from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color("white")
        self.penup()
        self.goto(position)
        self.setheading(90)

    def move_up(self):
        if self.ycor() < 250:
            self.forward(20)

    def move_down(self):
        if self.ycor() > -250:
            self.backward(20)