import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from view import view #importe le fichier view
from controller import controller #importe le fichier controller

#Permet d'initialiser la fenêtre, appelée avec le super dans classe Tableau
class Dessin(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

#On vérifie s'il y a déjà une instance de l'application, s'il y en a déjà une, on ouvre pas de nouvelle fenêtre et on l'ouvre uniquement quand l'ancienne sera quitée
app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

class Tableau(QMainWindow):
    def __init__(self):
        super().__init__() #Appelle la classe initiale
        controller.__init__(self) #On exécute ici ce qu'il se trouve dans controller.py

    def paintEvent(self, event): #On définit une fonction paintEvent
        view.paintEvent(self, event) #On exécute ici ce qu'il se trouve dans view.py (affichage du plateau, de ses mises à jour et des touches)

    def keyPressEvent(self, event):
        self.keypush = event.key() #Donne à keypush la valeur retournée par event.key
        self.update() #Permet de mettre à jour l'affichage à chaque event (principalement appui d'une touche)

# Application 
fen = Tableau() #fen prend la valeur de ce qu'il se passe dans la classe tableau
fen.show() #On affiche la fenêtre

app.exec_() #On exécute l'application