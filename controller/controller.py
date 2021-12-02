import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QAction, qApp
from PyQt5.QtMultimedia import QSound
from model import model

def __init__(self):
    self.resize(401,442) #Redimension fenêtre 
    self.setWindowTitle("Sokoban by Foxers") #Titre de la fenêtre
    QSound.play("other/gameMusic.wav") #On joue la musique principale du jeu (format wav exclusif avec QSound)
    self.keypush = None #Initialise la capture des touches du clavier
    self.posx = model.level1PosX() #Position de départ x du joueur
    self.posy = model.level1PosY() #Position de départ y du joueur
    self.compteurMouvements = 0 #On initialise le compteur de mouvements
    self.statusBar().showMessage("Nombre de mouvements : {}".format(self.compteurMouvements)) #Affiche le compteur de mouvements en début de partie
    self.compteurVictoires = 0 #On initialise le nombre de victoires
    self.nbObjetsBienPlaces = 0 #On initialise le nombre d'objets bien placés

    #Pour quitter le jeu
    exitAct = QAction("Quitter", self) #Bouton quitter
    exitAct.setShortcut("Ctrl+W") #Ajout du raccourci clavier + écrit le raccourci clavier dans le bouton
    exitAct.setStatusTip('Quitter le jeu') #Affiche un message en bas
    exitAct.triggered.connect(qApp.quit) #Quitte le jeu si on appuie sur ce bouton

    #Pour recommencer le jeu
    def restart():
        QtCore.QCoreApplication.quit()
        QtCore.QProcess.startDetached(sys.executable, sys.argv)
    
    reloadLevel = QAction("Recommencer le jeu", self) #Bouton recommencer le jeu
    reloadLevel.setShortcut("Ctrl+R") #Ajout du raccourci clavier + écrit le raccourci clavier dans le bouton
    reloadLevel.setStatusTip('Recommencer le jeu') #Affiche un message en bas
    reloadLevel.triggered.connect(lambda: restart()) #Redémarre le jeu si on appuie sur ce bouton (lambda sert à appeler une autre fonction, sans ça, on ne peut qu'appeler des fonctions de Qt)

    #Les boutons dans la barre de menu et le menu déroulant        
    menubar = self.menuBar() #Donne à la variable menubar la valeur self.menuBar()
    fileMenu = menubar.addMenu('Jeu') #Ajout dans la barre de menu du bouton Jeu
    fileMenu.addAction(reloadLevel) #Ajout du bouton pour recharger le niveau
    fileMenu.addAction(exitAct) #Ajout du bouton pour quitter le jeu

    #Barre du bas
    self.statusBar().setStyleSheet("background-color : #DCDCDC") #Barre du bas en couleur grise
    self.statusBar().showMessage("Nombre de mouvements : {}".format(self.compteurMouvements)) #Écrit dans la barre du bas le nb de mouvements

    #Liste des murs (1 = Mur | 2 = Caisse)
    self.listePlateau = model.level1ListePlateau() #listePlateau prend la valeur du la liste plateau contenu dans model level1ListePlateau

    self.nombreCaisse = 0 #Initialise le nombre de caisses sur le plateau (pour tester la fin de la partie)
    #Compte le nombre de caisses
    for i in range(8):
        for j in range(8):
            if self.listePlateau[j][i] == 2: #S'il y a une caisse dans la matrice
                self.nombreCaisse+=1 #Alors on ajoute 1 au nombre de caisses du jeu (permet de futurs tests de vérification de fin de partie)
                #print("NOMBRE DE CAISSES : ",self.nombreCaisse)

    #Liste des joueurs (1 = Emplacement du joueur)
    self.listeJoueur = model.level1listeJoueur() #listeJoueur prend la valeur du la liste joueur contenu dans model level1listeJoueur

    #Liste des objets (3 = Emplacement des objets)
    self.listeObjets = model.level1listeObjets() #listeObjets prend la valeur du la liste objets contenu dans model listeObjets