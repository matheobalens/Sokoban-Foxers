import os
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from model import model

def paintEvent(self,event):
    ##################################
    #          Partie murs
    ##################################
    
    mur = QPainter(self) # recupere le QPainter du widget
    mur.setPen(Qt.black) #Contour des cases en noir
    mur.setBrush(QColor(121,138,148)) #Intérieur des cases en gris
    
    #Dessine les murs grâce à listePlateau == 1
    for i in range(8):
        for j in range(8):
            if self.listePlateau[j][i] == 1: #S'il y a un mur (représenté par un 1 dans le tableau)
                mur.drawRect(i*50,j*50+21,50,50) #x y taillex tailley Le + 21 est là pour décaler le plateau à cause de la barre de menu

    ##################################
    #        Partie caisses
    ##################################

    caisse = QPainter(self) # recupere le QPainter du widget
    caisse.setPen(Qt.black) #Contour des cases en noir
    caisse.setBrush(QColor(222,184,135)) #Intérieur des cases en marron

    #Déplacer des caisses
    #Pour aller à droite
    if (self.keypush == Qt.Key_D) and self.listePlateau[int(self.posy)][int(self.posx+1)]==2 and not self.listePlateau[int(self.posy)][int(self.posx+2)]==1 and not self.listePlateau[int(self.posy)][int(self.posx+2)]==2: #Si on appuie sur D et qu'il y a une caisse après et qu'il n'y a pas un mur devant la caisse et qu'il n'y a pas de caisse devant la caisse
        self.listePlateau[self.posy][self.posx+2] = 2 #On ajoute une caisse vers la droite dans le tableau (et donc plateau)
        self.listePlateau[self.posy][self.posx+1] = 0 #On enlève la caisse de l'ancien emplacement dans le tableau (et donc plateau)
        print(self.listePlateau)

    #Pour aller à gauche
    elif (self.keypush == Qt.Key_Q) and self.listePlateau[int(self.posy)][int(self.posx-1)]==2 and not self.listePlateau[int(self.posy)][int(self.posx-2)]==1 and not self.listePlateau[int(self.posy)][int(self.posx-2)]==2: #Si on appuie sur Q et qu'il y a une caisse après et qu'il n'y a pas un mur devant la caisse et qu'il n'y a pas de caisse devant la caisse
        self.listePlateau[self.posy][self.posx-2] = 2 #On ajoute une caisse vers la gauche dans le tableau (et donc plateau)
        self.listePlateau[self.posy][self.posx-1] = 0 #On enlève la caisse de l'ancien emplacement dans le tableau (et donc plateau)
        print(self.listePlateau)

    #Pour aller en haut
    elif (self.keypush == Qt.Key_Z) and self.listePlateau[int(self.posy-1)][int(self.posx)]==2 and not self.listePlateau[int(self.posy-2)][int(self.posx)]==1 and not self.listePlateau[int(self.posy-2)][int(self.posx)]==2: #Si on appuie sur Z et qu'il y a une caisse après et qu'il n'y a pas un mur devant la caisse et qu'il n'y a pas de caisse devant la caisse
        self.listePlateau[self.posy-2][self.posx] = 2 #On ajoute une caisse vers le haut dans le tableau (et donc plateau)
        self.listePlateau[self.posy-1][self.posx] = 0 #On enlève la caisse de l'ancien emplacement dans le tableau (et donc plateau)
        print(self.listePlateau)

    #Pour aller en bas
    elif (self.keypush == Qt.Key_S) and self.listePlateau[int(self.posy+1)][int(self.posx)]==2 and not self.listePlateau[int(self.posy+2)][int(self.posx)]==1 and not self.listePlateau[int(self.posy+2)][int(self.posx)]==2: #Si on appuie sur S et qu'il y a une caisse après et qu'il n'y a pas un mur devant la caisse et qu'il n'y a pas de caisse devant la caisse
        self.listePlateau[self.posy+2][self.posx] = 2 #On ajoute une caisse vers le bas dans le tableau (et donc plateau)
        self.listePlateau[self.posy+1][self.posx] = 0 #On enlève la caisse de l'ancien emplacement dans le tableau (et donc plateau)
        print(self.listePlateau)
    
    #Dessine les caisses et ses updates
    for i in range(8):
        for j in range(8):
            if self.listePlateau[j][i] == 2: #Si on rencontre une caisse (2) dans la listePlateau
                caisse.drawRect(i*50,j*50+21,50,50) #x y taillex tailley #+21 pour le décalage avec le menu


    ##################################
    #         Partie joueur
    ##################################

    player = QPainter(self) #appelle QPainter
    player.setRenderHint(QPainter.Antialiasing) #Permet de faire un cercle beaucoup moins pixélisé
    player.setPen(Qt.black) #contour du cercle
    player.setBrush(Qt.blue) #intérieur du cercle

    #Pour aller à droite
    if (self.keypush == Qt.Key_D) and not self.listePlateau[int(self.posy)][int(self.posx+1)]==1 and not self.listePlateau[int(self.posy)][int(self.posx+1)]==2: #Si on appuie sur la touche D et qu'il n'y a pas de mur (1) et de caisse (2)
        self.posx += 1 #On avance de 1 la position x du joueur sur le plateau
        self.listeJoueur[self.posy][self.posx] = 1 #On ajoute un joueur vers la droite dans le tableau (et donc plateau)
        self.listeJoueur[self.posy][self.posx-1] = 0 #On enlève le joueur de l'ancien emplacement dans le tableau (et donc plateau)
        self.compteurMouvements+=1 #On ajoute 1 au compteur de mouvements
        self.keypush = None #Enlève le event qui créé pleins de bugs de le comptage de mouvements
        #print("Nombre de mouvements : ",self.compteurMouvements) #On affiche le nombre de mouvements dans la console
        self.statusBar().showMessage("Nombre de mouvements : {}".format(self.compteurMouvements))#On affiche le nombre de mouvements

    #Pour aller à gauche
    elif (self.keypush == Qt.Key_Q) and not self.listePlateau[int(self.posy)][int(self.posx-1)]==1 and not self.listePlateau[int(self.posy)][int(self.posx-1)]==2: #Si on appuie sur la touche Q et qu'il n'y a pas de mur (1) et de caisse (2)
        self.posx -= 1 #On recule de 1 la position x du joueur sur le plateau
        self.listeJoueur[self.posy][self.posx] = 1 #On ajoute un joueur vers la gauche dans le tableau (et donc plateau)
        self.listeJoueur[self.posy][self.posx+1] = 0 #On enlève le joueur de l'ancien emplacement dans le tableau (et donc plateau)
        self.compteurMouvements+=1 #On ajoute 1 au compteur de mouvements
        self.keypush = None #Enlève le event qui créé pleins de bugs dans le comptage de mouvements
        #print("Nombre de mouvements : ",self.compteurMouvements) #On affiche le nombre de mouvements dans la console
        self.statusBar().showMessage("Nombre de mouvements : {}".format(self.compteurMouvements))#On affiche le nombre de mouvements
        #print(self.posx,self.posy)
        #print(self.listeJoueur)

    #Pour aller en haut
    elif (self.keypush == Qt.Key_Z) and not self.listePlateau[int(self.posy-1)][int(self.posx)]==1 and not self.listePlateau[int(self.posy-1)][int(self.posx)]==2: #Si on appuie sur la touche Z et qu'il n'y a pas de mur (1) et de caisse (2)
        self.posy -= 1 #On recule de 1 la position y du joueur sur le plateau
        self.listeJoueur[self.posy][self.posx] = 1 #On ajoute un joueur vers le haut dans le tableau (et donc plateau)
        self.listeJoueur[self.posy+1][self.posx] = 0 #On enlève le joueur de l'ancien emplacement dans le tableau (et donc plateau)
        self.compteurMouvements+=1 #On ajoute 1 au compteur de mouvements
        self.keypush = None #Enlève le event qui créé pleins de bugs de le comptage de mouvements
        #print("Nombre de mouvements : ",self.compteurMouvements) #On affiche le nombre de mouvements dans la console
        self.statusBar().showMessage("Nombre de mouvements : {}".format(self.compteurMouvements))#On affiche le nombre de mouvements
        #print(self.posx,self.posy)
        #print(self.listeJoueur)

    #Pour aller en bas
    elif (self.keypush == Qt.Key_S) and not self.listePlateau[int(self.posy+1)][int(self.posx)]==1 and not self.listePlateau[int(self.posy+1)][int(self.posx)]==2: #Si on appuie sur la touche S et qu'il n'y a pas de mur (1) et de caisse (2)
        self.posy += 1 #On avance de 1 la position y du joueur sur le plateau
        self.listeJoueur[self.posy][self.posx] = 1 #On ajoute un joueur vers le bas dans le tableau (et donc plateau)
        self.listeJoueur[self.posy-1][self.posx] = 0 #On enlève le joueur de l'ancien emplacement dans le tableau (et donc plateau)
        self.compteurMouvements+=1 #On ajoute 1 au compteur de mouvements
        self.keypush = None #Enlève le event qui créé pleins de bugs de le comptage de mouvements
        #print("Nombre de mouvements : ",self.compteurMouvements) #On affiche le nombre de mouvements dans la console
        self.statusBar().showMessage("Nombre de mouvements : {}".format(self.compteurMouvements))#On affiche le nombre de mouvements
        #print(self.posx,self.posy)
        #print(self.listeJoueur)

    #Dessine le plateau et ses updates
    for i in range(8):
        for j in range(8): #Double boucle for pour parcourir la matrice
            if self.listeJoueur[j][i] == 1: #Si on rencontre le joueur (1)
                self.posx = i #La position x du joueur prend la valeur de la coordonnée i de la matrice
                self.posy = j #La position y du joueur prend la valeur de la coordonnée i de la matrice
                player.drawEllipse(i*50+1,j*50+21+1,49,49) #+21 pour le décalage avec le menu. J'ai mis un 49 au lieu de 50 et un + 1 pour corriger un léger décalage provoqué par l'antialiasing

    ##################################
    #         Partie objets
    ##################################
    objet = QPainter(self) #appelle QPainter
    objet.setRenderHint(QPainter.Antialiasing) #Permet de faire un cercle beaucoup moins pixélisé
    objet.setPen(Qt.black) #contour du cercle
    objet.setBrush(Qt.yellow) #intérieur du cercle

    for i in range(8):
        for j in range(8): #Double boucle for pour parcourir la matrice
            if self.listeObjets[j][i] == 3: #Si on rencontre un objet (3) dans le tableau
                objet.drawEllipse(i*50+15,j*50+15+21,20,20) #+15 pour centrer l'objet et + 21 pour le décalage avec le menu

    ##################################
    # On teste si la partie est gagnée
    ##################################
    
    compteur = 0 #On initialise le compteur utilisé dans la double boucle for ci-dessous
    for i in range(8):
        for j in range(8):
            if (self.listeObjets[j][i] == 3) and (self.listePlateau[j][i] == 2): #Si on rencontre un objet (3) et qu'un rencontre une caisse au mêmes indices des tableaux listeObjets et listePlateau
                compteur += 1 #On compte le nombre de caisses bien placées
    self.nbObjetsBienPlaces=compteur #nbObjetsBienPlaces prend la valeur du compteur
    #print("BIEN PLACES : ",self.nbObjetsBienPlaces)
    #print("CAISSES : ",self.nombreCaisse)

    if ((self.nbObjetsBienPlaces == self.nombreCaisse) and self.nombreCaisse>=1): #Si le nombre d'objets bien placés est égal au nombre de caisses (et que le nombre de caisses est ≥ à 1 car sinon, le jeu peut considérer que la partie est gagnée lors de tests de niveaux où on ne place pas de caisses)
        self.compteurVictoires+=1 #On incrémente de 1 le compteur de victoires pour passer au niveau suivant ou vérifier que le jeu est terminé 
        #On charge le niveau suivant
        if self.compteurVictoires == 1: #Si on a gagné 1 niveau
            print("Niveau 2") #On affiche dans la console "Niveau 2"
            self.listePlateau = model.level2ListePlateau() #Le tableau listePlateau prend la valeur de level2ListePlateau
            self.listeJoueur = model.level2listeJoueur() #Le tableau listeJoueur prend la valeur de level2listeJoueur
            self.listeObjets = model.level2listeObjets() #Le tableau listeObjets prend la valeur de level2listeObjets
            self.compteurMouvements = 0 #On réinitialise le compteur de mouvements à 0
            self.statusBar().showMessage(self.tr("Nombre de mouvements : {}".format(self.compteurMouvements))) #On affiche le nombre de mouvements
            self.posx = model.level2PosX() #posx prend la valeur de level2PosX
            self.posy = model.level2PosY() #posy prend la valeur de level2PosY
        #On charge le niveau suivant
        if self.compteurVictoires == 2: #Si on a gagné 2 niveaux
            print("Niveau 3") #On affiche dans la console "Niveau 3"
            self.listePlateau = model.level3ListePlateau() #Le tableau listePlateau prend la valeur de level3ListePlateau
            self.listeJoueur = model.level3listeJoueur() #Le tableau listeJoueur prend la valeur de level3listeJoueur
            self.listeObjets = model.level3listeObjets() #Le tableau listeObjets prend la valeur de level3listeObjets
            self.posx = model.level3PosX() #posx prend la valeur de level2PosX
            self.posy = model.level3PosY() #posy prend la valeur de level2PosY
            self.compteurMouvements = 0 #On réinitialise le compteur de mouvements à 0
            self.statusBar().showMessage(self.tr("Nombre de mouvements : {}".format(self.compteurMouvements))) #On affiche le nombre de mouvements
        if self.compteurVictoires == 3: #Si on a gagné 3 niveaux (donc fini le jeu)
            #print("You win !!! \U0001F3C6") #On dit qu'on a gagné
            os.system('python other/win.py') #On exécute le script python win.py
            QtCore.QCoreApplication.quit() #On ferme le jeu une fois qu'on a fini d'exécuter le script python (donc qu'on le ferme)
        self.nbObjetsBienPlaces = 0 #On réinitialise le nombre d'objets bien placés à 0
        self.nombreCaisse = 0 #On réinitialise le nombre de caisses bien placés à 0
        #On recompte le nombre de caisses pour mettre à jour self.nombreCaisse
        for i in range(8):
            for j in range(8):
                if self.listePlateau[j][i] == 2: #Quand on rencontre une caisse (2) dans le tableau
                    self.nombreCaisse+=1 #On incrémente de 1 le nombre de caisses sur le plateau
                    #print("NOMBRE DE CAISSES : ",self.nombreCaisse)
        #On passe au niveau d'après quand tout est réinitialisé
        self.update() #On met à jour l'affichage