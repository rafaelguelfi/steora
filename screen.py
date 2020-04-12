import sys
import os
import textwrap
import pickle
import json
import time

os.system('clear')

frame = {
   'H'	: '═',
   'V'	: '║',
   'VH'	: '╬',

   'upper-right-corner'	: '╗',
   'down-right-corner'	: '╝',
   'upper-left-corner'	: '╔',
   'down-left-corner'	: '╚',

   'V-left'	: '╣',
   'V-right'	: '╠',
   'H-upper'	: '╩',
   'H-down'	: '╦',
}

class color:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'
    lightblack = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    lightyellow = '\033[93m'
    lightblue = '\033[94m'
    lightmagenta = '\033[95m'
    lightcyan = '\033[96m'
    lightwhite = '\033[97m'

    blackbg = '\033[40m'
    redbg = '\033[41m'
    greenbg = '\033[42m'
    yellowbg = '\033[43m'
    bluebg = '\033[44m'
    magentabg = '\033[45m'
    cyanbg = '\033[46m'
    whitebg = '\033[47m'
    lightblackbg = '\033[100m'
    lightredbg = '\033[101m'
    lightgreenbg = '\033[102m'
    lightyellowbg = '\033[103m'
    lightbluebg = '\033[104m'
    lightmagentabg = '\033[105m'
    lightcyanbg = '\033[106m'
    lightwhitebg = '\033[107m'

    bold = '\033[1m'
    underline = '\033[4m'
    blink = '\033[5m'
    stroke = '\033[9m'
    end = '\033[0m'

def screen(screename, text, optiontitle, options):
    # text = '1234567890123456789012345678901234567890123456789012345678901234567890' \
    #        '1234567890123456789012345678901234567890123456789012345678901234567890' \
    #        '1234567890123456789012345678901234567890123456789012345678901234567890' \
    #        '1234567890123456789012345678901234567890123456789012345678901234567890' \
    #        '1234567890123456789012345678901234567890123456789012345678901234567890' \
    #        '1234567890123456789012345678901234567890123456789012345678901234567890' \
    #        '1234567890123456789012345678901234567890123456789012345678901234567890' \
    #        '1234567890123456789012345678901234567890123456789012345678901234567890' \
    #        '1234567890123456789012345678901234567890123456789012345678901234567890' \
    #        '1234567890123456789012345678901234567890123456789012345678901234567890' \
    #        '1234567890123456789012345678901234567890123456789012345678901234567890' \
    #        '1234567890123456789012345678901234567890123456789012345678901234567890' \
    #        '1234567890123456789012345678901234567890123456789012345678901234567890' \
    #        '1234567890123456789012345678901234567890123456789012345678901234567890'
    # cabem 980 caracteres
 #   optiontitle = 'OPTIONTITLE UMA OPÇÃO'

    # options = "1)______________ 2)______________ 3)______________ 4)______________ " \
    #          "5)______________ 6)______________ 7)______________ 8)______________ " \
    #          "9)______________ 10)_____________ 11)_____________ 12)_____________ " \
    #          "13)_____________ 14)_____________ 15)_____________ 16)_____________ "

#    screename = 'ISSO É UM TESTE'

    version = '0.00'

    wrapped_text = textwrap.wrap(text,replace_whitespace=False,expand_tabs=False)

    width = 75
    height = 20 - len(wrapped_text)

    def TEXT():
        for line in wrapped_text:
            print(line.center(width - 2))

    def OPTIONS():
        print(options.center(width-2))

    FOOTNOTE = f'Version {version}'.rjust(width - 2, (frame['H']))
    SCREENTITLE = f'{screename}'.center(width - 2, frame['H'])
    OPTIONTITLE = f'{optiontitle}'.center(width - 2, frame['H'])

    for i in range(height):
        for j in range(width):
            if (i==0 and j==0):
                print(frame['upper-left-corner']+SCREENTITLE+frame['upper-right-corner'])
                TEXT()
            elif (i==height-5 and (j==0)):
                print(frame['V-right']+OPTIONTITLE+frame['V-left'])
                OPTIONS()
                print(frame['down-left-corner']+FOOTNOTE+frame['down-right-corner'])
                global inpt
                inpt=input('> ')
        print()

