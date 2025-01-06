from turtle import Turtle

class Scoreboard(Turtle):
    score = 0
    high_score = 0
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.get_high_score()
        self.update_score()

    def get_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            self.high_score = 0
        return self.high_score

    def update_score(self):
        self.clear()
        self.goto(0, 290 - 40)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 18, "bold"))

    def game_over(self):
        self.goto(0, -200)
        self.write("Game Over", align="center", font=("Arial", 24, "bold"))

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score

            print(f"New high score: {self.high_score}")
            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))
        self.update_score()