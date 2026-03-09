from pathlib import Path

dossiers = [
    ("Bureau", "📁"),
    ("Téléchargement", "⬇️"),
    ("Documents", "📄"),
    ("Images", "🖼️"),
    ("Musique", "🎵"),
    ("Vidéos", "🎬"),
    ("Projets", "📂"),
]


for nom, icone in dossiers:
    print(f"[{icone}] {nom}")

def affiche():
    a=input("Desktop")
    b=input("fichier ")
    donnee = Path.home()/a/b
    if donnee.exists():
        if donnee.is_dir():
            return donnee
        elif donnee.is_file():
            return donnee


def ouvrir():
    chemin=Path.home()/"Desktop"/"n.txt"
    with open(chemin,"r") as fichiers:
        print(fichiers.read())

def supprimer():
    chemin=Path.home()/"Desktop"/"n.txt"
    Path(chemin).unlink()

def creer():
    chemin=Path.home()/"Desktop"/"n.txt"
    with open(chemin,"w") as fichier:
        print(fichier)

def renomer():
    chemin=Path.home()/"Desktop"/"n.txt"
