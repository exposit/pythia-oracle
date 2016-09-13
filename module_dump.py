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

module_name = 'moduleA'

advDict = {
     'Start' :
        { 'title' : "Start Room",
          'shown' : 0,
          'text' : [
            ['You are in a maze of twisty passages, all alike.', 'no_format'],
            ['There\'s an ogre here.', 'no_format'],
          ],
          'exits' : [
            ['Defeat it in single combat and choose [[jump|success|opt1]]. If it defeats you, go to [[jump|defeat|opt2]]. If you want to run away, choose option [[jump|flee|opt3]].', 'italic'],
          ],
          'opt1' :
              {'display' : "success",
               'jump'  : "OgreTreasure",
               'exitmsg'  : "Congratulations! You've defeated the ogre. On its body you see...",
               'pause' : True,
              },
          'opt2' :
              {'display' : "defeat",
               'jump'  : "The End",
               'exitmsg'  : "You have perished!",
               'exitformat' : 'bold',
               'pause' : True,
              },
          'opt3' :
              {'display' : "flee",
               'jump'  : "Start",
               'exitmsg'  : "You run away screaming.",
               'pause' : True,
              },
        },
    'OgreTreasure' :
        { 'title' : "Start Room, Atop a Pile of Loot",
          'shown' : 0,
          'text' : [
            ['There\'s a pile of [[desc|treasure here|dragondesc]]', 'no_format'],
            ['This is a second <<var.large>> line of text [[jump|start|opt1]] shown to the reader. blockb', 'bold_italic'],
            ['This is a <<var.large>> second3 line of text [[toggle|clickable toggle|dragontoggle]] shown to the reader. blockb', 'bold_italic'],
          ],
          'exitlist' : ['opt1', 'opt2'],
          'opt1' :
              {'display' : "new display",
               'jump'  : "Start",
               'exitmsg'  : "You exit to the next block via 1",
               'pause' : True,
              },
          'opt2' :
              {'display' : "banana",
               'jump'  : "Start",
               'exitmsg'  : "You exit to the next block via 2.",
               'pause' : True,
              },
        },
    'The End' :
        { 'title' : "Start Room, At an Ogre's Feet",
          'shown' : 0,
          'text' : [
            ['You have perished in single combat against a <<var.large>> ogre. And this is the end. Make a new game to continue.', 'bold'],
          ],
          'exitlist' : ['opt1', 'opt2'],
          'opt1' :
              {'display' : "start over",
               'jump'  : "Start",
               'exitmsg'  : "Do over!",
               'pause' : True,
              },
          'opt2' :
              {'display' : "banana",
               'jump'  : "Start",
               'exitmsg'  : "You exit to the next block via 2.",
               'pause' : True,
              },
        },
    }

def makeAdventure():
    with open("." + os.sep + "resources" + os.sep + "modules" + os.sep + module_name + os.sep + "adventure.txt", "w") as f:
        json.dump(advDict, f)

makeAdventure()
