# -*- coding: utf-8 -*
#
# Module Creator/Helper
#
# To use, replace the advDict contents with your adventure.  Tthen run this file with
# 'python module_dump.py'.
#

import os
import json
import config
import random

module_name = 'Oracle\'s Decree'

advDict = {
     'Start' :
        { 'title' : "Trackless Desert",
          'shown' : 0,
          'text' : [
            ['Far from a uniform waste, the desert terrain varies considerably.', 'no_format'],
            ['Chunks of rock protrude from the sand, topped by hardy succulents.', 'no_format'],
            ['The wind raises brown, gritty plumes from steep-sided dunes.', 'no_format'],
            ['Shifting sand absorbs the energy of every step you make, never letting you hit your stride.', 'no_format'],
            ['Hard, cracked sedimentary rock rakes up in layers.', 'no_format'],
            ['The wind howls through a forest of red standstone that has been carved into undulating shapes by windblown grit.', 'no_format'],
          ],
          'exits' : [
            ['Check for an encounter. If none, keep [[jump|exploring|opt1]].', 'italic'],
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
            ['You could investigate [[desc|one|fishbite]]', 'italic'],
          ],
          'exits' : [
            ['Check for an encounter. If none, keep [[jump|exploring|opt1]].', 'italic'],
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
    }

def makeAdventure():
    with open("." + os.sep + "resources" + os.sep + "modules" + os.sep + module_name + os.sep + "adventure.txt", "w") as f:
        json.dump(advDict, f)

makeAdventure()
