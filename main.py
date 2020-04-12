import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys
import title
import screen
import math
import data.local as local
import data.skills as skills
import data.enemies as enemies
from pygame import mixer
import random
import json
import pickle


class playerclass:
    def __init__(self):
        self.name = ''
        self.race=''
        self.system= ''
        self.planet= ''
        self.city = ''
        self.local = ''
        self.spaceship = False
        self.spaceshipmodel = 'None'

        self.quests={}     # id: {'questname':'','questdescription':'','questprogress':'0/5'}
        self.questsdone={}

        self.newmessage = False
        self.messages = {}     # id: {'from':'', 'message':''}
        self.readmessages = {}

        self.exp = 0
        self.lvl = (math.floor((math.sqrt(40000+800*self.exp)-200)/400)+1)

        self.atribpointstotal=5*self.lvl - 5
        self.atribpointsspent=0
        self.atribpoints=self.atribpointstotal-self.atribpointsspent

        self.skills={'PILOT':4,'FIRST AID':2,'MEDITATE':1}                 #skillname: lvl

        self.dexb = 1
        self.agib = 1
        self.intb = 1
        self.lukb = 1

        self.dexmod=0
        self.agimod=0
        self.intmod=0
        self.lukmod=0

        self.dex = self.dexb + self.dexmod
        self.agi = self.agib + self.agimod
        self.int = self.intb + self.intmod
        self.luk = self.lukb + self.lukmod

        self.firepowermod=0
        self.firepower = 1 + self.firepowermod

        self.resistancemod=0
        self.res = 1 + self.resistancemod

        self.fleemod=0
        self.flee=self.agi+self.fleemod

        self.cri=(self.dex+self.luk)/100

        self.HP=100
        self.HPnb=math.ceil(self.HP*0.15)
        self.SP=100
        self.SPnb = math.ceil(self.SP * 0.15)
        self.HPb = f'='*self.HPnb     #fazer as bars atualizarem
        self.SPb=f'='*self.SPnb

        self.money=0

        self.eqp1='None'        #helmet
        self.eqp2='None'        #chest
        self.eqp3='None'        #gloves
        self.eqp4='None'        #pants
        self.eqp5='None'        #boots
        self.eqp6='None'        #accessory1
        self.eqp7='None'        #accessory2

        self.weapon='None'       
        self.shield='None'

        self.items={'Arrow':4,'Broken shield':1,'Trap':2,'Plasma grenade':5}           #item:quantidade

        self.karma=0

    def update(self):
        if self.HP > 100:
            self.HP=100
        if self.SP > 100:
            self.SP=100
        self.lvl = (math.floor((math.sqrt(40000+800*self.exp)-200)/400)+1)
        self.HPnb=math.ceil(self.HP*0.15)
        self.HPb = f'=' * self.HPnb
        self.SPnb = math.ceil(self.SP * 0.15)
        self.SPb=f'='*self.SPnb
        self.dex = self.dexb + self.dexmod
        self.agi = self.agib + self.agimod
        self.int = self.intb + self.intmod
        self.luk = self.lukb + self.lukmod
        self.firepower = 1 + self.firepowermod
        self.res = 1 + self.resistancemod
        self.flee=self.agi+self.fleemod
        self.cri=(self.dex+self.luk)/100
        self.atribpointstotal=5*self.lvl - 5
        self.atribpoints=self.atribpointstotal-self.atribpointsspent
        if len(self.messages)>0:
            self.newmessage = True
player=playerclass()

class enemyclass:
    def __init__(self,nome,lvl,HPfull,HP,dex,agi,int,luk,firepower,resistance):
        self.name=nome
        self.level=lvl
        self.HPfull=HPfull
        self.HP=HP
        self.dex=dex
        self.agi=agi
        self.int=int
        self.luk=luk
        self.firepower=firepower
        self.res=resistance
        self.flee=self.agi
        self.cri=(self.dex+self.luk)/100
        self.HPnb=math.ceil(self.HP*0.15)
        self.HPb = f'=' * self.HPnb

    def update(self):
        self.HPnb=math.ceil(self.HP*0.15)
        self.HPb = f'=' * self.HPnb

    def restore(self):
        self.HP = self.HPfull

for e in range(0,len(list(enemies.enemies.keys()))):
    globals()[str(list(enemies.enemies.keys())[e])]=enemyclass(enemies.enemies[list(enemies.enemies.keys())[e]]['name'],enemies.enemies[list(enemies.enemies.keys())[e]]['lvl'],enemies.enemies[list(enemies.enemies.keys())[e]]['HPfull'],enemies.enemies[list(enemies.enemies.keys())[e]]['HP'],enemies.enemies[list(enemies.enemies.keys())[e]]['dex'],enemies.enemies[list(enemies.enemies.keys())[e]]['agi'],enemies.enemies[list(enemies.enemies.keys())[e]]['int'],enemies.enemies[list(enemies.enemies.keys())[e]]['luk'],enemies.enemies[list(enemies.enemies.keys())[e]]['firepower'],enemies.enemies[list(enemies.enemies.keys())[e]]['resistance'])

messagecombat = ''

def tutorial():
    screename = f'STEORA'

    text = f'Welcome to the world of Steora, {player.name}! This is a quick tutorial to show the mechanism of the game! As you may had realized, everything is text based, where you type the selected option. The option will always me shown in the box below.'

    optiontitle = ''
    options = '...........................................................................\n' \
              '.............................ENTER TO CONTINUE.............................\n' \
              '...........................................................................\n' \
              '...........................................................................'
    screen.screen(screename, text, optiontitle, options)

    bar = f'''⠀⠀⠀LVL {player.lvl}⠀⠀⠀ ⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀       {player.system}
⠀⠀⠀HP:{screen.color.lightred}{player.HPb}{screen.color.end}       {' ' * (15 - player.HPnb)}                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        {player.planet}
⠀⠀⠀SP:{screen.color.lightyellow}{player.SPb}{screen.color.end}        {' ' * (15 - player.SPnb)}                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        {player.city}
    '''
    text = f'Above will be indicating some informations, as your level, your life points (HP) and your stamina points (SP). On the right will be showing your location, first the system you are, then the planet or satellite and lastly your location on a given planet/satellite.'

    screen.screengame(bar, screename, text, optiontitle, options)

