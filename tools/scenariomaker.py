# -*- coding: utf-8 -*
#
# Scenario Creator/Helper
#
# To use, replace the advDict contents with your adventure.  Then run this file with
# 'python scenariomaker.py'.
#
#
# Text content from the adventure "Oracle's Decree" is Copyright © 2015 Michael Prescott
# http://creativecommons.org/licenses/by-nc/3.0/
# Find more adventure locations at http://blog.trilemma.com
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
               'exitmsg'  : "You trudge across the sand.",
               'pause' : False,
              },
        },
    'Sand Domes' :
        { 'title' : "Trackless Desert, Sand Domes",
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
               'exitmsg'  : "You trudge across the sand.",
               'pause' : False,
              },
        },
    'The Hermit' :
        { 'title' : "Desert, Hermit's Stone",
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
             'exitmsg'  : "You trudge across the sand.",
             'pause' : False,
            },
        },
    'Heelan Bandits' :
        { 'title' : "Desert, Heelan Scouts",
          'shown' : 0,
          'text' : [
            ['These stooped, bipedal reptiles are sandy beige with bright blue stripes. They carry crude bronze knives, staves, and favor filigreed gold cuffs and piercings as jewellery.', 'no_format'],
            ['Make a perception check; on a success click [[toggle|here|heelanambush]]. If you fail, click [[toggle|here|heelansurprise]].', 'italic'],
          ],
         'exits' : [
          ['If you survive, keep [[jump|exploring|opt1]].', 'italic'],
        ],
        'opt1' :
            {'display' : "exploring",
             'jump'  : "Start",
             'exitmsg'  : "You trudge across the sand.",
             'pause' : False,
            },
        },
    'Buried Oracle' :
        { 'title' : "Trackless Wastes, The Buried Oracle",
          'shown' : 0,
          'text' : [
            ['A giant toad slumbers under the sand, surrounded by a field of dried dung and scraps of book leather. <<A Heelan petitioner is pouring flasks of water onto it to awaken it. if setPetitioner else There is no one here but a discarded water canteen lies nearby.>>', 'no_format'],
            ['If it is woken up, click [[desc|here|woketoad]].', 'italic'],
          ],
         'exits' : [
          ['Keep [[jump|exploring|opt1]].', 'italic'],
        ],
        'opt1' :
            {'display' : "exploring",
             'jump'  : "Start",
             'exitmsg'  : "You trudge across the sand.",
             'pause' : False,
            },
        },
    'Hunting Party' :
        { 'title' : "Trackless Wastes, Hunting Party",
          'shown' : 0,
          'text' : [
            ['Gyo-ritt, Heelan proudskull, leads a small band of hunters. Decorative silver bullets have been drilled into his face and wrists. He and his six escorts are mounted on water shades; brilliant jade pennants  ap from their spear points.', 'no_format'],
            ['Gyo-ritt is looking for sport worthy of his honor and reputation as a hunter of champions, but is tired and willing to settle for lesser game.', 'no_format'],
            ['Learn more if you manage to take his [[desc|spear|spear]] from him.', 'italic'],
          ],
         'exits' : [
          ['If you win or otherwise get him to talk, [[jump|talk to him further|learndance]]. If you lose or are a strong, intimidating type, [[jump|he has something to ask you|hermitrequest]]. Or keep [[jump|exploring|opt1]].', 'italic'],
        ],
        'opt1' :
            {'display' : "exploring",
             'jump'  : "Start",
             'exitmsg'  : "You trudge across the sand.",
             'pause' : False,
            },
        },
    'Starsleigh' :
        { 'title' : "Trackless Desert, Starsleigh",
          'shown' : 0,
          'text' : [
            ['This crashed Vinteralf zephyr-chariot is a mass of twisted, silvery metal engraved with astrological patterns. If touched, it whines loudly and sinks a little deeper in the sand.', 'no_format'],
            ['If you have the charioteer\'s helm, [[desc|click here|activatesleigh]].', 'italic'],
          ],
         'exits' : [
          ['Keep [[jump|exploring|opt1]].', 'italic'],
        ],
        'opt1' :
            {'display' : "exploring",
             'jump'  : "Start",
             'exitmsg'  : "You trudge across the sand.",
             'pause' : False,
            },
        },
    'Water Shade' :
        { 'title' : "Trackless Desert, Water Shade",
          'shown' : 0,
          'text' : [
            ['Water shades are pony-sized with four-fingered ‘hands’ and a tendril-like tongue. They patrol the desert, following travellers’ tracks unerringly.', 'no_format'],
            ['[[toggle|Learn more.|learnmore]]', 'italic'],
          ],
         'exits' : [
          ['Keep [[jump|exploring|opt1]].', 'italic'],
        ],
        'opt1' :
            {'display' : "exploring",
             'jump'  : "Start",
             'exitmsg'  : "You trudge across the sand.",
             'pause' : False,
            },
        },
    'Sand Sprites' :
        { 'title' : "Trackless Desert, Sand Sprites",
          'shown' : 0,
          'text' : [
            ['The whorls of dust that play across the dunes were once undines—water spirits— now exiled to the surface by Nirsiesel’s magic. This is what has made the land dry.', 'no_format'],
            ['If you know their secret and act on it, [[desc|click here|sanddance]].', 'italic'],
          ],
         'exits' : [
          ['Keep [[jump|exploring|opt1]].', 'italic'],
        ],
        'opt1' :
            {'display' : "exploring",
             'jump'  : "Start",
             'exitmsg'  : "You trudge across the sand.",
             'pause' : False,
            },
        },
    'Pelaago' :
        { 'title' : "Trackless Desert, Pelaago Ruins",
          'shown' : 0,
          'text' : [
            ['In their original form, the cliff tunnels of Pelaago were part of a Vinteralf Stellarium. The ice has long gone, leaving only the caves.', 'no_format'],
          ],
         'exits' : [
          ['Explore the [[jump|ruins|opt2]]. Or keep [[jump|exploring|opt1]].', 'italic'],
        ],
        'opt1' :
            {'display' : "exploring",
             'jump'  : "Start",
             'exitmsg'  : "You trudge across the sand.",
             'pause' : False,
            },
        'opt2' :
            {'display' : "exploring",
             'jump'  : "Copyright",
             'exitmsg'  : "And that's the end of the scenario, for now...",
             'pause' : True,
            },
        },
        'Copyright' :
        { 'title' : "Oracle's Decree copyright",
          'shown' : 0,
          'text' : [
            ['Text content from the adventure \"Oracle\'s Decree\" is Copyright © 2015 Michael Prescott', 'no_format'],
            ['Licensed under http://creativecommons.org/licenses/by-nc/3.0/', 'no_format'],
            ['Find more adventure locations at http://blog.trilemma.com!', 'no_format'],
          ],
         'exits' : [
          ['Go your own way, or keep [[jump|exploring|opt1]].', 'italic'],
        ],
        'opt1' :
            {'display' : "exploring",
             'jump'  : "Start",
             'exitmsg'  : "You trudge across the sand.",
             'pause' : False,
            },
        },
    }

def makeAdventure():
    with open("." + os.sep + "resources" + os.sep + "scenarios" + os.sep + scenario_name + os.sep + "scenario.txt", "w") as f:
        json.dump(advDict, f)

makeAdventure()
