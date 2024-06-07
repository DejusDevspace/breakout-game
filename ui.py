from turtle import Turtle


class Interface(Turtle):
    def __init__(self):
        # Initialize the super class (Turtle)
        super().__init__()
        self.bricks = []
        # Dictionary of brick layers and corresponding layer colors
        self.layers = {
            # y position: color
            (240, 260): 'red',
            (220, 200): 'orange',
            (180, 160): 'green',
            (140, 120): 'yellow'
        }

    def initialize(self):
        # TODO: Complete the description
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
