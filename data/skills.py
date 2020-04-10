skills = {
    'PILOT':{
        'active':False,
        'lvl':[1,2,3,4,5],
        'skilldescription':{1:'Allow the character to pilot a tiny spaceship.',
                     2:'Allow the character to pilot a small spaceship.',
                     3:'Allow the character to pilot a medium spaceship.',
                     4:'Allow the character to pilot a big spaceship.',
                     5:'Allow the character to pilot a huge spaceship.'},
    },
    'FIRST AID':{
        'active':True,
        'lvl':[1,2,3],
        'skilldescription':{1:'Costs 15 SP to restore 10 HP.',
                     2:'Costs 20 SP to restore 20 HP.',
                     3:'Costs 25 SP to restore 30 HP.',},
        'skillcost':{1:15,
                   2:20,
                   3:25},
        'skilluse':{1:'player.HP,player.SP=player.HP+10,player.SP-15',
               2:'player.HP,player.SP=player.HP+20,player.SP-20',
               3:'player.HP,player.SP=player.HP+30,player.SP-25',}
    },
    'MEDITATE':{
        'active':True,
        'lvl':[1],
        'skilldescription':{1:'The character enter in a meditative state restoring 30 SP.'},
        'skillcost':{1:0},
        'skilluse':{1:'player.SP+=30'}
    }



}