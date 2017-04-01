# coding: utf8
# @Author: Quentin Lemaire
# @Date:   2017-02-27T20:28:53+01:00
# @Email:  quentin.lemaire@supinfo.com
# @Filename: globales.py
# @Last modified by:   SkYNewZ
# @Last modified time: 2017-04-01T03:33:11+02:00
# @License: 214520
# @Copyright: SUPINFO


import pygame
import math
pygame.init()

# affichage initiale
window = pygame.display.set_mode((720, 720))
pygame.display.set_caption('LOGO')
background = pygame.image.load("background.png").convert()
window.blit(background, (0, 0))

class tortue():
    """classe comportant tous les attributs et toutes les méthodes correspondants, déplacements de la tortue et calculs"""
    def __init__(self):
        # _____ATTRIBUTS_____

        # taille de l'image tortue
        self.dimensions_x = 50
        self.dimensions_y = 50
        self.img = pygame.image.load("turtle.png").convert_alpha()

        # centre de l'écran
        self.x = 720/2
        self.y = 720/2

        # attibut de l'angle
        self.angle = 0

        # traits et affichage
        self.width = 1
        self.pencil = True
        self.HiddenTurtle = True
        self.color = "FFFFFF"

        # tableaux pour stockages des coordonées pour affichage des traits, par défaut
        self.x_1 = []
        self.y_1 = []
        self.x_2 = []
        self.y_2 = []
        self.tabColor = []

        # screen commandes
        self.commandes = pygame.image.load("command_list.png").convert_alpha()
        self.displayHelp = False
        # ____FIN ATTRIBUS____

    # associe la commande avec l'action -> prop = proprietes pour les commandes (pixel, angle...)
    def moving(self, x, prop):
        # convertir en int la prop seulement si c'est pour avancer ou tourner
        if x >= 0 and x<4:
            try:
                prop = int(prop)
            except Exception as e:
                print(e)
                x = -1

        # déplacements
        if x == 0 :
            self.moveForward(prop)
            if self.pencil : self.tabColor.append(self.convertHexToRgb(self.color))
        if x == 1 :
            self.moveBackward(prop)
            if self.pencil : self.tabColor.append(self.convertHexToRgb(self.color))

        # rotation 2 => Droite; 3 => Gauche
        if x == 2 : self.rotate(-1 * prop)
        if x == 3 : self.rotate(prop)

        # changer la couleur
        if x == 4 : self.setColor("".join(prop))

        # écriture ou non 5 => pas de crayon; 6 => crayon activé
        if x == 5 : self.pencil = False
        if x == 6 : self.pencil = True

        # clean traits, replacer la tortue au centre et face vers le haut
        if x == 7 : self.cleanTurtle()

        # afficher ou masquer la tortue
        # 8 => masquer; 9 => afficher
        if x == 8 : self.displayTurtle(8)
        if x == 9 : self.displayTurtle(9)

        # help or exit
        if x == 10 : self.changeHelp()

    # rotation dans les DEUX sens
    def rotate(self, x):
        # rechargement de l'image pour éviter les mauvais affichages
        self.img = pygame.image.load("turtle.png").convert_alpha()

        # incrémentation de l'angle
        self.angle += x
        # modula 360 pour rester dans un cercle complet (360°)
        self.angle %= 360
        self.setImg(pygame.transform.rotate(self.img, self.angle))

    # affiche ou masque l'aide
    def changeHelp(self):
        # si l'affichage du l'aide est activé, le desactiver
        if self.displayHelp:
            self.displayHelp = False
        # si l'affichage du l'aide est désactivé, l'activer
        else:
            self.displayHelp = True

    # affiche ou masque la tortue
    def displayTurtle(self, x):
        # le x sert a faire la différence entre afficher et masquer. # 8 => masquer; 9 => afficher
        # si la tortue est affiché
        if self.HiddenTurtle and x == 8:
            self.HiddenTurtle = False
        # si la tortue est maquée
        elif self.HiddenTurtle == False and x == 9:
            self.HiddenTurtle = True

    # nettoyer l'écran, reset les tableaux des lignes et replace la tortue vers le haut
    def cleanTurtle(self):
        self.x = 720/2
        self.y = 720/2
        self.angle = 0
        self.color = "FFFFFF"
        self.x_1 = []
        self.y_1 = []
        self.x_2 = []
        self.y_2 = []
        self.tabColor = []
        self.img = pygame.image.load("turtle.png").convert_alpha()

    # méthode pour avancer la tortue
    def moveForward(self, x):

        # A
        # | \
        # |  \
        # |   \
        # |    \
        # |     \
        # |      \
        # |       \
        # |        \
        # |         \
        # |          \
        # |___________\
        # B             C

        # copie des anciennes coordonnées - soustraction en y pour le décalage de la surface noire
        if self.pencil:
            self.x_1.append(self.x)
            self.y_1.append(self.y - 70)

        # calcul des nouvelles coordonées
        self.x = self.x + x * math.cos(math.radians(self.angle))
        self.y = self.y - x * math.sin(math.radians(self.angle))

        # copie des nouvelle coordonées pour tracer les lignes
        if self.pencil:
            self.x_2.append(self.x)
            self.y_2.append(self.y - 70)


    # méthode pour reculer la photo
    def moveBackward(self, x):
        # copie des anciennes coordonnées - soustraction pour décalage de la surface noire
        if self.pencil:
            self.x_1.append(self.x)
            self.y_1.append(self.y - 70)

        # calcul des nouvelles coordonées
        self.x = self.x - x * math.cos(math.radians(self.angle))
        self.y = self.y + x * math.sin(math.radians(self.angle))

        # copie des nouvelle coordonées
        if self.pencil:
            self.x_2.append(self.x)
            self.y_2.append(self.y - 70)


    # méthode pour dessiner toutes les lignes renseignées
    def drawLines(self):
        for i in range(len(self.x_1)) : pygame.draw.line(window, self.tabColor[i], (self.x_1[i], self.y_1[i]), (self.x_2[i], self.y_2[i]), self.width)


    # début getter et setter
    # ____________________________________
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getAngle(self):
        return self.angle

    def getImg(self):
        return self.img

    def setX(self, arg):
        self.x = arg

    def setY(self, arg):
        self.y = arg

    def setAngle(self, arg):
        self.angle = arg

    def setImg(self, arg):
        self.img = arg

    def getHelp(self):
        return self.displayHelp

    def getHelpImg(self):
        return self.commandes

    def getHiddenOrNot(self):
        return self.HiddenTurtle

    def getColor(self):
        #  return self.color
        return self.convertHexToRgb(self.color)

    # défini la couleur
    def setColor(self, x):
        self.color = x

    def convertHexToRgb(self, value):
        try:
            c = tuple(int(value[i:i+2], 16) for i in (0, 2 ,4))
            return c
        except Exception as e:
            print(e)


    # _________________________________
    # fin getter setter

