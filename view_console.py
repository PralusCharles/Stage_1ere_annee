class ConsoleView():
    print("\nMenu :")
    print("1. Créer une saison")
    print("2. Créer une ligue")
    print("3. Ajouter une équipe")
    print("4. Créer une journée")
    print("5. Programmer un match")
    print("6. Afficher les données")
    print("7. Quitter")

    choice = input("Choix : ")

    if choice == "1":
        create_season()
    elif choice == "2":
        create_league()
    elif choice == "3":
        add_team()
    elif choice == "4":
        create_fixture()
    elif choice == "5":
        schedule_match()
    elif choice == "6":
        show_data()
    elif choice == "7":
        break
    else:
        print("Erreur: Choix invalide")

print("Programme terminé.")