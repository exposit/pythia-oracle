# basic python file to dump a module to json for adventure purposes
import os
import json
import config

pseudoDict = {
     'Start' :
        { 'title' : "Start Room",
          'status' : 0,
          'text' : [
            ['This is the text shown to the reader.', 'no_format'],
            ['This is a second line of text shown to the reader.', 'italic'],
          ],
          'opt1' :
              {'display' : "opt display",
               'jump'  : "BlockB",
               'exitmsg'  : "You exit to the next block via 1",
               'pause' : True,
              },
          'opt2' :
              {'display' : "opt2 display",
               'jump'  : "BlockB",
               'exitmsg'  : "You exit to the next block via 2.",
               'exitstatus' : 'bold',
               'pause' : True,
              },
          'opt3' :
              {'display' : "opt3 display",
               'jump'  : "BlockB",
               'exitmsg'  : "You exit to the next block via 3.",
               'pause' : True,
              },
        },
    'BlockB' :
        { 'title' : "Block B",
          'status' : 0,
          'text' : [
            ['This is the [ref=md_dragondesc][color=0000ff]clickable display[/ref][/color] text shown to the reader blockb.', 'no_format'],
            ['This is a second line of text [ref=mj_dragonjump][color=0000ff]clickable jump[/ref][/color] shown to the reader. blockb', 'bold_italic'],
            ['This is a second3 line of text [ref=mt_dragontoggle][color=0000ff]clickable toggle[/ref][/color] shown to the reader. blockb', 'bold_italic'],
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
    }

# this is the primary configuration variable
# at a minimum, you'll want to adjust the Refs
module = dict(
    active = True,
    name = "",
    block = "Start",
    descRefs = [
        ['dragondesc', 'This is a very scary red dragon.', 'bold', 'any']
    ],
    toggleRefs = [
        ['dragontoggle', 'This is a large blue dragon.', 'This is a large red dragon.'],
    ],
    jumpRefs = [
        ['dragonjump', 'blockC', 'You attack the dragon!', 'bold_italic', 'once', True],
    ],
)

def makeAdventure():
    with open("." + os.sep + "adventure.txt", "w") as f:
        json.dump(pseudoDict, f)

    with open("." + os.sep + "config.txt", "w") as f:
        tempDict = {}
        tempDict['general'] = config.general
        tempDict['user'] = config.user
        tempDict['module'] = module
        json.dump(tempDict, f)


makeAdventure()
