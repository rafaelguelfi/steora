import numpy as np
import random
import noise
import math
from screen import color as color
import pickle
import json
import os

##########################GERADOR DE NOME#######################################
def newname():
    global name
    name = []
    nm1 = ["a", "e", "i", "o", "u", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    nm2 = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z",
           "br", "cr", "dr", "gr", "kr", "pr", "sr", "tr", "str", "vr", "zr", "bl", "cl", "fl", "gl", "kl", "pl", "sl",
           "vl", "zl", "ch", "sh", "ph", "th"]
    nm3 = ["a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "ae", "ai", "ao", "au", "aa",
           "ea", "ei", "eo", "eu", "ee", "ia", "io", "iu", "oa", "oi", "oo", "ua", "ue"]
    nm4 = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z",
           "br", "cr", "dr", "gr", "kr", "pr", "sr", "tr", "str", "vr", "zr", "bl", "cl", "fl", "hl", "gl", "kl", "ml",
           "nl", "pl", "sl", "tl", "vl", "zl", "ch", "sh", "ph", "th", "bd", "cd", "gd", "kd", "ld", "md", "nd", "pd",
           "rd", "sd", "zd", "bs", "cs", "ds", "gs", "ks", "ls", "ms", "ns", "ps", "rs", "ts", "ct", "gt", "lt", "nt",
           "st", "rt", "zt", "bb", "cc", "dd", "gg", "kk", "ll", "mm", "nn", "pp", "rr", "ss", "tt", "zz"]
    nm5 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "b", "c", "d", "f", "g", "h", "k", "l", "m", "n", "p",
           "r", "s", "t", "x", "y", "b", "c", "d", "f", "g", "h", "k", "l", "m", "n", "p", "r", "s", "t", "x", "y",
           "cs", "ks", "ls", "ms", "ns", "ps", "rs", "ts", "ys", "ct", "ft", "kt", "lt", "nt", "ph", "sh", "th"]
    for i in range(10):
        if i<5:
            rnd=random.randint(0,len(nm1)-1)
            rnd2=random.randint(0,len(nm2)-1)
            rnd3 = random.randint(0,len(nm3)-1)
            rnd6 = random.randint(0,len(nm5)-1)
            nname = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm5[rnd6]
            name.append(nname.capitalize())
        else:
            rnd = random.randint(0,len(nm1)-1)
            rnd2 = random.randint(0,len(nm2)-1)
            rnd3 = random.randint(0,len(nm3)-1)
            rnd4 = random.randint(0,len(nm4)-1)
            rnd5 = random.randint(0,len(nm3)-1)
            if rnd3 > 14:
                while rnd5>14:
                    rnd5 = random.randint(0,len(nm3)-1)
            rnd6 = random.randint(0,len(nm5)-1)
            nname=nm1[rnd]+nm2[rnd2]+nm3[rnd3]+nm4[rnd4]+nm3[rnd5]+nm5[rnd6]
            name.append(nname.capitalize())

    name=(str(name[random.randint(0,len(name)-1)])).upper()

##########################GERADOR DE SISTEMAS###################################

