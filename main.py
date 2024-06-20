from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from ui import Interface
import time

# Default:
RED, ORANGE, GREEN, YELLOW = 7, 5, 3, 1


def out_of_bounds(obj: Turtle) -> bool:
    if obj.ycor() < interface.borders['bottom'] or obj.ycor() > interface.borders['top'] or obj.xcor() \
            < interface.borders['left'] or obj.xcor() > interface.borders['right']:
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
    # Checking if ball is out of bounds
    if out_of_bounds(ball):
        print('Out of bounds!')

screen.exitonclick()
