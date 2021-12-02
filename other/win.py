import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QSound

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        QSound.play("other/winMusic.wav") #On joue la musique principale du jeu (format wav exclusif avec QSound)
        self.setWindowTitle("You win !!! \U0001F3C6") #Titre de la fenêtre
        self.resize(500,500) #Redimension fenêtre
        self.label = QLabel(self) #Emplacement pour l'image
        self.pixmap = QPixmap('other/win.png') #Chemin de l'image
        self.label.setPixmap(self.pixmap) #Chargement de l'image
        self.label.resize(self.pixmap.width(), self.pixmap.height()) #On redimentionne l'image
        self.show() #On affiche tout
  
# create pyqt5 app
App = QApplication(sys.argv)
window = Window()
  
# start the app
sys.exit(App.exec())