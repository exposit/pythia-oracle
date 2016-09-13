# -*- coding: utf-8 -*
#
# Scenario Creator/Helper
#
# To use, replace the advDict contents with your adventure.  Tthen run this file with
# 'python scenario_dump.py'.
#

import os
import json
import config
import random

scenario_name = 'Oracle\'s Decree'

advDict = {
     'Start' :
        { 'title' : "Trackless Desert",
          'shown' : 0,
          'text' : [
            ['Far from a uniform waste, the desert terrain varies considerably.', 'no_format'],
            ['Chunks of rock protrude from the sand, topped by hardy succulents.', 'no_format'],
            ['The wind raises brown, gritty plumes from steep-sided dunes.', 'no_format'],
            ['Shifting sand absorbs the energy of every step you make, never letting you hit your stride.', 'no_format'],
            ['Hard, cracked sedimentary rock flakes up in layers.', 'no_format'],
            ['The wind howls through a forest of red standstone that has been carved into undulating shapes by windblown grit.', 'no_format'],
          ],
          'exits' : [
            ['Keep [[func|exploring|overlandEncounter]].', 'italic'],
          ],
          'opt1' :
              {'display' : "exploring",
               'jump'  : "Start",
               'exitmsg'  : "You trudge through the wastes.",
               'pause' : True,
              },
        },
    'Sand Domes' :
        { 'title' : "Sand Domes",
          'shown' : 0,
          'text' : [
            ['These round, sandy hills are actually thin, brittle crusts over pits of brackish water.', 'no_format'],
            ['You could investigate [[desc|one|fishbite]] to see if there\'s any water', 'italic'],
          ],
          'exits' : [
            ['Keep [[jump|exploring|opt1]].', 'italic'],
          ],
          'opt1' :
              {'display' : "exploring",
               'jump'  : "Start",
               'exitmsg'  : "You trudge through the wastes.",
               'pause' : True,
              },
        },
    'The Hermit' :
        { 'title' : "Trackless Wastes, Hermit's Stone",
          'shown' : 0,
          'text' : [
            ['A dirty hermit seated upon a spire of rock offers you the secret of drinking dust if you beat him at gambling.', 'no_format'],
            ['You could [[desc|gamble|gamble]] with him, if you have anything to wager.', 'italic'],
          ],
         'exits' : [
          ['If you win or otherwise get him to talk, [[jump|talk to him further|learndance]]. If you lose or are a strong, intimidating type, [[jump|he has something to ask you|hermitrequest]]. Or keep [[jump|exploring|opt1]].', 'italic'],
        ],
        'opt1' :
            {'display' : "exploring",
             'jump'  : "Start",
             'exitmsg'  : "You trudge through the wastes.",
             'pause' : True,
            },
        },
    'Heelan Bandits' :
        { 'title' : "Trackless Wastes, Hermit's Stone",
          'shown' : 0,
          'text' : [
            ['A dirty hermit seated upon a spire of rock offers you the secret of drinking dust if you beat him at gambling.', 'no_format'],
            ['You could [[desc|gamble|gamble]] with him, if you have anything to wager.', 'italic'],
          ],
         'exits' : [
          ['If you win or otherwise get him to talk, [[jump|talk to him further|learndance]]. If you lose or are a strong, intimidating type, [[jump|he has something to ask you|hermitrequest]]. Or keep [[jump|exploring|opt1]].', 'italic'],
        ],
        'opt1' :
            {'display' : "exploring",
             'jump'  : "Start",
             'exitmsg'  : "You trudge through the wastes.",
             'pause' : True,
            },
        },
    'Buried Oracle' :
        { 'title' : "Trackless Wastes, Hermit's Stone",
          'shown' : 0,
          'text' : [
            ['A dirty hermit seated upon a spire of rock offers you the secret of drinking dust if you beat him at gambling.', 'no_format'],
            ['You could [[desc|gamble|gamble]] with him, if you have anything to wager.', 'italic'],
          ],
         'exits' : [
          ['If you win or otherwise get him to talk, [[jump|talk to him further|learndance]]. If you lose or are a strong, intimidating type, [[jump|he has something to ask you|hermitrequest]]. Or keep [[jump|exploring|opt1]].', 'italic'],
        ],
        'opt1' :
            {'display' : "exploring",
             'jump'  : "Start",
             'exitmsg'  : "You trudge through the wastes.",
             'pause' : True,
            },
        },
    'Hunting Party' :
        { 'title' : "Trackless Wastes, Hermit's Stone",
          'shown' : 0,
          'text' : [
            ['A dirty hermit seated upon a spire of rock offers you the secret of drinking dust if you beat him at gambling.', 'no_format'],
            ['You could [[desc|gamble|gamble]] with him, if you have anything to wager.', 'italic'],
          ],
         'exits' : [
          ['If you win or otherwise get him to talk, [[jump|talk to him further|learndance]]. If you lose or are a strong, intimidating type, [[jump|he has something to ask you|hermitrequest]]. Or keep [[jump|exploring|opt1]].', 'italic'],
        ],
        'opt1' :
            {'display' : "exploring",
             'jump'  : "Start",
             'exitmsg'  : "You trudge through the wastes.",
             'pause' : True,
            },
        },
    'Starsleigh' :
        { 'title' : "Trackless Wastes, Hermit's Stone",
          'shown' : 0,
          'text' : [
            ['A dirty hermit seated upon a spire of rock offers you the secret of drinking dust if you beat him at gambling.', 'no_format'],
            ['You could [[desc|gamble|gamble]] with him, if you have anything to wager.', 'italic'],
          ],
         'exits' : [
          ['If you win or otherwise get him to talk, [[jump|talk to him further|learndance]]. If you lose or are a strong, intimidating type, [[jump|he has something to ask you|hermitrequest]]. Or keep [[jump|exploring|opt1]].', 'italic'],
        ],
        'opt1' :
            {'display' : "exploring",
             'jump'  : "Start",
             'exitmsg'  : "You trudge through the wastes.",
             'pause' : True,
            },
        },
    'Water Shade' :
        { 'title' : "Trackless Wastes, Hermit's Stone",
          'shown' : 0,
          'text' : [
            ['A dirty hermit seated upon a spire of rock offers you the secret of drinking dust if you beat him at gambling.', 'no_format'],
            ['You could [[desc|gamble|gamble]] with him, if you have anything to wager.', 'italic'],
          ],
         'exits' : [
          ['If you win or otherwise get him to talk, [[jump|talk to him further|learndance]]. If you lose or are a strong, intimidating type, [[jump|he has something to ask you|hermitrequest]]. Or keep [[jump|exploring|opt1]].', 'italic'],
        ],
        'opt1' :
            {'display' : "exploring",
             'jump'  : "Start",
             'exitmsg'  : "You trudge through the wastes.",
             'pause' : True,
            },
        },
    'Sand Sprites' :
        { 'title' : "Trackless Wastes, Hermit's Stone",
          'shown' : 0,
          'text' : [
            ['A dirty hermit seated upon a spire of rock offers you the secret of drinking dust if you beat him at gambling.', 'no_format'],
            ['You could [[desc|gamble|gamble]] with him, if you have anything to wager.', 'italic'],
          ],
         'exits' : [
          ['If you win or otherwise get him to talk, [[jump|talk to him further|learndance]]. If you lose or are a strong, intimidating type, [[jump|he has something to ask you|hermitrequest]]. Or keep [[jump|exploring|opt1]].', 'italic'],
        ],
        'opt1' :
            {'display' : "exploring",
             'jump'  : "Start",
             'exitmsg'  : "You trudge through the wastes.",
             'pause' : True,
            },
        },
    'Pelago' :
        { 'title' : "Trackless Wastes, Hermit's Stone",
          'shown' : 0,
          'text' : [
            ['A dirty hermit seated upon a spire of rock offers you the secret of drinking dust if you beat him at gambling.', 'no_format'],
            ['You could [[desc|gamble|gamble]] with him, if you have anything to wager.', 'italic'],
          ],
         'exits' : [
          ['If you win or otherwise get him to talk, [[jump|talk to him further|learndance]]. If you lose or are a strong, intimidating type, [[jump|he has something to ask you|hermitrequest]]. Or keep [[jump|exploring|opt1]].', 'italic'],
        ],
        'opt1' :
            {'display' : "exploring",
             'jump'  : "Start",
             'exitmsg'  : "You trudge through the wastes.",
             'pause' : True,
            },
        },
    }

def makeAdventure():
    with open("." + os.sep + "resources" + os.sep + "scenarios" + os.sep + scenario_name + os.sep + "scenario.txt", "w") as f:
        json.dump(advDict, f)

makeAdventure()