def newsystem():
    global systemname
    newname()
    systemname=name
    shape = (14,70)

    global planetname1, planetname2, planetname3, planetname4, planetname5, planetname6
    newname()
    planetname1 = name
    newname()
    planetname2 = name
    newname()
    planetname3 = name
    newname()
    planetname4 = name
    newname()
    planetname5 = name
    newname()
    planetname6 = name

    typesofplanet=['EarthLike','Forest','Desert','Oceans','Ice']

    global nplanets
    global nptype
    nplanets=np.random.randint(1,7)
    nptype=[]

    for i in range(nplanets):
        nptype.append(typesofplanet[np.random.randint(0,5)])

    systemnew = np.zeros(shape)

    a,b = shape[0]/2, shape[1]/2
    r1 = 6
    r=[1.3,1.3,1.4,1.4]
    r2=r[np.random.randint(0,4)]
    r3=r[np.random.randint(0,4)]
    r4=r[np.random.randint(0,4)]
    r5=r[np.random.randint(0,4)]
    r6=r[np.random.randint(0,4)]
    r7=r[np.random.randint(0,4)]
    y,x = np.ogrid[-a:a, -b:b]

    mask = ((x+36)**2)/5+((y-5)**2)/1 <= r1**2      #estrela

    def sixplanets():
        randx2=-30
        randx3= -20
        randx4=-10
        randx5=0
        randx6=7
        randx7=18

        randy2=np.random.randint(-3,6)
        randy3=np.random.randint(-3,6)
        randy4=np.random.randint(-3,6)
        randy5=np.random.randint(-3,6)
        randy6=np.random.randint(-3,6)
        randy7=np.random.randint(-3,6)

        global mask2, mask3, mask4, mask5, mask6, mask7
        mask2 = ((x+randx2)**2)/5+((y+randy2)**2)/1 <= r2**2
        mask3 = ((x+randx3)**2)/5+((y+randy3)**2)/1 <= r3**2
        mask4 = ((x+randx4)**2)/5+((y+randy4)**2)/1 <= r4**2
        mask5 = ((x+randx5)**2)/5+((y+randy5)**2)/1 <= r5**2
        mask6 = ((x+randx6)**2)/5+((y+randy6)**2)/1 <= r6**2
        mask7 = ((x+randx7)**2)/5+((y+randy7)**2)/1 <= r7**2

        lm2 = ((x+randx2)**2)/5+((y+randy2-3)**2)/1 == 0
        lm3 = ((x+randx3)**2)/5+((y+randy3-3)**2)/1 == 0
        lm4 = ((x+randx4)**2)/5+((y+randy4-3)**2)/1 == 0
        lm5 = ((x+randx5)**2)/5+((y+randy5-3)**2)/1 == 0
        lm6 = ((x+randx6)**2)/5+((y+randy6-3)**2)/1 == 0
        lm7 = ((x+randx7)**2)/5+((y+randy7-3)**2)/1 == 0

        for i in range(shape[0]):
            for j in range(shape[1]):
                if mask[i][j]:
                    systemnew[i][j] = 1
                elif lm2[i][j]:
                    systemnew[i][j] = 16
                elif lm3[i][j]:
                    systemnew[i][j] = 15
                elif lm4[i][j]:
                    systemnew[i][j] = 14
                elif lm5[i][j]:
                    systemnew[i][j] = 13
                elif lm6[i][j]:
                    systemnew[i][j] = 12
                elif lm7[i][j]:
                    systemnew[i][j] = 11
                elif mask2[i][j]:
                    systemnew[i][j] = 2
                elif mask3[i][j]:
                    systemnew[i][j] = 3
                elif mask4[i][j]:
                    systemnew[i][j] = 4
                elif mask5[i][j]:
                    systemnew[i][j] = 5
                elif mask6[i][j]:
                    systemnew[i][j] = 6
                elif mask7[i][j]:
                    systemnew[i][j] = 7
                else:
                    systemnew[i][j] = 0

    def fiveplanets():

        randx2=-25
        randx3= -15
        randx4=-5
        randx5=6
        randx6=15

        randy2=np.random.randint(-3,6)
        randy3=np.random.randint(-3,6)
        randy4=np.random.randint(-3,6)
        randy5=np.random.randint(-3,6)
        randy6=np.random.randint(-3,6)

        global mask2, mask3, mask4, mask5, mask6, mask7
        mask2 = ((x+randx2)**2)/5+((y+randy2)**2)/1 <= r2**2
        mask3 = ((x+randx3)**2)/5+((y+randy3)**2)/1 <= r3**2
        mask4 = ((x+randx4)**2)/5+((y+randy4)**2)/1 <= r4**2
        mask5 = ((x+randx5)**2)/5+((y+randy5)**2)/1 <= r5**2
        mask6 = ((x+randx6)**2)/5+((y+randy6)**2)/1 <= r6**2

        lm2 = ((x+randx2)**2)/5+((y+randy2-3)**2)/1 == 0
        lm3 = ((x+randx3)**2)/5+((y+randy3-3)**2)/1 == 0
        lm4 = ((x+randx4)**2)/5+((y+randy4-3)**2)/1 == 0
        lm5 = ((x+randx5)**2)/5+((y+randy5-3)**2)/1 == 0
        lm6 = ((x+randx6)**2)/5+((y+randy6-3)**2)/1 == 0

        for i in range(shape[0]):
            for j in range(shape[1]):
                if mask[i][j]:
                    systemnew[i][j] = 1
                elif lm2[i][j]:
                    systemnew[i][j] = 15
                elif lm3[i][j]:
                    systemnew[i][j] = 14
                elif lm4[i][j]:
                    systemnew[i][j] = 13
                elif lm5[i][j]:
                    systemnew[i][j] = 12
                elif lm6[i][j]:
                    systemnew[i][j] = 11
                elif mask2[i][j]:
                    systemnew[i][j] = 2
                elif mask3[i][j]:
                    systemnew[i][j] = 3
                elif mask4[i][j]:
                    systemnew[i][j] = 4
                elif mask5[i][j]:
                    systemnew[i][j] = 5
                elif mask6[i][j]:
                    systemnew[i][j] = 6
                else:
                    systemnew[i][j] = 0

    def fourplanets():

        randx2=-30
        randx3= -15
        randx4=0
        randx5=15

        randy2=np.random.randint(-3,6)
        randy3=np.random.randint(-3,6)
        randy4=np.random.randint(-3,6)
        randy5=np.random.randint(-3,6)

        global mask2, mask3, mask4, mask5, mask6, mask7
        mask2 = ((x+randx2)**2)/5+((y+randy2)**2)/1 <= r2**2
        mask3 = ((x+randx3)**2)/5+((y+randy3)**2)/1 <= r3**2
        mask4 = ((x+randx4)**2)/5+((y+randy4)**2)/1 <= r4**2
        mask5 = ((x+randx5)**2)/5+((y+randy5)**2)/1 <= r5**2

        lm2 = ((x+randx2)**2)/5+((y+randy2-3)**2)/1 == 0
        lm3 = ((x+randx3)**2)/5+((y+randy3-3)**2)/1 == 0
        lm4 = ((x+randx4)**2)/5+((y+randy4-3)**2)/1 == 0
        lm5 = ((x+randx5)**2)/5+((y+randy5-3)**2)/1 == 0

        for i in range(shape[0]):
            for j in range(shape[1]):
                if mask[i][j]:
                    systemnew[i][j] = 1
                elif lm2[i][j]:
                    systemnew[i][j] = 14
                elif lm3[i][j]:
                    systemnew[i][j] = 13
                elif lm4[i][j]:
                    systemnew[i][j] = 12
                elif lm5[i][j]:
                    systemnew[i][j] = 11
                elif mask2[i][j]:
                    systemnew[i][j] = 2
                elif mask3[i][j]:
                    systemnew[i][j] = 3
                elif mask4[i][j]:
                    systemnew[i][j] = 4
                elif mask5[i][j]:
                    systemnew[i][j] = 5
                else:
                    systemnew[i][j] = 0

    def threeplanets():

        randx2=-20
        randx3= 0
        randx4=15

        randy2=np.random.randint(-3,6)
        randy3=np.random.randint(-3,6)
        randy4=np.random.randint(-3,6)

        global mask2, mask3, mask4, mask5, mask6, mask7
        mask2 = ((x+randx2)**2)/5+((y+randy2)**2)/1 <= r2**2
        mask3 = ((x+randx3)**2)/5+((y+randy3)**2)/1 <= r3**2
        mask4 = ((x+randx4)**2)/5+((y+randy4)**2)/1 <= r4**2

        lm2 = ((x+randx2)**2)/5+((y+randy2-3)**2)/1 == 0
        lm3 = ((x+randx3)**2)/5+((y+randy3-3)**2)/1 == 0
        lm4 = ((x+randx4)**2)/5+((y+randy4-3)**2)/1 == 0

        for i in range(shape[0]):
            for j in range(shape[1]):
                if mask[i][j]:
                    systemnew[i][j] = 1
                elif lm2[i][j]:
                    systemnew[i][j] = 13
                elif lm3[i][j]:
                    systemnew[i][j] = 12
                elif lm4[i][j]:
                    systemnew[i][j] = 11
                elif mask2[i][j]:
                    systemnew[i][j] = 2
                elif mask3[i][j]:
                    systemnew[i][j] = 3
                elif mask4[i][j]:
                    systemnew[i][j] = 4
                else:
                    systemnew[i][j] = 0

    def twoplanets():
        randx2=-20
        randx3= 10

        randy2=np.random.randint(-3,6)
        randy3=np.random.randint(-3,6)

        global mask2, mask3, mask4, mask5, mask6, mask7
        mask2 = ((x+randx2)**2)/5+((y+randy2)**2)/1 <= r2**2
        mask3 = ((x+randx3)**2)/5+((y+randy3)**2)/1 <= r3**2

        lm2 = ((x+randx2)**2)/5+((y+randy2-3)**2)/1 == 0
        lm3 = ((x+randx3)**2)/5+((y+randy3-3)**2)/1 == 0


        for i in range(shape[0]):
            for j in range(shape[1]):
                if mask[i][j]:
                    systemnew[i][j] = 1
                elif lm2[i][j]:
                    systemnew[i][j] = 12
                elif lm3[i][j]:
                    systemnew[i][j] = 11
                elif mask2[i][j]:
                    systemnew[i][j] = 2
                elif mask3[i][j]:
                    systemnew[i][j] = 3
                else:
                    systemnew[i][j] = 0

    def oneplanet():
        randx2=np.random.randint(-20,15)

        randy2=np.random.randint(-3,6)

        global mask2, mask3, mask4, mask5, mask6, mask7
        mask2 = ((x+randx2)**2)/5+((y+randy2)**2)/1 <= r2**2

        lm2 = ((x+randx2)**2)/5+((y+randy2-3)**2)/1 == 0

        for i in range(shape[0]):
            for j in range(shape[1]):
                if mask[i][j]:
                    systemnew[i][j] = 1
                elif lm2[i][j]:
                    systemnew[i][j] = 11
                elif mask2[i][j]:
                    systemnew[i][j] = 2
                else:
                    systemnew[i][j] = 0

    global availableplanetsnumber
    global systemoptions
    global planetslist

    if nplanets is 6:
        availableplanetsnumber = ['0', '1', '2', '3', '4', '5','6']
        planetslist=[planetname1,planetname2,planetname3,planetname4,planetname5,planetname6]
        systemoptions = f'{f"1){planetname1}.....2){planetname2}.....3){planetname3}.....4){planetname4}":.^75}\n' \
                 f'{f"5){planetname5}.....6){planetname6}":.^75}\n' \
                 f'...........................................................................\n' \
                 f'...........................................................0)BACK..........'
        sixplanets()
    elif nplanets is 5:
        availableplanetsnumber = ['0', '1', '2', '3', '4','5']
        planetslist=[planetname1,planetname2,planetname3,planetname4,planetname5]
        systemoptions = f'{f"1){planetname1}.....2){planetname2}.....3){planetname3}.....4){planetname4}":.^75}\n' \
                 f'{f"5){planetname5}":.^75}\n' \
                 f'...........................................................................\n' \
                 f'...........................................................0)BACK..........'
        fiveplanets()
    elif nplanets is 4:
        availableplanetsnumber = ['0', '1', '2', '3','4']
        planetslist=[planetname1,planetname2,planetname3,planetname4]
        systemoptions = f'{f"1){planetname1}.....2){planetname2}.....3){planetname3}.....4){planetname4}":.^75}\n' \
                 f'................................................................................\n' \
                 f'...........................................................................\n' \
                 f'...........................................................0)BACK..........'
        fourplanets()
    elif nplanets is 3:
        availableplanetsnumber = ['0', '1', '2','3']
        planetslist=[planetname1,planetname2,planetname3]
        systemoptions = f'{f"1){planetname1}.....2){planetname2}.....3){planetname3}":.^75}\n' \
                 f'...........................................................................\n' \
                 f'...........................................................................\n' \
                 f'...........................................................0)BACK..........'
        threeplanets()
    elif nplanets is 2:
        availableplanetsnumber=['0','1','2']
        planetslist=[planetname1,planetname2]
        systemoptions = f'{f"1){planetname1}.....2){planetname2}":.^75}\n' \
                 f'...........................................................................\n' \
                 f'...........................................................................\n' \
                 f'...........................................................0)BACK..........'
        twoplanets()
    elif nplanets is 1:
        availableplanetsnumber=['0','1']
        planetslist=[planetname1]
        systemoptions = f'{f"1){planetname1}":.^75}\n' \
                 f'...........................................................................\n' \
                 f'...........................................................................\n' \
                 f'...........................................................0)BACK..........'
        oneplanet()


    def transform(systemnew):
        global systemmap
        systemmap = ''
        for i in range(shape[0]):
            for j in range(shape[1]):
                if systemnew[i][j] == 0:
                    systemmap=systemmap+(' ')
                elif systemnew[i][j] == 1:
                    systemmap=systemmap+(f'{color.lightyellow}*{color.end}')
                elif systemnew[i][j] == 2:
                    if nptype[0] is 'EarthLike':
                        systemmap=systemmap+(f'{color.cyan}+{color.end}')
                    elif nptype[0] is 'Forest':
                        systemmap=systemmap+(f'{color.green}+{color.end}')
                    elif nptype[0] is 'Desert':
                        systemmap=systemmap+(f'{color.yellow}+{color.end}')
                    elif nptype[0] is 'Oceans':
                        systemmap=systemmap+(f'{color.blue}+{color.end}')
                    elif nptype[0] is 'Ice':
                        systemmap=systemmap+(f'{color.white}+{color.end}')
                elif systemnew[i][j] == 3:
                    if nptype[1] is 'EarthLike':
                        systemmap=systemmap+(f'{color.cyan}+{color.end}')
                    elif nptype[1] is 'Forest':
                        systemmap=systemmap+(f'{color.green}+{color.end}')
                    elif nptype[1] is 'Desert':
                        systemmap=systemmap+(f'{color.yellow}+{color.end}')
                    elif nptype[1] is 'Oceans':
                        systemmap=systemmap+(f'{color.blue}+{color.end}')
                    elif nptype[1] is 'Ice':
                        systemmap=systemmap+(f'{color.white}+{color.end}')
                elif systemnew[i][j] == 4:
                    if nptype[2] is 'EarthLike':
                        systemmap=systemmap+(f'{color.cyan}+{color.end}')
                    elif nptype[2] is 'Forest':
                        systemmap=systemmap+(f'{color.green}+{color.end}')
                    elif nptype[2] is 'Desert':
                        systemmap=systemmap+(f'{color.yellow}+{color.end}')
                    elif nptype[2] is 'Oceans':
                        systemmap=systemmap+(f'{color.blue}+{color.end}')
                    elif nptype[2] is 'Ice':
                        systemmap=systemmap+(f'{color.white}+{color.end}')
                elif systemnew[i][j] == 5:
                    if nptype[3] is 'EarthLike':
                        systemmap=systemmap+(f'{color.cyan}+{color.end}')
                    elif nptype[3] is 'Forest':
                        systemmap=systemmap+(f'{color.green}+{color.end}')
                    elif nptype[3] is 'Desert':
                        systemmap=systemmap+(f'{color.yellow}+{color.end}')
                    elif nptype[3] is 'Oceans':
                        systemmap=systemmap+(f'{color.blue}+{color.end}')
                    elif nptype[3] is 'Ice':
                        systemmap=systemmap+(f'{color.white}+{color.end}')
                elif systemnew[i][j] == 6:
                    if nptype[4] is 'EarthLike':
                        systemmap=systemmap+(f'{color.cyan}+{color.end}')
                    elif nptype[4] is 'Forest':
                        systemmap=systemmap+(f'{color.green}+{color.end}')
                    elif nptype[4] is 'Desert':
                        systemmap=systemmap+(f'{color.yellow}+{color.end}')
                    elif nptype[4] is 'Oceans':
                        systemmap=systemmap+(f'{color.blue}+{color.end}')
                    elif nptype[4] is 'Ice':
                        systemmap=systemmap+(f'{color.white}+{color.end}')
                elif systemnew[i][j] == 7:
                    if nptype[5] is 'EarthLike':
                        systemmap=systemmap+(f'{color.cyan}+{color.end}')
                    elif nptype[5] is 'Forest':
                        systemmap=systemmap+(f'{color.green}+{color.end}')
                    elif nptype[5] is 'Desert':
                        systemmap=systemmap+(f'{color.yellow}+{color.end}')
                    elif nptype[5] is 'Oceans':
                        systemmap=systemmap+(f'{color.blue}+{color.end}')
                    elif nptype[5] is 'Ice':
                        systemmap=systemmap+(f'{color.white}+{color.end}')
                elif systemnew[i][j] == 11:
                    systemmap=systemmap+(f'{color.redbg}1{color.end}')
                elif systemnew[i][j] == 12:
                    systemmap=systemmap+(f'{color.redbg}2{color.end}')
                elif systemnew[i][j] == 13:
                    systemmap=systemmap+(f'{color.redbg}3{color.end}')
                elif systemnew[i][j] == 14:
                    systemmap=systemmap+(f'{color.redbg}4{color.end}')
                elif systemnew[i][j] == 15:
                    systemmap=systemmap+(f'{color.redbg}5{color.end}')
                elif systemnew[i][j] == 16:
                    systemmap=systemmap+(f'{color.redbg}6{color.end}')
            systemmap=systemmap+'\n'

    transform(systemnew)

