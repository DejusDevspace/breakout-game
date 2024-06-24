from turtle import Turtle

SCORE_FONT = ('Montserrat', 15, 'normal')
# GAME_OVER_FONT = ('Montserrat', 30, 'bold')
LIVES_FONT = ('Montserrat', 12, 'normal')


class Interface(Turtle):
    def __init__(self, **kwargs):
        # Initialize the super class (Turtle)
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        # List of brick objects
        self.bricks = []
        # Borders for collision coordinates
        self.borders = {
            'left': -370,
            'right': 360,
            'bottom': -265,
            'top': 270,
        }
        # Dictionary of brick layers and corresponding layer colors
        self.layers = kwargs.get('layers', {
            # y position: color
            (220, 240): 'red',
            (180, 200): 'orange',
            (140, 160): 'green',
            (100, 120): 'yellow'
        })
        # Check if user inputs a dictionary: if specifying layers manually
        if not isinstance(self.layers, dict):
            raise TypeError("parameter: 'layers' must be a dictionary")

        self.score = 0
        self.score_text = None
        self.lives = 5  # Default number of lives
        self.live_text = None
        self.hearts = ''

    def setup_(self):
        """
        Creates the specified layers of bricks and their colors on the game interface.

        Format: (y-axis position): 'color'

        Default layers:
            {
                (220, 240): 'red',
                (180, 200): 'orange',
                (140, 160): 'green',
                (100, 120): 'yellow'
            }

        Initializes the scoreboard.
        """

        # ----- Creating layers of brick ----- #
        for heights, color in self.layers.items():
            # Loop through each height position
            for i in heights:
                for j in range(-355, 370, 50):
                    brick = Turtle()
                    brick.shape('square')
                    brick.color(color)
                    brick.shapesize(stretch_wid=0.5, stretch_len=2)
                    brick.penup()
                    brick.goto(j, i)
                    self.bricks.append(brick)

        # ----- Creating a straight line at the top of the game interface ----- #
        self.draw_hor_line(290)

        # ----- Creating the score object ----- #
        self.score_text = Turtle()
        self.score_text.color('white')
        self.score_text.penup()
        self.score_text.goto(-10, 265)
        self.write_score(self.score_text)
        self.score_text.hideturtle()

        self.live_text = Turtle()
        self.live_text.color('cyan')
        self.live_text.penup()
        self.live_text.goto(200, 265)
        self.write_lives(self.live_text, self.lives)
        self.live_text.hideturtle()

        # ----- Creating a straight line at the bottom of the score object ----- #
        self.draw_hor_line(260)

        # Creating lines at both edges of the interface to indicate boundaries
        self.draw_ver_line(370)
        self.draw_ver_line(-400)

        # Creating a horizontal line at the bottom of the game interface
        self.draw_hor_line(-285)

    @staticmethod
    def draw_hor_line(y: int) -> None:
        """
        Draws a line at the specified horizontal position on the interface.

        :param y: The y-coordinate at which to draw the line.
        :type y: int
        """
        for i in range(-400, 400, 20):
            line = Turtle()
            line.shape('square')
            line.color('white')
            line.penup()
            line.shapesize(stretch_wid=0.1, stretch_len=2)
            line.goto(i, y)
            line.pendown()
            line.forward(10)
            line.penup()

    @staticmethod
    def draw_ver_line(x: int) -> None:
        """
        Draws a line at the specified vertical position on the interface.

        :param x: The x-coordinate at which to draw the line.
        :type x: int
        """
        for i in range(-290, 290, 40):
            line = Turtle()
            line.shape('square')
            line.color('white')
            line.setheading(0)
            line.penup()
            line.shapesize(stretch_wid=2, stretch_len=0.1)
            line.goto(x, i)
            line.forward(10)
            line.penup()

    def write_score(self, score_object: Turtle) -> None:
        """
        Writes the current score of the player on the game interface

        :param score_object: The object to write the score with.
        :type score_object: Turtle instance
        """
        score_object.write('Score: {:03}'.format(self.score), align='center', font=SCORE_FONT)

    def write_lives(self, lives_object: Turtle, lives: int) -> None:
        """
        Writes the number of lives the player has left

        :param lives_object: The object to write the lives with
        :param lives: The number of lives the player has
        :type lives_object: Turtle instance
        :type lives: int
        """
        for i in range(lives):
            self.hearts += '❤️'
        lives_object.write(f'{self.hearts}', align='left', font=LIVES_FONT)

    def update_score(self, points: int) -> None:
        """
        Updates the score of the user by specified number of points and writes it on the interface

        :param points: The number of points to be added to current score
        :type points: int
        """
        self.score_text.clear()
        self.score += points
        self.write_score(self.score_text)

    def update_lives(self):
        pass

    def refresh(self):
        # TODO: Add refresh functionality
        pass

    # TODO: Create lives count (hearts)
