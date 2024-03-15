import turtle


class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()  # Call the constructor of the superclass
        self.penup()  # Lift the pen to avoid drawing lines
        self.color('white')  # Set the color of the paddle to white
        self.shape("square")  # Set the shape of the paddle to a square
        self.turtlesize(stretch_wid=5, stretch_len=1)  # Stretch the square to make it a rectangle
        self.setposition(position)  # Set the initial position of the paddle

    def up(self):
        # Move the paddle up by adjusting its y-coordinate
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        # Move the paddle down by adjusting its y-coordinate
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