newsystem()

print(systemmap)
print(systemoptions)

newlocal={
    systemname:{
        'map':systemmap,
        'available':availableplanetsnumber,
        'planets':planetslist,
        'options':systemoptions,
    },
}
#########################GERADOR DE PLANETAS####################################

for p in range(nplanets):
    shape = (18,70)
    scale = 5
    octaves = 8
    persistence = 0.5
    lacunarity = 2
    seed = np.random.randint(0,100)

    type=list(reversed(nptype))[p]

    planetname=planetslist[p]

    planeta = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            planeta[i][j] = noise.pnoise2(i/scale,
                                        j/scale,
                                        octaves=octaves,
                                        persistence=persistence,
                                        lacunarity=lacunarity,
                                        repeatx=70,
                                        repeaty=18,
                                        base=seed)

    a,b = shape[0]/2, shape[1]/2
    r = 4.7
    y,x = np.ogrid[-a:a, -b:b]
    # creates a mask with True False values
    # at indices
    mask = (x**2)/20+(y**2)/1 <= r**2

    newplanet = np.zeros_like(planeta)

    for i in range(shape[0]):
        for j in range(shape[1]):
            if mask[i][j]:
                newplanet[i][j] = planeta[i][j]
            else:
                newplanet[i][j] = -0.8

    ncities=['1', '2', '3', '4', '5']
    nc=-1
    
    global cityname1, cityname2, cityname3, cityname4, cityname5
    newname()
    cityname1 = name
    newname()
    cityname2 = name
    newname()
    cityname3 = name
    newname()
    cityname4 = name
    newname()
    cityname5 = name


    if list(reversed(nptype))[p] is 'EarthLike':
        def transform(newplanet):
            global nc, planetmap
            planetmap=''
            for i in range(shape[0]):
                for j in range(shape[1]):
                    if newplanet[i][j] == -0.8:
                        planetmap+=(' ')
                    elif newplanet[i][j] < -0.05:
                        planetmap+=(f'{color.lightblue}~{color.end}')
                    elif newplanet[i][j] < -0.046:
                        nc = (nc + 1)
                        if nc > 4:
                            planetmap+=(f'{color.lightblue}~{color.end}')
                            nc = nc - 1
                        else:
                            planetmap+=(f'{color.redbg}{ncities[nc]}{color.end}')
                    elif newplanet[i][j] < 0.2:
                        planetmap+=(f'{color.green}+{color.end}')
                    elif newplanet[i][j] < 0.3:
                        planetmap+=(f'{color.lightblack}^{color.end}')
                    elif newplanet[i][j] < 1.0:
                        planetmap+=(f'{color.white}^{color.end}')
                planetmap+='\n'

    elif list(reversed(nptype))[p] is 'Forest':
        def transform(newplanet):
            global nc, planetmap
            planetmap=''
            for i in range(shape[0]):
                for j in range(shape[1]):
                    if newplanet[i][j] == -0.8:
                        planetmap+=(' ')
                    elif newplanet[i][j] < -0.1:
                        planetmap+=(f'{color.lightblue}~{color.end}')
                    elif newplanet[i][j] < -0.095:
                        nc = (nc + 1)
                        if nc > 4:
                            planetmap+=(f'{color.lightblue}~{color.end}')
                            nc = nc - 1
                        else:
                            planetmap+=(f'{color.redbg}{ncities[nc]}{color.end}')
                    elif newplanet[i][j] < 0.1:
                        planetmap+=(f'{color.green}+{color.end}')
                    elif newplanet[i][j] < 0.6:
                        planetmap+=(f'{color.green}*{color.end}')
                    elif newplanet[i][j] < 1.0:
                        planetmap+=(f'{color.green}^{color.end}')
                planetmap += '\n'

    elif list(reversed(nptype))[p] is 'Desert':
        def transform(newplanet):
            global nc, planetmap
            planetmap = ''
            for i in range(shape[0]):
                for j in range(shape[1]):
                    if newplanet[i][j] == -0.8:
                        planetmap+=(' ')
                    elif newplanet[i][j] < -0.3:
                        planetmap+=(f'{color.lightblue}~{color.end}')
                    elif newplanet[i][j] < -0.29:
                        nc = (nc + 1)
                        if nc > 4:
                            planetmap+=(f'{color.lightblue}~{color.end}')
                            nc=nc-1
                        else:
                            planetmap+=(f'{color.redbg}{ncities[nc]}{color.end}')
                    elif newplanet[i][j] < 0.1:
                        planetmap+=(f'{color.yellow}+{color.end}')
                    elif newplanet[i][j] < 0.6:
                        planetmap+=(f'{color.yellow}*{color.end}')
                    elif newplanet[i][j] < 1.0:
                        planetmap+=(f'{color.lightblack}^{color.end}')
                planetmap += '\n'

    elif list(reversed(nptype))[p] is 'Oceans':
        def transform(newplanet):
            global nc, planetmap
            planetmap = ''
            for i in range(shape[0]):
                for j in range(shape[1]):
                    if newplanet[i][j] == -0.8:
                        planetmap+=(' ')
                    elif newplanet[i][j] < 0.1:
                        planetmap+=(f'{color.lightblue}~{color.end}')
                    elif newplanet[i][j] < 0.105:
                        nc = (nc + 1)
                        if nc > 4:
                            planetmap+=(f'{color.lightblue}~{color.end}')
                            nc = nc - 1
                        else:
                            planetmap+=(f'{color.redbg}{ncities[nc]}{color.end}')
                    elif newplanet[i][j] < 0.3:
                        planetmap+=(f'{color.green}+{color.end}')
                    elif newplanet[i][j] < 0.6:
                        planetmap+=(f'{color.lightblack}^{color.end}')
                    elif newplanet[i][j] < 1.0:
                        planetmap+=(f'{color.white}^{color.end}')
                planetmap += '\n'

    elif list(reversed(nptype))[p] is 'Ice':
        def transform(newplanet):
            global nc, planetmap
            planetmap = ''
            for i in range(shape[0]):
                for j in range(shape[1]):
                    if newplanet[i][j] == -0.8:
                        planetmap+=(' ')
                    elif newplanet[i][j] < -0.3:
                        planetmap+=(f'{color.lightblue}~{color.end}')
                    elif newplanet[i][j] < -0.29:
                        nc = (nc + 1)
                        if nc > 4:
                            planetmap+=(f'{color.lightblue}~{color.end}')
                        else:
                            planetmap+=(f'{color.redbg}{ncities[nc]}{color.end}')
                    elif newplanet[i][j] < 0.1:
                        planetmap+=(f'{color.white}+{color.end}')
                    elif newplanet[i][j] < 0.6:
                        planetmap+=(f'{color.lightwhite}*{color.end}')
                    elif newplanet[i][j] < 1.0:
                        planetmap+=(f'{color.lightwhite}^{color.end}')
                planetmap += '\n'

    transform(newplanet)

    print(planetname)

    print(planetmap)

    global availablecitiesnumber, citylist, planetoption
    if nc+1 is 5:
        availablecitiesnumber = ['0', '1', '2', '3', '4','5']
        citylist = [cityname1, cityname2, cityname3, cityname4, cityname5]
        planetoption = f'{f"1){cityname1}.....2){cityname2}.....3){cityname3}.....4){cityname4}":.^75}\n' \
                 f'{f"5){cityname5}":.^75}\n' \
                 f'...........................................................................\n' \
                 f'...........................................................0)BACK..........'
    elif nc+1 is 4:
        availablecitiesnumber = ['0', '1', '2', '3','4']
        citylist = [cityname1, cityname2, cityname3, cityname4]
        planetoption = f'{f"1){cityname1}.....2){cityname2}.....3){cityname3}.....4){cityname4}":.^75}\n' \
                 f'...........................................................................\n' \
                 f'...........................................................................\n' \
                 f'...........................................................0)BACK..........'
    elif nc+1 is 3:
        availablecitiesnumber = ['0', '1', '2','3']
        citylist = [cityname1, cityname2, cityname3]
        planetoption = f'{f"1){cityname1}.....2){cityname2}.....3){cityname3}":.^75}\n' \
                 f'...........................................................................\n' \
                 f'...........................................................................\n' \
                 f'...........................................................0)BACK..........'
    elif nc+1 is 2:
        availablecitiesnumber=['0','1','2']
        citylist = [cityname1, cityname2]
        planetoption = f'{f"1){cityname1}.....2){cityname2}":.^75}\n' \
                 f'...........................................................................\n' \
                 f'...........................................................................\n' \
                 f'...........................................................0)BACK..........'
    elif nc+1 is 1:
        availablecitiesnumber=['0','1']
        citylist = [cityname1]
        planetoption = f'{f"1){cityname1}":.^75}\n' \
                 f'...........................................................................\n' \
                 f'...........................................................................\n' \
                 f'...........................................................0)BACK..........'
    elif nc+1 is 0:
        availablecitiesnumber=['0']
        citylist = []
        planetoption = f'...........................................................................\n' \
                 f'...........................................................................\n' \
                 f'...........................................................................\n' \
                 f'...........................................................0)BACK..........'

    print(planetoption)

    newp={
        'map':planetmap,
        'cities': citylist,
        'available':availablecitiesnumber,
        'options':planetoption,
    }

    newlocal[systemname][planetname]=newp

