from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.1)

    snake.move()
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.raise_score()

    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290:
        score.reset_score()
        snake.reset_snake()

    for snake_body in snake.snake[1:]:
        if snake.snake_head.distance(snake_body) < 10:
            score.reset_score()
            snake.reset_snake()

screen.exitonclick()
