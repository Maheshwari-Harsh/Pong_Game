# TODO 1 Create the screen
# TODO 2 Create and move a paddle
# TODO 3 Create and move a another paddle
# TODO 4 Create and move ball
# TODO 5 Detect collision with wall and bounce
# TODO 6 Detect collision with paddle and bounce
# TODO 7 Detect when paddle misses the ball
# TODO 8 Keep track of score

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

# To draw the dashed line in the middle of the screen.
timmy = Turtle()
timmy.color("white")
timmy.hideturtle()
timmy.penup()
timmy.goto(0, -300)
timmy.setheading(90)
timmy.pendown()
for step in range(60):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect if ball misses the r_paddle
    if ball.xcor() > 380:
        ball.restart()
        scoreboard.l_point()

    # detect if ball misses the l_paddle
    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_point()

screen.exitonclick()
