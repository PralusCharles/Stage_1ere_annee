import tkinter as tk
from Controller import Controller
from view_console import ConsoleView
from view_tkinter import TkinterView

def main():
    print("Choisissez le mode d'affichage :")
    print("1. Console")
    print("2. Tkinter")

    choice = input("Choix : ")

    if choice == "1":
        run_console_mode()
    elif choice == "2":
        run_tkinter_mode()
    else:
        print("Choix invalide")

def run_console_mode():
    controller = Controller()
    console_view = ConsoleView()
    console_view.run()

def run_tkinter_mode():
    root = tk.Tk()
    controller = Controller()
    tkinter_view = TkinterView(root, controller)

    create_season_button = tk.Button(root, text="Créer une saison", command=tkinter_view.create_season)
    create_season_button.grid(row=2, column=2, padx=10, pady=5)
    home_team_label = tk.Label(root, text="Équipe à domicile:")
    home_team_label.grid(row=5, column=0, padx=10, pady=5)
    tkinter_view.home_team_entry = tk.Entry(root)
    tkinter_view.home_team_entry.grid(row=5, column=1, padx=10, pady=5)

    away_team_label = tk.Label(root, text="Équipe à l'extérieur:")
    away_team_label.grid(row=6, column=0, padx=10, pady=5)
    tkinter_view.away_team_entry = tk.Entry(root)
    tkinter_view.away_team_entry.grid(row=6, column=1, padx=10, pady=5)

    date_label = tk.Label(root, text="Date du match:")
    date_label.grid(row=7, column=0, padx=10, pady=5)
    tkinter_view.date_entry = tk.Entry(root)
    tkinter_view.date_entry.grid(row=7, column=1, padx=10, pady=5)

    create_fixture_button = tk.Button(root, text="Créer un match", command=tkinter_view.create_fixture)
    create_fixture_button.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
