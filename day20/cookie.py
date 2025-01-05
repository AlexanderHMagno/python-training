import turtle
import random

class Cookie:
    def __init__(self):
        self.cookie = turtle.Turtle()
        self.cookie.shape("circle")
        self.cookie.color("yellow")
        self.cookie.penup()
        self.create_cookie()
    
    def create_cookie(self):
        cookie_x = random.randint(-280, 280)
        cookie_y = random.randint(-280, 280)
        self.cookie.goto(cookie_x, cookie_y)