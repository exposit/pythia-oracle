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
    version = '1.3.0',
    # this doesn't work right and I hate it
    pretitle = '---',
    posttitle = '---',
    # settings for the top bar
    enter_behavior = "plain",
    edit_behavior = "read",
    bookmarks = [-9,-9,-9,-9,-9,-9],
    tracker = 0,
    # settings for the seed button; shouldn't need to change directly unless swapping between seeds and mythic
    seed_func = 'useMythicComplex',       # useTwoPartSeed, useThreePartSeed, useAllSeed, useMythicComplex
    seed_type = 'medieval romance',       # see seed panel for options
    seed_subtype = 'adjective',
    seed_subtype_pretty = 'Complex',
    seed_alt_func = '',                   # set to '' to remove second button
    seed_alt_type = 'medieval romance',
    seed_alt_subtype = 'verb',
    seed_alt_subtype_pretty = 'Action',
    # exclude maps from loading; try setting these True in savegame/config.txt if your game is slow
    exclude_ddmap = False,
    exclude_gridmap = False,
    # actor panel
    actor_index_state = 0,
    # character sheet panel
    max_character_sheets = 6,
    total_pcs_to_show = 2,
    half_size_rows = 23,                 # this is best at 23 or 7
    # find and jump
    findList = [],
    findIndex = 0,
    # toggles for merging and dice qualities; these can be set in program
    use_dice_qualities = False,
    # secrets and triggers
    secrets = [],
    # random chance stuff for oracles -- used by fu oracle only atm
    random_chance_list = [0,1,3,5,10,15,20,25,50,75,99,100],
    random_event_chance = 5,
    # monsters
    monsters = ["","","","","","",],
    # script plots
    current_sequence = "Status Quo",
    resolve = 0,
    # mythic stuff
    use_main_tracker_for_mythic = True,
    mythic_use_random_event_rolls = True,
    mythic_genre = 'Standard',
    mythic_context = "Start",
    mythic_context_list = ['Start', 'The Adventure So Far', 'The Mystery Is...?', 'Social', 'Personal', 'PCs'],
    mythic_genre_list = ['Standard', 'Horror', 'Action-Adventure', 'Mystery', 'Social', 'Personal', 'Epic'],
    mythic_chaos_factor = 5,
    mythic_current_acting = 'average',
    mythic_current_likeliness = 'fifty-fifty',
    mythic_current_difficulty = 'average',
    # end mythic stuff
    dungeon_stocking_method = 'Gygax',       # Gygax or Moldovay
    trap_status = '',
    # pythy stuff
    use_pythy_auto_complete = False,
    default_pythy_source = "use-all",
    pythy_predict_box_count = 3,
    pythy_next_word_count = 3,
    pythy_sentence_model = "mixed",         # short, long, mixed
)

formats = dict(
    # each entry on the status list should have a corresponding formatting entry
    status_tags = ['plain', 'aside', 'oracle', 'result', 'query', 'mechanic1', 'mechanic2', 'ephemeral'],
    # this is the base for all subsequent font sizes
    basefontsize = 14,
    # this is where you set the colors that will be used in formatting tags/display, format as '9d2e39'
    highlight_color = styles.curr_palette['accent1'],     # color1
    alternate_color = styles.curr_palette['secondary'],   # color2
    transitory_color = styles.curr_palette['accent2'],    # color3 & ephemeral
    # mechanics formatting; expects these keywords but can be swapped around
    oracle = "bold",
    result = "italic",
    query = "bold_italic",
    aside = "italic",
    # assign colors with color1, color2, etc.
    mechanic1 = "color1",
    mechanic2 = "color2",
    ephemeral = "color3",
    # fiction formatting; expects these keywords but can be swapped around
    bold = "bold",
    italic = "italic",
    bold_italic = "bold_italic",
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
)

