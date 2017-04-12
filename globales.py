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

"initial display"
window = pygame.display.set_mode((720, 720))
pygame.display.set_caption('LOGO')
background = pygame.image.load("background.png").convert()
window.blit(background, (0, 0))


class TurtleClass:
    """turtle object, with moving and display"""

    def __init__(self):
        """
        constructor
        """
        "_____ATTRIBUTE_____"

        "size of turtle image"
        self.dimensions_x = 50
        self.dimensions_y = 50
        self.img = pygame.image.load("TurtleClass.png").convert_alpha()

        "center of screen"
        self.x = 720 / 2
        self.y = 720 / 2

        "attribute of angle"
        self.angle = 0

        "display and lines"
        self.width = 1
        self.pencil = True
        self.HiddenTurtle = True
        self.color = "FFFFFF"

        "array for trace lines"
        self.x_1 = []
        self.y_1 = []
        self.x_2 = []
        self.y_2 = []
        self.tabColor = []

        self.commands = pygame.image.load("command_list.png").convert_alpha()
        self.displayHelp = False
        "____FIN ATTRIBUTES____"

    def moving (self, x, prop):
        """
        associate command with action and give properties
        :param x: command
        :type x: string
        :param prop: color or coordinate or distance
        :type prop: string or int
        :return: 
        :rtype: 
        """
        if 0 <= x < 4:
            try:
                prop = int(prop)
            except Exception as e:
                print(e)
                x = -1

        "moves"
        if x == 0:
            self.move_forward(prop)
            if self.pencil:
                self.tabColor.append(self.convertHexToRgb(self.color))
        if x == 1:
            self.move_backward (prop)
            if self.pencil:
                self.tabColor.append(self.convertHexToRgb(self.color))

        """
        Rotate
        2 => Right
        3 => Left
        """
        if x == 2:
            self.rotate(-1 * prop)
        if x == 3:
            self.rotate(prop)

        """Change color"""
        if x == 4:
            self.setColor("".join(prop))

        """
        Write or not
        5=> not write
        6=> write
        """
        if x == 5:
            self.pencil = False
        if x == 6:
            self.pencil = True

        """clean traits, replace the turtle et face upward"""
        if x == 7:
            self.clean_turtle ()

        """
        display or not the turtle
        8 => hide
        9 => display
        """
        if x == 8:
            self.displayTurtle(8)
        if x == 9:
            self.displayTurtle(9)

        """help or exit"""
        if x == 10:
            self.display_help()

    def rotate(self, x):
        """
        rotation
        :param x: degrees
        :type x: int
        :return: 
        :rtype: 
        """

        """reload the turtle image"""
        self.img = pygame.image.load("TurtleClass.png").convert_alpha ()

        """increase angle"""
        self.angle += x
        """modulo 360 to stay in a circle(360°)"""
        self.angle %= 360
        self.setImg(pygame.transform.rotate(self.img, self.angle))

    def display_help(self):
        """
        hide or display help
        :return: 
        :rtype: 
        """
        """if help displayed, hide it
        if help hidden, display it"""
        if self.displayHelp:
            self.displayHelp = False

        elif not self.displayHelp:
            self.displayHelp = True

    def display_turtle(self, x):
        """
        hide or display the turtle
        :param self: 
        :type self: 
        :param x: id help
        :type x: int
        :return: 
        :rtype: 
        """
        """
        8 => hide
        9 => display
        """

        if self.HiddenTurtle and x == 8:
            self.HiddenTurtle = False

        elif self.HiddenTurtle == False and x == 9:
            self.HiddenTurtle = True

    def clean_turtle(self):
        """
        clean turtle and place face upward
        :return: 
        :rtype: 
        """
        self.x = 720 / 2
        self.y = 720 / 2
        self.angle = 0
        self.color = "FFFFFF"
        self.x_1 = []
        self.y_1 = []
        self.x_2 = []
        self.y_2 = []
        self.tabColor = []
        self.img = pygame.image.load("TurtleClass.png").convert_alpha ()

    def move_forward(self, x):
        """
        move upward TurtleClass
        :param x: distance
        :type x: int
        :return: 
        :rtype: 
        """

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

        "copy old coordinates - subtract pour black surface"
        if self.pencil:
            self.x_1.append(self.x)
            self.y_1.append(self.y - 70)

        "new coordinates"
        self.x = self.x + x * math.cos (math.radians (self.angle))
        self.y = self.y - x * math.sin (math.radians (self.angle))

        "copy for drawing lines"
        if self.pencil:
            self.x_2.append (self.x)
            self.y_2.append (self.y - 70)

    def move_backward(self, x):
        """
        move backward TurtleClass
        :param x: distance
        :type x: int
        :return: 
        :rtype: 
        """
        "copy old coordinates"
        if self.pencil:
            self.x_1.append(self.x)
            self.y_1.append(self.y - 70)

        "new coordinates"
        self.x = self.x - x * math.cos (math.radians (self.angle))
        self.y = self.y + x * math.sin (math.radians (self.angle))

        "copy new coordinates"
        if self.pencil:
            self.x_2.append(self.x)
            self.y_2.append(self.y - 70)

    def draw_lines(self):
        """
        draw knew lines
        :return: 
        :rtype: 
        """
        for i in range(len (self.x_1)):
            pygame.draw.line(window, self.tabColor[i], (self.x_1[i], self.y_1[i]), (self.x_2[i], self.y_2[i]),
                             self.width)

    """Setter & getters"""
    def getX(self):
        """
        get coordinate x
        :return: coordinate x
        :rtype: int
        """
        return self.x

    def getY(self):
        """
        get coordinate y
        :return: coordinate y
        :rtype: int
        """
        return self.y

    def getAngle(self):
        """
        get angle
        :return: angle
        :rtype: int
        """
        return self.angle

    def getImg(self):
        """
        get image
        :return: object image
        :rtype: object
        """
        return self.img

    def setX(self, arg):
        """
        set coordinate x
        :param arg: coordinate x
        :type arg: int
        :return: 
        :rtype: 
        """
        self.x = arg

    def setY(self, arg):
        """
        set coordinate y
        :param arg: coordinate y
        :type arg: int
        :return: 
        :rtype: 
        """
        self.y = arg

    def setAngle(self, arg):
        """
        set angle
        :param arg: angle
        :type arg: int
        :return: 
        :rtype: 
        """
        self.angle = arg

    def setImg(self, arg):
        """
        set image to reload
        :param arg: image
        :type arg: object
        :return: 
        :rtype: 
        """
        self.img = arg

    def getHelp(self):
        """
        know if help is display
        :return: 
        :rtype: 
        """
        return self.displayHelp

    def getHelpImg(self):
        """
        get help image
        :return: help image
        :rtype: object
        """
        return self.commands

    def getHiddenOrNot(self):
        """
        return if turtle is displayed
        :return: turtle
        :rtype: object
        """
        return self.HiddenTurtle

    def getColor(self):
        """
        return color
        :return: color
        :rtype: string
        """
        return self.convertHexToRgb (self.color)

    def setColor (self, x):
        """
        set color
        :param x: color
        :type x: string
        :return: 
        :rtype: 
        """
        self.color = x

    def convertHexToRgb(self, value):
        """
        convert string HEX in RGB
        :param value: color (HEX)
        :type value: string
        :return: color (RGB)
        :rtype: tuple
        """
        try:
            c = tuple (int (value[i:i + 2], 16) for i in (0, 2, 4))
            return c
        except Exception as e:
            print(e)
    """end setters & getters"""


