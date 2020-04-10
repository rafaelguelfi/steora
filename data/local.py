import json

local = {
    'map': "   .      *     .       .    *        +         +     .      \u001b[5m*\u001b[0m       .     \n  *      .            .         *         *      \u001b[5m+\u001b[0m           \u001b[41m7\u001b[0m   +      .  \n    +        \u001b[5m*\u001b[0m         *      +     .        .   \u001b[41m4\u001b[0m    .     *     .    *   \n.       .    \u001b[41m2\u001b[0m   .  +        .         *       .         +           +     \n    *      +       *      .      .       *        .          .     .    \u001b[5m*\u001b[0m  \n  .     +      .            \u001b[5m*\u001b[0m          .        +     .     \u001b[5m*\u001b[0m   .    *  \u001b[41m9\u001b[0m .\n  *      .            .     \u001b[41m11\u001b[0m  *         *      +          \u001b[41m5\u001b[0m   +       .  \n    +        \u001b[5m*\u001b[0m         *      +     .        .        .     *     .    *   \n.       .    \u001b[41m6\u001b[0m  .   +        .           \u001b[41m1\u001b[0m     .         +           +     \n    *      +       *      .      .                \u001b[5m+\u001b[0m          .     .    *  \n  .     \u001b[5m*\u001b[0m      .          *          .        +    \u001b[41m13\u001b[0m .     *   .    *    .\n    *   \u001b[41m3\u001b[0m  +       *      . \u001b[41m12\u001b[0m   .       \u001b[5m*\u001b[0m        .          .     .    *  \n  .     +      .            \u001b[5m*\u001b[0m          . \u001b[41m8\u001b[0m       +     .     *   .    *    .\n  *      .            .         *         *      +              \u001b[5m+\u001b[0m       .  \n    +        *         *      +     .        .        .     *   \u001b[41m10\u001b[0m .   *   ",
    'available': ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
    'systems': ['KARSOV','ALGIEBA','MIRA','MUSCA','POLLUX','RAFFLE','SADALSUUD','SAIPH','SIRAH','SOL','TARAZED','THUBAN','UNUKALHAI'],
    'options':"........1)KARSOV.........2)ALGIEBA.....3)MIRA..............4)MUSCA.........\n........5)POLLUX.........6)RAFFLE......7)SADALSUUD.........8)SAIPH.........\n........9)SIRAH.........10)SOL........11)TARAZED..........12)THUBAN........\n........13)UNUKALHAI....14)OUTROS..........................0)BACK..........\n",

    'KARSOV': {
        'map': "                                                                      \n                                                \u001b[37m+\u001b[0m                     \n                                               \u001b[37m+\u001b[0m\u001b[37m+\u001b[0m\u001b[37m+\u001b[0m                    \n                                                \u001b[37m+\u001b[0m                     \n                                                                      \n                                                \u001b[41m1\u001b[0m                     \n\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m                                                              \n\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m                                                            \n\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m                                                          \n\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m                                                        \n\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m                                                       \n\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m                                                       \n\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m                                                       \n\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m\u001b[90m.\u001b[0m                                                       \n",
        'planets': ["KARSOV'S BASE"],
        'available': ['0', '1'],
        'options': ".............................1)KARSOV'S BASE...............................\n...........................................................................\n...........................................................................\n...........................................................0)BACK..........",

        "KARSOV'S BASE": {
            'map': '',
            'cities': ['NORTH KARSOV','WEST KARSOV','CENTRAL KARSOV','EAST KARSOV','SOUTH KARSOV'],
            'available':['0','1','2','3','4','5'],
            'options': "..............................1)NORTH KARSOV...............................\n.............2)WEST KARSOV...3)CENTRAL KARSOV...4)EAST KARSOV..............\n..............................5)SOUTH KARSOV...............................\n...........................................................0)BACK..........",

            'CENTRAL KARSOV': {
                'map': "                                                                      \n                              ...........                             \n                           .... \u001b[47m \u001b[0m    \u001b[47m \u001b[0m\u001b[47m \u001b[0m ....                          \n                         ...\u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[41m2\u001b[0m\u001b[47m \u001b[0m       ...                        \n                       ...  \u001b[47m \u001b[0m  \u001b[47m \u001b[0m  \u001b[47m \u001b[0m\u001b[47m \u001b[0m   \u001b[47m \u001b[0m    \u001b[47m \u001b[0m...                      \n                       ..   \u001b[47m \u001b[0m  \u001b[47m \u001b[0m\u001b[41m3\u001b[0m  \u001b[47m \u001b[0m  \u001b[47m \u001b[0m\u001b[41m1\u001b[0m    \u001b[47m \u001b[0m\u001b[47m \u001b[0m..                      \n                      .. \u001b[47m \u001b[0m\u001b[41m4\u001b[0m \u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[47m \u001b[0m              ..                     \n                      .. \u001b[47m \u001b[0m\u001b[47m \u001b[0m  \u001b[47m \u001b[0m       \u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m     ..                     \n                       ..   \u001b[41m5\u001b[0m\u001b[47m \u001b[0m  \u001b[47m \u001b[0m  \u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[41m7\u001b[0m\u001b[47m \u001b[0m   \u001b[47m \u001b[0m  ..                      \n                       ...  \u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[41m6\u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[47m \u001b[0m   ...                      \n                         ...   \u001b[47m \u001b[0m  \u001b[47m \u001b[0m  \u001b[47m \u001b[0m  \u001b[41m8\u001b[0m\u001b[47m \u001b[0m ...                        \n                           ....         ....                          \n                              ...........                             \n",
                'places':['SPACEPORT','KARSOV BANK','COMMERCIAL ASSOCIATION OF STEORA','GALACTIC LIBRARY','ASTROHISTORY ACADEMY','CENTRAL RESTAURANT','LEAGUE OF STEORA HEADQUARTERS','SPACE EXPLORATION ASSOCIATION'],
                'available': ['0', '1', '2', '3', '4', '5', '6','7','8'],
                'options':".....1)SPACEPORT...2)KARSOV BANK...3)COMMERCIAL ASSOCIATION OF STEORA......\n4)....GALACTIC LIBRARY...5)ASTROHISTORY ACADEMY...6)CENTRAL RESTAURANT.....\n.....7)LEAGUE OF STEORA HEADQUARTERS...8)SPACE EXPLORATION ASSOCIATION.....\n...........................................................0)BACK..........",
            },
            'NORTH KARSOV': {
                'map': "                                  ...                                 \n                                ..\u001b[47m \u001b[0m  ..                               \n                              ..  \u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[41m1\u001b[0m..                             \n                            .. \u001b[47m \u001b[0m\u001b[47m \u001b[0m       \u001b[47m \u001b[0m..                           \n                          ..  \u001b[47m \u001b[0m\u001b[41m2\u001b[0m\u001b[47m \u001b[0m       \u001b[47m \u001b[0m\u001b[47m \u001b[0m ..                         \n                        ..\u001b[47m \u001b[0m  \u001b[47m \u001b[0m\u001b[47m \u001b[0m    \u001b[47m \u001b[0m        \u001b[47m \u001b[0m..                       \n                      .. \u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[47m \u001b[0m           ..                     \n                      ..\u001b[47m \u001b[0m\u001b[41m3\u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m  \u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[41m4\u001b[0m\u001b[47m \u001b[0m     \u001b[47m \u001b[0m\u001b[41m5\u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m  ..                     \n                        ..     \u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m     \u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m..                       \n                          ..               ..                         \n                            ..     \u001b[47m \u001b[0m\u001b[47m \u001b[0m  \u001b[47m \u001b[0m\u001b[47m \u001b[0m..                           \n                              ..    \u001b[47m \u001b[0m  ..                             \n                                ..   ..                               \n",
                'places':['SPACEPORT','MEDICINE ACADEMY','CENTER OF BIOTECHNOLOGY RESEARCH','KARSOV HOSPITAL','PHARMA PLAZA'],
                'available': ['0', '1', '2', '3', '4', '5'],
                'options':"..................1)SPACEPORT.........2)MEDICINE ACADEMY...................\n........3)CENTER OF BIOTECHNOLOGY RESEARCH.......4)KARSOV HOSPITAL.........\n..............................5)PHARMA PLAZA...............................\n...........................................................0)BACK..........",
            },
            'SOUTH KARSOV': {
                'map': "                                ..   ..                               \n                              ..       ..                             \n                            .. \u001b[47m \u001b[0m\u001b[47m \u001b[0m        ..                           \n                          ..    \u001b[47m \u001b[0m    \u001b[47m \u001b[0m  \u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m..                         \n                        ..\u001b[47m \u001b[0m     \u001b[47m \u001b[0m    \u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[41m1\u001b[0m\u001b[47m \u001b[0m  ..                       \n                      .. \u001b[47m \u001b[0m\u001b[47m \u001b[0m    \u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[47m \u001b[0m       \u001b[47m \u001b[0m\u001b[47m \u001b[0m  ..                     \n                      .. \u001b[47m \u001b[0m\u001b[47m \u001b[0m      \u001b[47m \u001b[0m\u001b[41m2\u001b[0m\u001b[47m \u001b[0m       \u001b[47m \u001b[0m\u001b[47m \u001b[0m  ..                     \n                        ..\u001b[41m3\u001b[0m  \u001b[47m \u001b[0m  \u001b[47m \u001b[0m\u001b[47m \u001b[0m    \u001b[47m \u001b[0m      ..                       \n                          ..\u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[47m \u001b[0m    ..                         \n                            .. \u001b[47m \u001b[0m  \u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[41m4\u001b[0m\u001b[47m \u001b[0m  ..                           \n                              ..  \u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m..                             \n                                ..   ..                               \n                                  ...                                 \n",
                'places':['SPACEPORT','SHOOTING ACADEMY','GAB PUB','BELIC PLAZA'],
                'available': ['0', '1', '2', '3', '4'],
                'options':"....................1)SPACEPORT.....2)SHOOTING ACADEMY.....................\n.........................3)GAB PUB...4)BELIC PLAZA.........................\n...........................................................................\n...........................................................0)BACK..........",
            },
            'EAST KARSOV': {
                'map': "                                                                      \n                                .......                               \n                           ......\u001b[47m \u001b[0m\u001b[41m1\u001b[0m\u001b[47m \u001b[0m  ......                          \n                      ......\u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[47m \u001b[0m       ......                     \n                 ......     \u001b[47m \u001b[0m\u001b[41m2\u001b[0m\u001b[47m \u001b[0m \u001b[41m3\u001b[0m\u001b[47m \u001b[0m      \u001b[47m \u001b[0m  \u001b[47m \u001b[0m\u001b[47m \u001b[0m  \u001b[47m \u001b[0m......                \n            ...... \u001b[47m \u001b[0m     \u001b[47m \u001b[0m  \u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m     \u001b[47m \u001b[0m\u001b[47m \u001b[0m     \u001b[47m \u001b[0m\u001b[47m \u001b[0m    ......           \n       ......                        \u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[47m \u001b[0m    \u001b[47m \u001b[0m\u001b[47m \u001b[0m       ......      \n       ......       \u001b[47m \u001b[0m\u001b[47m \u001b[0m  \u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m        \u001b[47m \u001b[0m  \u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[47m \u001b[0m   \u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m    \u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m......      \n            ......  \u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[41m4\u001b[0m\u001b[47m \u001b[0m   \u001b[47m \u001b[0m\u001b[47m \u001b[0m       \u001b[47m \u001b[0m\u001b[47m \u001b[0m      \u001b[47m \u001b[0m\u001b[41m5\u001b[0m\u001b[47m \u001b[0m  ......           \n                 ......     \u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[47m \u001b[0m             \u001b[47m \u001b[0m\u001b[47m \u001b[0m......                \n                      ......\u001b[41m6\u001b[0m\u001b[47m \u001b[0m   \u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[47m \u001b[0m     ......                     \n                           ......\u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[47m \u001b[0m......                          \n                                .......                               \n",
                'places':['SPACEPORT','FITO PLAZA','ZOO PLAZA','ASTROBIOLOGY ACADEMY','GREENHOUSES','ASTROSCIENCE MUSEUM'],
                'available':['0','1','2','3','4','5','6'],
                'options':"................1)SPACEPORT....2)FITO PLAZA....3)ZOO PLAZA.................\n..................4)ASTROBIOLOGY ACADEMY....5)GREENHOUSES..................\n...........................6)ASTROSCIENCE MUSEUM...........................\n...........................................................0)BACK..........",
            },
            'WEST KARSOV': {
                'map': "                                                                      \n                                .......                               \n                           ......\u001b[47m \u001b[0m\u001b[47m \u001b[0m   ......                          \n                      ......               ......                     \n                 ......         \u001b[47m \u001b[0m  \u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m         ......                \n            ...... \u001b[47m \u001b[0m      \u001b[47m \u001b[0m        \u001b[47m \u001b[0m\u001b[47m \u001b[0m         \u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[41m1\u001b[0m\u001b[47m \u001b[0m  ......           \n       ......      \u001b[47m \u001b[0m\u001b[47m \u001b[0m    \u001b[47m \u001b[0m\u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[47m \u001b[0m                \u001b[47m \u001b[0m\u001b[47m \u001b[0m          ......      \n       ......   \u001b[47m \u001b[0m  \u001b[47m \u001b[0m\u001b[47m \u001b[0m   \u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m         \u001b[47m \u001b[0m\u001b[41m2\u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m     \u001b[47m \u001b[0m\u001b[41m3\u001b[0m\u001b[47m \u001b[0m   \u001b[47m \u001b[0m\u001b[47m \u001b[0m    ......      \n            ......    \u001b[47m \u001b[0m \u001b[47m \u001b[0m\u001b[41m4\u001b[0m\u001b[47m \u001b[0m    \u001b[47m \u001b[0m    \u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[47m \u001b[0m  \u001b[47m \u001b[0m\u001b[47m \u001b[0m  \u001b[47m \u001b[0m\u001b[47m \u001b[0m\u001b[41m5\u001b[0m\u001b[47m \u001b[0m  ......           \n                 ......\u001b[47m \u001b[0m                   \u001b[47m \u001b[0m\u001b[47m \u001b[0m   ......                \n                      ...... \u001b[47m \u001b[0m  \u001b[47m \u001b[0m\u001b[47m \u001b[0m  \u001b[47m \u001b[0m\u001b[47m \u001b[0m   \u001b[47m \u001b[0m\u001b[47m \u001b[0m......                     \n                           ......\u001b[47m \u001b[0m  \u001b[47m \u001b[0m\u001b[47m \u001b[0m......                          \n                                .......                               \n",
                'places':['SPACEPORT','FLIGHT ACADEMY','ALTITUD PLAZA', 'KISTO WORKSHOP', 'PIT-STOP CAFE'],
                'available':['0','1','2','3','4','5'],
                'options':"..........1)SPACEPORT......2)FLIGHT ACADEMY......3)ALTITUD PLAZA...........\n................4)KISTO WORKSHOP...........5)PIT-STOP CAFE.................\n...........................................................................\n...........................................................0)BACK..........",
            },
        },
    },
    'SAIPH':{
        'map': '',
        'planets': ['ALNITAK'],

        'ALNITAK': {
            'map': '',
            'cities': ['SARMACIA'],

            'SARMACIA': {
                'map': '',
            },
        },
    },
    'POLLUX': {
        'map': '',
        'planets': ['TWEEL'],

        'TWEEL': {
            'map': '',
            'cities': ['CHEURHULL'],

            'CHEURHULL': {
                'map': '',
            },
        },
    },
    'SIRAH': {
        'map': '',
        'planets': ['ALPHERATZ'],

        'ALPHERATZ': {
            'map': '',
            'cities': ['VICHI'],

            'VICHI': {
                'map': '',
            },
        },
    },
    'SOL': {
        'map': '',
        'planets': ['TERRA'],

        'TERRA': {
            'map': '',
            'cities': ['LUSAKA'],

            'LUSAKA': {
                'map': '',
            },
        },
    },
    'MIRA': {
        'map': '',
        'planets': ['KAFFAL'],

        'KAFFAL': {
            'map': '',
            'cities': ['BALAENA'],

            'BALAENA': {
                'map': '',
            },
        },
    },
    'TARAZED': {
        'map': '',
        'planets': ['ALSHAIN'],

        'ALSHAIN': {
            'map': '',
            'cities': ['VROTON'],

            'VROTON': {
                'map': '',
            },
        },
    },
    'ALGIEBA': {
        'map': '',
        'planets': ['REGULUS'],

        'REGULUS': {
            'map': '',
            'cities': ['EYLANBU'],

            'EYLANBU': {
                'map': '',
            },
        },
    },
    'RAFFLE': {
        'map': '',
        'planets': ['NEPENTHES'],

        'NEPENTHES': {
            'map': '',
            'cities': ['ANERORA'],

            'ANERORA': {
                'map': '',
            },
        },
    },
    'UNUKALHAI': {
        'map': '',
        'planets': ['OPHOS'],

        'OPHOS': {
            'map': '',
            'cities': ['KOLIS'],

            'KOLIS': {
                'map': '',
            },
        },
    },
    'SADALSUUD': {
        'map': '',
        'planets': ['SVA'],

        'SVA': {
            'map': '',
            'cities': ['UMILLE'],

            'UMILLE': {
                'map': '',
            },
        },
    },
    'MUSCA': {
        'map': '',
        'planets': ['ALPHA MUS'],

        'ALPHA MUS': {
            'map': '',
            'cities': ['CHOXPOOL'],

            'CHOXPOOL': {
                'map': '',
            },
        },
    },
    'THUBAN': {
        'map': '',
        'planets': ['ELTANIN'],

        'ELTANIN': {
            'map': '',
            'cities': ['UWITA'],

            'UWITA': {
                'map': '',
            },
        },
    },
}
