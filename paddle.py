from turtle import Turtle

# The position increment for movement
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self):
        # Initialize the super class
        super().__init__()
        self.shape('square')
        self.color('blue')
        self.penup()  # Avoids drawing line on movement
        self.goto(0, -250)
        self.shapesize(stretch_wid=0.5, stretch_len=5)  # Size of the paddle object

    def move_left(self) -> None:
        """Moves the paddle to the left along the x-axis."""
        x_position = self.xcor()  # Get the current x coordinate
        # Subtract the move distance from the current x coordinate and go there
        self.goto(x=x_position - MOVE_DISTANCE, y=self.ycor())

    def move_right(self) -> None:
        """Moves the paddle to the right along the x-axis."""
        x_position = self.xcor()  # Get the current x coordinate
        # Add the move distance to the current x coordinate and go there
        self.goto(x=x_position + MOVE_DISTANCE, y=self.ycor())
