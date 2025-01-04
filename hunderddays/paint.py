
import turtle

from ColorManager import ColorManager
class TurtleManager:
    def __init__(self, path_to_image):
        self.screen = self._setup_screen()
        self.franky = self._setup_turtle()
        self.color_manager = ColorManager(path_to_image)
        self.franky.speed(1)

    def set_speed(self, speed):
        self.franky.speed(speed)
        
    def _setup_screen(self):
        screen = turtle.Screen()
        screen.screensize(300, 300)
        turtle.colormode(255)
        return screen
        
    def _setup_turtle(self):
        franky = turtle.Turtle('turtle')
        franky.penup()
        franky.hideturtle()
        franky.goto(self.screen.screensize()[0], self.screen.screensize()[1])
        franky.showturtle()
        franky.pendown()
        return franky
        
    def draw_rectangle(self):
        coordinates = [
            (-self.screen.screensize()[0], self.screen.screensize()[1]),
            (-self.screen.screensize()[0], -self.screen.screensize()[1]),
            (self.screen.screensize()[0], -self.screen.screensize()[1]),
            (self.screen.screensize()[0], self.screen.screensize()[1])
        ]
        
        self.franky.color(self.color_manager.get_random_color())
        
        for coordinate in coordinates:
            self.franky.goto(coordinate)
        
            
    def draw_circle(self):
        
        self.franky.penup()
        self.franky.goto(0, -self.screen.screensize()[1])
        self.franky.pendown()
        self.franky.color(self.color_manager.get_random_color())
        self.franky.circle(self.screen.screensize()[0])
        
        
    def draw_triangle(self):
        coordinates_triangles = [
            (self.screen.screensize()[0], self.screen.screensize()[1]),
            (-self.screen.screensize()[0], self.screen.screensize()[1]),
            (0, -self.screen.screensize()[1])
        ]
        self.franky.color(self.color_manager.get_random_color())
        
        for coordinate in coordinates_triangles:
            self.franky.dot(20, 'yellow')
            self.franky.goto(coordinate)
        
            
    def run(self):
        self.draw_rectangle()
        self.franky.begin_fill()
        self.draw_circle()
        self.draw_triangle()
        self.franky.end_fill()
        print(self.screen.screensize())
        print(self.franky.position())
        self.screen.exitonclick()

if __name__ == "__main__":
    app = TurtleManager('image.jpg')
    app.set_speed(10)
    app.run()