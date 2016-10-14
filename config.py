#!/usr/bin/env python
#-*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------
#  Configuration and variables
#
##---------------------------------------------------------------------------------------

import styles
import os

debug = True

#------------------------------------------------------------------------
# Changes to the following are stored in save games
#------------------------------------------------------------------------

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
    max_character_sheets = 6,
    total_pcs_to_show = 2,
    half_size_rows = 23,
    findList = [],
    findIndex = 0,
    merge = True,
)

formats = dict(
    basefontsize = 14,
    transitory_color = styles.curr_palette['accent2'],    # color3 & ephemeral, format as '9d2e39'
    highlight_color = styles.curr_palette['accent1'],     # color1
    alternate_color = styles.curr_palette['secondary'],   # color2
    # mechanics formatting; expects these keywords but can be swapped around
    oracle = "bold",
    result = "italic",
    query = "bold_italic",
    aside = "italic",
    # don't change these directly; change transitory_color, highlight_color, etc
    mechanic1 = "color1",
    mechanic2 = "color2",
    ephemeral = "color3",
    # fiction formatting; expects these keywords but can be swapped around
    bold = "bold",
    italic = "italic",
    bold_italic = "bold_italic",
    # don't change these directly; change transitory_color, highlight_color, etc
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

#------------------------------------------------------------------------
# Changes to the following are game-wide and not stored in save games
#------------------------------------------------------------------------

curr_title = "replace me"

# dice presets
dice_presets = ["1d4", "1d6", "1d8", "1d10", "1d100", "2d4", "2d6", "2d8", "2d10", "1d20"]
dice_spinner_list = ["4", "6", "8", "20"]

# font sizes
basefont = str(formats['basefontsize']) + "dp"
basefont60 = str(formats['basefontsize']*.70) + "dp"
basefont75 = str(formats['basefontsize']*.80) + "dp"
basefont80 = str(formats['basefontsize']*.85) + "dp"
basefont90 = str(formats['basefontsize']*.95) + "dp"
baseheight = str(formats['basefontsize']+10) + "dp"
tallheight = str(formats['basefontsize']+15) + "dp"
tripleheight = str(formats['basefontsize']*3+10) + "dp"
quintupleheight = str(formats['basefontsize']*5+10) + "dp"
octupleheight = str(formats['basefontsize']*8+10) + "dp"
maintextfont = str(formats['basefontsize']*1) + "dp"
aiheight = baseheight

#------------------------------------------------------------------------
# Don't mess with anything below this line
#------------------------------------------------------------------------

curr_game_dir = "." + os.sep + "saves" + os.sep + "quicksave" + os.sep
curr_adv = "." + os.sep + "resources" + os.sep + "modules" + os.sep + "moduleA" + os.sep

#------------------------------------------------------------------------
# Config array holders; don't change or edit these
#------------------------------------------------------------------------

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

tempGmapArray = []
gmapArray = {}

imgLabelArray = []
imgTextArray = []
