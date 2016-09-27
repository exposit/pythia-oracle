#!/usr/bin/env python
#-*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------
#  Configuration and variables
#
##---------------------------------------------------------------------------------------

import styles
import os

debug = True

curr_game_dir = "." + os.sep + "saves" + os.sep + "quicksave" + os.sep
curr_adv = "." + os.sep + "resources" + os.sep + "modules" + os.sep + "moduleA" + os.sep

curr_title = "replace me"

# color stuff
#transitory_color = styles.curr_palette['accent2']
#highlight_color = styles.curr_palette['accent1']
#alternate_color = styles.curr_palette['secondary']
#link_color = styles.curr_palette['accent2']
#visited_link_color = styles.curr_palette['accent1']

general = dict(
    pretitle = '------------------------------------------',
    posttitle = '------------------------------------------',
    enter_behavior = "plain",
    edit_behavior = "read",
    bookmarks = [-9,-9,-9,-9,-9,-9],
    tracker = 0,
    seed_func = 'useTwoPartSeed',         # useTwoPartSeed, useThreePartSeed, useAllSeed
    seed_type = 'medieval romance',       # see seed panel for options
    seed_subtype = 'adjective',
    seed_subtype_pretty = 'Desc',
    seed_alt_func = '',                   # set to '' to remove second button
    seed_alt_type = 'medieval romance',
    seed_alt_subtype = 'verb',
    seed_alt_subtype_pretty = 'Action',
    actor_index_state = 0,
    total_pcs_to_show = 2,
    findList = [],
    findIndex = 0,
)

formats = dict(
    basefontsize = 16,
    transitory_color = styles.curr_palette['accent2'],
    highlight_color = styles.curr_palette['accent1'],
    alternate_color = styles.curr_palette['secondary'],
    # mechanics formatting
    oracle = "bold",
    result = "italic",
    query = "bold_italic",
    aside = "italic",
    mechanic1 = "color1",
    mechanic2 = "color2",
    ephemeral = "color3",
    # fiction formatting
    bold = "bold",
    italic = "italic",
    bold_italic = "bold_italic",
    color1 = "color1",
    color2 = "color2",
    color3 = "color3",
    # scenario/in block links
    link_color = styles.curr_palette['accent2'],
    visited_link_color = styles.curr_palette['accent1'],
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
textFieldLabelArray = []
textStatusLabelArray = []

trackLabelArray = []
trackStatusLabelArray = []

pcKeyLabelArray = []
pcValueLabelArray = []

tempMapArray = []
mapArray = {}

# font sizes; feel free to edit these
# also, going to move all of these to the general array so they can be saved and loaded on a game by game basis
basefont = str(formats['basefontsize']) + "dp"
basefont60 = str(formats['basefontsize']*.60) + "dp"
basefont75 = str(formats['basefontsize']*.75) + "dp"
basefont80 = str(formats['basefontsize']*.80) + "dp"
basefont90 = str(formats['basefontsize']*.90) + "dp"
baseheight = str(formats['basefontsize']+10) + "dp"
tallheight = str(formats['basefontsize']+15) + "dp"
tripleheight = str(formats['basefontsize']*3+10) + "dp"
quintupleheight = str(formats['basefontsize']*5+10) + "dp"
octupleheight = str(formats['basefontsize']*8+10) + "dp"
maintextfont = str(formats['basefontsize']*.90) + "dp"
aiheight = baseheight