#    text = f'Agora vou apresentar o menu de quando se está no modo terrestre! Começando pelo final, as informações da sua nave! Digite a opção!'
#
#    options = '...........................................................................\n' \
#             '.......................................................6)NAVE..............\n' \
#             '...........................................................................\n' \
#             '...........................................................................'
#    screen.screengame(bar, screename, text, optiontitle, options)
#
#    while screen.inpt is not '6':
#        screen.screengame(bar, screename, text, optiontitle, options)
#
#    text = f'Infelizmente você não possui nenhuma nave no momento... Mas aqui será o lugar para visualizar informações como nível de energia, estado de avaria, tripulação, carregamento, etc.'
#
#    optiontitle='NAVE'
#
#    options = '...........................................................................\n' \
#             '............................ENTER PARA VOLTAR..............................\n' \
#             '...........................................................................\n' \
#             '...........................................................................'
#    screen.screen(screename, text, optiontitle, options)
#
    text = f'Now check your messages!'

    optiontitle=''

    options = f'...........................................................................\n' \
             f'..............................5)MENSAGENS..................................\n' \
             f'...........................................................................\n' \
             f'...........................................................................'
    screen.screengame(bar, screename, text, optiontitle, options)

    while screen.inpt is not '5':
        screen.screengame(bar, screename, text, optiontitle, options)

    text = f"The messages will show up as you progress in the game, they will indicate the possibility of accept a quest somewhere in the galaxy... Don't worry on keep looking everytime, you'll know there is a new message when the option starts blink like this: {screen.color.blink}5)MENSAGENS{screen.color.end}"

    optiontitle='MENSAGENS'

    options = '...........................................................................\n' \
             '............................ENTER TO GO BACK...............................\n' \
             '...........................................................................\n' \
             '...........................................................................'
    screen.screen(screename, text, optiontitle, options)

    text = f'I guess you got it! This is the full bar in the walking mode, go to the option 3)PERSONAGEM to see a resume of your character!'

    optiontitle=''

    options = '....1)WALK....................2)BACKPACK...............3)CHARACTER.........\n' \
              f'....4)QUESTS..................{"5)MESSAGES" if player.newmessage is False else f"{screen.color.blink}5)MESSAGES{screen.color.end}"}...............{"6)SPACESHIP" if player.spaceship is True else "..........."}.........\n' \
              '...........................................................................\n' \
              '....S)SAVE....................C)SETTINGS...............X)QUIT GAME.........'
    screen.screengame(bar, screename, text, optiontitle, options)

    while screen.inpt is not '3':
        screen.screengame(bar, screename, text, optiontitle, options)

    screename = 'STEORA'

    text = f'''    LVL: {player.lvl}                                         Experência: {player.exp}

    HP: {player.HP}% 
    SP: {player.SP}%
                                               Attribute Point: {player.atribpoints}
    These are your primary attributes,        Dexterity:⠀⠀⠀⠀⠀{player.dexb}+{player.dexmod} = {player.dex}
    as you progress through the game        Agility:⠀⠀⠀⠀{player.agib}+{player.agimod} = {player.agi}
    and earn experience, you'll got some     Intelligence: {player.intb}+{player.intmod} = {player.int}
    attribute points to distribute and        Luck:    ⠀⠀⠀ {player.lukb}+{player.lukmod} = {player.luk}     
    strengthen your character! These, by 
    it's turn will be used to calculate the secondary
    attributes and your capacity to realize certain actions.'''

    optiontitle = f'{player.name}'
    options = '...........................................................................\n' \
             '............................ENTER TO CONTINUE..............................\n' \
             '...........................................................................\n' \
             '...........................................................................'
    screen.screenfree(screename, text, optiontitle, options)

    text = f'''    LVL: {player.lvl}                                         Experência: {player.exp}
    
    HP: {player.HP}% 
    SP: {player.SP}%
                                               Attribute Points: {player.atribpoints}
    Fire Power: {player.firepower}                           Dexterity:⠀⠀⠀⠀⠀{player.dexb}+{player.dexmod} = {player.dex}
    Resistance: {player.res}                             Agility:⠀⠀⠀⠀{player.agib}+{player.agimod} = {player.agi}
    Flee: {player.flee}                                 Intelligence: {player.intb}+{player.intmod} = {player.int}
    Critical Rate: {player.cri}                      Luck:    ⠀⠀⠀ {player.lukb}+{player.lukmod} = {player.luk}     
    
    These are your secondary attributes, calculated from your      
    primary attributes and items or equipments you're using.     
    They basically determine your perfomance in the combat.          '''

    screen.screenfree(screename, text, optiontitle, options)

    text = f'''    LVL: {player.lvl}                                         Experência: {player.exp}

    HP: {player.HP}% 
    SP: {player.SP}%
                                               Attribute Points: {player.atribpoints}
    Fire Power: {player.firepower}                           Dexterity:⠀⠀⠀⠀⠀{player.dexb}+{player.dexmod} = {player.dex}
    Resistance: {player.res}                             Agility:⠀⠀⠀⠀{player.agib}+{player.agimod} = {player.agi}
    Flee: {player.flee}                                 Intelligence: {player.intb}+{player.intmod} = {player.int}
    Critical Rate: {player.cri}                      Luck:    ⠀⠀⠀ {player.lukb}+{player.lukmod} = {player.luk}     

    Lastly, your skills, you can access them through here to know more later!

                                Skills:                               
    {", ".join(list(player.skills.keys()))}'''

    screen.screenfree(screename, text, optiontitle, options)

    player.newmessage = True

    text = f'Looks like you got a message!'

    optiontitle=''

    options = '....1)WALK....................2)BACKPACK...............3)CHARACTER.........\n' \
              f'....4)QUESTS..................{"5)MESSAGES" if player.newmessage is False else f"{screen.color.blink}5)MESSAGES{screen.color.end}"}...............{"6)SPACESHIP" if player.spaceship is True else "..........."}.........\n' \
              '...........................................................................\n' \
              '....S)SAVE....................C)SETTINGS...............X)QUIT GAME.........'
    screen.screengame(bar, screename, text, optiontitle, options)

    while screen.inpt is not '5':
        screen.screengame(bar, screename, text, optiontitle, options)

    player.newmessage = False

    text = f"Attention youngs of {player.city}! The Emissary of the League of Steora will be realizing the selection process for those who has interest in joining the Academy of Flight in the Karsov's Base!"

    optiontitle='MENSAGENS'

    options = '...........................................................................\n' \
              '...........................................................................\n' \
              '..............................ENTER TO GO BACK.............................\n' \
              '...........................................................................'
    screen.screen(screename, text, optiontitle, options)

    text = f"Wow!! That is an opportunity that you can't let it pass! This process are rare! Select 1)WALK to go to the Emissary!"

    optiontitle=''

    options = '....1)WALK....................2)BACKPACK...............3)CHARACTER.........\n' \
              f'....4)QUESTS..................{"5)MESSAGES" if player.newmessage is False else f"{screen.color.blink}5)MESSAGES{screen.color.end}"}...............{"6)SPACESHIP" if player.spaceship is True else "..........."}.........\n' \
              '...........................................................................\n' \
              '....S)SAVE....................C)SETTINGS...............X)QUIT GAME.........'
    screen.screengame(bar, screename, text, optiontitle, options)

    while screen.inpt is not '1':
        screen.screengame(bar, screename, text, optiontitle, options)

    text = local.local[player.system][player.planet][player.city]["map"]

    optiontitle=f'{player.city}'

    options = '....1)WALK....................2)BACKPACK...............3)CHARACTER.........\n' \
              f'....4)QUESTS..................{"5)MESSAGES" if player.newmessage is False else f"{screen.color.blink}5)MESSAGES{screen.color.end}"}...............{"6)SPACESHIP" if player.spaceship is True else "..........."}.........\n' \
              '...........................................................................\n' \
              '....S)SAVE....................C)SETTINGS...............X)QUIT GAME.........'
    screen.screenwalk(screename, text, optiontitle, options)
    game_loop()

