from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title('Breakout')

paddle = Paddle()

# Add an event listener to the screen for key presses
screen.listen()
screen.onkeypress(paddle.move_left, 'Left')
screen.onkeypress(paddle.move_right, 'Right')

screen.exitonclick()
