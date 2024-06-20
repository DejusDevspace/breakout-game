from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from ui import Interface
import time

# Default: Brick scores...
RED, ORANGE, GREEN, YELLOW = 7, 5, 3, 1


def missed_paddle(obj: Turtle) -> bool:
    """
    Checks if the ball falls below the paddle's position on the interface

    :param obj: The object to check position of
    :type obj: An instance of the Turtle class
    :return: True if ball falls below paddle position, False otherwise
    :rtype: bool
    """
    if obj.ycor() < interface.borders['bottom']:
        return True
    return False


# Create the screen object
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title('Breakout')

# Accelerate drawing process and placement of instances on the screen
screen.tracer(0)

# Create an instance of the paddle object
paddle = Paddle()

# Create and instance of the ball object
ball = Ball()

# Create and initialize the game interface
interface = Interface()
interface.setup_()

# Adding event listeners to the screen for key presses
screen.listen()
# Move to the left while left key is pressed
screen.onkeypress(paddle.move_left, 'Left')
# Move to the right while right key is pressed
screen.onkeypress(paddle.move_right, 'Right')

start = True
while start:
    time.sleep(ball.sleep_time)
    screen.update()
    ball.move()

    # Checking if the ball makes contact with the paddle
    if ball.distance(paddle) < paddle.collision_distance and ball.ycor() < paddle.position:
        ball.ver_bounce()

    # Checking if ball is out of bounds horizontally
    if ball.xcor() < interface.borders['left'] or ball.xcor() > interface.borders['right']:
        ball.hor_bounce()

    # Checking if ball is out of bounds vertically (top only)
    if ball.ycor() > interface.borders['top']:
        ball.ver_bounce()

    # Checking if the paddle misses the ball
    if missed_paddle(ball):
        # TODO: Player loses a point
        pass

screen.exitonclick()