def game_loop():
    while True is True:

        def character():

            def seeskils():

                def useskils():
                    optiontitle = 'USE SKILL'
                    options = '...........................................................................\n' \
                             '...........................TYPE THE SKILL TO USE...........................\n' \
                             '.............................(ENTER TO GO BACK)............................\n' \
                             '...........................................................................'
                    screen.screenfree(screename, text, optiontitle, options)
                    if screen.inpt is '':
                        seeskils()
                    elif screen.inpt.upper() in list(player.skills.keys()):
                        if habilidades.skills[screen.inpt.upper()]['active'] is True:
                            if player.SP >= habilidades.skills[screen.inpt.upper()]['skillcost'][player.skills[screen.inpt.upper()]]:
                                exec(habilidades.skills[screen.inpt.upper()]['skilluse'][player.skills[screen.inpt.upper()]])
                                player.update()
                                seeskils()
                            else:
                                options = '...........................................................................\n' \
                                         '..................................LOW SP...................................\n' \
                                         '.............................(ENTER TO GO BACK)............................\n' \
                                         '...........................................................................'
                                screen.screenfree(screename, text, optiontitle, options)
                                useskils()
                        else:
                            options = '...........................................................................\n' \
                                     ".....................THIS SKILL CAN'T BE USED THIS WAY.....................\n" \
                                     '.............................(ENTER TO GO BACK)............................\n' \
                                     '...........................................................................'
                            screen.screenfree(screename, text, optiontitle, options)
                            useskils()
                    else:
                        useskils()


                text = f'''
    {list(player.skills.keys())[0] + " LVL " + str(list(player.skills.values())[0]) if len(player.skills) >= 1 else ""}
    {skills.skills[list(player.skills.keys())[0]]['skilldescription'][list(player.skills.values())[0]] if len(player.skills) >= 1 else ""}

    {list(player.skills.keys())[1] + " LVL " + str(list(player.skills.values())[1]) if len(player.skills) >= 2 else ""}
    {skills.skills[list(player.skills.keys())[1]]['skilldescription'][list(player.skills.values())[1]] if len(player.skills) >= 2 else ""}
    
    {list(player.skills.keys())[2] + " LVL " + str(list(player.skills.values())[2]) if len(player.skills) >= 3 else ""}
    {skills.skills[list(player.skills.keys())[2]]['skilldescription'][list(player.skills.values())[2]] if len(player.skills) >= 3 else ""}
    {list(player.skills.keys())[3] + " LVL " + str(list(player.skills.values())[3]) if len(player.skills) >= 4 else ""}
    {list(player.skills.keys())[4] + " LVL " + str(list(player.skills.values())[4]) if len(player.skills) >= 5 else ""} 
    {list(player.skills.keys())[5] + " LVL " + str(list(player.skills.values())[5]) if len(player.skills) >= 6 else ""}  
    {list(player.skills.keys())[6] + " LVL " + str(list(player.skills.values())[6]) if len(player.skills) >= 7 else ""}  '''

                optiontitle = f'SKILS'
                options = '.....1)USE................................................................\n' \
                         '...........................................................................\n' \
                         '...........................................................................\n' \
                         '.......................................................0)BACK..............'
                screen.screenfree(screename, text, optiontitle, options)
                if screen.inpt is '1':
                    useskils()
                elif screen.inpt is '0':
                    character()
                else:
                    seeskils()

            def distributeattr():
                screename = 'STEORA'

                text = f'''                           Attribute Points: {player.atribpoints}                     
    Fire Power: {player.firepower}         {" "*(3-len(str(player.firepower)))}                    Dexterity: ⠀⠀⠀{player.dexb}+{player.dexmod} = {player.dex}
    Resistance: {player.res}               {" "*(3-len(str(player.res)))}              Agility:⠀⠀⠀ ⠀ {player.agib}+{player.agimod} = {player.agi}
    Flee: {player.flee}                    {" "*(3-len(str(player.flee)))}               Intelligence: {player.intb}+{player.intmod} = {player.int}
    Critical Rate: {player.cri}            {" "*(6-len(str(player.cri)))}           Luck:    ⠀⠀⠀  {player.lukb}+{player.lukmod} = {player.luk}     


                           Cost per Attribute:                          
                            Dexterity:     {math.floor((math.sqrt(1+4*player.dexb)-1)/2)+1}                           
                            Agility:       {math.floor((math.sqrt(1+4*player.agib)-1)/2)+1}                           
                            Intelligence:  {math.floor((math.sqrt(1+4*player.intb)-1)/2)+1}                           
                            Luck:          {math.floor((math.sqrt(1+4*player.lukb)-1)/2)+1}                           
    '''

                optiontitle = 'ATTRIBUTES'
                options = '............1)DEXTERITY......................2)AGILITY.....................\n' \
                         '............3)INTELLIGENCE...................4)LUCK........................\n' \
                         '...........................................................................\n' \
                         '.......................................................0)BACK..............'
                screen.screenfree(screename, text, optiontitle, options)

                if screen.inpt is '1':
                    if player.atribpoints >= (math.floor((math.sqrt(1+4*player.dexb)-1)/2)+1):
                        player.atribpointsspent += (math.floor((math.sqrt(1+4*player.dexb)-1)/2)+1)
                        player.dexb += 1
                        player.update()
                        distributeattr()
                    elif player.atribpoints < (math.floor((math.sqrt(1+4*player.dexb)-1)/2)+1):
                        distributeattr()
                elif screen.inpt is '2':
                    if player.atribpoints >= (math.floor((math.sqrt(1+4*player.agib)-1)/2)+1):
                        player.atribpointsspent += (math.floor((math.sqrt(1+4*player.agib)-1)/2)+1)
                        player.agib += 1
                        player.update()
                        distributeattr()
                    elif player.atribpoints < (math.floor((math.sqrt(1+4*player.agib)-1)/2)+1):
                        distributeattr()
                elif screen.inpt is '3':
                    if player.atribpoints >= (math.floor((math.sqrt(1+4*player.intb)-1)/2)+1):
                        player.atribpointsspent += (math.floor((math.sqrt(1+4*player.intb)-1)/2)+1)
                        player.intb += 1
                        player.update()
                        distributeattr()
                    elif player.atribpoints < (math.floor((math.sqrt(1+4*player.intb)-1)/2)+1):
                        distributeattr()
                elif screen.inpt is '4':
                    if player.atribpoints >= (math.floor((math.sqrt(1+4*player.lukb)-1)/2)+1):
                        player.atribpointsspent += (math.floor((math.sqrt(1+4*player.lukb)-1)/2)+1)
                        player.lukb += 1
                        player.update()
                        distributeattr()
                    elif player.atribpoints < (math.floor((math.sqrt(1+4*player.lukb)-1)/2)+1):
                        distributeattr()
                elif screen.inpt is '0':
                    character()
                else:
                    distributeattr()

            screename = 'STEORA'

            text = f'''    LVL: {player.lvl}                                         Experience: {player.exp}

    HP: {player.HP}  
    SP: {player.SP} 
                                               Attribute Points: {player.atribpoints}
    Fire Power: {player.firepower}       {" "*(3-len(str(player.firepower)))}                   Dexterity:⠀⠀⠀⠀⠀{player.dexb}+{player.dexmod} = {player.dex}
    Resistance: {player.res}             {" "*(3-len(str(player.res)))}             Agility:⠀⠀⠀   ⠀{player.agib}+{player.agimod} = {player.agi}
    Flee: {player.flee}                  {" "*(3-len(str(player.flee)))}              Intelligence:  {player.intb}+{player.intmod} = {player.int}
    Critical Rate: {player.cri}          {" "*(6-len(str(player.cri)))}          Luck:    ⠀⠀⠀   {player.lukb}+{player.lukmod} = {player.luk}     

                                Skills:                               

    {", ".join(list(player.skills.keys()))}'''

            optiontitle = f'{player.name.upper()}'
            options = '....1)SKILLS..............................2)DISTRIBUTE ATTRIBUTE POINTS....\n' \
                      '...........................................................................\n' \
                      '...........................................................................\n' \
                      '.......................................................0)BACK..............'
            screen.screenfree(screename, text, optiontitle, options)

            if screen.inpt is '1':
                seeskils()
            elif screen.inpt is '2':
                distributeattr()
            elif screen.inpt is '0':
                return
            else:
                character()

        def walk():

            def place():
                print('WIP')
                game()

            screename = f'STEORA'

            text = local.local[player.system][player.planet][player.city]['map']

            optiontitle = f'{player.city}'
            options = local.local[player.system][player.planet][player.city]['options']
            screen.screenfree(screename, text, optiontitle, options)
            while screen.inpt not in local.local[player.system][player.planet][player.city]["available"]:
                screen.screenfree(screename, text, optiontitle, options)
            if screen.inpt is "0":
                game()
            else:
                player.local = local.local[player.system][player.planet][player.city]["places"][int(screen.inpt)-1]
                place()

        def backpack():

            def itemdetail():
                optiontitle = f'ITEM DETAIL'
                options = '...........................................................................\n' \
                         '.........................TYPE THE NAME OF THE ITEM.........................\n' \
                         '.............................(ENTER TO GO BACK)............................\n' \
                         '...........................................................................'
                screen.screenfree(screename, text, optiontitle, options)
                if screen.inpt.lower().capitalize() in (list(player.items.keys()) or player.eqp1 or player.eqp2 or player.eqp3 or player.eqp4 or player.eqp5 or player.eqp6 or player.weapon or player.shield):
                    print('Em costrução')
                elif screen.inpt is '':
                    backpack()
                else:
                    itemdetail()

            def itemuse():
                optiontitle = f'USE ITEM'
                options = '...........................................................................\n' \
                         '.........................TYPE THE NAME OF THE ITEM.........................\n' \
                         '.............................(ENTER TO GO BACK)............................\n' \
                         '...........................................................................'
                screen.screenfree(screename, text, optiontitle, options)
                if screen.inpt.lower().capitalize() in (list(player.items.keys()) or player.eqp1 or player.eqp2 or player.eqp3 or player.eqp4 or player.eqp5 or player.eqp6 or player.weapon or player.shield):
                    print('Em costrução')
                elif screen.inpt is '':
                    backpack()
                else:
                    itemuse()

            def itemequip():
                optiontitle = f'EQUIP ITEM'
                options = '...........................................................................\n' \
                         '.........................TYPE THE NAME OF THE ITEM.........................\n' \
                         '.............................(ENTER TO GO BACK)............................\n' \
                         '...........................................................................'
                screen.screenfree(screename, text, optiontitle, options)
                if screen.inpt.lower().capitalize() in list(player.items.keys()):
                    print('Em costrução')
                elif screen.inpt is '':
                    backpack()
                else:
                    itemequip()

            def itemthrow():

                def itemthrowqt():
                    options = '...........................................................................\n' \
                             '..................TYPE THE QUANTITY THAT YOU WANT TO THROW.................\n' \
                             '.............................(ENTER TO GO BACK)............................\n' \
                             '...........................................................................'
                    screen.screenfree(screename, text, optiontitle, options)
                    if screen.inpt is '':
                        itemthrow()
                    else:
                        try:
                            qtd = abs(int(screen.inpt))
                            player.items[item] -= qtd
                            if player.items[item] <= 0:
                                del player.items[item]
                                backpack()
                            else:
                                backpack()
                        except ValueError:
                            itemthrowqt()

                optiontitle = f'THROW AWAY ITEM'
                options = '...........................................................................\n' \
                         '.........................TYPE THE NAME OF THE ITEM.........................\n' \
                         '.............................(ENTER TO GO BACK)............................\n' \
                         '...........................................................................'
                screen.screenfree(screename, text, optiontitle, options)
                item = screen.inpt.lower().capitalize()
                if item in list(player.items.keys()):
                    if player.items[item] is 1:
                        del player.items[item]
                        backpack()
                    else:
                        itemthrowqt()
                elif screen.inpt is '':
                    backpack()
                else:
                    itemthrow()

            screename = 'STEORA'

            text = f'''    Equipments:               Money: {player.money} {screen.color.stroke}Q{screen.color.end}⠀⠀⠀⠀⠀⠀⠀⠀⠀ Items: {len(player.items)}/18
    {player.eqp1}, {player.eqp2}, {player.eqp3}    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {player.eqp4}, {player.eqp5}, {player.eqp6}                Weapon: {player.weapon}       Shield: {player.shield}

            {list(player.items.keys())[0]+": "+ str(list(player.items.values())[0]) if len(player.items)>=1 else ""}{" "*(30-len(str(list(player.items.keys())[0]+": "+ str(list(player.items.values())[0])))) if len(player.items)>=1 else " "}{list(player.items.keys())[1]+": "+ str(list(player.items.values())[1]) if len(player.items)>=2 else ""}
            {list(player.items.keys())[2]+": "+ str(list(player.items.values())[2]) if len(player.items)>=3 else ""}{" "*(30-len(str(list(player.items.keys())[2]+": "+ str(list(player.items.values())[2])))) if len(player.items)>=3 else " "}{list(player.items.keys())[3]+": "+ str(list(player.items.values())[3]) if len(player.items)>=4 else ""}
            {list(player.items.keys())[4]+": "+ str(list(player.items.values())[4]) if len(player.items)>=5 else ""}{" "*(30-len(str(list(player.items.keys())[4]+": "+ str(list(player.items.values())[4])))) if len(player.items)>=5 else " "}{list(player.items.keys())[5]+": "+ str(list(player.items.values())[5]) if len(player.items)>=6 else ""}
            {list(player.items.keys())[6]+": "+ str(list(player.items.values())[6]) if len(player.items)>=7 else ""}{" "*(30-len(str(list(player.items.keys())[6]+": "+ str(list(player.items.values())[6])))) if len(player.items)>=7 else ""}{list(player.items.keys())[7]+": "+ str(list(player.items.values())[7]) if len(player.items)>=8 else ""}
            {list(player.items.keys())[8]+": "+ str(list(player.items.values())[8]) if len(player.items)>=9 else ""}{" "*(30-len(str(list(player.items.keys())[8]+": "+ str(list(player.items.values())[8])))) if len(player.items)>=9 else ""}{list(player.items.keys())[9]+": "+ str(list(player.items.values())[9]) if len(player.items)>=10 else ""} 
            {list(player.items.keys())[10]+": "+ str(list(player.items.values())[10]) if len(player.items)>=11 else ""}{" "*(30-len(str(list(player.items.keys())[10]+": "+ str(list(player.items.values())[10])))) if len(player.items)>=11 else ""}{list(player.items.keys())[11]+": "+ str(list(player.items.values())[11]) if len(player.items)>=12 else ""}  
            {list(player.items.keys())[12]+": "+ str(list(player.items.values())[12]) if len(player.items)>=13 else ""}{" "*(30-len(str(list(player.items.keys())[12]+": "+ str(list(player.items.values())[12])))) if len(player.items)>=13 else ""}{list(player.items.keys())[13]+": "+ str(list(player.items.values())[13]) if len(player.items)>=14 else ""}  
            {list(player.items.keys())[14]+": "+ str(list(player.items.values())[14]) if len(player.items)>=15 else ""}{" "*(30-len(str(list(player.items.keys())[14]+": "+ str(list(player.items.values())[14])))) if len(player.items)>=15 else ""}{list(player.items.keys())[15]+": "+ str(list(player.items.values())[15]) if len(player.items)>=16 else ""}  
            {list(player.items.keys())[16]+": "+ str(list(player.items.values())[16]) if len(player.items)>=17 else ""}{" "*(30-len(str(list(player.items.keys())[16]+": "+ str(list(player.items.values())[16])))) if len(player.items)>=17 else ""}{list(player.items.keys())[17]+": "+ str(list(player.items.values())[17]) if len(player.items)>=18 else ""}'''

            optiontitle = f'BACKPACK'
            options = '..............1)DETAILS.............................2)EQUIP...............\n' \
                     '...............3)USE.................................4)THROW AWAY..........\n' \
                     '...........................................................................\n' \
                     '.......................................................0)BACK..............'
            screen.screenfree(screename, text, optiontitle, options)

            if screen.inpt is '1':
                itemdetail()

            elif screen.inpt is '2':
                itemequip()

            elif screen.inpt is '3':
                itemuse()

            elif screen.inpt is '4':
                itemthrow()

            elif screen.inpt is '0':
                game()
            else:
                backpack()

        def messages():

            def readnewmessage(text):
                optiontitle = 'READ NEW MESSAGES'
                options = '...........................................................................\n' \
                         '.......................TYPE THE NUMBER OF THE MESSAGE......................\n' \
                         '.............................(ENTER TO GO BACK)............................\n' \
                         '...........................................................................'
                screen.screenfree(screename, text, optiontitle, options)
                if screen.inpt is '':
                    messages()
                else:
                    try:
                        id = abs(int(screen.inpt))
                        if id in list(player.messages.keys()):
                            text = f'''Mensagem de {player.messages[id]['de']}: {player.messages[id]['msg']}'''
                            options = '...........................................................................\n' \
                                     '...........................................................................\n' \
                                     '.............................ENTER PARA VOLTAR.............................\n' \
                                     '...........................................................................'
                            screen.screen(screename, text, optiontitle, options)
                            if id != len(player.messages):
                                player.readmessages[len(player.readmessages)+1]=player.messages.pop(id)
                                if len(player.readmessages) > 10:
                                    for j in range(1, 11):
                                        player.readmessages[j] = player.readmessages.pop(j+1)
                                for i in range(id,len(player.messages)+1):
                                    print(i)

                                    player.messages[i]=player.messages.pop(i+1)

                                messages()
                            else:
                                player.readmessages[len(player.readmessages)+1]=player.messages.pop(id)
                                if len(player.readmessages) > 10:
                                    for j in range(1, 11):
                                        player.readmessages[j] = player.readmessages.pop(j+1)
                                if len(player.messages)==0:
                                    player.newmessage=False
                                messages()
                        else:
                            readnewmessage(text)
                    except ValueError:
                        readnewmessage(text)

            def readoldmessage():
                text = f'''                       Your old messages are:                       

                                {str(list(player.readmessages.keys())[9]) + ") from " + player.readmessages[10]['de'] if len(player.readmessages) == 10 else ""}
                                {str(list(player.readmessages.keys())[8]) + ") from " + player.readmessages[9]['de'] if len(player.readmessages) >= 9 else ""}
                                {str(list(player.readmessages.keys())[7]) + ") from " + player.readmessages[8]['de'] if len(player.readmessages) >= 8 else ""}
                                {str(list(player.readmessages.keys())[6]) + ") from " + player.readmessages[7]['de'] if len(player.readmessages) >= 7 else ""}
                                {str(list(player.readmessages.keys())[5]) + ") from " + player.readmessages[6]['de'] if len(player.readmessages) >= 6 else ""}
                                {str(list(player.readmessages.keys())[4]) + ") from " + player.readmessages[5]['de'] if len(player.readmessages) >= 5 else ""}
                                {str(list(player.readmessages.keys())[3]) + ") from " + player.readmessages[4]['de'] if len(player.readmessages) >= 4 else ""}
                                {str(list(player.readmessages.keys())[2]) + ") from " + player.readmessages[3]['de'] if len(player.readmessages) >= 3 else ""}
                                {str(list(player.readmessages.keys())[1]) + ") from " + player.readmessages[2]['de'] if len(player.readmessages) >= 2 else ""}
                                {str(list(player.readmessages.keys())[0]) + ") from " + player.readmessages[1]['de'] if len(player.readmessages) >= 1 else ""}
'''
                optiontitle = 'OLD MESSAGES'
                options = '...........................................................................\n' \
                         '.......................TYPE THE NUMBER OF THE MESSAGE......................\n' \
                         '.............................(ENTER TO GO BACK)............................\n' \
                         '...........................................................................'
                screen.screenfree(screename, text, optiontitle, options)
                if screen.inpt is '':
                    messages()
                else:
                    try:
                        id = abs(int(screen.inpt))
                        if id in list(player.readmessages.keys()):
                            text = f'''Message from {player.readmessages[id]['from']}: {player.readmessages[id]['message']}'''
                            options = '...........................................................................\n' \
                                     '...........................................................................\n' \
                                     '..............................ENTER TO GO BACK.............................\n' \
                                     '...........................................................................'
                            screen.screen(screename, text, optiontitle, options)
                            readoldmessage()
                        else:
                            readoldmessage()
                    except ValueError:
                        readoldmessage()


            screename = 'STEORA'

            text = f'''                       Your new messages are:                       

                                {str(list(player.messages.keys())[0])+") from "+ player.messages[1]['from'] if len(player.messages)>=1 else "Não há novas mensagens!"}
                                {str(list(player.messages.keys())[1])+") from "+ player.messages[2]['from'] if len(player.messages)>=2 else ""}
                                {str(list(player.messages.keys())[2])+") from "+ player.messages[3]['from'] if len(player.messages)>=3 else ""}
                                {str(list(player.messages.keys())[3])+") from "+ player.messages[4]['from'] if len(player.messages)>=4 else ""}
                                {str(list(player.messages.keys())[4])+") from "+ player.messages[5]['from'] if len(player.messages)>=5 else ""}
                                {str(list(player.messages.keys())[5])+") from "+ player.messages[6]['from'] if len(player.messages)>=6 else ""}
                                {str(list(player.messages.keys())[6])+") from "+ player.messages[7]['from'] if len(player.messages)>=7 else ""}
                                {str(list(player.messages.keys())[7])+") from "+ player.messages[8]['from'] if len(player.messages)>=8 else ""}
                                {str(list(player.messages.keys())[8])+") from "+ player.messages[9]['from'] if len(player.messages)>=9 else ""}
                                {str(list(player.messages.keys())[9])+") from "+ player.messages[10]['from'] if len(player.messages)>=10 else ""}
'''

            optiontitle = 'MESSAGES'

            options = '.......1)READ NEW MESSAGE...................2)READ OLD MESSAGES...........\n' \
                     '...........................................................................\n' \
                     '...........................................................................\n' \
                     '.......................................................0)BACK..............'
            screen.screenfree(screename, text, optiontitle, options)

            if screen.inpt is '1':
                if len(player.messages) is 0:
                    text = f'There are no new message!'
                    options = '...........................................................................\n' \
                             '...........................................................................\n' \
                             '..............................ENTER TO GO BACK.............................\n' \
                             '...........................................................................'
                    screen.screen(screename, text, optiontitle, options)
                    messages()
                else:
                    readnewmessage(text)
            elif screen.inpt is '2':
                readoldmessage()
            elif screen.inpt is '0':
                game()
            else:
                messages()

        def quests():

            def questdetail(text):
                optiontitle = 'QUEST DETAIL'
                options = '...........................................................................\n' \
                         '........................TYPE THE NUMBER OF THE QUEST.......................\n' \
                         '.............................(ENTER TO GO BACK)............................\n' \
                         '...........................................................................'
                screen.screenfree(screename, text, optiontitle, options)
                if screen.inpt is '':
                    quests()
                else:
                    try:
                        id = abs(int(screen.inpt))
                        if id in list(player.quests.keys()):
                            text = f'''Quest {player.quests[id]['questname']}! Progress: {player.quests[id]['questprogress']}. {player.quests[id]['questdescription']}'''
                            options = '...........................................................................\n' \
                                     '...........................................................................\n' \
                                     '..............................ENTER TO GO BACK.............................\n' \
                                     '...........................................................................'
                            screen.screen(screename, text, optiontitle, options)
                            quests()
                        else:
                            questdetail(text)
                    except ValueError:
                        questdetail(text)

            def questsfinished():
                text = f'''                       Your finished quests are:                          

            {str(list(player.questsdone.keys())[0]) + ") " + player.questsdone[1]['questname'] + " " + player.questsdone[1]['questprogress'] if len(player.questsdone) >= 1 else "There are no finished quests yet!"}
            {str(list(player.questsdone.keys())[1]) + ") " + player.questsdone[2]['questname'] + " " + player.questsdone[1]['questprogress'] if len(player.questsdone) >= 2 else ""}
            {str(list(player.questsdone.keys())[2]) + ") " + player.questsdone[3]['questname'] + " " + player.questsdone[1]['questprogress'] if len(player.questsdone) >= 3 else ""}
            {str(list(player.questsdone.keys())[3]) + ") " + player.questsdone[4]['questname'] + " " + player.questsdone[1]['questprogress'] if len(player.questsdone) >= 4 else ""}
            {str(list(player.questsdone.keys())[4]) + ") " + player.questsdone[5]['questname'] + " " + player.questsdone[1]['questprogress'] if len(player.questsdone) >= 5 else ""}
            {str(list(player.questsdone.keys())[5]) + ") " + player.questsdone[6]['questname'] + " " + player.questsdone[1]['questprogress'] if len(player.questsdone) >= 6 else ""}
            {str(list(player.questsdone.keys())[6]) + ") " + player.questsdone[7]['questname'] + " " + player.questsdone[1]['questprogress'] if len(player.questsdone) >= 7 else ""}
            {str(list(player.questsdone.keys())[7]) + ") " + player.questsdone[8]['questname'] + " " + player.questsdone[1]['questprogress'] if len(player.questsdone) >= 8 else ""}
            {str(list(player.questsdone.keys())[8]) + ") " + player.questsdone[9]['questname'] + " " + player.questsdone[1]['questprogress'] if len(player.questsdone) >= 9 else ""}
            {str(list(player.questsdone.keys())[9]) + ") " + player.questsdone[10]['questname'] + " " + player.questsdone[1]['questprogress'] if len(player.questsdone) >= 10 else ""}
            '''
                optiontitle = 'FINISHED QUESTS'
                options = '...........................................................................\n' \
                         '........................TYPE THE NUMBER OF THE QUEST.......................\n' \
                         '.............................(ENTER TO GO BACK)............................\n' \
                         '...........................................................................'
                screen.screenfree(screename, text, optiontitle, options)
                if screen.inpt is '':
                    quests()
                else:
                    try:
                        id = abs(int(screen.inpt))
                        if id in list(player.questsdone.keys()):
                            text = f'''Quest {player.quests[id]['questname']}! Progress: {player.quests[id]['questprogress']}. {player.quests[id]['questdescription']}'''
                            options = '...........................................................................\n' \
                                     '...........................................................................\n' \
                                     '..............................ENTER TO GO BACK.............................\n' \
                                     '...........................................................................'
                            screen.screen(screename, text, optiontitle, options)
                            quests()
                        else:
                            questsfinished()
                    except ValueError:
                        questsfinished()

            screename = 'STEORA'

            text = f'''                       Your current quests are:               

            {str(list(player.quests.keys())[0]) + ") " + player.quests[1]['questname']+" "+player.quests[1]['questprogress'] if len(player.quests) >= 1 else "There are no accepted quests!"}
            {str(list(player.quests.keys())[1]) + ") " + player.quests[2]['questname']+" "+player.quests[1]['questprogress'] if len(player.quests) >= 2 else ""}
            {str(list(player.quests.keys())[2]) + ") " + player.quests[3]['questname']+" "+player.quests[1]['questprogress'] if len(player.quests) >= 3 else ""}
            {str(list(player.quests.keys())[3]) + ") " + player.quests[4]['questname']+" "+player.quests[1]['questprogress'] if len(player.quests) >= 4 else ""}
            {str(list(player.quests.keys())[4]) + ") " + player.quests[5]['questname']+" "+player.quests[1]['questprogress'] if len(player.quests) >= 5 else ""}
            {str(list(player.quests.keys())[5]) + ") " + player.quests[6]['questname']+" "+player.quests[1]['questprogress'] if len(player.quests) >= 6 else ""}
            {str(list(player.quests.keys())[6]) + ") " + player.quests[7]['questname']+" "+player.quests[1]['questprogress'] if len(player.quests) >= 7 else ""}
            {str(list(player.quests.keys())[7]) + ") " + player.quests[8]['questname']+" "+player.quests[1]['questprogress'] if len(player.quests) >= 8 else ""}
            {str(list(player.quests.keys())[8]) + ") " + player.quests[9]['questname']+" "+player.quests[1]['questprogress'] if len(player.quests) >= 9 else ""}
            {str(list(player.quests.keys())[9]) + ") " + player.quests[10]['questname']+" "+player.quests[1]['questprogress'] if len(player.quests) >= 10 else ""}
            '''

            optiontitle = 'QUESTS'

            options = '.......1)QUEST DETAIL........................2)SEE FINISHED QUESTS.........\n' \
                      '...........................................................................\n' \
                      '...........................................................................\n' \
                      '.......................................................0)BACK..............'
            screen.screenfree(screename, text, optiontitle, options)

            if screen.inpt is '1':
                if len(player.quests) is 0:
                    text = f'There are no accepted quests!'
                    options = '...........................................................................\n' \
                             '...........................................................................\n' \
                             '..............................ENTER TO GO BACK.............................\n' \
                             '...........................................................................'
                    screen.screen(screename, text, optiontitle, options)
                    quests()
                else:
                    questdetail(text)
            elif screen.inpt is '2':
                questsfinished()
            elif screen.inpt is '0':
                game()
            else:
                quests()

        def config():
            screename = 'STEORA'
            text = f'''



                               MUSIC: {"ON" if title.cfg.music is True else "OFF"}
                               AUTOSAVE: {"ON" if title.cfg.autosave is True else "OFF"}






            '''
            optiontitle = 'SETTINGS'
            options = '.................1)MUSIC........................2)AUTOSAVE.................\n' \
                     '...........................................................................\n' \
                     '...........................................................................\n' \
                     '...............................0)BACK......................................'
            screen.screenfree(screename, text, optiontitle, options)
            if screen.inpt is '1':
                if title.cfg.musica == True:
                    mixer.music.pause()
                    title.cfg.musica = False
                else:
                    mixer.music.play(-1)
                    title.cfg.musica = True
                with open('cfg.p', 'wb') as fp:
                    pickle.dump(title.cfg.musica, fp)
                    pickle.dump(title.cfg.autosave, fp)
                config()
            elif screen.inpt is '2':
                if title.cfg.autosave == True:
                    title.cfg.autosave = False
                else:
                    title.cfg.autosave = True
                with open('cfg.p', 'wb') as fp:
                    pickle.dump(title.cfg.musica, fp)
                    pickle.dump(title.cfg.autosave, fp)
                config()
            elif screen.inpt is '0':
                game()
            else:
                config()

        def save():
            with open(player.name.lower()+'.p', 'wb') as fp:
                pickle.dump(player.name, fp)
                pickle.dump(player.race, fp)
                pickle.dump(player.system, fp)
                pickle.dump(player.planet, fp)
                pickle.dump(player.city, fp)
                pickle.dump(player.local, fp)
                pickle.dump(player.spaceship, fp)
                pickle.dump(player.spaceshipmodel, fp)
                pickle.dump(player.quests, fp)
                pickle.dump(player.questsdone, fp)
                pickle.dump(player.newmessage, fp)
                pickle.dump(player.messages, fp)
                pickle.dump(player.readmessages, fp)
                pickle.dump(player.exp, fp)
                pickle.dump(player.atribpointsspent, fp)
                pickle.dump(player.skills, fp)
                pickle.dump(player.dexb, fp)
                pickle.dump(player.agib, fp)
                pickle.dump(player.intb, fp)
                pickle.dump(player.lukb, fp)
                pickle.dump(player.dexmod, fp)
                pickle.dump(player.agimod, fp)
                pickle.dump(player.intmod, fp)
                pickle.dump(player.lukmod, fp)
                pickle.dump(player.firepowermod, fp)
                pickle.dump(player.resistancemod, fp)
                pickle.dump(player.fleemod, fp)
                pickle.dump(player.HP, fp)
                pickle.dump(player.SP, fp)
                pickle.dump(player.money, fp)
                pickle.dump(player.eqp1, fp)
                pickle.dump(player.eqp2, fp)
                pickle.dump(player.eqp3, fp)
                pickle.dump(player.eqp4, fp)
                pickle.dump(player.eqp5, fp)
                pickle.dump(player.eqp6, fp)
                pickle.dump(player.eqp7, fp)
                pickle.dump(player.weapon, fp)
                pickle.dump(player.shield, fp)
                pickle.dump(player.items, fp)
                pickle.dump(player.karma, fp)

        def combat():
            enemy=trainingdummy

            def attack():
                global messagecombat
                if player.SP >= 5:
                    if player.dex > enemy.agi:
                        if player.cri*100 >= random.randint(0,101):
                            enemy.HP -= (player.firepower * 10 / enemy.res)
                            messagecombat=f'You took {(player.firepower * 10 / enemy.res)} from the enemy HP!'
                        else:
                            enemy.HP-=(player.firepower*2/enemy.res)
                            messagecombat=f'You took {(player.firepower * 2 / enemy.res)} from the enemy HP!'
                    else:
                        if random.randint(0,101)>=50:
                            if player.cri * 100 >= random.randint(0, 101):
                                enemy.HP -= (player.firepower * 10 / enemy.res)
                                messagecombat = f'You took {(player.firepower * 10 / enemy.res)} from the enemy HP!'
                            else:
                                enemy.HP -= (player.firepower * 2 / enemy.res)
                                messagecombat = f'You took {(player.firepower * 2 / enemy.res)} from the enemy HP!'
                        else:
                            messagecombat=f'You missed!'
                    player.SP -= 5
                    if enemy.dex > player.agi:
                        if enemy.cri*100 >= random.randint(0,100):
                            player.HP -= (enemy.firepower * 10 / player.res)
                            messagecombat+=f' And lost {enemy.firepower * 10 / player.res} HP!'
                        else:
                            player.HP -= (enemy.firepower * 2 / player.res)
                            messagecombat += f' And lost {enemy.firepower * 2 / player.res} HP!'
                    else:
                        if random.randint(0,101)>=50:
                            if enemy.cri * 100 >= random.randint(0, 100):
                                player.HP -= (enemy.firepower * 10 / player.res)
                                messagecombat += f' And lost {enemy.firepower * 10 / player.res} HP!'
                            else:
                                player.HP -= (enemy.firepower * 2 / player.res)
                                messagecombat += f' And lost {enemy.firepower * 2 / player.res} HP!'
                        else:
                            messagecombat+= f' The enemy missed!'
                    enemy.update()
                    player.update()
                    if enemy.HP <= 0:
                        enemy.restaurar()
                        player.SP = 100
                        player.update()
                        enemy.update()
                        game()
                    else:
                        combat()
                else:
                    messagecombat='Not enough SP!'
                    combat()

