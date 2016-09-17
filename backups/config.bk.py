#!/usr/bin/env python
#-*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------
#  Configuration and variables
#
##---------------------------------------------------------------------------------------

import styles
import os

curr_game_dir = "." + os.sep + "saves" + os.sep + "quicksave" + os.sep
curr_adv = "." + os.sep + "resources" + os.sep + "modules" + os.sep + "moduleA" + os.sep

curr_title = "replace me"

# color stuff
transitory_color = styles.curr_palette['accent2']
highlight_color = styles.curr_palette['accent1']
alternate_color = styles.curr_palette['secondary']
link_color = styles.curr_palette['accent2']
visited_link_color = styles.curr_palette['accent1']

general = dict(
    pretitle = '---',
    posttitle = '---',
    enter_behavior = "PLAIN",
    edit_behavior = "READ",
    bookmarks = [-9,-9,-9,-9,-9,-9],
    tracker = 0,
    basefontsize = 16,
    complex_func = 'useTwoPartSeed',   # useTwoPartSeed, useThreePartSeed, useSingleSeed
    complex_type = 'medieval romance', # see seed panel for options
    #complex_type_alternate = 'medieval romance action'
)

scenario = dict(
    active = False,
    use_core = True,
    use_oracle = True,
    name = "",
    block = "Start",
    oracle = "fu",
    oracle_func = "fu",
)

user = dict(
    temp = 0,
)

actorArray = []
actorStatusArray = []
actorLabelArray = []
actorStatusLabelArray = []

threadArray = []
threadStatusArray = []
threadLabelArray = []
threadStatusLabelArray = []

textArray = []
textStatusArray = []
textLabelArray = []
textStatusLabelArray = []

trackLabelArray = []
trackStatusLabelArray = []

pcKeyLabelArray = []
pcValueLabelArray = []

tempMapArray = []
mapArray = {}

# font sizes; feel free to edit these
# also, going to move all of these to the general array so they can be saved and loaded on a game by game basis
basefont = str(general['basefontsize']) + "dp"
basefont75 = str(general['basefontsize']*.75) + "dp"
basefont80 = str(general['basefontsize']*.80) + "dp"
basefont90 = str(general['basefontsize']*.90) + "dp"
baseheight = str(general['basefontsize']+10) + "dp"
tallheight = str(general['basefontsize']+15) + "dp"
tripleheight = str(general['basefontsize']*3+10) + "dp"
octupleheight = str(general['basefontsize']*8+10) + "dp"
maintextfont = str(general['basefontsize']) + "dp"
aiheight = baseheight