class History():
    """afficher et organiser les différents historiques"""
    def __init__(self):
        # deux tableaux pour stocker les historiques
        self.a = []
        self.b = []

        self.color = (255, 255, 255)

    # organiser les historiques, faire les changement du plus récent au plus ancien - recoit un tableau en parametre
    def drawHistory(self, arg):
        self.b = self.a[:]
        self.a = arg[:]
        del self.a[-1]
    # afficher les historiques
    def displayHistory(self):
        # display history
        fontObj = pygame.font.Font('freesansbold.ttf',18)
        string = fontObj.render("".join(self.a),True,self.color)
        window.blit(string,(affichage.getX(), 680))
        string = fontObj.render("".join(self.b),True,self.color)
        window.blit(string,(affichage.getX(), 660))


class Display():
    """classe pour tout ce qui concerne les affichages en general"""
    def __init__(self):
        self.x_Diplay = 5
        self.y_Diplay = 700
        self.police = pygame.font.Font('freesansbold.ttf', 18)
        self.color = (255, 255, 255)
        self.inputString = ["?", "_"]

    # affiche le tableau inputString dans la console du jeu
    def DisplayThis(self):
        objetWrite = self.police.render("".join(self.inputString),True,self.color)
        window.blit(objetWrite,(self.x_Diplay, self.y_Diplay))

    # _____GETTER ET SETTER______

    def getX(self):
        return self.x_Diplay

    def getY(self):
        return self.y_Diplay

    def getInputString(self):
        return self.inputString

    # redefini le tableau de caractère
    def setInputString(self, x):
        self.inputString = x

    def appendInputString(self, x):
        self.inputString.append(x)

    def delInputString(self, x):
        del self.inputString[x]
    # _____FIN GETTER ET SETTER______


# instance des 3 objets
tortue = tortue()
history = History()
affichage = Display()