#            def itemuse():

            def runaway():
                global messagecombat
                if player.agi>enemy.agi:
                    game()
                else:
                    if random.randint(0,101)>=30:
                        game()
                    else:
                        messagecombat='You failed to escape!'
                        if enemy.dex > player.agi:
                            if enemy.cri * 100 >= random.randint(0, 100):
                                player.HP -= (enemy.firepower * 10 / player.res)
                                messagecombat += f' And lost {enemy.firepower * 10 / player.res} HP!'
                            else:
                                player.HP -= (enemy.firepower * 2 / player.res)
                                messagecombat += f' And lost {enemy.firepower * 2 / player.res} HP!'
                        else:
                            if random.randint(0, 101) >= 50:
                                if enemy.cri * 100 >= random.randint(0, 100):
                                    player.HP -= (enemy.firepower * 10 / player.res)
                                    messagecombat += f' And lost {enemy.firepower * 10 / player.res} HP!'
                                else:
                                    player.HP -= (enemy.firepower * 2 / player.res)
                                    messagecombat += f' And lost {enemy.firepower * 2 / player.res} HP!'
                            else:
                                messagecombat += f' The enemy missed!'
                        enemy.update()
                        player.update()
                        combat()

            screename = f'STEORA'
            bar = f'''⠀⠀⠀LVL {player.lvl}⠀⠀⠀ ⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{' ' * (3 - len(str(player.lvl)))}⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀       {player.system}
⠀⠀⠀HP:{screen.color.lightred}{player.HPb}{screen.color.end}       {' ' * (15 - player.HPnb)}                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        {player.planet}
⠀⠀⠀SP:{screen.color.lightyellow}{player.SPb}{screen.color.end}        {' ' * (15 - player.SPnb)}                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        {player.city}
                '''
            text = f'''        some description of the enemy goes here
                
                
{' '*int((75-len(messagecombat))/2)}{messagecombat}


                        {enemy.name} (LVL {enemy.level})
                        HP: {screen.color.lightred}{enemy.HPb}{screen.color.end}'''
            optiontitle = f'''COMBAT'''
            options = '..............1)ATTACK...........................2)USE ITEM..............\n' \
                     '...........................................................................\n' \
                     '.................................0)RUN AWAY................................\n' \
                     '...........................................................................'
            screen.screencombat(bar, screename, text, optiontitle, options)

            if screen.inpt is '1':
                attack()
