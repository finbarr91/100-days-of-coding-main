from turtle import Turtle
MOVE=False
ALIGNMENT="center"
FONT=("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_keeper()
        self.update_scoreboard()


    def score_keeper(self):
        self.color('white')
        self.score=0
        self.penup()
        self.goto(0, 270)
        self.hideturtle()



    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align = ALIGNMENT, move=MOVE,font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.color('white')
        self.write(f"GAME OVER!!!", align=ALIGNMENT, move=MOVE, font=FONT)

        
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
