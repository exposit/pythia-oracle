#!/usr/bin/env python
#-*- coding: utf-8 -*-
##-------------------------------------------------------------------------------------------------------------------------------------------
#  Configuration and variables
#
##-------------------------------------------------------------------------------------------------------------------------------------------

import styles
import os

curr_game_dir = "." + os.sep + "saves" + os.sep + "quicksave" + os.sep
curr_title = "replace me"

# color stuff
transitory_color = styles.curr_palette['accent2']
highlight_color = styles.curr_palette['accent1']
alternate_color = styles.curr_palette['secondary']

general = dict(
    pretitle = '---',
    posttitle = '---',
    enter_behavior = "PLAIN",
    edit_behavior = "READ",
    bookmarks = [-9,-9,-9,-9,-9,-9],
    tracker = 0,
    basefontsize = 16,
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

activePanelsLeft = []
activePanelsRight = []

basefont = str(general['basefontsize']) + "dp"
basefont75 = str(general['basefontsize']*.75) + "dp"
basefont80 = str(general['basefontsize']*.80) + "dp"
baseheight = str(general['basefontsize']+10) + "dp"
