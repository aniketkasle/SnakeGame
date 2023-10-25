from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        # scoreboard css
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    # Display score at center
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Aerial", 20, "normal"))

    # Game over message to display game end
    # def game_over(self):
    #    self.goto(0, 0)
    #   self.write("Game Over", align="center", font=("Aerial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # update score in display
    def increase_score(self):
        self.score += 1

        self.update_scoreboard()
