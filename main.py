# @Author: Jean Debuisson  <jeandebuisson>
# @Date:   2017-03-02T09:52:49+01:00
# @Email:  214783@supinfo.com
# @Filename: main.py
# @Last modified by:   Quentin Lemaire
# @Last modified time: 2017-03-13T12:30:06+01:00
# @License: 214783
# @Copyright: SUPINFO


from globales import *
from pygame import *
from functions import *

def main():
    game = 1
    while game:
        for event in pygame.event.get():
            if event.type == QUIT:
                game = 0

            if event.type == KEYDOWN:
                # lance l'execution de reconnaissance de la lettre et effectue les opérations en fonction
                letter = wichLetter(event.key)

            # flip screen
            reloadScreen()

if __name__ == '__main__':
    main()
