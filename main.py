from turtle import Screen
from paddle import Paddle
from ball import Ball
from ui import Interface
import time

# TODO: Declare points variables for different brick layers

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
    # Test
    if ball.ycor() < interface.borders['bottom']:
        print('collision')

screen.exitonclick()
