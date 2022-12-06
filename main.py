from tkinter import messagebox
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SCREEN_SIZE = 600
SEGMENT_SIZE = 20
FOOD_SIZE = SEGMENT_SIZE / 2
LOWER_BOUNDS = int(-(SCREEN_SIZE / 2) + FOOD_SIZE)
UPPER_BOUNDS = int((SCREEN_SIZE / 2) - FOOD_SIZE)

screen = Screen()
screen.setup(SCREEN_SIZE, SCREEN_SIZE)
screen.tracer(False)
screen.bgcolor("black")
screen.title("Snake")
screen.listen()

food = Food(SEGMENT_SIZE, LOWER_BOUNDS, UPPER_BOUNDS)
snake = Snake(SEGMENT_SIZE)
scoreboard = Scoreboard(UPPER_BOUNDS, FOOD_SIZE)


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
        invalid_food_positions = [food.position()]
        while food.position() in invalid_food_positions:
            food.move()
            for segment in snake.snake:
                if food.distance(segment) < FOOD_SIZE:
                    invalid_food_positions.append(food.position())

        snake.add_segment()
        scoreboard.increase_score()


def is_game_over():
    x, y = snake.head.position()
    if x <= LOWER_BOUNDS or y <= LOWER_BOUNDS or x >= UPPER_BOUNDS or y >= UPPER_BOUNDS:
        return True

    # check if head is in same position as any snake segment
    for segment in snake.snake[4:]:
        if snake.head.distance(segment) < FOOD_SIZE:
            return True

    return False


def set_listeners(scr):
    scr.onkeypress(key="Up", fun=up)
    scr.onkeypress(key="Down", fun=down)
    scr.onkeypress(key="Left", fun=left)
    scr.onkeypress(key="Right", fun=right)
    scr.onkeypress(key="Return", fun=restart)


def move():
    snake.move()
    check_if_food_eaten()
    screen.update()
    time.sleep(.1)
    screen.update()


def play():
    while True:
        move()
        if is_game_over():
            scoreboard.game_over()
            return False


def restart():
    scoreboard.reset_scoreboard()
    snake.reset()


set_listeners(screen)

while True:
    restart()
    game_over = is_game_over()
    while not game_over:
        game_over = play()

