# -*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------------------
#  world & dungeon panel
#
#
##---------------------------------------------------------------------------------------------------

import imports
from imports import *
import config

def exclude():
    return False

def onEnter(self):
    #print("update my own widgets")
    for key in config.user['saved_dungeons']:
        self.nextAreaButton.disabled = False
        self.dungeonSpinner.values.append(key)

def initPanel(self):

        self.dungeonAItem = AccordionItem(title='Dungeon & Wilderness', background_normal='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', background_selected='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', min_space = config.aiheight)
        
        dungeonMainBox = BoxLayout(orientation='vertical')

        dungeonMainBox.add_widget(Label(text='General Questions', size_hint=(1,.10), font_size=config.basefont90))

        button = Button(text="More or Less Than Expected?", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=moreOrLessRoll)
        dungeonMainBox.add_widget(button)

        button = Button(text="How Difficult Is it?", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.function = 'howDifficultWeighted'
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=miscChartRoll)
        dungeonMainBox.add_widget(button)

        dungeonMainBox.add_widget(Label(text='What\'s Do I See?', size_hint=(1,.1), font_size=config.basefont90))
        
        button = Button(text="Monster, Treasure, Trap?", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.function = 'getRoomContents'
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=miscChartRoll)
        dungeonMainBox.add_widget(button)
        
        button = Button(text="Trap?", background_normal='', size_hint=(1,.1), background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.function = 'getTrapStatus'
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=miscChartRoll)
        dungeonMainBox.add_widget(button)

        dungeonSpecialBox = GridLayout(cols=2, size_hint=(1,.20))
        
        button = Button(text="First Impression", background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.qty = 99
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=getSpecialFeature)
        dungeonSpecialBox.add_widget(button)

        button = Button(text="Single Item", background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.qty = 1
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=getSpecialFeature)
        dungeonSpecialBox.add_widget(button)
        
        dungeonMainBox.add_widget(dungeonSpecialBox)
        
        button = Button(text="What Did It Do?", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.function = 'whatDidItDo'
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=miscChartRoll)
        dungeonMainBox.add_widget(button)
        
        button = Button(text="Make A Saving Throw", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.function = 'makeASavingThrow'
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=miscChartRoll)
        dungeonMainBox.add_widget(button)
        
        dungeonMainBox.add_widget(Label(text='Node Dungeon', size_hint=(1,.10), font_size=config.basefont90))
        
        dungeonNodeBox = GridLayout(cols=3, size_hint=(1,.10))
        
        button = Button(text="New Theme", background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=getDungeonAreaTheme)
        dungeonNodeBox.add_widget(button)

        button = Button(text="New Type", background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=getDungeonAreaType)
        dungeonNodeBox.add_widget(button)
        
        button = Button(text="New Activity", background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=getDungeonAreaActivityLevel)
        dungeonNodeBox.add_widget(button)
        
        dungeonMainBox.add_widget(dungeonNodeBox)
        
        self.nextAreaButton = Button(text="Next Area", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont', disabled=True)
        self.nextAreaButton.self = self
        self.nextAreaButton.bind(on_press=self.pressGenericButton)
        self.nextAreaButton.bind(on_release=getFullDungeonArea)
        dungeonMainBox.add_widget(self.nextAreaButton)
        
        # dungeon spinner for saving/loading
        self.dungeonSpinner = Spinner(
        text='None',
        values=[],
        background_normal='',
        background_color=accent1,
        background_down='',
        background_color_down=accent2,
        size_hint=(1,.20),
        )
        self.dungeonSpinner.self = self
        self.dungeonSpinner.bind(text=changeDungeonArea)
        dungeonMainBox.add_widget(self.dungeonSpinner)
        
        button = Button(text="New Dungeon", size_hint=(1,.10), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=newDungeonArea)
        dungeonMainBox.add_widget(button)
        
        dungeonMainBox.add_widget(Label(text='Diagram Mapping', size_hint=(1,.10), font_size=config.basefont90))

        button = Button(text="What Direction?", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.function = 'whatDirection'
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=miscChartRoll)
        dungeonMainBox.add_widget(button)

        button = Button(text="What Is The Room Like?", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.function = 'roomLike'
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=miscChartRoll)
        dungeonMainBox.add_widget(button)

        button = Button(text="What Is The Passage like?", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.function = 'passageLike'
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=miscChartRoll)
        dungeonMainBox.add_widget(button)

        dungeonMainBox.add_widget(Label(text="Grid Mapping", size_hint=(1,.10), font_size=config.basefont90))

        button = Button(text="Get Grid Room Pattern", size_hint=(1,.10), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=getGridRoomPattern)
        dungeonMainBox.add_widget(button)

        button = Button(text="Get Grid Corridor Pattern", size_hint=(1,.10), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=getGridCorridorPattern)
        dungeonMainBox.add_widget(button)

        button = Button(text="Get Grid Exits", size_hint=(1,.10), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=getGridExits)
        dungeonMainBox.add_widget(button)

        self.dungeonAItem.add_widget(dungeonMainBox)

        return self.dungeonAItem

#---------------------------------------------------------------------------------------------------
# dungeoncrawl & wilderness panel button functions
#---------------------------------------------------------------------------------------------------

def miscChartRoll(*args):
    args[0].background_color = neutral
    self = args[0].self
    result = eval(args[0].function)()
    updateCenterDisplay(self, result)

def moreOrLessRoll(*args):
    args[0].background_color = neutral
    self = args[0].self
    text = "expected"
    if len(self.textInput.text) > 0:
        text = self.textInput.text

    result = morelessWeighted(text)
    updateCenterDisplay(self, result)
    self.textInput.text = ""

#---------------------------------------------------------------------------------------------------
# --> miscellaneous
#
#---------------------------------------------------------------------------------------------------

def newDungeonArea(button):
    
    self = button.self
    button.background_color = neutral
    
    current_dungeon_name = self.textInput.text
    if current_dungeon_name == "":
        current_dungeon_name = "Dungeon " + str(len(config.user['saved_dungeons']))

    self.dungeonSpinner.values = self.dungeonSpinner.values + [current_dungeon_name]
    config.user["current_dungeon_name"] = current_dungeon_name
    config.user['saved_dungeons'][current_dungeon_name] = []
    self.dungeonSpinner.text = current_dungeon_name
    
    self.nextAreaButton.disabled = False
    
def getFullDungeonArea(button):
    
    self = button.self
    button.background_color = neutral
    
    current_dungeon_name = config.user["current_dungeon_name"]
    past_dungeon_areas = config.user['saved_dungeons'][current_dungeon_name]
    
    if len(past_dungeon_areas) > 0:
        current_theme = past_dungeon_areas[-1][0]
        current_type = past_dungeon_areas[-1][1]
        current_activity = past_dungeon_areas[-1][2]
    
    else:
        current_theme = random.choice(config.user['dungeon_area_themes'])
        current_type = random.choice(config.user['dungeon_area_types'])
        current_activity = random.choice(config.user['dungeon_area_activity_level'])
    
    backtrack_chance = config.user['backtrack_chance']
    dungeon_theme_randomness = config.user['dungeon_theme_randomness']
    dungeon_type_randomness = config.user['dungeon_type_randomness']
    dungeon_activity_randomness = config.user['dungeon_activity_randomness']
    
    room_count = str(random.randint(1, 4) * 2)

    backtrack_roll = random.randint(1, 100)
    
    theme_change_roll = random.randint(1, 100)
    type_change_roll = random.randint(1, 100)
    activity_change_roll = random.randint(1, 100)
    
    # is this area the same type as the last?
    if theme_change_roll <= dungeon_theme_randomness:
        possible_themes = random.sample(config.user['dungeon_area_themes'], 2)
        if possible_themes[0] != current_theme:
            new_theme = possible_themes[0]
        else:
            new_theme = possible_themes[1]
    else:
        new_theme = current_theme
        
    if type_change_roll <= dungeon_type_randomness:
        possible_types = random.sample(config.user['dungeon_area_types'], 2)
        if possible_types[0] != current_type:
            new_type = possible_types[0]
        else:
            new_type = possible_types[1]
    else:
        new_type = current_type
        
    if activity_change_roll <= dungeon_activity_randomness:
        possible_activity = random.sample(config.user['dungeon_area_activity_level'], 2)
        if possible_activity[0] != current_activity:
            new_activity = possible_activity[0]
        else:
            new_activity = possible_activity[1]
    else:
        new_activity = current_activity
        
    # now, see if the new stuff takes effect or if we're going back to an existing area        
    if backtrack_roll <= backtrack_chance and len(past_dungeon_areas) > 1:
        index = random.randint(0, len(past_dungeon_areas)-1)
        new_theme = past_dungeon_areas[index][0]
        new_type = past_dungeon_areas[index][1]
        new_activity = past_dungeon_areas[index][2]
        result = "[Area] You've found a connection to an already explored area. Type: " + new_type + " (" + new_theme + ", " + new_activity + ") [" + str(index+1) + "]. You can explore " + room_count + " more rooms in the old area or continue into a new area."
    else:
        past_dungeon_areas.append([new_theme, new_type, new_activity])
        new_area = new_type + " (" + new_theme + ", " + new_activity + ")"
        result = "[Area] " + new_area + " [" + str(len(past_dungeon_areas)) + "]" + "." + " Explore " + room_count + " rooms, then roll again."
        config.user['dungeon_index'] = -1
        
    updateCenterDisplay(self, result, 'result')
    
def getDungeonAreaTheme(button):
    
    self = button.self
    button.background_color = neutral
    
    theme = random.choice(config.user['dungeon_area_themes'])
    result = "[Area Theme] " + theme + "."
    updateCenterDisplay(self, result, 'result')
    
def getDungeonAreaType(button):
    self = button.self
    button.background_color = neutral
    
    theme = random.choice(config.user['dungeon_area_types'])
    result = "[Area Type] " + theme + "."
    updateCenterDisplay(self, result, 'result')

def getDungeonAreaActivityLevel(button):
    self = button.self
    button.background_color = neutral
    
    theme = random.choice(config.user['dungeon_area_activity_level'])
    result = "[Area Activity] " + theme + "."
    updateCenterDisplay(self, result, 'result')
    
def changeDungeonArea(spinner, value):
    
    self = spinner.self

    past_dungeon_areas = config.user['saved_dungeons'][value]
    config.user["current_dungeon_name"] = value
    
    new_area = "Dungeon is now ... " + config.user['current_dungeon_name'] + ". "
    if len(past_dungeon_areas) > 0:
        new_theme = past_dungeon_areas[-1][0]
        new_type = past_dungeon_areas[-1][1]
        new_activity = past_dungeon_areas[-1][2]
        new_area = new_area + "Current area is " + new_type + " (" + new_theme + ", " + new_activity + ")" + " [" + str(len(past_dungeon_areas)) + "]" + "."
    
    updateCenterDisplay(self, new_area, 'result')

def getDungeonSetPiece(button):
    pass

def howDifficultWeighted():

    rolls = [random.randint(1,4), random.randint(1,4)]
    maxroll = max(rolls)
    minroll = min(rolls)

    diff = rolls[0] - rolls[1]
    chart = {
        -3 : "Trivial.",
        -2 : "Fairly easy.",
        -1 : "A bit easy.",
         0 : "On par with hero's abilities.",
         1 : "A bit difficult.",
         2 : "Fairly difficult.",
         3 : "Overwhelming.",
    }

    result = "[How Difficult?] " + chart[diff] + " [" + str(diff) + "]"
    return result

def morelessWeighted(text="expected"):

    chart = {
        2 : "Much less than ",
        3 : "Less than ",
        4 : "A bit less than ",
        5 : "As ",
        6 : "A bit more than ",
        7 : "More than ",
        8 : "Much more than ",
    }

    roll = random.randint(1,4) + random.randint(1,4)

    result = "[More or Less] " + chart[roll] + text + "."
    return result

def whatDirection():

    chart = {
        1 : "North or Up",
        2 : "Northeast",
        3 : "East or Right",
        4 : "Southeast",
        5 : "South or Down",
        6 : "Southwest",
        7 : "West or Left",
    }

    roll = random.randint(1,7)

    result = "[Direction] " + chart[roll] + ". If this direction won't work, use up or down."
    return result

def roomLike():

    oppositesChart = [
        ["rough", "smooth"],
        ["gleaming", "dull"],
        ["slick", "dry"],
        ["crumbling", "intact"],
        ["extreme", "mild"],
        ["cared for", "disused"],
        ["stone", "metal"],
        ["wood", "brick"],
        ["wood", "metal"],
        ["stone", "brick"],
        ["painted", "bare"],
        ["finished", "unfinished"],
        ["ostentatious", "spartan"],
        ["bare", "stuffed"],
        ["worn", "new-looking"],
        ["expansive", "miserly"],
        ["lavish", "spare"],
        ["bright", "dim"],
        ["pristine", "dirty"],
        ["faded", "vibrant"],
        ["slippery", "sticky"],
        ["broken", "unmarred"],
    ]
    descChart = []
    for pairList in oppositesChart:
        descChart.append(random.choice(pairList))

    roll = random.randint(1, 3)
    descList = random.sample(descChart, roll)
    desc = ', '.join(descList)

    shapeChart = [
        "round", "square", "oval", "elongated", "rectangular", "trapezoidal",
    ]

    roll = random.choice([1,1,1,2])
    shapeList = random.sample(shapeChart, roll)
    shape = ', '.join(shapeList)

    sizeChart = [
        "large", "small", "average", "standard", "medium", "cubby", "alcove", "cavern", "nook", "chamber", "vault", "great", "negligible", "brief", "vast", "expansive", "extensive", "double-size",
    ]
    size = random.choice(sizeChart)

    purposeChart = [
        "sleeping", "eating", "bathing", "bodily functions", "imprisoning", "killing", "disposal", "studying", "reading", "working", "crafting", "disassembling", "assembling", "interrogating", "relaxing", "recuperating", "mending", "rending", "cooking", "exercise", "planning", "plotting", "praying", "keeping", "displaying", "storing", "feasting", "resting", "meditating", "confining", "stashing", "protecting"
    ]

    roll = random.choice([1,2])
    purposeList = random.sample(purposeChart, roll)
    purpose = ', '.join(purposeList)

    result = "[Room] " + desc + " [Purpose] " + purpose + " [Size] " + size + " [Shape] " + shape
    return result

def passageLike():

    veerChart = ["continues straight", "ends abruptly", "winds left", "winds right", "sharp bend left", "sharp bend right", "slopes up or passes stairs", "slopes down or passes stairs", "doubles back"]

    veer = random.choice(veerChart)

    extrasChart = {
        2 : "nothing",
        3 : "an intersection",
        4 : "a side passage",
        5 : "nothing",
        6 : "a exit or arch or gap in the wall",
        7 : "special",
        8 : "nothing",
    }

    roll = random.randint(1,4) + random.randint(1,4)
    extras = extrasChart[roll]

    specialChart = [
        "obstacle blocking path", "water", "pit", "chasm or stairs", "skylight or light source", "treasure", "useful item", "stairs", "shaft"
    ]
    if extras == "special":
        extras = random.choice(specialChart)

    result = "[Passage] " + veer + " [Special] " + extras
    return result

def getRoomContents():

    if config.general['dungeon_stocking_method'] == "Gygax":
        
        chart = { "Empty": 12, "Monster Only": 2, "Monster & Treasure": 3, "Special or Stairway": 1, "Trick/Trap": 1, "Treasure": 1 }

        contents = random.choice([k for k in chart for dummy in range(chart[k])])
        
        config.general['trap_status'] = "No."
        
        if contents == "Trick/Trap":
            config.general['trap_status'] = "Yes!"
            contents = "Empty"

    else:
        
        chart = { "Monster": 2, "Trap": 1, "Special": 1, "Empty" : 2 }
        contents = random.choice([k for k in chart for dummy in range(chart[k])])

        troll = random.randint(1,6)

        treasure = ""
        if contents == "Monster" and troll <= 3:
            treasure = "Treasure!"
        elif contents == "Trap" and troll <= 2:
            treasure = "Treasure!"
        elif contents == "Empty" and troll == 1:
            treasure = "Treasure!"
        else:
            treasure = "No Treasure!"

        config.general['trap_status'] = "No."
        if contents == "Trap":
            config.general['trap_status'] = "Yes!"
            contents = "Empty"
        
        contents = contents + ". " + treasure

    return "[Room Contents] " + contents

def getTrapStatus():
    
    trap = config.general['trap_status']
    config.general['trap_status'] = random.choice(["Yes!", "No."])
    
    return "[Is There a Trick or Trap?] " + trap
             
def makeASavingThrow():
             
    saveChart = config.user['saving_throws']
    if len(saveChart) == 0:
        saveChart =  [ "Poison", "Death", "Breath", "Magic", "Dexterity", "Constitution", "Luck", "Wisdom" ]
    
    return "[Roll] Saving throw vs. " + random.choice(saveChart)
             
def whatDidItDo():
    
    # generic effects that can be changed or removed only        
    effectSub = [ "changed", "reversed", "removed", "increased", "reduced"]
    targetSub = [ "one of your stats (roll a \"Defining Attribute\")", "an aspect of your alignment or morality", "part of your personality (roll a \"Defining Characteristic\")", "your gender", "your libido", "one of your emotions regarding someone else", "one of your preferences", "one of your desires", "one of your weaknesses", "one of your strengths", "your appeal to others of your species", "your appeal to others of the opposite sex", "your judgement", "your race or species" ]
    
    effects = [x + " " + y for x in effectSub for y in targetSub ]

    # unique effects
    singles = [ "removes one of your possessions", "adds an item to your inventory", "denatures a magical item you are carrying", "imbues an item you are carrying with a magical effect", "makes you think you're a monster", "drives you mad with emotion (roll on \"Reaction: Negative\")", "drives you mad with emotion (roll on \"Reaction: Positive\")", "teleported you somewhere else", "dyed your skin an unusual color", "poisoned you", "made you taller", "shrank you", "filled the room with gas", "transformed you into a monster", "transformed you into an animal", "took away your memory", "took a memory that was important to you", "geased you", "bestowed a spell like ability on you", "bestowed the effects of a first level spell on you", "bestowed the effects of a second level spell on you", "bestowed the effects of a third level spell on you", "bestowed the effects of a fourth level spell on you", "bestowed the effects of a fifth level spell on you", "bestowed a nearby monster's spell-like ability on you", "swapped your mind with that of a creature nearby", "made you a werecreature", "called forth your own personal guardian spirit to haunt you", "gave you the memories of someone else in addition to your own", "showed you a vision of somewhere else", "showed you a vision of your own likely future", "taught you the True Name of someone very powerful", "implanted a powerful urge or compulsion", "endowed you with the last lingering knowledge of a lost arcane tradition", "tattooed a map on your skin", "tattooed a prophecy on your skin", "tattooed an arcane ritual on your skin", "infused you with the essence of an extraplanar creature", "has the same effects as a love potion", "puts you into a deep sleep that resembles death", "makes you irresistable to a nearby type of monster", "removes your ability to lie", "removes your ability to tell the truth", "curses you to become a monster if you engage in carnal activity", "curses you to kill the one you love", "curses you with great luck while everyone around you suffers misfortune", "blesses you with luck", "blesses you with fertility", "blesses those you touch with fertility", "blesses you with great health", "blesses those you touch with great health", "blesses you with longevity", "reduces your age by one category", "reduces your age by two categories", "reverts you physically to childhood", "grants you the ability to speak with fish", "grants you the ability to speak with animals", "grants you the ability to speak with birds", "grants you the ability to speak with reptiles", "grants you the ability to speak to plants", "grants you the ability to see and converse with the dead", "curses you to see and hear the dead, often mistaking them for the living", "grants you the ability to speak a random language", "strikes you blind", "makes you extremely drunk", "makes you mildly tipsy", "heals you", "makes you immune to disease", "removes your need to sleep", "curses you with nightmares", "made everyone you know forget you", "made you insubstantial", "gave you incredible arcane knowledge that you can't use but others will want to dig out of your head", "gave you a minor psychic quirk", "has linked you to someone else emotionally and physically; from now on you feel what they feel and vice versa", "gave you the ability to use a mage cantrip as if you were a mage", "turned you into a sentient tool that best represents your skills", "gives you the ability to see in the dark", "makes you appear to be something you're not", "made you fall in love with someone even if they're not here", "showed you a vision of your one true love", "showed you the truth of some deeply cherished belief", "showed you the truth of a painful memory", "causes hallucinations", "summons a creature to grant you a wish", "grants you a wish to the best of its ability but it is kind of dim", "grants you a wish in good faith", "bestows upon you the ability to always find a way to indulge yourself in a weakness", "bestows upon you the knowledge of the high priest of a dead god", "injects a spirit into your mind; when you sleep the spirit takes over", "merges you with a person held in stasis", "transforms half of you", "curses you to transform into a generic version of whatever living non-insect creature you first touch after sunset each night", "swaps your heart for a mystical gem that someone wants back", "grants you the ability to turn into flame at will; you will now do this involuntarily when startled or extremely excited", "implants a series of nightmares about a long-ago tragedy into your subconscious", "gives you a vision of a terrifying, world-shattering danger approaching", "rewires a bit of your mind; you gain an odd quirk and the ability to see auras", "marks you as the Chosen One; this may or may not be relevant to anything", "causes you to black out and then puppets your body to achieve some purpose (use the \"Backstory\" generator to see what happened during the black out)", "shows you a vision of a great treasure and how to find it" ]
    
    chart = singles + effects + config.user['what_did_it_do_effects']
    if config.user['what_did_it_do_effects_merge'] == "user" and len(config.user['what_did_it_do_effects_merge']) >= config.user['max_effects']:
        chart = config.user['what_did_it_do_effects']
    
    count = 1
    if random.randint(1,100) <= config.user['chance_of_multiple_effects']:
        count = random.randint(1,config.user['max_effects'])
    
    result = random.sample(chart, count)
    
    awareChart = [ "don't realize at first that something's happened", "don't notice anything amiss", "know immediately that something's wrong", "feel strange", "suffer a vision", "don't realize at first that something's happened", "don't notice anything amiss", "know immediately that something's wrong", "feel strange", "suffer a vision", "don't realize at first that something's happened", "don't notice anything amiss", "know immediately that something's wrong", "feel strange", "suffer a vision", "know immediately the effects", "know the effects and the ramifications", "know one of the effects immediately but not the other (if there's only one effect, push this button again and take all the results from that too)", "are protected from any consequences as long as you maintain the rules of the people who created the effect", "won't be affected until you wake up from your next sleep or see your next sunrise", "won't be affected until you next commit an act related to the effect", "won't be affected until you commit a sin", "will pass the effect to the next person you touch, curing you", "are contagious like a disease; people you touch must save or contract the effect(s) as well", "are knocked unconscious", "know that it's not all bad (use this generator until you get at least one positive effect and combine with your original one)", "are given a chance to change your fate (use this generator once more, then pick which of the results you like best)", "are caught at the epicenter of a magical vortex (get an effect for each person in the room and one more effect for yourself)", "suffer the same fate as your comrades (everyone present shares the same effect you do)", "start convulsing as multiple magical effects take effect (use this generator 1d6+1 more times and take all the results from those rolls too)" ]

    return "[What Did It Do?] It " + ' and it '.join(result) + ". You " + random.choice(awareChart) + "."
             
def getSpecialFeature(button, *args):

    button.background_color = neutral
    qty = button.qty
    self = button.self

    if qty > 1:
        qty = random.randint(1,3)

    chart = ["strange glyphs", "blacksmith tools and forge", "an old wagon", "grates in the wall along the floor", "grates up high near the ceiling", "an adventurer's discarded pack", "broken furniture", "an adventuring party", "phosphorescent lichen", "a sprung trap", "a spring", "a river or stream", "a trickle of water", "a lake or pool", "a draft from somewhere", "wine casks", "barrels", "smoke", "murals on the walls", "a dire warning", "cages", "a statue", "an unconscious person", "a person in stasis", "a petrified statue", "an altar", "glowing mushrooms", "a weapon rack", "an armor rack", "a pile of refuse", "a pile of rubble", "a fallen pillar", "a vat of liquid", "round smooth crystals embedded in the floor", "a lichen. mold, and fungi farm", "a fountain", "a pile of books", "webs", "an imprisoned demon", "footprints in the dust", "faded banners and pennants", "a throne", "a body with crude challenge on it", "scavengers feeding on a corpse", "a balcony or ledge", "a coffin", "a shattered brick arch with stone behind it", "one of the floor slabs is loose", "a faded mosaic on the floor", "a smashed mirror", "a skull", "a pedestal", "misspelled graffiti", "articulate scrawling", "a fissure a foot wide", "an iron brazier", "a row of manacles", "a weathered journal", "an iron cage suspended from the ceiling", "a grate in the floor", "shadowy alcoves", "a dark niche", "a shrine", "several shrines", "a painting face down on the floor", "a dozen extremely well-wrought statues", "a wounded creature", "broken statues", "a pristine square of floor", "a number of piles of dirty hay and refuse", "a chest", "an ornate wardrobe", "an ornate desk", "an ornate bed", "a row of cots", "signs of an animal", "a sign", "a tiled floor", "a makeshift camp", "a stockpile", "a cauldron", "a hole in the wall", "a hole in the floor", "scratch marks on wall", "very cold", "very warm", "steps down to recessed area", "a rickety bridge", "something that gleams high up on the wall", "twisted wreckage", "a hole in the ceiling", "stairs", "a ladder", "a tree", "an immediately detectable overt magical effect", "a sudden chill in the air", "a blast of heat", "a fire", "spoor", "a discarded lunch", "a blood stain", "blood spatter", "a makeshift alchemy lab", "a pile of alchemical cast-off items", "a discarded backpack", "a torn and battered satchel", "a round sphere hovering in mid-air", "a crystal ball", "cards scattered on the floor", "clothes scattered on the floor", "a tangle of armor and weapons and bones", "bones", "armor", "weapons", "a weapon", "grass", "the sun", "a will-o-wisp", "a bowl of fruit", "a basket", "an esoteric theorum", "glowing runes", "a bucket", "the scent of soft perfume", "a posed diorama", "bones sorted by type", "artfully arranged body parts", "art pieces on display", "numerous pedestals and alcoves", "a pattern of nails in the wall", "furniture", "refuse", "a nest", "a sleeping pallet", "a camp", "a person in a trap", "a person who is stuck", "a monster who is stuck", "a monster in a trap", "a wounded monster", "someone who is occupied", "the floor is wet", "the floor is slippery", "there's a narrow ledge", "a coffin; something is banging on the inside of the lid", "a golem that appears to be half-buried in the floor", "a sack", "a box", "an iron-banded chest", "a rusty metal box", "a wooden crate with the lid nailed on", "a leather satchel", "a pile of provisions", "a suit of armor", "a destroyed camp", "a make-shift shrine", "a mosaic on the ceiling", "a gallery of paintings", "a faceless statue", "a golem made of unusual materials", "a book", "a pile of scrolls", "a stack of books", "a shattered iron cage", "a handful of brass tacks", "a waterfall", "glass stairs", "a large mirror", "a painting that takes up the entire wall", "a row of jars", "a bed", "a hammock", "a tent", "the remains of a bloody conflict", "corpses strewn about", "corpses hung on hooks", "torture devices", "a bloodstained table", "a butcher block", "a pile of rusty metal",  ]

    chart = chart + config.user['special_features']
        
    special = random.sample(chart, qty)

    result = "[In the Room] " + ", ".join(special)

    updateCenterDisplay(self, result)

def getGridRoomPattern(*args):

    args[0].background_color = neutral
    self = args[0].self

    result = ""
    pattern = 0
    start = 1
    end = 0
    exits = []
    group = []
    graphic = "\n\n"
    lines = random.randint(1,6) + random.randint(1,6)

    for depth in range(1, lines):
        if depth == 1:
            maxwidth = random.randint(1,4) + random.randint(1,4)
            end = maxwidth
            graphic = graphic + ("* " *(maxwidth+2))

        repeat = random.randint(1,100)

        if pattern == 4 and repeat >= 10:
            result = result + "\n" + str(depth) + ": " + ", ".join(mark)
        elif pattern == 5 and repeat >= 50:
            result = result + "\n" + str(depth) + ": " + str(start) + " to " + str(end)
        elif pattern > 0 and repeat >= 50 and pattern != 4:
            result = result + "\n" + str(depth) + ": " + str(start) + " to " + str(end)
        else:
            pattern = random.randint(1,7)
            if pattern <= 3:
                end = random.randint(start, maxwidth)
                result = result + "\n" + str(depth) + ": " + str(start) + " to " + str(end)
            elif pattern == 4:
                mark = []
                group = random.sample(range(maxwidth), random.randint(start,maxwidth))
                group.sort()
                end = -9
                start = 1
                for item in group:
                    if item > 0:
                        mark.append(str(item))
                result = result + "\n" + str(depth) + ": " + ", ".join(mark)
            elif pattern == 5:
                roll1 = random.randint(start,maxwidth)
                roll2 = random.randint(start,maxwidth)
                if roll1 == roll2:
                    roll2 = roll2 + 1
                end = max(roll1, roll2)
                start = min(roll1, roll2)
                result = result + "\n" + str(depth) + ": " + str(start) + " to " + str(end)
            else:
                start = 1
                end = maxwidth
                result = result + "\n" + str(depth) + ": " + str(start) + " to " + str(end)

        gline = ""
        for i in range(maxwidth+2):
            if end != -9:
                if i < start or i > end:
                    gline = gline + "* "
                else:
                    gline = gline + "X "
            else:
                if i in group and i > 0:
                    gline = gline + "X "
                else:
                    gline = gline + "* "

        graphic = graphic + "\n" + gline

    graphic = graphic + "\n" + ("* " *(maxwidth+2))

    result = "[Grid Room] " + graphic

    updateCenterDisplay(self, result)

def getGridCorridorPattern(*args):

    args[0].background_color = neutral
    self = args[0].self

    pattern = []
    intersection = []

    for i in range(1,10):
        pattern.append("1 by " + str(i))

    for i in range(2, 10):
        for x in range(1,10):
            intersection.append(", 1 by " + str(x) + " intersection at " + str(i))

    roll = random.randint(0, len(pattern)-1)
    base = pattern[roll]

    base = base + random.choice([", vertical", ", horizontal"])

    if roll > 1 and random.randint(1,100) > 80:
        base = base + random.choice(intersection)

    result = "[Corridor] " + base

    updateCenterDisplay(self, result)

def getGridExits(*args):

    args[0].background_color = neutral
    self = args[0].self

    result = ""

    roll = random.randint(0,5)

    chart = [ "North or Up", "East or Right", "South or Down", "West or Left",]

    exits = []
    for i in range(roll):
        exits.append(random.choice(chart))



    result = "[Exits] " + str(roll) + " " + ", ".join(exits)

    updateCenterDisplay(self, result)
