
from turtle import Turtle
from random import randint


def round_to(base=10, number=0):
    return base * round(number / base)


class Food(Turtle):

    def __init__(self, segment_size, lower_bounds, upper_bounds):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.penup()

        self.segment_size = segment_size
        self.lower_bounds = lower_bounds
        self.upper_bounds = upper_bounds
        self.move()

    def move(self):
        x = randint(self.lower_bounds, self.upper_bounds)
        y = randint(self.lower_bounds, self.upper_bounds)
        # round to make sure it lines up with snake
        x = round_to(base=self.segment_size, number=x)
        y = round_to(base=self.segment_size, number=y)

        self.goto(x, y)
