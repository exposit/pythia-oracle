#!/usr/bin/env python
#-*- coding: utf-8 -*-
##-------------------------------------------------------------------------------------------------------------------------------------------
#  Configuration and variables
#
##-------------------------------------------------------------------------------------------------------------------------------------------

import styles

curr_game_dir = "./saves/quicksave/"

# color stuff
transitory_color = styles.curr_palette['accent2']
highlight_color = styles.curr_palette['accent1']
alternate_color = styles.curr_palette['secondary']

general = dict(
    pretitle = ' ',
    posttitle = ' ',
    enter_behavior = "PLAIN",
    edit_behavior = "READ",
    bookmarks = [-9,-9,-9,-9,-9,-9],
    tracker = 0,
    basefontsize = 16,
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
