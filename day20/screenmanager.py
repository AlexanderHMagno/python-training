import snake
import turtle
import time
import random
import cookie
import scoreboard

class ScreenManager:

    snake = None
    cookie = None 
    score = 0
    game_is_on = True
    game_paused = False

    def __init__(self):
        self.screen = turtle.Screen()
        self.setup_screen()
        self.restart_game()

    def setup_screen(self):
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Turtlenake Game")
        self.screen.tracer(0)

    def setup_controls(self):
        self.screen.listen()
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down") 
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")
        self.screen.onkey(self.pause_game, "p")
        self.screen.onkey(self.restart_game, "r")

    def pause_game(self):
        print("Game paused")
        if self.game_paused:
            self.game_paused = False
        else:
            self.game_paused = True

    def restart_game(self):
        self.screen.reset()
        self.score = 0
        self.game_is_on = True
        self.game_paused = False
        self.snake = snake.Snake()
        self.cookie = cookie.Cookie()
        self.scoreboard = scoreboard.Scoreboard()
        self.setup_controls()

    def run_game(self):

      #how can i make the cookie appear in a random position? and then make it disappear after it is eaten?
        while self.game_is_on:
            
            self.screen.update()
            time.sleep(0.1)
            
            if not self.game_paused:
                self.snake.move()
                if self.snake.check_cookie_collision(self.cookie):
                    self.scoreboard.increase_score()

                if self.snake.check_body_collision():
                    self.game_is_on = False
                    print("Game over")

        if not self.game_is_on:
          restart = self.screen.textinput("Game Over", "Do you want to play again? (y/n)")
          if restart == "y":
            self.restart_game()
            self.run_game()
        
        self.screen.mainloop()
