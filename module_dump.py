# -*- coding: utf-8 -*self
#
# Module Creator/Helper
#
# To use, replace the advDict contents with your adventure.  Tthen run this file with 'python
# module_dump.py'.
#
# [Adventure content licensing terms]
#
#

import os
import json
import config
import random

module_name = 'moduleA'

advDict = {
     'Start' :
        { 'title' : "Start Room",
          'status' : 0,
          'text' : [
            ['You are in a maze of twisty passages, all alike.', 'no_format'],
            ['There\'s an ogre here. Defeat it in single combat and choose "success". If it defeats you, go to "defeat". If you want to run away, choose option "flee".', 'italic'],
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
               'exitstatus' : 'bold',
               'pause' : True,
              },
          'opt3' :
              {'display' : "flee",
               'jump'  : "Flee",
               'exitmsg'  : "You run away screaming.",
               'pause' : True,
               'function' : 'Flee',
              },
        },
    'OgreTreasure' :
        { 'title' : "Start Room, Atop a Pile of Loot",
          'status' : 0,
          'text' : [
            ['There\'s a pile of [ref=md_dragondesc][color=0000ff]treasure here[/ref][/color]', 'no_format'],
            ['This is a second <<var.large>> line of text [ref=mj_dragonjump][color=0000ff]clickable jump[/ref][/color] shown to the reader. blockb', 'bold_italic'],
            ['This is a <<var.sleeping>> <<var.large>> second3 line of text [ref=mt_dragontoggle][color=0000ff]clickable toggle[/ref][/color] shown to the reader. blockb', 'bold_italic'],
          ],
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
          'status' : 0,
          'text' : [
            ['You have perished in single combat against a <<var.large>> ogre. And this is the end. Make a new game to continue.', 'bold'],
          ],
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
