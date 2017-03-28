# @Author: Quentin Lemaire
# @Date:   2017-02-28T16:59:36+01:00
# @Email:  quentin.lemaire@supinfo.com
# @Filename: functions.py
# @Last modified by:   Quentin Lemaire
# @Last modified time: 2017-03-14T17:16:50+01:00
# @License: 214520
# @Copyright: SUPINFO



import pygame
from globales import *
from pygame import *
from translateCommand import dissociate
pygame.init()

# fonction servant a recharger l'affichage
def reloadScreen():
    pygame.display.update()
    window.blit(background, (0, 0))
    tortue.drawLines()
    if tortue.getHiddenOrNot(): window.blit(tortue.getImg(), (tortue.getX()-25, tortue.getY() - 25-72))
    affichage.DisplayThis()
    history.displayHistory()
    if tortue.getHelp() : window.blit(tortue.getHelpImg(), (40, 100))


# fonction servant a renvoyer le caractrère tapé au clavier et l'ajouter a la liste
def wichLetter(key):
    # tableau de référence pour les lettres entrées
    keyCode = [113, 119, 101, 114, 116, 121, 117, 105, 111, 112, 97, 115, 100, 102, 103, 104, 106, 107, 108, 59, 122, 120, 99, 118, 98, 110, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265]
    letter = ["A", "Z", "E", "R", "T", "Y", "U", "I", "O", "P", "Q", "S", "D", "F", "G", "H", "J", "K", "L", "M", "W", "X", "C", "V", "B", "N", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    actionsKey = [8, 13, 32, 273]

    # si la lettre est valide dans l'un des 2 cas, il la retourne
    # si c'est une lettre ou un chiffre
    if (key in keyCode):
        affichage.delInputString(-1)
        idx = keyCode.index(key)
        # ajout de la lettre dans le tableau
        affichage.appendInputString(letter[idx])
        affichage.appendInputString("_")

    # si c'est la touche effacer, entrée, fleche du haut ou espace
    elif (key in actionsKey):
            # effacer
            if (key == 8): deleteInput()

            #space
            if (key == 32) :
                affichage.delInputString(-1)
                affichage.appendInputString(" ")
                affichage.appendInputString("_")

            #valider
            if (key == 13):
                validate()

            # rappel commande
            if key == 273:
                pass

    # sinon, il ne fait rien - gestion de l'erreur touche inconnue
    else :
        pass


#lorsque qu'on appui sur effacer - effacer le dernier caractère
def deleteInput():
    if (len(affichage.getInputString()) > 2) :
        affichage.delInputString(-2)


# effacer précedente commande - effacer la liste en laissant ? et _
def cleanPrompt():
    while (len(affichage.getInputString()) > 1):
        affichage.delInputString(-1)
    affichage.appendInputString("_")

# actions après la touche entrée
def validate():

    # dissocier les commandes et continuer pour l'execution
    dissociate()

    # historique - effectué le roulement
    history.drawHistory(affichage.getInputString())

    # clean previous command
    cleanPrompt()
