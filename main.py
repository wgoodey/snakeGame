from turtle import Turtle, Screen
from random import randint

SCREEN_SIZE = 600
LOWER_BOUNDS = int(-(SCREEN_SIZE / 2) + 10)
UPPER_BOUNDS = int((SCREEN_SIZE / 2) - 10)
SEGMENT_SIZE = 20
snake = []
food = Turtle("circle")
food.color("white")
food.penup()
# decrease food size by half
food.shapesize(0.5, 0.5)


def round_to(base=10, number=0):
    return base * round(number / base)


def update_position(coordinates, heading, mode):
    if mode == "add":
        mode = -1
    elif mode == "move":
        mode = 1

    # get position
    x, y = coordinates

    # update position
    if heading == 0:
        x += SEGMENT_SIZE * mode
    # facing left
    elif heading == 180:
        x -= SEGMENT_SIZE * mode
    # facing up
    elif heading == 90:
        y += SEGMENT_SIZE * mode
    # facing down
    else:
        y -= SEGMENT_SIZE * mode

    return x, y


def create_snake():
    for _ in range(3):
        add_segment()


def add_segment():
    if len(snake) == 0:
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
    else:
        new_segment = snake[len(snake) - 1].clone()
        position = new_segment.position()
        heading = new_segment.heading()
        new_segment.goto(update_position(position, heading, "add"))

    snake.append(new_segment)


def move_snake():
    screen.tracer(False)
    previous_position = snake[0].position()
    snake[0].goto(update_position(previous_position, snake[0].heading(), "move"))

    for i in range(1, len(snake)):
        current_position = snake[i].position()
        snake[i].goto(previous_position)
        previous_position = current_position

    screen.tracer(True)


def up():
    change_direction(90)


def down():
    change_direction(270)


def left():
    change_direction(180)


def right():
    change_direction(0)


def change_direction(angle):
    if abs(angle - snake[0].heading()) != 180:
        screen.tracer(False)
        snake[0].setheading(angle)
        screen.tracer(True)


def move_food():
    x = randint(LOWER_BOUNDS, UPPER_BOUNDS)
    y = randint(LOWER_BOUNDS, UPPER_BOUNDS)
    # round to make sure it lines up with snake
    x = round_to(base=SEGMENT_SIZE, number=x)
    y = round_to(base=SEGMENT_SIZE, number=y)

    screen.tracer(False)
    food.goto(x, y)
    screen.tracer(True)


def check_if_food_eaten():
    if snake[0].position() == food.position():
        add_segment()


def set_listeners(scr):
    scr.onkey(key="e", fun=up)
    scr.onkey(key="d", fun=down)
    scr.onkey(key="s", fun=left)
    scr.onkey(key="f", fun=right)
    scr.onkey(key="space", fun=move_snake)
    scr.onkey(key="\t", fun=add_segment)


screen = Screen()
screen.setup(SCREEN_SIZE, SCREEN_SIZE)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(False)
screen.listen()

set_listeners(screen)

create_snake()
add_segment()
move_food()

screen.exitonclick()
