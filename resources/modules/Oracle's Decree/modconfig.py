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
        'fishbite' : ['<<A large, frilled fish leaps out from beneath the thin sand and bites at you before taking flight! If you save, continue; otherwise, contract the sinking curse; for d3 days any passage over sand results in gradual sinking unless supported. if fishattack else The sand crumbles at your touch, revealing a small amount of loot.>>', 'bold_italic', 'any'],
        'gamble' : ['The hermit will accept almost anything of value as a wager, but cheats masterfully and has an amulet of good luck.', 'bold_italic', 'any'],
    },
    'toggleRefs' : {
        'dragontoggle' : ['The treasure is shiny.', 'The treasure is expensive.'],
    },
    'jumpRefs' : {
        'sanddomes' : {
          'display' : "Sand Domes",
          'jump'  : "Sand Domes",
          'exitmsg'  : "You come across some sand domes.",
          'pause' : True,
        },
        'meethermit' : {
          'display' : "Hermit",
          'jump'  : "The Hermit",
          'exitmsg'  : "You come across a hermit.",
          'pause' : True,
        },
        'learndance' : {
          'display' : "Hermit's Secret",
          'jump'  : "Start",
          'exitmsg'  : "From the hermit, you learn that dancing with the desert sylphs eases thirst for an entire day.",
          'pause' : True,
        },
        'hermitrequest' : {
          'display' : "Hermit's Request",
          'jump'  : "Start",
          'exitmsg'  : "He asks you to slay Nirsiesel, or find someone who can.",
          'pause' : True,
        },
    },
    'fishattack' : False,
    'large' : random.choice(["massive", "tiny"]),
    'overlandEncounterChart' : [["A field of Sand Domes", 'jump_sanddomes'], ["The Rag-Rock Hermit", "jump_meethermit"], ["Heelan Bandits", ""], ["Heelan Bandits", ""], ["The Buried Oracle", ""], ["The Heelan Hunting Party", ""], ["The Starsleigh", ""], ["A Water Shade", ""], ["Sand Sprites", ""], ["Pelaago", ""],],
}
