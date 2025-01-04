import turtle
import random

class Turtle:

    CONST_DIRECTIONS = [0, 90, 180, 270]

    def __init__(self):
        self.x = 0
        self.y = 0
        self.franky = turtle.Turtle()
        self.franky.shape("turtle")
        self.franky.color("green")
        self.speed = 1
        self.draw()

    def move(self):
        self.franky.forward(self.speed)

    def draw(self):
        turtle.goto(self.x, self.y)

    def change_color(self):
        colors = ["red", "blue", "green", "purple", "orange", "yellow", "pink", "brown", "cyan", "magenta"]
        current_color = self.franky.color()[0]
        current_index = colors.index(current_color) if current_color in colors else -1
        next_index = (current_index + 1) % len(colors)
        self.franky.color(colors[next_index])

    def square(self, steps):
        self.draw_shape(4, steps)

    def circle(self, radius):
        self.franky.circle(radius)

    def triangle(self, steps):
        self.draw_shape(3, steps)

    def draw_shape(self, sides, steps, dash=False):
        self.change_color()
        for _ in range(sides):
            self.draw_line(steps, dash)
            self.franky.left(360 / sides)

    def pentagon(self, steps):
        self.draw_shape(5, steps)

    def heptagon(self, steps):
        self.draw_shape(7, steps, dash=True)

    def nonagon(self, steps):
        self.draw_shape(9, steps)

    def decagon(self, steps):
        self.draw_shape(10, steps)

    def hexagon(self, steps):
        self.draw_shape(6, steps)

    def octagon(self, steps):
        self.draw_shape(8, steps)

    def toggle_pen(self):
        if self.franky.isdown():
            self.franky.penup()
        else:
            self.franky.pendown()

    def reset(self):
        self.franky.reset()
        self.franky.penup()
        self.franky.home()
        self.franky.pendown()

    def draw_line(self, length, dash=False):    
        
        if dash:
            for _ in range(length):
                # self.toggle_pen()
                self.franky.forward(self.speed * 2)
                # self.toggle_pen()
        else:
            self.franky.forward(self.speed * length)
    
    def random_path(self, length, straight=False):
        self.change_color()
        self.franky.forward(self.speed * length)
        if straight:
            self.franky.left(random.choice(self.CONST_DIRECTIONS))
        else:
            self.franky.left(random.randint(0, 360))

    def change_tickness(self, tickness):
        self.franky.pensize(tickness)

    def change_speed(self, speed):
        self.franky.speed(speed)

    def spirograph(self, radius, angle):
        self.franky.circle(radius)
        self.franky.left(angle)


