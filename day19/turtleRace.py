import turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class MessageTurtle:
    def __init__(self, height):
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.penup() 
        self.turtle.goto(0, height)

    def write(self, message, align = "center", font = ("Arial", 16, "bold") ):
        self.clear()
        self.turtle.write(message, align=align, font=font)
    
    def clear(self):
        self.turtle.clear()
        


class TurtleCreator:
    def __init__(self, color):
      self.turtle = turtle.Turtle(shape='turtle')
      self.turtle.color(color)
      self.turtle.penup()
      
    def goto(self, x, y):
        self.turtle.goto(x, y)

    def move(self):
        self.turtle.forward(random.randint(1, 5))
    

class TurtleRace:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(width=500, height=400)
        self.screen.title("Turtle Race")
        self.turtles = []
        self.starting_y_position = []
        self.num_turtles = 0
        self.predicted_winner = ""
        self.message_turtle = MessageTurtle(-180)
        self.message_static = MessageTurtle(-160)
        
    
    def _create_turtles(self):

        height = self.screen.screensize()[1]
        distance = height / ( self.num_turtles)
        self.starting_y_position = [(height / 2) - (i * distance) for i in range(self.num_turtles)]
        for i in range(self.num_turtles):
            turtle = TurtleCreator(COLORS[i % len(COLORS)])
            self.turtles.append(turtle)
    
    def set_starting_position(self):
        for turtle in self.turtles:
            turtle.goto(-230, self.starting_y_position[self.turtles.index(turtle)])

    def start_race(self):
        while not self.check_winner()[0]:
            self.check_lider()
            for turtle in self.turtles:
                turtle.move()
        self.check_predicted_winner()

    def check_lider(self):
        lider = self.turtles[0]
        for turtle in self.turtles:
            if turtle.turtle.xcor() > lider.turtle.xcor():
                lider = turtle
        
        self.message_turtle.write(lider.turtle.color()[0])


    def check_winner(self):
        for turtle in self.turtles:
            if turtle.turtle.xcor() > 220:
                return (True, turtle.turtle.color()[0])
        return (False, None)

    def check_predicted_winner(self):
        if self.predicted_winner == self.check_winner()[1]:
            self.message_turtle.write(f"You won! The winner is {self.check_winner()[1]}")
        else:
            self.message_turtle.write(f"You lost! The winner is {self.check_winner()[1]}")
        
        restart = turtle.textinput("Turtle Race", "Do you want to play again? (y/n)")
        if restart == "y":
            self.inittialize_race()
        else:
            self.screen.bye()
    
    def clear_screen(self):
        self.turtles = []
        self.starting_y_position = []
        self.screen.clear()
        self.message_static.write("The lider is: ", align="center", font=("Arial", 16, "bold"))
    
    def inittialize_race(self):
        self.clear_screen()
        self.num_turtles = int(turtle.numinput("Turtle Race", "How many turtles do you want to race? (1-20)", minval=1, maxval=20, default=6) )
        self._create_turtles()
        self.set_starting_position()
        self.predicted_winner = turtle.textinput("Turtle Race", f"Who will win the race? Enter a color: {'/ '.join(COLORS)}").lower()
        self.start_race()


turtle_race = TurtleRace()
turtle_race.inittialize_race()
turtle_race.screen.exitonclick()
