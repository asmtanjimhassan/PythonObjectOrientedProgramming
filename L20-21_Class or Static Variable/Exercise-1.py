class Player:
    team_run = 0            # Static or Class Variable
    def __init__(self, run):
        self.run = run      # instance variable
        self.teamrun = 0
    def hit_four(self):
        self.run += 4
        Player.team_run += 4

    def hit_six(self):
        self.run += 6
        Player.team_run += 6

sakib = Player(0)
tamim = Player(0)

tamim.hit_four()
tamim.hit_four()
sakib.hit_six()

print("Sakib: ", sakib.run)
print("Tamim: ", tamim.run)

print("Team Run: ", Player.team_run)

""" A class property every object will share"""
