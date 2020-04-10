import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import screen
import data.races as races
from pygame import mixer
import pickle

class config:
    def __init__(self):
        self.music=True
        self.autosave=False
cfg=config()

if os.path.exists('cfg.p'):
    with open('cfg.p', 'rb') as fp:
        cfg.music = pickle.load(fp)
        cfg.autosave = pickle.load(fp)

mixer.init()
mixer.music.load('data/SpaceOddity.mp3')
if cfg.music is True:
    mixer.music.play(-1)


def setting():
    screename ='STEORA'
    text =f'''
    
    
    
                               MUSIC: {"ON" if cfg.music is True else "OFF"}
                               AUTOSAVE: {"ON" if cfg.autosave is True else "OFF"}
    
    
    
    
    
    
    '''
    optiontitle='SETTINGS'
    options = '.................1)MUSIC........................2)AUTOSAVE.................\n' \
             '...........................................................................\n' \
             '............................ENTER TO GO BACK...............................\n' \
             '...........................................................................'
    screen.screenfree(screename, text, optiontitle, options)
    if screen.entrada is '1':
        if cfg.music==True:
            mixer.music.stop()
            cfg.music=False
        else:
            mixer.music.play(-1)
            cfg.music=True
        with open('cfg.p', 'wb') as fp:
            pickle.dump(cfg.music, fp)
            pickle.dump(cfg.autosave, fp)
        setting()
    elif screen.entrada is '2':
        if cfg.autosave==True:
            cfg.autosave=False
        else:
            cfg.autosave=True
        with open('cfg.p', 'wb') as fp:
            pickle.dump(cfg.music, fp)
            pickle.dump(cfg.autosave, fp)
        setting()
    elif screen.entrada is '':
        titlescreen()
    else:
        setting()

