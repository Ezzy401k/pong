import turtle


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()  # Call the constructor of the superclass
        self.shape("circle")  # Set the shape of the ball to a circle
        self.color("white")  # Set the color of the ball to white
        self.penup()  # Lift the pen to avoid drawing lines
        self.x_move = 10  # Set the initial movement speed in the x-direction
        self.y_move = 10  # Set the initial movement speed in the y-direction
        self.move_speed = 0.1  # Set the initial movement speed

    def move(self):
        # Calculate the new position of the ball based on the current movement speed
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        # Move the ball to the new position
        self.goto(new_x, new_y)

    def y_bounce(self):
        # Reverse the direction of movement in the y-direction (cause bounce)
        self.y_move *= -1
        # Reduce the movement speed to simulate damping
        self.move_speed *= 0.9

    def x_bounce(self):
        # Reverse the direction of movement in the x-direction (cause bounce)
        self.x_move *= -1
        # Reduce the movement speed to simulate damping
        self.move_speed *= 0.9

    def reset_position(self):
        # Reset the position of the ball to the center of the screen
        self.goto(0, 0)
        # Reverse the direction of movement in the x-direction (change direction)
        self.x_move *= -1
        # Reset the movement speed to its initial value
        self.move_speed = 0.1
