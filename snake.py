from turtle import Turtle, Screen


class Snake:

    def __init__(self, segment_size, screen, heading=0):
        self.segment_size = segment_size
        self.screen = screen
        self.snake = []
        self.heading = heading

    def create_snake(self):
        for _ in range(3):
            self.add_segment()

    def get_heading(self):
        return self.heading

    def add_segment(self):
        if len(self.snake) == 0:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
        else:
            new_segment = self.snake[len(self.snake) - 1].clone()
            x, y = new_segment.position()
            # get heading and adjust position accordingly
            # facing right
            if new_segment.heading() == 0:
                x -= self.segment_size
            # facing left
            elif new_segment.heading() == 180:
                x += self.segment_size
            # facing up
            elif new_segment.heading() == 90:
                y -= self.segment_size
            # facing down
            elif new_segment.heading() == 270:
                y += self.segment_size

            # move segment to end of body
            new_segment.goto(x, y)

        self.snake.append(new_segment)

    def change_direction(self, angle):
        if abs(angle - self.snake[0].heading()) != 180:
            self.screen.tracer(False)
            self.snake[0].setheading(angle)
            self.screen.tracer(True)
            print(f"Changed heading to {angle}")




