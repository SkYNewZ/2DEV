# coding: utf8
# @Author: Quentin Lemaire
# @Date:   2017-02-28T16:59:36+01:00
# @Email:  quentin.lemaire@supinfo.com
# @Filename: functions.py
# @Last modified by:   SkYNewZ
# @Last modified time: 2017-04-01T02:27:04+02:00
# @License: 214520
# @Copyright: SUPINFO



import pygame
from globales import *
from pygame import *
from translateCommand import dissociate

pygame.init()


def reload_screen():
    """
    refresh screen
    :return: 
    :rtype: 
    """
    pygame.display.update()
    window.blit(background, (0, 0))
    turtle_object.draw_lines()
    if turtle_object.getHiddenOrNot():
        window.blit(turtle_object.getImg(), (turtle_object.getX() - 25, turtle_object.getY() - 25 - 72))
    display_object.display_this()
    history.display_history()
    if turtle_object.getHelp():
        window.blit(turtle_object.getHelpImg(), (40, 100))


def which_letter(key_letter):
    """
    send character and append to the list
    :param key_letter: letters's key
    :type key_letter: int
    :return: 
    :rtype: 
    """
    "refer array"
    key_code = [113, 119, 101, 114, 116, 121, 117, 105, 111, 112, 97, 115, 100, 102, 103, 104, 106, 107, 108, 59, 122,
               120, 99, 118, 98, 110, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 40, 41]
    letter = ["A", "Z", "E", "R", "T", "Y", "U", "I", "O", "P", "Q", "S", "D", "F", "G", "H", "J", "K", "L", "M", "W",
              "X", "C", "V", "B", "N", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "[", "]"]
    actions_key = [8, 13, 32, 273]

    "letter or number"
    if key_letter in key_code:
        display_object.delInputString(-1)
        idx = key_code.index(key_letter)
        display_object.appendInputString(letter[idx])
        display_object.appendInputString("_")

    elif key_letter in actions_key:
        "backspace"
        if key_letter == 8:
            delete_input()

        "space"
        if key_letter == 32:
            display_object.delInputString(-1)
            display_object.appendInputString(" ")
            display_object.appendInputString("_")

        "enter"
        if key_letter == 13:
            validate()

        "upper"
        if key_letter == 273:
            pass

    else:
        "if error, do nothing, just pass"
        pass


def delete_input():
    """
    delete last character
    :return: 
    :rtype: 
    """
    if len(display_object.getInputString()) > 2:
        display_object.delInputString(-2)


def clean_prompt():
    """
    delete "_" and "?"
    :return: 
    :rtype: 
    """
    while len(display_object.getInputString()) > 1:
        display_object.delInputString(-1)
    display_object.appendInputString("_")


def validate():
    """
    enter key, do rest   
    :return: none
    :rtype: none
    """
    "dissociate command and property"
    dissociate()

    "do history"
    history.draw_history(display_object.getInputString())

    "clean previous command"
    clean_prompt()
