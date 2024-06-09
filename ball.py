from turtle import Turtle
# import time

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
        self.sleep_time = 0.1

    def move(self):
        """Moves the ball along the game interface"""
        new_x = self.xcor() - self.x_move  # Negative addition to make ball move downwards
        new_y = self.ycor() - self.y_move
        self.goto(new_x, new_y)