#            elif screen.inpt is '2':
#                itemuse()
            elif screen.inpt is '0':
                runaway()
            else:
                combat()

        def game():
            player.update()

            screename = f'STEORA'

            bar = f'''⠀⠀⠀LVL {player.lvl}⠀⠀⠀ ⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{' ' * (3 - len(str(player.lvl)))}⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀       {player.system}
⠀⠀⠀HP:{screen.color.lightred}{player.HPb}{screen.color.end}       {' ' * (15 - player.HPnb)}                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        {player.planet}
⠀⠀⠀SP:{screen.color.lightyellow}{player.SPb}{screen.color.end}        {' ' * (15 - player.SPnb)}                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        {player.city}
                            '''
            text = f'Welcome!'

            optiontitle = ''
            options = '....1)WALK....................2)BACKPACK...............3)CHARACTER.........\n' \
                     f'....4)QUESTS..................{"5)MESSAGES" if player.newmessage is False else f"{screen.color.blink}5)MESSAGES{screen.color.end}"}...............{"6)SPACESHIP" if player.spaceship is True else "..........."}.........\n' \
                     '...........................................................................\n' \
                     '....S)SAVE....................C)SETTINGS...............X)QUIT GAME.........'
            screen.screengame(bar, screename, text, optiontitle, options)
            if screen.inpt is '1':
                walk()
            elif screen.inpt is '2':
                backpack()
            elif screen.inpt is '3':
                character()
            elif screen.inpt is '4':
                quests()
            elif screen.inpt is '5':
                messages()
            elif screen.inpt is '9':
                combat()
            elif screen.inpt in ['s','S']:
                save()
            elif screen.inpt in ['c','C']:
                config()
            elif screen.inpt in ['x','X']:
                if title.cfg.autosave is True:
                    with open(player.name.lower() + '.p', 'wb') as fp:
                        pickle.dump(player.name, fp)
                        pickle.dump(player.race, fp)
                        pickle.dump(player.system, fp)
                        pickle.dump(player.planet, fp)
                        pickle.dump(player.city, fp)
                        pickle.dump(player.local, fp)
                        pickle.dump(player.spaceship, fp)
                        pickle.dump(player.spaceshipmodel, fp)
                        pickle.dump(player.quests, fp)
                        pickle.dump(player.questsdone, fp)
                        pickle.dump(player.newmessage, fp)
                        pickle.dump(player.messages, fp)
                        pickle.dump(player.readmessages, fp)
                        pickle.dump(player.exp, fp)
                        pickle.dump(player.atribpointsspent, fp)
                        pickle.dump(player.skills, fp)
                        pickle.dump(player.dexb, fp)
                        pickle.dump(player.agib, fp)
                        pickle.dump(player.intb, fp)
                        pickle.dump(player.lukb, fp)
                        pickle.dump(player.dexmod, fp)
                        pickle.dump(player.agimod, fp)
                        pickle.dump(player.intmod, fp)
                        pickle.dump(player.lukmod, fp)
                        pickle.dump(player.firepowermod, fp)
                        pickle.dump(player.resistancemod, fp)
                        pickle.dump(player.fleemod, fp)
                        pickle.dump(player.HP, fp)
                        pickle.dump(player.SP, fp)
                        pickle.dump(player.money, fp)
                        pickle.dump(player.eqp1, fp)
                        pickle.dump(player.eqp2, fp)
                        pickle.dump(player.eqp3, fp)
                        pickle.dump(player.eqp4, fp)
                        pickle.dump(player.eqp5, fp)
                        pickle.dump(player.eqp6, fp)
                        pickle.dump(player.eqp7, fp)
                        pickle.dump(player.weapon, fp)
                        pickle.dump(player.shield, fp)
                        pickle.dump(player.items, fp)
                        pickle.dump(player.karma, fp)
                    sys.exit()
                else:
                    sys.exit()
            else:
                game()




