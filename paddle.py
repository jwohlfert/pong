from turtle import Turtle

LEFT_POSITION = (-350, 0)
RIGHT_POSITION = (350, 0)


class Paddle(Turtle):
    def __init__(self, paddle_side):
        super().__init__()
        self.paddle = None
        self.create_paddle(paddle_side)

    def create_paddle(self, side):
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.turtlesize(stretch_wid=5, stretch_len=1)
        self.paddle.color("white")
        self.paddle.penup()
        if side.lower() == "right":
            self.paddle.goto(RIGHT_POSITION)
        elif side.lower() == "left":
            self.paddle.goto(LEFT_POSITION)
        else:
            raise ValueError(f"'{side}' is not a valid input. Valid inputs are 'left' or 'right'")

    def move_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(x=self.paddle.xcor(), y=new_y)

    def move_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(x=self.paddle.xcor(), y=new_y)
