from turtle import Screen
from snake import Snake
from food import Food
import time

SCREEN_SIZE = 600
LOWER_BOUNDS = int(-(SCREEN_SIZE / 2) + 10)
UPPER_BOUNDS = int((SCREEN_SIZE / 2) - 10)
SEGMENT_SIZE = 20
FOOD_SIZE = SEGMENT_SIZE / 2

screen = Screen()
screen.setup(SCREEN_SIZE, SCREEN_SIZE)
screen.tracer(False)
screen.bgcolor("black")
screen.title("Snake")
screen.listen()

food = Food(SEGMENT_SIZE, LOWER_BOUNDS, UPPER_BOUNDS)
snake = Snake(SEGMENT_SIZE)


def up():
    snake.change_direction(90)


def down():
    snake.change_direction(270)


def left():
    snake.change_direction(180)


def right():
    snake.change_direction(0)


def check_if_food_eaten():
    if snake.head.distance(food.position()) < FOOD_SIZE:
        print("ate food")
        food.move()
        snake.add_segment()

def game_over():
    x, y = snake.get_position()
    if x <= LOWER_BOUNDS or y <= LOWER_BOUNDS or x >= UPPER_BOUNDS or y >= UPPER_BOUNDS:
        return True
    # check if head is in same position as any snake segment

    return False


def set_listeners(scr):
    scr.onkeypress(key="e", fun=up)
    scr.onkeypress(key="d", fun=down)
    scr.onkeypress(key="s", fun=left)
    scr.onkeypress(key="f", fun=right)

    # TODO: remove these listeners
    scr.onkeypress(key="space", fun=move)
    # scr.onkeypress(key="\t", fun=add_segment)


def move():
    snake.move()
    check_if_food_eaten()
    screen.update()
    time.sleep(.1)
    screen.update()


set_listeners(screen)

while True:
    move()
    if game_over():
        break

screen.exitonclick()