user = dict(
    temp = 0,
    # point crawl dungeon stuff
    # area themes
    dungeon_area_themes = ['Treasure', 'Stone', 'Lust', 'Pain', 'Ice', 'Fire', 'Water', 'Sorrow', 'Grief', 'Respite', 'Forsaken', 'Fury', 'Violence', 'Spite', 'Gold', 'Silver', 'Jewels', 'Fungus', 'Plants', 'Garden', 'Magic', 'Study', 'Home', 'Maze', 'Library', 'Clockwork', 'Demonic', 'Hellish', 'Chaotic', 'Malice' ],
    # area types
    dungeon_area_types = ['Dungeon', 'Dwelling', 'Lair', 'Temple', 'Caverns', 'Caves', 'Tunnels', 'Wilderness', 'Crypts', 'Catacombs', 'Lab', 'Fortress', 'Mine', 'City', 'Garden'],
    # level of activity
    dungeon_area_activity_level = ['Deserted', 'Infested', 'Swarming', 'Inactive', 'Active', 'Busy', 'Desolate', 'Abandoned', 'Empty', 'Haunted', 'Quiet', 'Heavily Trafficked', 'Contested', 'Contested', 'Contested'],
    # how likely the next area is to be the same as the current one; lower is more of the initial area
    dungeon_theme_randomness = 85,
    dungeon_type_randomness = 30,
    dungeon_activity_randomness = 50,
    # these control the current theme and any past ones
    current_dungeon_name = "",
    saved_dungeons = {},
    # how likely is it you'll find a connection to a previous area? Lower is less chance.
    backtrack_chance = 10,
    # tests called for by triggers from the secrets panel; if this list is empty it will use the default instead
    trigger_tests = ['Perception', 'Wisdom', 'Knowledge', 'Search', 'Listen', 'Intelligence', 'Awareness', 'Spot', 'Specialist'],
    # resolution qualifiers; if this list is empty it will use the default instead
    resolution_qualifiers = ["Time Required", "Outside Influences", "Knowledge", "Skill", "Luck", "Style", "Power", "Finesse"],
    # hit locations; if this list is empty it will use the default instead
    hit_locations = [],
    # only these saving throws will be called for by the dungeon panel; if this list is empty it will use the default instead
    saving_throws = [ "Poison", "Death", "Breath", "Magic", "Dexterity", "Constitution", "Luck", "Wisdom" ],
    # use the default "what did it do" effects? Set to "all" to use user and default or "user" to just use user; empty list for just defaults
    what_did_it_do_effects_merge = "all",
    # user-defined special effects for the "what did it do" pool
    what_did_it_do_effects = [ ],  # for this to be used it needs to have at least as many elements as "max_effects"
    # chance of multiple effects from one special item -- lower is less likely, set to 0 to only ever have one effect
    chance_of_multiple_effects = 20,
    # max number of effects that could potentially be on a special item
    max_effects = 3,
    # extra effects for the special features button
    special_features = [ ],
    # memory for gmbot
    memory = [],
    # word lists for pythy
    next_word_list = [" ", " " , " "],
    predict_word_list = [" ", " " , " "],
)

#------------------------------------------------------------------------
# Changes to the following are game-wide and not stored in save games
#------------------------------------------------------------------------

# do you want spinners or cycling buttons? Don't set this True unless you bought your computer yesterday
use_spinner_status = False

# should ephemeral tagged blocks be shown in logs? Used on a logform by logform basis.
show_ephemeral_in_logs = False

# these will be copied in as YAML Front Matter into log templates calling for it
yaml_for_markdown = '''
---
layout: post
title: Jekyll Blog Update
---
'''

# newfont family is any formatting contained in a "plain" block and is used to override setmainfont
# definecolor orange isn't actually used, it's just here so you can see how to do HTML formatting
yaml_for_pdf = '''
---
fontsize: 10pt
sansfont: Ubuntu Mono
mainfont: Lora
title: your title
header-includes:
   - \usepackage{xcolor}
   - \usepackage{fontspec}
   - \definecolor{light-gray}{gray}{0.60}
   - \definecolor{orange}{HTML}{FF7F00}
   - \setmainfont[UprightFeatures = {Color=black}, ItalicFeatures = {Color=light-gray}, BoldFeatures = {Color=light-gray}, BoldItalicFeatures = {Color=light-gray} ] {Lora}
   - \setmonofont[UprightFeatures = {Color=light-gray}] {Ubuntu Mono}
   - \\newfontfamily\plain[ItalicFeatures = {Color=black}, BoldFeatures = {Color=black}, BoldItalicFeatures = {Color=black}] {Lora}
---
'''

# which oracle will the ??? button call?
oracle = "mythic"          # change to 'fu' to use fu as the default
oracle_func = "mythic"     # change to 'fu' to use fu as the default

# dice presets; first should be 10 items, the second 2
dice_presets = ["1d4", "1d6", "1d8", "1d10", "1d100", "2d4", "2d6", "2d8", "2d10", "1d20"]
dice_spinner_list = ["6", "10"]

# these are used for plot generation
max_plot_subjects = 3
max_plot_elements = 3

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
blockstatusfont = str(formats['basefontsize']*.80) + "dp"
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
textBoxArray = []

trackLabelArray = []
trackStatusLabelArray = []

pcKeyLabelArray = []
pcValueLabelArray = []

tempMapArray = []
mapArray = {}

tempGmapArray = []
gmapArray = {}

imgLabelArray = []
