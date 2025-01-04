from turtle import Screen
from Turtle import Turtle


# screen = Screen()
# screen.exitonclick()

# Create a turtle
STEPS = 100

franky = Turtle()
# franky.square(STEPS)
# # franky.circle(STEPS)
# franky.triangle(STEPS)
# franky.hexagon(STEPS)
# franky.octagon(STEPS)
# franky.pentagon(STEPS)
# franky.heptagon(STEPS)
# franky.nonagon(STEPS)
# franky.decagon(STEPS)
# franky.draw_shape(20, STEPS)
franky.change_tickness(1)
franky.change_speed(100)

# for _ in range(STEPS):
#     franky.random_path(STEPS, straight=True)

for _ in range(360):
    franky.spirograph(100, 1)
    franky.change_color()


screen = Screen()
screen.exitonclick()
