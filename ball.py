from turtle import Turtle

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
        self.speed = 0.1  # Controls the speed of the ball
        self.sped_up = False
        self.hit_count = 0
        self.upper_col = 0

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

    def speed_up(self) -> None:
        """Increases the speed of the ball"""
        self.speed *= 0.7

    def refresh(self) -> None:
        """Returns the ball to the starting position and resets the ball speed"""
        self.home()
        self.hit_count = 0
        self.speed = 0.1
