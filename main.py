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

def main():
    global start

    while start:
        time.sleep(ball.speed)
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
            # Shrink the size of the paddle
            paddle.shrink()

        # Checking if the paddle misses the ball
        if missed_paddle(ball):
            interface.update_lives()
            print('hit:', ball.hit_count)
            ball.refresh()

        # Checking if the ball hits a brick
        for brick in interface.bricks:
            if ball.distance(brick) < 30:
                # Increase the hit count of the ball
                ball.hit_count += 1
                ball.sped_up = False

                # Bounce the ball in the opposite direction
                ball.ver_bounce()

                # Increase ball speed if ball comes in contact with orange or red bricks
                if brick.color()[0] == 'orange' or brick.color()[0] == 'red':
                    ball.upper_col += 1
                    # Speed increases for every third collision
                    if ball.upper_col % 3 == 0:
                        ball.speed_up()
                        paddle.MOVE_DISTANCE += 5
                        print(f'Three upper bricks: {ball.speed}\nPad: {paddle.MOVE_DISTANCE}')

                # Remove the brick from the interface
                brick.hideturtle()
                # Remove the bricks from the list of bricks
                interface.bricks.remove(brick)
                # Increase the score according to the color of the brick that was hit
                interface.update_score(scores[brick.color()[0]])

        # Increasing ball speed after every 4th and 12th hit
        if ball.hit_count % 4 == 0 and ball.hit_count != 0 and not ball.sped_up:
            ball.speed_up()
            ball.sped_up = True
            print(ball.hit_count)
            print(f'4 hits: {ball.speed}')
        if ball.hit_count % 12 == 0 and ball.hit_count != 0 and not ball.sped_up:
            ball.speed_up()
            ball.sped_up = True
            print(ball.hit_count)
            print(f'12 hits: {ball.speed}')

        # Initialize the next round if the player clears first set of bricks
        if len(interface.bricks) == 0:
            interface.next_round()

        # Check if player is out of lives and end the game
        if interface.lives == 0:
            start = False
            interface.game_over()

        # End the game after two rounds
        if interface.rounds > 2:
            start = False
            interface.winner()

    screen.exitonclick()


if __name__ == '__main__':
    main()
