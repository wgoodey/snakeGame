from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self, upper_bounds, segment_size):
        super().__init__()
        self.score = 0
        self.upper_bounds = upper_bounds
        self.segment_size = segment_size
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.goto(0, upper_bounds - segment_size)
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
