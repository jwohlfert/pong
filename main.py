from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.colormode(255)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

LEFT_POSITION = (-350, 0)
RIGHT_POSITION = (350, 0)

right_paddle = Paddle(paddle_coordinates=RIGHT_POSITION)
left_paddle = Paddle(paddle_coordinates=LEFT_POSITION)

screen.listen()
screen.onkey(key="Up", fun=right_paddle.move_up)
screen.onkey(key="Down", fun=right_paddle.move_down)
screen.onkey(key="w", fun=left_paddle.move_up)
screen.onkey(key="s", fun=left_paddle.move_down)

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
