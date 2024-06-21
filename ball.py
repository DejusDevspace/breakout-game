from turtle import Turtle
# import time
from random import randint

# Distance for movement of the ball across the screen
MOVE_DISTANCE = 10


class Ball(Turtle):
    def __init__(self):
        # Initialize the super class (Turtle)
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_DISTANCE
        self.sleep_time = 0.1  # Controls the speed of the ball

    def move(self) -> None:
        """Moves the ball along the game interface"""
        new_x = self.xcor() - self.x_move
        new_y = self.ycor() - self.y_move  # Negative addition to make ball move downwards
        self.goto(new_x, new_y)

    def ver_bounce(self) -> None:
        """
        Vertical bounce: Moves the ball in the opposite direction along the y-axis
        """
        self.y_move *= -1

    def hor_bounce(self) -> None:
        """
        Horizontal bounce: Moves the ball in the opposite direction along the x-axis
        """
        self.x_move *= -1

    def speed_up(self):
        # TODO: Increase ball speed
        self.sleep_time *= 0.7

    def refresh(self):
        # TODO: Create ball reset functionality
        pass
