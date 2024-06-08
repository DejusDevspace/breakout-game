from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        # Initialize the super class (Turtle)
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        # self.x_move = 10
        # self.y_move = 10
        # self.sleep_time = 0.1
