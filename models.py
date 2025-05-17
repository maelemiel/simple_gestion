from database import get_db

def get_projets():
    db = get_db()
    return db.execute('SELECT * FROM Projets').fetchall()

def get_taches():
    db = get_db()
    return db.execute('''
        SELECT Taches.id, Projets.nom AS projet, Taches.description, Taches.statut, Taches.date_limite
        FROM Taches
        JOIN Projets ON Taches.projet_id = Projets.id
    ''').fetchall()

def add_projet(nom):
    db = get_db()
    db.execute("INSERT INTO Projets (nom) VALUES (?)", (nom,))
    db.commit()

def add_tache(projet_id, description, statut, date_limite):
    db = get_db()
    db.execute("INSERT INTO Taches (projet_id, description, statut, date_limite) VALUES (?, ?, ?, ?)",
               (projet_id, description, statut, date_limite))
    db.commit()

def update_statut(id, statut):
    db = get_db()
    db.execute("UPDATE Taches SET statut = ? WHERE id = ?", (statut, id))
    db.commit()