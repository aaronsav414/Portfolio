from turtle import Turtle

class Ball(Turtle):
    def __init__(self, start_position, r, l):
        super().__init__()
        self.shapesize(1, 1)
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(start_position)
        self.r = r
        self.l = l


    def move(self):
        r = True
        l = False

        while self.distance(r_paddle) > 3:
            new_x = self.xcor() - 5
            new_y = self.ycor() - 5
            self.goto(new_x, new_y)
            if self.distance(r_paddle) < 3:
                l = True
                r = False
        while self.distance(l_paddle) > 3:
            new_x = self.xcor() + 5
            new_y = self.ycor() + 5
            self.goto(new_x, new_y)
            if self.distance(l_paddle) < 3:
                l = False
                r = True