########INICIALIZA#######
        player.update()
        game()

title.titlescreen()
if title.loaded is True:
    with open(title.savefile, 'rb') as fp:
        player.name = pickle.load(fp)
        player.race = pickle.load(fp)
        player.system = pickle.load(fp)
        player.planet = pickle.load(fp)
        player.city = pickle.load(fp)
        player.local = pickle.load(fp)
        player.spaceship = pickle.load(fp)
        player.spaceshipmodel = pickle.load(fp)
        player.quests = pickle.load(fp)
        player.questsdone = pickle.load(fp)
        player.newmessage = pickle.load(fp)
        player.messages = pickle.load(fp)
        player.readmessages = pickle.load(fp)
        player.exp = pickle.load(fp)
        player.atribpointsspent = pickle.load(fp)
        player.skills = pickle.load(fp)
        player.dexb = pickle.load(fp)
        player.agib = pickle.load(fp)
        player.intb = pickle.load(fp)
        player.lukb = pickle.load(fp)
        player.dexmod = pickle.load(fp)
        player.agimod = pickle.load(fp)
        player.intmod = pickle.load(fp)
        player.lukmod = pickle.load(fp)
        player.firepowermod = pickle.load(fp)
        player.resistancemod = pickle.load(fp)
        player.fleemod = pickle.load(fp)
        player.HP = pickle.load(fp)
        player.SP = pickle.load(fp)
        player.money = pickle.load(fp)
        player.eqp1 = pickle.load(fp)
        player.eqp2 = pickle.load(fp)
        player.eqp3 = pickle.load(fp)
        player.eqp4 = pickle.load(fp)
        player.eqp5 = pickle.load(fp)
        player.eqp6 = pickle.load(fp)
        player.eqp7 = pickle.load(fp)
        player.weapon = pickle.load(fp)
        player.shield = pickle.load(fp)
        player.items = pickle.load(fp)
        player.karma = pickle.load(fp)
    game_loop()

