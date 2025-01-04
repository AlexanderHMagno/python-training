#class Car
#attributes: color, make, model, year
#methods: drive, stop, turn

class Car:
    def __init__(self, color, make, model, year):
        self.color = color
        self.make = make
        self.model = model
        self.year = year


    def drive(self):
        print(f"The {self.color} {self.make} {self.model} is driving.")

    def stop(self):
        print(f"The {self.color} {self.make} {self.model} is stopping.")

    def turn(self, direction):
        print(f"The {self.color} {self.make} {self.model} is turning {direction}.")