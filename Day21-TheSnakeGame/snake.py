from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.bodys=[]
        self.create_snake()
        self.head=self.bodys[0]

    def create_snake(self):
        body1 = Turtle("square")
        body1.penup()
        body1.color("white")

        body2 = Turtle("square")
        body2.penup()
        body2.color("white")
        body2.goto(-20, 0)

        body3 = Turtle("square")
        body3.penup()
        body3.color("white")
        body3.goto(-40, 0)

        self.bodys = [body1, body2, body3]

    def move(self):
        for seg in range(len(self.bodys) - 1, 0, -1):
            new_x = self.bodys[seg - 1].xcor()
            new_y = self.bodys[seg - 1].ycor()
            self.bodys[seg].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left (self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self):

        new_body = Turtle("square")
        new_body.penup()
        new_body.color("white")
        self.bodys.append(new_body)

    def extend(self):
        self.add_segment()