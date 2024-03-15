import turtle

FONT = ("Courier", 50, "normal")  # Define the font for the scoreboard text


class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()  # Call the constructor of the superclass
        self.color("white")  # Set the color of the text to white
        self.penup()  # Lift the pen to avoid drawing lines
        self.hideturtle()  # Hide the turtle icon
        self.l_score = 0  # Initialize the left player's score to 0
        self.r_score = 0  # Initialize the right player's score to 0
        self.update_scoreboard()  # Update the scoreboard with the initial scores

    def update_scoreboard(self):
        # Move the turtle to the left player's score position and write the score
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=FONT)
        # Move the turtle to the right player's score position and write the score
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=FONT)

    def l_point(self):
        # Increment the left player's score by 1 and update the scoreboard
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        # Increment the right player's score by 1 and update the scoreboard
        self.r_score += 1
        self.update_scoreboard()
