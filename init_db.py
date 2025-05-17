import sqlite3

# Connexion à la base (ou création si elle n'existe pas)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Création des tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS Projets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Taches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    projet_id INTEGER,
    description TEXT NOT NULL,
    statut TEXT DEFAULT 'À faire',
    date_limite DATE,
    FOREIGN KEY (projet_id) REFERENCES Projets(id)
)
''')

# Insertion de données exemples
cursor.execute("INSERT INTO Projets (nom) VALUES ('Site Web'), ('Rapport')")

cursor.execute("INSERT INTO Taches (projet_id, description, statut, date_limite) VALUES (1, 'Créer la maquette', 'En cours', '2025-05-25')")
cursor.execute("INSERT INTO Taches (projet_id, description, statut, date_limite) VALUES (2, 'Collecter les données', 'À faire', '2025-05-30')")

conn.commit()
conn.close()