import turtle

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.writer = turtle.Turtle()
        self.writer.hideturtle()
        self.writer.penup()
        self.writer.color("white")
        self.update_score()

    def update_score(self):
        self.writer.clear()
        self.writer.goto(0, 290 - 40)
        self.writer.write(f"Score: {self.score}", align="center", font=("Arial", 18, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_score()