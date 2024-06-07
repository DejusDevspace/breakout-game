from turtle import Screen
from paddle import Paddle
from ui import Interface

# Create the screen object
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title('Breakout')

# Accelerate drawing
screen.tracer(0)

# Create an instance of the paddle object
paddle = Paddle()

# Create and initialize the game interface
interface = Interface()
interface.initialize()

# Add an event listener to the screen for key presses
screen.listen()
# Move the left while left key is pressed
screen.onkeypress(paddle.move_left, 'Left')
# Move the right while right key is pressed
screen.onkeypress(paddle.move_right, 'Right')

# Show the screen after drawings have been made
screen.update()
screen.exitonclick()
