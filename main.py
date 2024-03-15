import turtle
import paddle
import time
import ball
import scoreboard

# Set up the game screen
screen = turtle.Screen()
screen.screensize(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # Turn off automatic screen updates

# Create left and right paddles
l_paddle = paddle.Paddle((450, 0))
r_paddle = paddle.Paddle((-450, 0))

# Create the ball and scoreboard objects
ball = ball.Ball()
scoreboard = scoreboard.ScoreBoard()

# Draw the design at the bottom of the screen
design = turtle.Turtle()
design.color("white")
design.hideturtle()
design.penup()
design.goto(0, -300)

coordinates = [[90, 30], [180, 23], [270, 30], [0, 46], [90, 30], [180, 23]]
for move in coordinates:
    design.setheading(move[0])
    for i in range(move[1]):
        design.pendown()
        design.forward(10)
        design.penup()
        design.forward(10)

# Set up keyboard bindings for paddle movement
screen.listen()
screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")
screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")

# Main game loop
game_is_on = True
while game_is_on:
    # Update the screen
    screen.update()
    # Pause to control the ball's movement speed
    time.sleep(ball.move_speed)
    # Move the ball
    ball.move()

    # Handle ball bouncing off top and bottom walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.y_bounce()

    # Handle ball bouncing off paddles
    if ball.xcor() == 430 and ball.distance(l_paddle) < 60 or ball.xcor() == -430 and ball.distance(r_paddle) < 60:
        ball.x_bounce()

    # Handle scoring when ball passes left or right boundary
    if ball.xcor() > 450:
        scoreboard.clear()
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -450:
        scoreboard.clear()
        scoreboard.r_point()
        ball.reset_position()

# Exit the game when clicked
screen.exitonclick()
