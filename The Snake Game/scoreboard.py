from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Times New Roman', 24, 'bold')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.start_scoreboard()

    def start_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_scoreboard(self):
        self.score += 1
        self.start_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.start_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
