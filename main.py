import turtle
import paddle
import time
import ball
import scoreboard

screen = turtle.Screen()
screen.screensize(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = paddle.Paddle((450, 0))
r_paddle = paddle.Paddle((-450, 0))

ball = ball.Ball()
scoreboard = scoreboard.ScoreBoard()

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


screen.listen()
screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")
screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")

game_is_on = True

while game_is_on:

    screen.update()  # Update the screen
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.y_bounce()

    if ball.xcor() == 430 and ball.distance(l_paddle) < 60 or ball.xcor() == -430 and ball.distance(r_paddle) < 60:
        ball.x_bounce()

    if ball.xcor() > 450:
        scoreboard.clear()
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -450:
        scoreboard.clear()
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()
