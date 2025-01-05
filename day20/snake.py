import turtle

class Snake:
    CONST_MOVE_DISTANCE = 20
    STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            self.add_segment(self.STARTING_POSITIONS[i])

    def add_segment(self, position):
        new_segment = turtle.Turtle("turtle")
        new_segment.color("white")
        new_segment.speed('slowest')
        new_segment.penup()
        new_segment.hideturtle()
        new_segment.goto(position)
        new_segment.showturtle()

        if len(self.snake) == 0:  
          new_segment.shape("turtle")
          new_segment.color("green")
        
        self.snake.append(new_segment)
      

    def move(self):
      
        for seg_num in range(len(self.snake) - 1, 0, -1):
            segment = self.snake[seg_num - 1]
            new_x = segment.xcor()
            new_y = segment.ycor() 
            heading = segment.heading()
            self.translate_x(segment, new_x)
            self.translate_y(segment, new_y)
            self.snake[seg_num].goto(new_x, new_y) 
            self.snake[seg_num].setheading(heading)       

        self.snake[0].forward(self.CONST_MOVE_DISTANCE)

    def translate_y(self, segment, y_cor):
        if y_cor > 290:
            segment.hideturtle()
            segment.sety(-300)
        
        elif y_cor < -290:
            segment.hideturtle()
            segment.sety(300)

    def translate_x(self, segment, x_cor): 
           #If X coordinate is greater than 290, set it to -290
        if x_cor > 290:
            segment.hideturtle()
            segment.setx(-300)
        
        #If X coordinate is less than -290, set it to 290
        elif x_cor < -300:
            segment.hideturtle()
            segment.setx(290)
        
        segment.showturtle()

    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)
    
    def check_body_collision(self):
        
        for segment in self.snake[1:]:
            if self.snake[0].distance(segment) < 10:
                return True
        return False

    def check_cookie_collision(self, cookie):
        if self.snake[0].distance(cookie.cookie) < 20:
            print("Cookie eaten")
            cookie.create_cookie()
            self.add_segment(self.snake[-1].position())
            return 1
        
        return 0
        