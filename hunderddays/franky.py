import turtle

# Initialize Screen
screen = turtle.Screen()
# screen.setup(width=800, height=600)
screen.title("Turtle Graphics")

# Create Turtle
franky = turtle.Turtle()
franky.shape("turtle")
franky.color("blue")

# Perform Actions
try:
    franky.penup()
    franky.goto(0, 100)
    franky.pendown()
    franky.circle(50)
except turtle.TurtleGraphicsError as e:
    print(f"Turtle graphics error: {e}")

# Keep Window Open
screen.exitonclick()
