class Team():
    def __init__(self, name):
        self.name = name

class Fixture():
    def __init__(self, home_team, away_team, date):
        self.home_team = home_team
        self.away_team = away_team
        self.date = date

class League():
    def __init__(self, name, season):
        self.name = name
        self.season = season
        self.teams = []
        self.fixtures = []

class Season():
    def __init__(self, label, id):
        self.label = label
        self.id = id
        self.leagues = []

    def create_league(self, name):
        league = League(name, self)
        self.leagues.append(league)
        return league
