# -*- coding: utf-8 -*
#
# Scenario configuration
#
# Text content from the adventure "Oracle's Decree" is Copyright © 2015 Michael Prescott
# http://creativecommons.org/licenses/by-nc/3.0/
# Find more adventure locations at http://blog.trilemma.com
#

import random

scenario = {
    'active' : True,                # if this is False scenario will not run
    'use_core' : True,              # use core generators?
    'use_oracle': True,             # use an oracle, ie, show ??? button?
    'oracle' : 'fu',                # module to look in when ??? button is pressed
    'oracle_func' : 'fu',           # function in module to run when ??? button is pressed
    'name' : "",
    'block' : "Copyright",          # starting block that will be shown at beginning
    'descRefs' : {
        'fishbite' : ['<<A large, frilled fish leaps out from beneath the thin sand and bites at you before taking flight! If you save, continue; otherwise, contract the sinking curse; for d3 days any passage over sand results in gradual sinking unless supported. if fishattack else The sand crumbles at your touch, revealing a small amount of loot and some clean water.>>', 'bold_italic', 'repeatable', 'setFishOrWater'],
        'gamble' : ['The hermit will accept almost anything of value as a wager, but cheats masterfully and has an amulet of good luck.', 'bold_italic', 'once'],
        'woketoad' : ['The toad lashes out with its tongue, eating a fragment of a scroll. <<getProphecy>>', 'bold_italic', 'repeatable'],
        'spear' : ['His spear is a relic of his homeland and causes blood to catch  re as if it were oil.', 'bold_italic', 'once'],
        'sanddance' : ['Dancing with them relieves thirst for an entire day. In exchange, they demand a small service or token of gratitude, and if this is not performed, they attack.', 'bold_italic', 'once'],
        'activatesleigh' : ['If the wearer of the the charioteer’s helm approaches, it hums and rises into the air. It floats magically, carrying up to 4 people in whatever direction the helm points, except north - owing to the damage.', 'bold_italic', 'once'],
    },
    'toggleRefs' : {
        'heelanambush' : ['One of the scouts is attempting to circle around and attack from behind!'],
        'heelansurprise' : ['A scout circles behind you, surprising you from ambush!'],
        'learnmore' : ['They lick travellers\' footprints, which magically steals the life out of those who left them—fresh is best, but an hour old will do.\nAnyone pursued by a shade must consume twice the normal amount of food and water or collapse from exhaustion; each shade can affect d2 people.\nIf spotted and chased, shades will keep their distance. They move as swiftly as dogs, but tire if forced to run for an extended period.'],
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
        'findpelaago' : {
          'display' : "Pelaago",
          'jump'  : "Pelaago",
          'exitmsg'  : "The ruins of Pelago draw near.",
          'pause' : True,
        },
    },
    'fishattack' : False,
    'petitioner' : False,
    'overlandEncounterChart' : [["A field of Sand Domes", 'jump_sanddomes'], ["The Rag-Rock Hermit", "jump_meethermit"], ["Heelan Bandits", "jump_meetbandits"], ["Heelan Bandits", "jump_meetbandits"], ["The Buried Oracle", "jump_meetoracle"], ["The Heelan Hunting Party", "jump_meethuntingparty"], ["The Starsleigh", "jump_findstarsleigh"], ["A Water Shade", "jump_meetshade"], ["Sand Sprites", "jump_meetsprites"], ["Pelaago", "jump_findpelaago"],],
}
