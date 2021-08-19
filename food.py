from turtle import Turtle
from random import randrange


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        ran_x = randrange(-280, 280, 20)
        ran_y = randrange(-280, 280, 20)
        self.goto(ran_x, ran_y)

