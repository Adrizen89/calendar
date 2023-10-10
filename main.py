import tkinter as tk
from tkinter import ttk
import calendar
from calendrier.calendrier import Calendrier

# Définition de la classe principale de l'application
class App:
    def __init__(self, root):
        # Initialisation de la fenêtre principale
        self.root = root
        self.root.title("Calendrier Demo")
        self.root.geometry("500x400")

        # Création et placement du label pour le mois
        self.label_month = ttk.Label(root, text="Mois (01-12):")
        self.label_month.pack(pady=10)

        # Création et placement de l'entrée pour le mois
        self.entry_month = ttk.Entry(root)
        self.entry_month.pack(pady=10)

        # Création et placement du label pour l'année
        self.label_year = ttk.Label(root, text="Année (ex: 2023):")
        self.label_year.pack(pady=10)

        # Création et placement de l'entrée pour l'année
        self.entry_year = ttk.Entry(root)
        self.entry_year.pack(pady=10)

        # Création et placement du bouton pour afficher les jours
        self.button = ttk.Button(root, text="Afficher les jours", command=self.display_days)
        self.button.pack(pady=20)

        # Création du Treeview pour afficher le calendrier
        self.tree = ttk.Treeview(root, columns=('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'), show='headings')
        for col in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=70, anchor='center')
        self.tree.pack(pady=10)

    # Méthode pour afficher les jours dans le Treeview
    def display_days(self):
        month = int(self.entry_month.get())
        year = int(self.entry_year.get())
        days = Calendrier.get_days_of_month_formatted(year, month)

        # Suppression des jours précédemment affichés dans le Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Détermination du jour de la semaine du premier jour du mois
        first_day_weekday = calendar.weekday(year, month, 1)
        week = [""] * first_day_weekday

        # Insertion des jours (uniquement le chiffre) dans le Treeview
        for day in days:
            day_number = day.split()[1]  # Extraction du chiffre du jour
            week.append(day_number)
            if len(week) == 7:
                self.tree.insert('', 'end', values=week)
                week = []

        # Insertion des jours restants dans le Treeview
        if week:
            while len(week) < 7:
                week.append("")
            self.tree.insert('', 'end', values=week)


# Exécution de l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
