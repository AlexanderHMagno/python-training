import turtle




#I want to create a turtle that can move up, down, left, right with w d s a keys  
screen = turtle.Screen()
tim = turtle.Turtle()

def move_forwards():
    tim.forward(50)

def move_backwards():
    tim.backward(10)

def turn_left():
    tim.left(50)

def turn_right():
    tim.right(10)

def circle():
    tim.circle(50)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def toggle_fill():
    if tim.filling():
        tim.end_fill()
    else:
        tim.begin_fill()

screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards) 
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.onkey(key="f", fun=toggle_fill)
screen.onkey(key="g", fun=circle)
tim.end_fill()
screen.exitonclick()





