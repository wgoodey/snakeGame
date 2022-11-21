from turtle import Turtle

INITIAL_LENGTH = 3


class Snake:

    def __init__(self, segment_size, heading=0):
        self.segment_size = segment_size
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.head.setheading(heading)

    def create_snake(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        self.snake.append(new_segment)
        for _ in range(1, INITIAL_LENGTH):
            self.add_segment()

    def add_segment(self):
        new_segment = self.snake[-1].clone()
        self.snake.append(new_segment)

    def change_direction(self, angle):
        if abs(angle - self.head.heading()) != 180:
            self.head.setheading(angle)

    def move(self):
        leader_position = self.head.position()
        self.head.forward(self.segment_size)
        for i in range(1, len(self.snake)):
            current_position = self.snake[i].position()
            self.snake[i].goto(leader_position)
            leader_position = current_position
            self.snake[i].setheading(self.snake[i - 1].heading())
