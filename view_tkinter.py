import tkinter as tk
from Controller import Controller

class TkinterView():
    def __init__(self, window, controller):
        self.window = window
        self.window.title("Gestion de la ligue de football")

        self.controller = controller

        season_label = tk.Label(window, text="Saison :")
        season_label.grid(row=0, column=0, padx=10, pady=5)
        self.season_label_entry = tk.Entry(window)
        self.season_label_entry.grid(row=0, column=1, padx=10, pady=5)

        season_id_label = tk.Label(window, text="Identifiant :")
        season_id_label.grid(row=1, column=0, padx=10, pady=5)
        self.season_id_entry = tk.Entry(window)
        self.season_id_entry.grid(row=1, column=1, padx=10, pady=5)

        create_season_button = tk.Button(window, text="Créer une saison", command=self.create_season)
        create_season_button.grid(row=2, column=0, padx=10, pady=5)

        self.season_listbox = tk.Listbox(window)
        self.season_listbox.grid(row=0, column=2, rowspan=5, padx=10, pady=5)

    def create_season(self):
        label = self.season_label_entry.get()
        id = self.season_id_entry.get()

        status_code, message = self.controller.create_season(label, id)

        if status_code == 200:
            self.show_seasons()
        else:
            error_label = tk.Label(self.window, text=message, fg="red")
            error_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def show_seasons(self):
        self.season_listbox.delete(0, tk.END)
        for season in self.controller.model.leagues:
            self.season_listbox.insert(tk.END, f"Season: {season.label}, ID: {season.id}")
    def create_season(self):
        label = self.season_label_entry.get()
        id = self.season_id_entry.get()

        status_code, message = self.controller.create_season(label, id)

        if status_code == 200:
            self.show_seasons()
        else:
            # Afficher un message d'erreur
            error_label = tk.Label(self.window, text=message, fg="red")
            error_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
    
    def create_league(self):
        selected_season = self.season_listbox.get(tk.ACTIVE)
        league_name = self.league_name_entry.get()


        season_id = selected_season.split(", ID: ")[1]

        status_code, message = self.controller.create_league(season_id, league_name)

        if status_code == 200:
            self.show_seasons()
            self.show_leagues()
        else:
            # Afficher un message d'erreur
            error_label = tk.Label(self.window, text=message, fg="red")
            error_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
    

    def create_fixture(self):
        selected_league = self.league_listbox.get(tk.ACTIVE)
        home_team_name = self.home_team_entry.get()
        away_team_name = self.away_team_entry.get()
        date = self.date_entry.get()

        league_name = selected_league.split(", Season: ")[0].split("League: ")[1]

        status_code, message = self.controller.create_fixture(league_name, home_team_name, away_team_name, date)

        if status_code == 200:
            self.show_fixtures()
        else:
            # Afficher un message d'erreur
            error_label = tk.Label(self.window, text=message, fg="red")
            error_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5)