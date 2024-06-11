from turtle import Turtle

SCORE_FONT = ('Montserrat', 15, 'normal')


class Interface(Turtle):
    def __init__(self, **kwargs):
        # Initialize the super class (Turtle)
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.bricks = []
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

    def setup_(self):
        """
        Creates the specified layers of bricks and their colors on the game interface.\n
        \nformat: (y-axis position): 'color'\n
        Default layers:
         \ndict: {
            \n\t(220, 240): 'red',
            \n\t(180, 200): 'orange',
            \n\t(140, 160): 'green',
            \n\t(100, 120): 'yellow'
        \n}
        \nInitializes the scoreboard.
        """
        # ----- Creating layers of brick ----- #
        for heights, color in self.layers.items():
            # Loop through each height position
            for i in heights:
                for j in range(-360, 360, 50):
                    brick = Turtle()
                    brick.shape('square')
                    brick.color(color)
                    brick.shapesize(stretch_wid=0.5, stretch_len=2)
                    brick.penup()
                    brick.goto(j, i)
                    self.bricks.append(brick)

        # ----- Creating a straight line at the top of the screen ----- #
        self.draw_line(290)

        # ----- Creating the score object ----- #
        self.score_text = Turtle()
        self.score_text.color('white')
        self.score_text.penup()
        self.score_text.goto(-50, 265)
        self.write_score(self.score_text)
        self.score_text.hideturtle()

        # ----- Creating a straight line at the bottom of the score object ----- #
        self.draw_line(260)

    @staticmethod
    def draw_line(y_position: int) -> None:
        for i in range(-400, 400, 20):
            line = Turtle()
            line.shape('square')
            line.color('white')
            line.penup()
            line.shapesize(stretch_wid=0.1, stretch_len=2)
            line.goto(i, y_position)
            line.pendown()
            line.forward(10)
            line.penup()

    def write_score(self, score_object: Turtle):
        score_object.write('Score: {:03}'.format(self.score), align='center', font=SCORE_FONT)

    def update_score(self, points: int) -> None:
        """Updates the score of the user by specified number of points"""
        self.score_text.clear()
        self.score += points
        self.write_score(self.score_text)
