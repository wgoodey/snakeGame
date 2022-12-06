from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Lucida Console", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self, upper_bounds, segment_size, high_score=0):
        super().__init__()
        self.score = 0
        self.high_score = high_score
        self.upper_bounds = upper_bounds
        self.segment_size = segment_size
        self.color("red")
        self.penup()
        self.hideturtle()
        self.score_position = (0, upper_bounds - segment_size)
        self.goto(self.score_position)
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()

    def set_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        self.set_high_score()


    def reset_scoreboard(self):
        self.clear()
        self.__init__(self.upper_bounds, self.segment_size, self.high_score)

