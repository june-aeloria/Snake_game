from turtle import Turtle

with open('Highscore', 'r') as f:
    current_high = int(f.read())

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 240)
        self.color("white")
        self.write(f"Score: {self.score} Highest Score: {current_high}", align = "center", font=("Courier", 24, "bold"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.highest_score()

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER", align = "center", font=("Courier", 24, "bold"))

    def highest_score(self):
        global current_high
        if self.score > current_high:
            current_high = self.score
            with open('Highscore', 'w') as fi:
                fi.write(str(self.score))

        self.clear()
        self.write(f"Score: {self.score} Highest Score: {current_high}", align="center", font=("Courier", 24, "bold"))