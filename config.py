#!/usr/bin/env python
#-*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------
#  Configuration and variables
#
##---------------------------------------------------------------------------------------

import styles
import os

# set this to True to get lots of messaging
debug = True

# set this to true if you are manually editing your main file
# then back to False when you're satisfied it loads properly
# game will NOT save if this is True
manual_edit_mode = False

# this controls how often full zip backups are made
# options are 'app_exit' and 'app_start', and you can use both
backup_behavior = ['app_exit']
# backup_limit should be 0 (for unlimited) or a positive number
# if set to a negative, no backups will be made
backup_limit = 7

#------------------------------------------------------------------------
# Changes to the following are stored in save games
#------------------------------------------------------------------------

general = dict(
    version = '1.1.0',
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
    merge = False,
    secrets = [],
    random_chance_list = [0,1,3,5,10,15,20,25,50,75,99,100],
    random_event_chance = 5,
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
    # trigger_tests = ['Spot', 'Listen', 'Search']
)

#------------------------------------------------------------------------
# Changes to the following are game-wide and not stored in save games
#------------------------------------------------------------------------

# do you want spinners or cycling text buttons?
use_spinner_status = True

# if this is true the game name will be used for the title in logs
use_autotitle_in_logs = True

# this will be copied in as a YAML into log templates calling for it
# 'title' is also used for html play logs
yaml = dict(
    title = "Play Log",
    author = "your name",
    mainfont = "Lora",
    sansfont = "Ubuntu Mono",
    monofont = "Ubuntu Mono",
    fontsize = "10pt",
)

# dice presets; first should be 10 items, the second 2
dice_presets = ["1d4", "1d6", "1d8", "1d10", "1d100", "2d4", "2d6", "2d8", "2d10", "1d20"]
dice_spinner_list = ["6", "10"]

# font sizes -- some of these may be deprecated
basefont = str(formats['basefontsize']*.90) + "dp"
basefont60 = str(formats['basefontsize']*.70) + "dp"
basefont75 = str(formats['basefontsize']*.80) + "dp"
basefont80 = str(formats['basefontsize']*.85) + "dp"
basefont90 = str(formats['basefontsize']*.95) + "dp"
baseheight = str(formats['basefontsize']+10) + "dp"
tallheight = str(formats['basefontsize']+15) + "dp"
doubleheight = str(formats['basefontsize']*2+20) + "dp"
tripleheight = str(formats['basefontsize']*3+20) + "dp"
quintupleheight = str(formats['basefontsize']*5+10) + "dp"
octupleheight = str(formats['basefontsize']*8+10) + "dp"
#maintextfont = str(formats['basefontsize']*1) + "dp"
aiheight = baseheight

# font sizes that actually indicate what they do
actortagfont = str(formats['basefontsize']*.90) + "dp"
actorfont = str(formats['basefontsize']*.90) + "dp"
actorstatusfont = str(formats['basefontsize']*.90) + "dp"
blockstatusfont = str(formats['basefontsize']*.90) + "dp"
blockfont = str(formats['basefontsize']*.95) + "dp"
threadstatusfont = str(formats['basefontsize']*.90) + "dp"
threadfont = str(formats['basefontsize']*.90) + "dp"

actortagheight = str((formats['basefontsize']*.90)+20) + "dp"
threadheight = str((formats['basefontsize']*.90)+15) + "dp"

maintextinputfont = str(formats['basefontsize']*.95) + "dp"

fonts = [
    {
        "name": "titlefancyfont",
        "fn_regular": "resources/fonts/miamanueva/miamanueva.ttf",
    },
    {
        "name": "titlefont",
        "fn_regular": "resources/fonts/Cormorant/Cormorant-Regular.ttf",
        "fn_bold": "resources/fonts/Cormorant/Cormorant-Bold.ttf",
        "fn_italic": "resources/fonts/Cormorant/Cormorant-Italic.ttf",
        "fn_bolditalic": "resources/fonts/Cormorant/Cormorant-BoldItalic.ttf"
    },
    {
        "name": "maintextfont",
        "fn_regular": "resources/fonts/Open_Sans/OpenSans-Regular.ttf",
        "fn_bold": "resources/fonts/Open_Sans/OpenSans-Bold.ttf",
        "fn_italic": "resources/fonts/Open_Sans/OpenSans-Italic.ttf",
        "fn_bolditalic": "resources/fonts/Open_Sans/OpenSans-BoldItalic.ttf",
    },
]

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
#imgTextArray = []