if screen.inpt is '9':
    game_loop()

else:
    player.name=title.playername
    player.race=title.choosenrace
    player.planet=title.playersplanet
    player.system=title.playerssystem
    player.city=title.playerscity
    if player.race is 'Alnit':
        player.dexmod = 2
        player.update()
        tutorial()
    elif player.race is 'Destanis':
        player.lukmod=2
        player.update()
        tutorial()
    elif player.race is 'Droide':
        player.dexmod = 2
        player.update()
        tutorial()
    elif player.race is 'Human':
        player.agimod=2
        player.update()
        tutorial()
    elif player.race is 'Kait':
        player.intmod=2
        player.update()
        tutorial()
    elif player.race is 'Kal-sh':
        player.agimod=2
        player.update()
        tutorial()
    elif player.race is 'Lattu':
        player.intmod=2
        player.update()
        tutorial()
    elif player.race is 'Nephin':
        player.lukmod=2
        player.update()
        tutorial()
    elif player.race is 'Ophidian':
        player.intmod=2
        player.update()
        tutorial()
    elif player.race is 'Svastel':
        player.lukmod=2
        player.update()
        tutorial()
    elif player.race is 'Zayol':
        player.agimod=2
        player.update()
        tutorial()
    elif player.race is 'Zoraht':
        player.dexmod = 2
        player.update()
        tutorial()
    tutorial()