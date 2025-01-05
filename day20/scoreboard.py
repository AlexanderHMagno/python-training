from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 290 - 40)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 18, "bold"))

    def game_over(self):
        self.goto(0, -200)
        self.write("Game Over", align="center", font=("Arial", 24, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_score()