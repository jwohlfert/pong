from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.colormode(255)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(paddle_side="right")
left_paddle = Paddle(paddle_side="left")

screen.listen()
screen.onkey(key="Up", fun=right_paddle.move_up)
screen.onkey(key="Down", fun=right_paddle.move_down)

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
