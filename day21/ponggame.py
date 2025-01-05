from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

class PongGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Pong Game")
        self.screen.tracer(0)
        self.game_is_on = True

        self.paddle_left = Paddle((-350, 0))
        self.paddle_right = Paddle((350, 0))
        self.ball = Ball()
        self.scoreboard = Scoreboard()

        self.screen.listen()
        self.screen.onkey(self.paddle_left.move_up, "w")
        self.screen.onkey(self.paddle_left.move_down, "s")
        self.screen.onkey(self.paddle_right.move_up, "Up")
        self.screen.onkey(self.paddle_right.move_down, "Down")

    def start_game(self):

        while self.game_is_on:
            time.sleep(self.ball.move_speed)
            self.screen.update()
            self.ball.move()

            # Detect collision with wall
            if self.ball.ycor() > 280 or self.ball.ycor() < -280:
                self.ball.bounce_y()

            # Detect collision with paddle
            if self.ball.distance(self.paddle_left) < 50 and self.ball.xcor() < -320 or self.ball.distance(self.paddle_right) < 50 and self.ball.xcor() > 320:
                self.ball.bounce_x()

            # Detect paddle miss
            if self.ball.xcor() > 380:
                self.scoreboard.l_point()
                self.ball.reset_position()
            if self.ball.xcor() < -380:
                self.scoreboard.r_point()
                self.ball.reset_position()

    def game_over(self):
        self.screen.exitonclick()
