from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "bold")
FONT_2 = ("Courier", 28, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT_2)


    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
