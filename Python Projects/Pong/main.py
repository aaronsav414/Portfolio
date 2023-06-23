from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
screen = Screen()

screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball((0, 0), True, False)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")


screen.listen()
# Right Paddle
screen.onkey(key="Up", fun=r_paddle.moveup)
screen.onkey(key="Down", fun=r_paddle.movedown)
# Left Paddle
screen.onkey(key="w", fun=l_paddle.moveup)
screen.onkey(key="s", fun=l_paddle.movedown)

game_on = True

while game_on:
    screen.update()
    ball.move()





screen.exitonclick()