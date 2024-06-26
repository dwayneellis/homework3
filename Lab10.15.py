# CIS 2348 Homework 3 Fall 2020.
# Dwayne Ellis
# Student ID: #######
# Lab 10.15 Winning team (classes)
# Complete the Team class implementation

class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        percent = self.team_wins / (self.team_wins + self.team_losses)
        return percent

    def set_team_name(self, team_name):
        self.team_name = team_name

    def set_team_wins(self, team_wins):
        self.team_wins = team_wins

    def set_team_losses(self, team_losses):
        self.team_losses = team_losses


if __name__ == "__main__":

    team = Team()

    team_name = input()
    team_wins = float(input())
    team_losses = float(input())

    team.set_team_name(team_name)
    team.set_team_wins(team_wins)
    team.set_team_losses(team_losses)

    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team ' + str(team.team_name) + ' has a winning average!')
    else:
        print('Team ' + str(team.team_name) + ' has a losing average.')
