from turtle import Turtle
import random

class Cookie(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.create_cookie()
    
    def create_cookie(self):
        cookie_x = random.randint(-280, 280)
        cookie_y = random.randint(-280, 280)
        self.goto(cookie_x, cookie_y)