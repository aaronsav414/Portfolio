import colorgram
import random
from turtle import Turtle, Screen, colormode

timmy = Turtle()
timmy.shape('turtle')
colormode(255)

def draw_dots():
    for _ in range(10):

        timmy.dot(20, random.choice(color_tuples))
        timmy.fd(50)


# Extract 6 colors from an image.
colors = colorgram.extract('hirsty.png', 6)

color_tuples = [(251, 249, 245), (208, 165, 125), (250, 235, 237), (140, 49, 106), (164, 169, 38), (244, 80, 57)]

# for color in colors:
#     print(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuples.append((r, g, b))
#     print(color_tuples)

timmy.penup()
timmy.setheading(255)
timmy.forward(300)
timmy.setheading(0)


for _ in range(10):
    draw_dots()
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)



#
#

# draw_dots()
# draw_dots()


screen = Screen()
screen.exitonclick()