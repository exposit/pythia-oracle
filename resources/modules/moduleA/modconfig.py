# this is the primary configuration variable for this module
#
#   At a minimum, you'll want to adjust or remove the Refs
#
#      also note, random module variables are set when a module game is created, not 'on the fly' when
# they are called. For that you need to write a function and call it in your adventure.
#
import random

module = dict(
    active = True,
    name = "",
    block = "Start",
    descRefs = [
        ['dragondesc', 'This is a very <<var.large>> <<scary if dragonawake else sleeping>> red dragon.', 'bold', 'any']
    ],
    toggleRefs = [
        ['dragontoggle', 'The treasure is shiny.', 'The treasure is expensive.'],
    ],
    jumpRefs = [
        ['dragonjump', 'Start', 'You attack the <<var.large>> dragon!', 'bold_italic', 'once', True],
    ],
    dragonawake = False,
    large = random.choice(["massive", "tiny"])
)
