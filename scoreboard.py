from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Lucida Console", 12, "normal")
GAME_OVER = "GAME OVER"
DATA = "data.txt"


class Scoreboard(Turtle):

    def __init__(self, upper_bounds, segment_size):
        super().__init__()
        try:
            with open(DATA) as data:
                try:
                    high_score = int(data.read())
                except ValueError:
                    high_score = 0
        except FileNotFoundError:
            high_score = 0
        self.high_score = high_score
        self.score = 0

        self.upper_bounds = upper_bounds
        self.segment_size = segment_size
        self.color("red")
        self.penup()
        self.hideturtle()
        self.score_position = (0, upper_bounds - segment_size)
        self.update()


    def increase_score(self):
        self.score += 1
        self.update()

    def set_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(DATA, mode="w") as data:
                data.write(str(self.high_score))


    def update(self):
        self.clear()
        self.goto(self.score_position)
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.set_high_score()
        self.goto(0, 0)
        self.write(GAME_OVER, align=ALIGNMENT, font=FONT)


    def reset_scoreboard(self):
        self.clear()
        self.__init__(self.upper_bounds, self.segment_size)