def titlescreen():
    global loaded, savefile
    loaded = False
    savefile = ''

    screename = ''

    stars = f'''  *    .  *       .             *    {screen.color.blink}*{screen.color.end}
                           *   .        *       .      .       *    .     *   .     .         {screen.color.blink}*{screen.color.end}       .                .        ..  *       .    {screen.color.blink}*{screen.color.end}                     *           .     .  *        {screen.color.blink}*{screen.color.end}.       .                .        ..  {screen.color.blink}*{screen.color.end}           *           .         {screen.color.blink}*{screen.color.end}     .    .     .               .                             .  .  *       .             *                .         {screen.color.blink}*{screen.color.end} *   .        *       .       .       * *   .        {screen.color.blink}*{screen.color.end}       .       .       *'''

    logo ='''     _______.___________. _______   ______   .______          ___      
    /       |           ||   ____| /  __  \  |   _  \        /   \     
   |   (----`---|  |----`|  |__   |  |  |  | |  |_)  |      /  ^  \    
 ___\   \       |  |     |   __|  |  |  |  | |      /______/  /_\  \   
.----)   |      |  |     |  |____ |  `--´  | |  |\  \----./  _____  \  
|_______/       |__|     |_______| \______/  | _| `._____/__/     \__\ '''

    text = screen.color.lightcyan + logo + screen.color.end + stars
    
    optiontitle=''

    options = '................1)PLAY........................2)SETTINGS...................\n' \
             '...........................................................................\n' \
             '................3)HELP........................4)ABOUT......................\n' \
             '...............................5)QUIT......................................'

    screen.screen(screename, text, optiontitle, options)

    if screen.entrada is '1':
        screename = ''

        text = screen.color.lightcyan + logo + screen.color.end + stars

        optiontitle = 'PLAY'

        options = '...........................................................................\n' \
                 '................1)NEW GAME....................2)LOAD GAME..................\n' \
                 '............................ENTER TO GO BACK...............................\n' \
                 '...........................................................................'

        screen.screen(screename, text, optiontitle, options)

        if screen.entrada is '1':

            screename = f'INTRO'

            text = f"The year is 5733. Many civilizations of Steora - as the galaxy is called - had advanced significantly after the flourish of quasi-dimensional technology, allowing a movement that astrohistorians named galaticalization. The almost instantaneous quasi-dimensional communication served well for the strengthen of interracial diplomatic relationship, which culminated in the sign of the Karsov's Pact.    The Karsov's Pact is sign by the 12 races that has a status of permanent chair in the League of Steora. In this pact, it was guaranteed that the deep space, beyond the domains of a stellar system, should remain as autonomous region. The treaty also approved the construction of the Karsov's Base, a huge installation that orbits the supermassive black hole in the center of the galaxy, it's function is not only to be a safeport for interstellar travel, but also to harvest the energy from the black hole to the members of the League"

            optiontitle = ''

            options = '...........................................................................\n' \
                     '............................ENTER TO CONTINUE..............................\n' \
                     '...........................................................................\n' \
                     '...........................................................................'

            screen.screen(screename, text, optiontitle, options)

            text = f"As the Karsov's Pact stopped any attempt to establish a galactic government dictatorship, also stopped any race from legislate in space. Several groups faced that as an opportunity for space piracy, attacking cargo spaceships and hiding in remote planets and desert moons.                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀The consequence was the urge of bounty hunters across the galaxy, looking for personal gain and aiming to capture those who had a bounty on their head.                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀But, the deep space didn't became just a lawless land, several space explorers venture into the edges of Steora, looking for undiscovered worlds that may or may not present biological activity."

            screen.screen(screename, text, optiontitle, options)

            text = f"Space exploration is strongly encouraged by the League, aiming to reinforce the principle of the Knowledge Universalization established in the Pact, in such way to make the Unified System Catalogue (USC) accessible to all.                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Another measure taken with the Karsov's Pact is the formation of a single galactic economical block, facilitating and stimulating the trading between members of the League and adopting a common currency named Quain and symbolized by {screen.color.stroke}Q{screen.color.end}.                             ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀And in this context that you're in! But, what is your name?                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀(The name you choose will be used to load your game later!)"

            options = '...........................................................................\n' \
                     '..............................TYPE YOUR NAME...............................\n' \
                     '...........................................................................\n' \
                     '...........................................................................'

            screen.screen(screename, text, optiontitle, options)
            while screen.entrada is '':
                optiontitle = 'INVALID NAME!'
                screen.screen(screename, text, optiontitle, options)
            global playername
            playername = screen.entrada

            def racechoice():
                text=f"{playername}! Right... And which race you'll choose? Each race has a bonus in certain attribute and starts in a different planet!                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Races with bonus in Agility: Humans, Kal-shon, Zayolin                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Races with bonus in Dexterity: Alnits, Droides, Zorahtos                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Races with bonus in Intelligence: Kaitos, Lattuns, Ophidianos                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Races with bonus in Luck: Destanis, Nephinos, Svastos                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Choose a race to know more, don't worry, you can come back to here later!"

                optiontitle = ''
                options = '.....1)HUMANS..................2)KAL-SHON..................3)ZAYOLIN.......\n' \
                         '.....4)ALNITS..................5)DROIDES...................6)ZORAHTOS......\n' \
                         '.....7)KAITOS..................8)LATTUNS...................9)OPHIDIANOS....\n' \
                         '.....10)DESTANIS...............11)NEPHINOS.................12)SVASTOS......'
                screen.screen(screename, text, optiontitle, options)
                global playerrace
                playerrace = screen.entrada

                while screen.entrada not in ['1','2','3','4','5','6','7','8','9','10','11','12']:
                    optiontitle = 'INVALID OPTION'
                    screen.screen(screename, text, optiontitle, options)
                    playerrace = screen.entrada

                def racechoice2(playerrace):
                    screename = f'{races.races[playerrace]["name"]}'

                    text = f'The {races.races[playerrace]["name"]} are original inhabitants of the planet {races.races[playerrace]["planet"]} in the {races.races[playerrace]["system"]} System. Physically {races.races[playerrace]["description"]}. The bonus of this race is {races.races[playerrace]["bonus"]} points in {races.races[playerrace]["attribute"]} and the innate skills: {races.races[playerrace]["skills"]}'

                    optiontitle = 'CONFIRM RACE?'

                    options = '..........1)CONFIRM.....................3)CULTURAL INFORMATION.............\n' \
                             '...........................................................................\n' \
                             '..........2)SKILLS INFORMATION.........................0)BACK..............\n' \
                             '...........................................................................'
                    screen.screen(screename, text, optiontitle, options)
                    global playersplanet
                    global playerssystem
                    global playerscity
                    global choosenrace
                    if screen.entrada is '1':
                        playerscity=(races.races[playerrace]["city"]).upper()
                        playersplanet=(races.races[playerrace]["planet"]).upper()
                        playerssystem=(races.races[playerrace]["system"]).upper()
                        choosenrace=races.races[playerrace]["singularname"]

                    elif screen.entrada is '2':
                        screename = f'{races.races[playerrace]["name"]}: SKILLS'

                        text = f'WIP'

                        optiontitle = 'CONFIRM RACE?'

                        options = '...........................................................................\n' \
                                 '...........1)CONFIRM....................................0)BACK.............\n' \
                                 '...........................................................................\n' \
                                 '...........................................................................'
                        screen.screen(screename, text, optiontitle, options)
                        if screen.entrada is '1':
                            playerscity = (races.races[playerrace]["city"]).upper()
                            playersplanet = races.races[playerrace]["planet"]
                            playerssystem = races.races[playerrace]["system"]
                            choosenrace = races.races[playerrace]["singularname"]

                        else:
                            racechoice2(playerrace)
                    elif screen.entrada is '3':
                        screename = f'{races.races[playerrace]["name"]}: CULTURE'

                        text = f'The {races.races[playerrace]["name"]} {races.races[playerrace]["culture"]}'

                        optiontitle = 'CONFIRM RACE?'

                        options = '...........................................................................\n' \
                                 '...........1)CONFIRM....................................0)BACK.............\n' \
                                 '...........................................................................\n' \
                                 '...........................................................................'
                        screen.screen(screename, text, optiontitle, options)
                        if screen.entrada is '1':
                            playerscity = (races.races[playerrace]["city"]).upper()
                            playersplanet = races.races[playerrace]["planet"]
                            playerssystem = races.races[playerrace]["system"]
                            choosenrace = races.races[playerrace]["singularname"]

                        else:
                            racechoice2(playerrace)
                    else:
                        racechoice()
                racechoice2(playerrace)
            racechoice()

        elif screen.entrada is '2':
            screename = f'STEORA'
            text = f'What is your name?'
            optiontitle = 'LOAD GAME'
            options = '...........................................................................\n' \
                     '..............................TYPE YOUR NAME...............................\n' \
                     '...........................................................................\n' \
                     '...........................................................................'

            screen.screen(screename, text, optiontitle, options)
            while screen.entrada is '':
                optiontitle = 'INVALID NAME!'
                screen.screen(screename, text, optiontitle, options)
            if os.path.exists(screen.entrada.lower() + '.p'):
                loaded=True
                savefile=f'{screen.entrada.lower()}.p'
            else:
                titlescreen()
        else:
            titlescreen()
    elif screen.entrada is '2':
        setting()
    elif screen.entrada is '3':
        screename ='HELP'
        text= 'STEORA RPG its a text based game with the goal of space exploration,' \
               ' the options of action will appear bellow the main text.'
        optiontitle=''
        options = '...........................................................................\n' \
                 '.............................ENTER TO GO BACK..............................\n' \
                 '...........................................................................\n' \
                 '...........................................................................'
        screen.screen(screename, text, optiontitle, options)
        titlescreen()
    elif screen.entrada is '4':
        screename ='ABOUT'
        text= 'This is a working in progress project.'
        optiontitle=''
        options = '...........................................................................\n' \
                 '.............................ENTER TO GO BACK;.............................\n' \
                 '...........................................................................\n' \
                 '...........................................................................'
        screen.screen(screename, text, optiontitle, options)
        titlescreen()
    elif screen.entrada is '5':
        sys.exit()
    elif screen.entrada is '9':
        return
    else:
        titlescreen()