class History:
    """
    display and organise history
    """

    def __init__ (self):
        """
        stock histories
        """
        self.a = []
        self.b = []

        self.color = (255, 255, 255)

    def draw_history(self, arg):
        """
        organise histories, old -> last
        :param arg: array history
        :type arg: array
        :return: 
        :rtype: 
        """
        self.b = self.a[:]
        self.a = arg[:]
        del self.a[-1]

    def display_history(self):
        """
        display histories
        :return: 
        :rtype: 
        """
        font_obj = pygame.font.Font('freesansbold.ttf', 18)
        string = font_obj.render("".join (self.a), True, self.color)
        window.blit(string, (display_object.getX(), 680))
        string = font_obj.render("".join(self.b), True, self.color)
        window.blit(string, (display_object.getX(), 660))


class Display ():
    """display"""

    def __init__(self):
        self.x_display = 5
        self.y_display = 700
        self.police = pygame.font.Font('freesansbold.ttf', 18)
        self.color = (255, 255, 255)
        self.inputString = ["?", "_"]

    def display_this(self):
        """
        display shell
        :return: 
        :rtype: 
        """
        objet_write = self.police.render("".join (self.inputString), True, self.color)
        window.blit(objet_write, (self.x_display, self.y_display))

    "GETTER & SETTER"

    def getX(self):
        """
        
        :return: x
        :rtype: int
        """
        return self.x_display

    def getY(self):
        """
        get y display for history
        :return: y
        :rtype: int
        """
        return self.y_display

    def getInputString(self):
        """
        return array of shell
        :return: inputString
        :rtype: array
        """
        return self.inputString

    def setInputString(self, x):
        """
        refresh shell
        :param x: replacement
        :type x: array
        :return: 
        :rtype: 
        """
        self.inputString = x

    def appendInputString(self, x):
        """
        append at the end of inputString
        :param x: something
        :type x: int, string
        :return: 
        :rtype: 
        """
        self.inputString.append (x)

    def delInputString(self, x):
        """
        delete something from the array
        :param x: index
        :type x: int
        :return: 
        :rtype: 
        """
        del self.inputString[x]
        # _____FIN GETTER ET SETTER______


"Create instances"
turtle_object = TurtleClass()
history = History()
display_object = Display()