########################GERADOR DE CIDADES#################################

    for c in range(nc+1):

        cityname=citylist[c]

        shape = (13, 70)
        scale = 3
        octaves = 1
        persistence = 2
        lacunarity = 1
        seed = np.random.randint(0, 100)

        city = np.zeros(shape)
        for i in range(shape[0]):
            for j in range(shape[1]):
                city[i][j] = noise.pnoise2(i / scale,
                                             j / scale,
                                             octaves=octaves,
                                             persistence=persistence,
                                             lacunarity=lacunarity,
                                             repeatx=70,
                                             repeaty=17,
                                             base=seed)

        newcity = np.zeros_like(city)

        for i in range(shape[0]):
            for j in range(shape[1]):
                newcity[i][j] = (city[i][j]) * (city[i][j]) / 1.5

        def transform(city):
            nlocais = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
            global citymap
            citymap = ''
            global k
            k = -1
            for i in range(shape[0]):
                for j in range(shape[1]):
                    if city[i][j] < 0:
                        citymap+=(f' ')
                    elif city[i][j] < 0.05:
                        citymap+=(f' ')
                    elif city[i][j] < 0.2:
                        citymap+=(f'{color.whitebg} {color.end}')
                    elif city[i][j] < 0.26:
                        k = (k + 1)
                        if k > 13:
                            citymap+=(f'{color.whitebg} {color.end}')
                        else:
                            citymap+=(f'{color.redbg}{nlocais[k]}{color.end}')
                    elif city[i][j] < 0.3:
                        citymap+=(f'{color.whitebg} {color.end}')
                    elif city[i][j] < 0.4:
                        citymap+=(f'{color.whitebg} {color.end}')
                    elif city[i][j] < 0.5:
                        citymap+=(f'{color.whitebg} {color.end}')
                    elif city[i][j] < 0.6:
                        citymap+=(f'{color.whitebg} {color.end}')
                    elif city[i][j] < 0.7:
                        citymap+=(f'{color.whitebg} {color.end}')
                    elif city[i][j] < 0.8:
                        citymap+=(f'{color.whitebg} {color.end}')
                    elif city[i][j] < 0.9:
                        citymap+=(f'{color.whitebg} {color.end}')
                    elif city[i][j] < 1:
                        citymap+=(f'{color.whitebg} {color.end}')
                citymap+='\n'

            global cityoptions
            global availableplacesnumber

            if type is 'EarthLike':
                if k is 0:
                    availableplacesnumber = ['0', '1']
                    cityoptions = f'.....1)DOCAS...............................................................\n' \
                             f'...........................................................................\n' \
                             f'...........................................................................\n' \
                             f'...........................................................0)BACK..........'
                elif k is 1:
                    availableplacesnumber = ['0', '1', '2']
                    cityoptions = f'.....1)DOCAS______.....2)MERCADO____....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 2:
                    availableplacesnumber = ['0', '1', '2', '3']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)SUPR.ESPACI....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 3:
                    availableplacesnumber = ['0', '1', '2', '3', '4']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)SUPR.COMBAT...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 4:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)HOSPITAL___....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 5:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)MECÂNICO___....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 6:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 7:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 8:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 9:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 10:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....11)BAR________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 11:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....11)___________....12)EMISSÁRIO__...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 12:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....11)___________....12)___________...\n' \
                             f'....13)ANUNCIOS___....._____________....._____________.....0)BACK.._____...'
                else:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
                    cityoptions = f'.....1)DOCAS______.....2)MERCADO____.....3)SUPR.ESPACI.....4)SUPR.COMBAT...\n' \
                             f'.....5)HOSPITAL___.....6)MECÂNICO___.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....11)BAR________....12)EMISSÁRIO__...\n' \
                             f'....13)ANUNCIOS___....14)LOJADENAVES....._____________.....0)BACK.._____...'
            elif type is 'Forest':
                if k is 0:
                    availableplacesnumber = ['0', '1']
                    cityoptions = f'.....1)DOCAS...............................................................\n' \
                             f'...........................................................................\n' \
                             f'...........................................................................\n' \
                             f'...........................................................0)BACK..........'
                elif k is 1:
                    availableplacesnumber = ['0', '1', '2']
                    cityoptions = f'.....1)DOCAS______.....2)MERCADO____....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 2:
                    availableplacesnumber = ['0', '1', '2', '3']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)SUPR.ESPACI....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 3:
                    availableplacesnumber = ['0', '1', '2', '3', '4']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)SUPR.COMBAT...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 4:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)HOSPITAL___....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 5:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)MECÂNICO___....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 6:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 7:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 8:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 9:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 10:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....11)BAR________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 11:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....11)___________....12)EMISSÁRIO__...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 12:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....11)___________....12)___________...\n' \
                             f'....13)ANUNCIOS___....._____________....._____________.....0)BACK.._____...'
                else:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
                    cityoptions = f'.....1)DOCAS______.....2)MERCADO____.....3)SUPR.ESPACI.....4)SUPR.COMBAT...\n' \
                             f'.....5)HOSPITAL___.....6)MECÂNICO___.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....11)BAR________....12)EMISSÁRIO__...\n' \
                             f'....13)ANUNCIOS___....14)LOJADENAVES....._____________.....0)BACK.._____...'
            elif type is 'Desert':
                if k is 0:
                    availableplacesnumber = ['0', '1']
                    cityoptions = f'.....1)DOCAS...............................................................\n' \
                             f'...........................................................................\n' \
                             f'...........................................................................\n' \
                             f'...........................................................0)BACK..........'
                elif k is 1:
                    availableplacesnumber = ['0', '1', '2']
                    cityoptions = f'.....1)DOCAS______.....2)MERCADO____....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 2:
                    availableplacesnumber = ['0', '1', '2', '3']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)SUPR.ESPACI....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 3:
                    availableplacesnumber = ['0', '1', '2', '3', '4']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)SUPR.COMBAT...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 4:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)HOSPITAL___....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 5:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)MECÂNICO___....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 6:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 7:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 8:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 9:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 10:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....11)BAR________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 11:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....11)___________....12)EMISSÁRIO__...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 12:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....11)___________....12)___________...\n' \
                             f'....13)ANUNCIOS___....._____________....._____________.....0)BACK.._____...'
                else:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
                    cityoptions = f'.....1)DOCAS______.....2)MERCADO____.....3)SUPR.ESPACI.....4)SUPR.COMBAT...\n' \
                             f'.....5)HOSPITAL___.....6)MECÂNICO___.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....11)BAR________....12)EMISSÁRIO__...\n' \
                             f'....13)ANUNCIOS___....14)LOJADENAVES....._____________.....0)BACK.._____...'
            elif type is 'Oceans':
                if k is 0:
                    availableplacesnumber = ['0', '1']
                    cityoptions = f'.....1)DOCAS...............................................................\n' \
                             f'...........................................................................\n' \
                             f'...........................................................................\n' \
                             f'...........................................................0)BACK..........'
                elif k is 1:
                    availableplacesnumber = ['0', '1', '2']
                    cityoptions = f'.....1)DOCAS______.....2)MERCADO____....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 2:
                    availableplacesnumber = ['0', '1', '2', '3']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)SUPR.ESPACI....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 3:
                    availableplacesnumber = ['0', '1', '2', '3', '4']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)SUPR.COMBAT...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 4:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)HOSPITAL___....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 5:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)MECÂNICO___....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 6:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 7:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 8:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 9:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 10:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....11)BAR________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 11:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....11)___________....12)EMISSÁRIO__...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 12:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....11)___________....12)___________...\n' \
                             f'....13)ANUNCIOS___....._____________....._____________.....0)BACK.._____...'
                else:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
                    cityoptions = f'.....1)DOCAS______.....2)MERCADO____.....3)SUPR.ESPACI.....4)SUPR.COMBAT...\n' \
                             f'.....5)HOSPITAL___.....6)MECÂNICO___.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....11)BAR________....12)EMISSÁRIO__...\n' \
                             f'....13)ANUNCIOS___....14)LOJADENAVES....._____________.....0)BACK.._____...'
            elif type is 'Ice':
                if k is 0:
                    availableplacesnumber = ['0', '1']
                    cityoptions = f'.....1)DOCAS...............................................................\n' \
                             f'...........................................................................\n' \
                             f'...........................................................................\n' \
                             f'...........................................................0)BACK..........'
                elif k is 1:
                    availableplacesnumber = ['0', '1', '2']
                    cityoptions = f'.....1)DOCAS______.....2)MERCADO____....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 2:
                    availableplacesnumber = ['0', '1', '2', '3']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)SUPR.ESPACI....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 3:
                    availableplacesnumber = ['0', '1', '2', '3', '4']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)SUPR.COMBAT...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 4:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)HOSPITAL___....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 5:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)MECÂNICO___....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 6:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________....._____________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 7:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'....._____________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 8:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....._____________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 9:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....._____________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 10:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....11)BAR________....._____________...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 11:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....11)___________....12)EMISSÁRIO__...\n' \
                             f'....._____________....._____________....._____________.....0)BACK.._____...'
                elif k is 12:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
                    cityoptions = f'.....1)DOCAS______.....2)___________.....3)___________.....4)___________...\n' \
                             f'.....5)___________.....6)___________.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....11)___________....12)___________...\n' \
                             f'....13)ANUNCIOS___....._____________....._____________.....0)BACK.._____...'
                else:
                    availableplacesnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
                    cityoptions = f'.....1)DOCAS______.....2)MERCADO____.....3)SUPR.ESPACI.....4)SUPR.COMBAT...\n' \
                             f'.....5)HOSPITAL___.....6)MECÂNICO___.....7)___________.....8)___________...\n' \
                             f'.....9)___________....10)___________....11)BAR________....12)EMISSÁRIO__...\n' \
                             f'....13)ANUNCIOS___....14)LOJADENAVES....._____________.....0)BACK.._____...'


        transform(newcity)
        print(cityname)
        print(citymap)
        print(cityoptions)

        newc = {
            'map': citymap,
            'available': availableplacesnumber,
            'options': cityoptions,
        }


        newlocal[systemname][planetname][cityname]=newc

print(systemname)

with open('newlocal.json', 'w') as fp:
    json.dump(newlocal, fp, indent=4)