from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.snake_head = self.snake[0]

    def create_snake(self):
        snake_head = Turtle(shape="square")
        snake_head.penup()
        snake_head.color("green")
        self.snake.append(snake_head)

        for i in range(1, 3):
            self.grow_snake(i)

    def grow_snake(self, index):
        self.snake.append(Turtle(shape="square"))
        self.snake[index].color("white")
        self.snake[index].penup()

        x_cor = self.snake[index - 1].xcor()
        y_cor = self.snake[index - 1].ycor()
        self.snake[index].goto(x=x_cor, y=y_cor)

    def reset_snake(self):
        for body_part in self.snake:
            body_part.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.snake_head = self.snake[0]

    def extend(self):
        self.grow_snake(len(self.snake))

    def move(self, move_distance=20):
        move_distance = move_distance

        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(x=new_x, y=new_y)
        self.snake_head.forward(move_distance)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
