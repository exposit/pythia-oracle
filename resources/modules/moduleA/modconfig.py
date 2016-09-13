# -*- coding: utf-8 -*
# this is the primary configuration variable for this module
#
#   At a minimum, you'll want to adjust or remove the Refs
#
#      also note, random module variables are set when a module game is created, not 'on the fly' when
# they are called. For that you need to write a function and call it in your adventure.
#
# Text content from the adventure "Oracle's Decree" is Copyright © 2015 Michael Prescott
# http://creativecommons.org/licenses/by-nc/3.0/
# Find more adventure locations at http://blog.trilemma.com
#
import random

modvar = {
    'active' : True,
    'name' : "",
    'block' : "Start",
    'descRefs' : {
        'dragondesc' : ['This is a very <<var.large>> <<scary if dragonawake else sleeping>> red dragon.', 'bold', 'any'],
    },
    'toggleRefs' : {
        'dragontoggle' : ['The treasure is shiny.', 'The treasure is expensive.'],
    },
    'jumpRefs' : {
        'dragonjump' : {
          'display' : "banana",
          'jump'  : "Start",
          'exitmsg'  : "You exit to the next block via 2.",
          'pause' : True,
        },
    },
    'dragonawake' : False,
    'large' : random.choice(["massive", "tiny"]),
    'overlandEncounterChart' : [["A field of Sand Domes", ""], ["The Rag-Rock Hermit", ""], ["Heelan Bandits", ""], ["Heelan Bandits", ""], ["The Buried Oracle", ""], ["The Heelan Hunting Party", ""], ["The Starsleigh", ""], ["A Water Shade", ""], ["Sand Sprites", ""], ["Pelaago", ""],],
}
