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
        self.sleep_time = 0.1  # Controls the speed of the ball

    def move(self) -> None:
        """Moves the ball along the game interface"""
        # TODO: Attempt making ball move in different directions upon starting (x-axis randomization??)
        new_x = self.xcor() - self.x_move  # Negative addition to make ball move downwards
        new_y = self.ycor() - self.y_move
        self.goto(new_x, new_y)

    # TODO: Create bouncing effects for collisions
    def ver_bounce(self) -> None:
        """
        Vertical bounce: Moves the ball in the opposite direction along the y-axis
        """
        pass

    def hor_bounce(self) -> None:
        """
        Horizontal bounce: Moves the ball in the opposite direction along the x-axis
        """
        pass