def screengame(bar,screename, text, optiontitle, options):
    version = '0.00'

    wrapped_text = textwrap.wrap(text,replace_whitespace=False,expand_tabs=False)

    width = 75
    height = 20 - len(wrapped_text) - 4

    def BAR():
        print(bar)

    def TEXT():
        for line in wrapped_text:
            print(line.center(width - 2))

    def OPTIONS():
        print(options)

    FOOTNOTE = f'Version {version}'.rjust(width - 2, (frame['H']))
    SCREENTITLE = f'{screename}'.center(width - 2, frame['H'])
    OPTIONTITLE = f'{optiontitle}'.center(width - 2, frame['H'])

    for i in range(height):
        for j in range(width):
            if (i==0 and j==0):
                print(frame['upper-left-corner']+SCREENTITLE+frame['upper-right-corner'])
                BAR()
                TEXT()
            elif (i==height-5 and (j==0)):
                print(frame['V-right']+OPTIONTITLE+frame['V-left'])
                OPTIONS()
                print(frame['down-left-corner']+FOOTNOTE+frame['down-right-corner'])
                global inpt
                inpt=input('> ')
        print()

def screencombat(bar,screename, text, optiontitle, options):
    version = '0.00'

    width = 75
    height = 7

    def BAR():
        print(bar)

    def TEXT():
        print(text)

    def OPTIONS():
        print(options)

    FOOTNOTE = f'Version {version}'.rjust(width - 2, (frame['H']))
    SCREENTITLE = f'{screename}'.center(width - 2, frame['H'])
    OPTIONTITLE = f'{optiontitle}'.center(width - 2, frame['H'])

    for i in range(height):
        for j in range(width):
            if (i==0 and j==0):
                print(frame['upper-left-corner']+SCREENTITLE+frame['upper-right-corner'])
                BAR()
                TEXT()
            elif (i==height-5 and (j==0)):
                print(frame['V-right']+OPTIONTITLE+frame['V-left'])
                OPTIONS()
                print(frame['down-left-corner']+FOOTNOTE+frame['down-right-corner'])
                global inpt
                inpt=input('> ')
        print()

def screenfree(screename, text, optiontitle, options):
    version = '0.00'

#    wrapped_text = textwrap.wrap(text,replace_whitespace=False,expand_tabs=False)

    width = 75
    height = 7

    def TEXT():
        print(text)

    def OPTIONS():
        print(options)

    FOOTNOTE = f'Version {version}'.rjust(width - 2, (frame['H']))
    SCREENTITLE = f'{screename}'.center(width - 2, frame['H'])
    OPTIONTITLE = f'{optiontitle}'.center(width - 2, frame['H'])

    for i in range(height):
        for j in range(width):
            if (i==0 and j==0):
                print(frame['upper-left-corner']+SCREENTITLE+frame['upper-right-corner'])
                TEXT()
            elif (i==height-5 and (j==0)):
                print(frame['V-right']+OPTIONTITLE+frame['V-left'])
                OPTIONS()
                print(frame['down-left-corner']+FOOTNOTE+frame['down-right-corner'])
                global inpt
                inpt=input('> ')
        print()

def screenwalk(screename, text, optiontitle, options):
    version = '0.00'

#    wrapped_text = textwrap.wrap(text,replace_whitespace=False,expand_tabs=False)

    width = 75
    height = 6

    def TEXT():
        print()
        print(text)

    def OPTIONS():
        print(options)

    FOOTNOTE = f'Version {version}'.rjust(width - 2, (frame['H']))
    SCREENTITLE = f'{screename}'.center(width - 2, frame['H'])
    OPTIONTITLE = f'{optiontitle}'.center(width - 2, frame['H'])

    for i in range(height):
        for j in range(width):
            if (i==0 and j==0):
                print(frame['upper-left-corner']+SCREENTITLE+frame['upper-right-corner'])
                TEXT()
            elif (i==height-5 and (j==0)):
                print(frame['V-right']+OPTIONTITLE+frame['V-left'])
                OPTIONS()
                print(frame['down-left-corner']+FOOTNOTE+frame['down-right-corner'])
                global inpt
                inpt=input('> ')
        print()

os.system('clear')

