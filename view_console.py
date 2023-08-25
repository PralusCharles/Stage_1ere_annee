class ConsoleView():
    @staticmethod
    def show_seasons(seasons):
        for season in seasons:
            print(f"Season: {season.label}, ID: {season.id}")

    @staticmethod
    def show_league(league):
        print(f"League: {league.name}, Season: {league.season.label}")
        for team in league.teams:
            print(f"Team: {team.name}")
        for fixture in league.fixtures:
            print(f"Fixture: {fixture.home_team.name} vs {fixture.away_team.name}, Date: {fixture.date}")
