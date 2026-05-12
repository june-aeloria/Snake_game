from turtle import Turtle, Screen
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
class Snake:
    def __init__(self):
        self.segments = []
        self.screen = Screen()
        self.turtle = Turtle()
        for position in STARTING_POSITIONS:
            self.create_segments(position)

    def create_segments(self,position):
        gail = Turtle("square")
        gail.color("white")
        gail.penup()
        self.segments.append(gail)
        self.head = self.segments[0]
        gail.goto(position)


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            position_x = self.segments[seg_num - 1].xcor()
            position_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(position_x, position_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def extend(self):
        self.create_segments(self.segments[-1].position())

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)