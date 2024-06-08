from turtle import Turtle


class Interface(Turtle):
    def __init__(self, **kwargs):
        # Initialize the super class (Turtle)
        super().__init__()
        self.bricks = []
        # Dictionary of brick layers and corresponding layer colors
        self.layers = kwargs.get('layers', {
            # y position: color
            (240, 260): 'red',
            (220, 200): 'orange',
            (180, 160): 'green',
            (140, 120): 'yellow'
        })
        # Check if user inputs a dictionary: if specifying layers manually
        if not isinstance(self.layers, dict):
            raise TypeError("'layers' parameter must be a dictionary")

        self.score = 0

    def __setup__(self):
        """
        Creates the specified layers of bricks and their colors on the game interface.\n
        \nformat: (y-axis position): 'color'\n
        Default layers:
         \ndict: {
            \n\t(240, 260): 'red',
            \n\t(220, 200): 'orange',
            \n\t(180, 160): 'green',
            \n\t(140, 120): 'yellow'
        \n}
        \nInitializes the scoreboard.
        """
        # Create layers of brick
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

        # TODO: Create scoreboards
