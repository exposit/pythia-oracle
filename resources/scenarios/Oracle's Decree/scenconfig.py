# -*- coding: utf-8 -*
# this is the primary configuration variable for this scenario
#
#   At a minimum, you'll want to adjust or remove the Refs
#
#      also note, random scenario variables are set when a scenario game is created, not 'on the fly' when
# they are called. For that you need to write a function and call it in your adventure.
#
# Text content from the adventure "Oracle's Decree" is Copyright © 2015 Michael Prescott
# http://creativecommons.org/licenses/by-nc/3.0/
# Find more adventure locations at http://blog.trilemma.com
#
import random

scenario = {
    'active' : True,
    'name' : "",
    'block' : "Start",
    'descRefs' : {
        'fishbite' : ['<<A large, frilled fish leaps out from beneath the thin sand and bites at you before taking flight! If you save, continue; otherwise, contract the sinking curse; for d3 days any passage over sand results in gradual sinking unless supported. if fishattack else The sand crumbles at your touch, revealing a small amount of loot and some clean water.>>', 'bold_italic', 'repeatable', 'setFishOrWater'],
        'gamble' : ['The hermit will accept almost anything of value as a wager, but cheats masterfully and has an amulet of good luck.', 'bold_italic', 'once'],
    },
    'toggleRefs' : {
        'dragontoggle' : ['The treasure is shiny.', 'The treasure is expensive.'],
    },
    'jumpRefs' : {
        'sanddomes' : {
          'display' : "Sand Domes",
          'jump'  : "Sand Domes",
          'exitmsg'  : "You come across some sand domes.",
          'pause' : False,
        },
        'meethermit' : {
          'display' : "Hermit",
          'jump'  : "The Hermit",
          'exitmsg'  : "You come across a hermit.",
          'pause' : False,
        },
        'learndance' : {
          'display' : "Hermit's Secret",
          'jump'  : "Start",
          'exitmsg'  : "From the hermit, you learn that dancing with the desert sprites eases thirst for an entire day.",
          'pause' : True,
        },
        'hermitrequest' : {
          'display' : "Hermit's Request",
          'jump'  : "Start",
          'exitmsg'  : "He asks you to slay Nirsiesel, or find someone who can.",
          'pause' : True,
        },
        'meetbandits'
         : {
          'display' : "Heelan Scout Party",
          'jump'  : "Heelan Bandits",
          'pause' : False,
        },
        'meetoracle' : {
          'display' : "The Buried Oracle",
          'jump'  : "Buried Oracle",
          'pause' : False,
        },
        'meethuntingparty' : {
          'display' : "Heelan Hunting Party",
          'jump'  : "Hunting Party",
          'pause' : False,
        },
        'findstarsleigh' : {
          'display' : "The Starsleigh",
          'jump'  : "Starsleigh",
          'pause' : False,
        },
        'meetshade' : {
          'display' : "Water Shade",
          'jump'  : "Water Shade",
          'pause' : False,
        },
        'meetsprites' : {
          'display' : "Sand Sprites",
          'jump'  : "Sand Sprites",
          'pause' : False,
        },
        'findpelago' : {
          'display' : "Pelago",
          'jump'  : "Pelago",
          'exitmsg'  : "The ruins of Pelago draw near.",
          'pause' : True,
        },
    },
    'fishattack' : False,
    'large' : random.choice(["massive", "tiny"]),
    'overlandEncounterChart' : [["A field of Sand Domes", 'jump_sanddomes'], ["The Rag-Rock Hermit", "jump_meethermit"], ["Heelan Bandits", "jump_meetbandits"], ["Heelan Bandits", "jump_meetbandits"], ["The Buried Oracle", "jump_meetoracle"], ["The Heelan Hunting Party", "jump_meethuntingparty"], ["The Starsleigh", "jump_findstarsleigh"], ["A Water Shade", "jump_meetshade"], ["Sand Sprites", "jump_meetsprites"], ["Pelaago", "jump_findpelago"],],
}
