# coding: utf8
# @Author: Jean Debuisson  <jeandebuisson>
# @Date:   2017-03-02T09:52:49+01:00
# @Email:  214783@supinfo.com
# @Filename: main.py
# @Last modified by:   SkYNewZ
# @Last modified time: 2017-04-01T03:39:25+02:00
# @License: 214783
# @Copyright: SUPINFO

from globales import *
from pygame import *
from functions import *


def main():
    """
    main function
    :return: 
    :rtype: 
    """
    game = 1
    while game:
        for event in pygame.event.get():
            if event.type == QUIT:
                game = 0

            if event.type == KEYDOWN:
                # send letters's key
                which_letter(event.key)

            # flip screen
            reload_screen()

if __name__ == '__main__':
    main()
