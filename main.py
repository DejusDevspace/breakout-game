from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from ui import Interface
import time

# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------ SETUP ------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

# Default: Brick scores...
scores = {
    'yellow': 1,
    'green': 3,
    'orange': 5,
    'red': 7
}


def missed_paddle(obj: Turtle) -> bool:
    """
    Checks if the ball falls below the paddle's position on the interface

    :param obj: The object to check position of
    :type obj: An instance of the Turtle class
    :return: True if object falls below paddle position, False otherwise
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

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------- GAME ------------------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #

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
        # TODO: Player loses a life
        pass

    # TODO: Ball pace increments: 4 hits, 12 hits, collision with orange and red bricks
    # TODO: Paddle shrinks to one-half its size after ball breaks through to the upper wall

    # Checking if the ball hits a brick
    for brick in interface.bricks:
        if ball.distance(brick) < 30:
            # Bounce the ball in the opposite direction
            ball.ver_bounce()
            # Remove the brick from the interface
            brick.hideturtle()
            # Remove the bricks from the list of bricks
            interface.bricks.remove(brick)
            # Increase the score according to the color of the brick that was hit
            interface.update_score(scores[brick.color()[0]])

screen.exitonclick()
