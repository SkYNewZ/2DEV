# coding: utf8
# @Author: Quentin Lemaire
# @Date:   2017-03-09T14:18:47+01:00
# @Email:  quentin.lemaire@supinfo.com
# @Filename: translateCommand.py
# @Last modified by:   SkYNewZ
# @Last modified time: 2017-04-01T15:23:03+02:00
# @License: 214520
# @Copyright: SUPINFO

import pygame
import copy
from globales import *
from pygame import *

# dissocier la commande et les proprietes
def dissociate():
    # copie du tableau en gardant que la commande
    tab = affichage.getInputString()[1:-1]

    # dissocier la commande des proprietes
    prop = []
    commande = []
    tab_courant = commande
    for i in range(len(tab)):
        b = True
        if (tab[i] == " "):
            tab_courant = prop
            b = False
        if (b):
            tab_courant.append(tab[i])

    # tranfromer les données pour les exploiter
    commandeString = "".join(commande)
    prop = "".join(prop)

    # dictionnaire des commandes - pour association avec les différentes fonctions
    commandsList = dict()
    commandsList = {"AV" : 0, "RE" : 1, "TD" : 2, "TG" : 3, "FCC" : 4, "LC" : 5, "BC" : 6, "VE" : 7, "CT" : 8, "MT" : 9, "HELP" : 10}

    # si présent dans la liste, on continue
    if commandeString in commandsList:
        tortue.moving(commandsList[commandeString], prop)
    # sinon, inscrire dans la console - PREVOIR INSCRIRE DANS L'HISTORIQUE
    else :
        t = affichage.getInputString()[1:-1]
        t = "".join(t)
        affichage.setInputString(['?', t,' = > u', 'n', 'k', 'n', 'o', 'w', ' ', 'c', 'o', 'm', 'm', 'a', 'n', 'd', '_'])
