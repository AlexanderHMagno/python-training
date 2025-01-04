import turtle, random
# from ColorManager import ColorManager


class DotPainter:
    COLORS = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20)]
    CONST_DISTANCE = 50 # distance between dots in a row
    CONST_START_POSITION = (-200, -200)
    turning_head = 180


    def __init__(self):
        # self.color_manager = ColorManager('dot.jpg')

        # print(self.color_manager.list_of_colors)
        
        turtle.colormode(255)
        self.franky = turtle.Turtle()
        self.franky.speed('fastest')
        self.franky.hideturtle()
        self.screen = turtle.Screen()
        self.screen.title('Dot Painter')
        self.screen.bgcolor('black')
        self.franky.setposition(-200, -200)
        
       


    def draw_dot(self):
        self.franky.dot(20, random.choice(self.COLORS))
        self.franky.penup()
        self.franky.forward(50)
        self.franky.pendown() 

    def draw_dots(self):
        for _ in range(10):
            self.draw_dot() 

    def draw_dots_in_a_row(self):
        for _ in range(10):
            self.draw_dot()
        self.change_direction() 

    def draw_dots_in_a_column(self):
        for _ in range(10):
            self.draw_dot()
            self.franky.penup()
            self.franky.goto(0, -50)
            self.franky.pendown()

    def change_direction(self):
        self.franky.penup()

        new_x = self.franky.xcor() + (-self.CONST_DISTANCE if self.franky.xcor() == 300 else  self.CONST_DISTANCE)
        self.franky.goto(new_x, self.franky.ycor() + self.CONST_DISTANCE)

        print(self.franky.heading())
        self.franky.setheading(0 if self.franky.heading() == 180 else 180)
        self.franky.pendown()

    def draw_dots_in_a_grid(self):
        
        for _ in range(10):          
            self.draw_dots_in_a_row()




app = DotPainter()

app.draw_dots_in_a_grid()
turtle.done()