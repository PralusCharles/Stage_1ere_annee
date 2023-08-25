from Model import *

class Controller():
    def __init__(self):
        self.model = Season("2023", 1)

    def create_season(self, label, id):
        # Vérifier si une saison avec le même id existe déjà
        for existing_season in self.model.seasons:
            if existing_season.id == id:
                return 400, "Une saison avec cet identifiant existe déjà."

        # Créer la nouvelle saison
        new_season = Season(label, id)
        self.model.seasons.append(new_season)
        return 200, "Saison créée avec succès."
    
    def create_league(self, season_id, league_name):
        target_season = None
        for season in self.model.seasons:
            if season.id == season_id:
                target_season = season
                break

        if target_season is None:
            return 400, "La saison spécifiée n'existe pas."

        for existing_league in target_season.leagues:
            if existing_league.name == league_name:
                return 400, "Une ligue avec ce nom existe déjà dans cette saison."

        new_league = target_season.create_league(league_name)
        return 200, "Ligue créée avec succès."

    def create_fixture(self, league_name, home_team_name, away_team_name, date):
        target_league = None
        for season in self.model.seasons:
            for league in season.leagues:
                if league.name == league_name:
                    target_league = league
                    break
            if target_league:
                break

        if target_league is None:
            return 400, "La ligue spécifiée n'existe pas."

        home_team = next((team for team in target_league.teams if team.name == home_team_name), None)
        away_team = next((team for team in target_league.teams if team.name == away_team_name), None)

        if home_team is None or away_team is None:
            return 400, "Les équipes spécifiées ne font pas partie de cette ligue."

        # Ajoutez ici la vérification pour que la date soit dans le futur

        new_fixture = Fixture(home_team, away_team, date)
        target_league.fixtures.append(new_fixture)
        return 200, "Match programmé avec succès."