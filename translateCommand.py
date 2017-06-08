# coding: utf8
# @Author: Quentin Lemaire
# @Date:   2017-03-09T14:18:47+01:00
# @Email:  quentin.lemaire@supinfo.com
# @Filename: translateCommand.py
# @Last modified by:   SkYNewZ
# @Last modified time: 2017-04-01T15:26:39+02:00
# @License: 214520
# @Copyright: SUPINFO

import pygame
import copy
from globales import *
from pygame import *


def dissociate():
    """
    dissociate command and property
    :return: 
    :rtype: 
    """
    "copy array"
    tab = display_object.getInputString()[1:-1]

    "dissociate command and properties"
    prop = []
    command = []
    current_tab = command
    for i in range(len(tab)):
        b = True
        if tab[i] == " ":
            current_tab = prop
            b = False
        if b:
            current_tab.append(tab[i])

    "transform date to exploit"
    command = "".join(command)
    prop = "".join(prop)

    "associate command list"
    commands_list = {"AV": 0, "RE": 1, "TD": 2, "TG": 3, "FCC": 4, "LC": 5, "BC": 6, "VE": 7,
                     "CT": 8, "MT": 9, "HELP": 10, "REPETE": 11}

    repete_validation = 1
    error = [' = > u', 'n', 'k', 'n', 'o', 'w', ' ', 'c', 'o', 'm', 'm', 'a', 'n', 'd']
    if command == "REPETE" and len(prop) <= 0 or "]" not in prop or "[" not in prop:
        repete_validation = 0
        error = [' = > argument missing']

    "if in the list, continue"
    if command in commands_list and repete_validation:
        turtle_object.moving(commands_list[command], prop)
    else:
        "else, error in shell"
        t = display_object.getInputString()[1:-1]
        t = "".join(t)
        display_object.setInputString(
            ['?', t, "".join(error), '_'])
