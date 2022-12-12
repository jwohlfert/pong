import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.colormode(255)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

LEFT_POSITION = (-350, 0)
RIGHT_POSITION = (350, 0)

ball = Ball()
right_paddle = Paddle(paddle_coordinates=RIGHT_POSITION)
left_paddle = Paddle(paddle_coordinates=LEFT_POSITION)
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=right_paddle.move_up)
screen.onkey(key="Down", fun=right_paddle.move_down)
screen.onkey(key="w", fun=left_paddle.move_up)
screen.onkey(key="s", fun=left_paddle.move_down)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect ball hitting the top or bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect ball going past the paddle
    if ball.xcor() > 400:
        ball.ball_reset()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.ball_reset()
        scoreboard.r_point()

screen.exitonclick()
