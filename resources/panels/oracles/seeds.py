# -*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------------------
#
# Seed Panel
#
##---------------------------------------------------------------------------------------------------
import imports
from imports import *
import config
import imp

def exclude():
    return False

def onEnter(self):
    l = ToggleButtonBehavior.get_widgets('default_seed')
    for checkbox in l:
        if config.general['seed_func'] == checkbox.func and config.general['seed_type'] == checkbox.type:
            checkbox.active = True
    del l
    pass

def initPanel(self):

    self.seedsAItem = AccordionItem(title='Seeds & Complex Answers', background_normal='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', background_selected='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', min_space = config.aiheight)

    self.seedsMainBox = BoxLayout(orientation='vertical')

    self.seedArray = []
    self.displayArray = []

    seedfiles = glob.glob("." + os.sep + "resources" + os.sep + "panels" + os.sep + "seeds" + os.sep + "*.py")

    for item in seedfiles:
        waste, filename = item.rsplit(os.sep, 1)
        filename, ext = filename.rsplit('_', 1)
        self.seedArray.append(filename)

    self.seedArray = list(set(self.seedArray))

    for item in self.seedArray:
        if len(item) > 10 and " " in item:
            self.displayArray.append(item[:20])
        else:
            self.displayArray.append(item)

    self.seedsMainBox.add_widget(Label(text="Verb Noun", size_hint=(1,.20)))

    self.seedsTwoPartGrid = GridLayout(cols=2)

    for seedpack in self.seedArray:

        index = self.seedArray.index(seedpack)

        # checkbox for making default
        checkbox = CheckBox(size_hint=(.10,1), height=config.baseheight, group='default_seed')
        checkbox.self = self
        checkbox.func = 'useTwoPartSeed'
        checkbox.type = seedpack
        checkbox.bind(active=setDefaultSeed)
        self.seedsTwoPartGrid.add_widget(checkbox)

        button = Button(text=self.displayArray[index], size_hint=(.90,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans', font_size=config.basefont90)
        button.self = self
        button.pack = seedpack
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=useTwoPartSeed)
        self.seedsTwoPartGrid.add_widget(button)

    self.seedsMainBox.add_widget(self.seedsTwoPartGrid)

    self.seedsTitleGrid = GridLayout(cols=3, size_hint=(1,.15))
    self.seedsTitleGrid.add_widget(Label(text=" ", size_hint=(.10,1)))
    self.seedsTitleGrid.add_widget(Label(text="Description", size_hint=(.45,1)))
    self.seedsTitleGrid.add_widget(Label(text="Action", size_hint=(.45,1)))
    self.seedsMainBox.add_widget(self.seedsTitleGrid)

    self.seedsThreePartGrid = GridLayout(cols=3)

    for seedpack in self.seedArray:

        index = self.seedArray.index(seedpack)

        # checkbox for defaults
        checkbox = CheckBox(size_hint=(.10,1), height=config.baseheight, group='default_seed')
        checkbox.self = self
        checkbox.func = 'useThreePartSeed'
        checkbox.type = seedpack
        checkbox.bind(active=setDefaultSeed)
        self.seedsThreePartGrid.add_widget(checkbox)

        button = Button(text=self.displayArray[index], size_hint=(.45,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans', font_size=config.basefont80)
        button.self = self
        button.subtype = "adjective"
        button.pack = seedpack
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=useThreePartSeed)
        self.seedsThreePartGrid.add_widget(button)

        button = Button(text=self.displayArray[index], size_hint=(.45,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans', font_size=config.basefont80)
        button.self = self
        button.subtype = "verb"
        button.pack = seedpack
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=useThreePartSeed)
        self.seedsThreePartGrid.add_widget(button)

    self.seedsMainBox.add_widget(self.seedsThreePartGrid)

    self.seedsMainBox.add_widget(Label(text="Adverb Adjective Verb Noun", size_hint=(1,.20)))

    self.seedsAllGrid = GridLayout(cols=2)

    for seedpack in self.seedArray:

        index = self.seedArray.index(seedpack)

        checkbox = CheckBox(size_hint=(.10,1), height=config.baseheight, group='default_seed')
        checkbox.self = self
        checkbox.func = 'useAllSeed'
        checkbox.type = seedpack
        checkbox.bind(active=setDefaultSeed)
        self.seedsAllGrid.add_widget(checkbox)

        button = Button(text=self.displayArray[index], size_hint=(.90,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans', font_size=config.basefont90)
        button.self = self
        button.pack = seedpack
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=useAllSeed)
        self.seedsAllGrid.add_widget(button)

    self.seedsMainBox.add_widget(self.seedsAllGrid)

    self.seedsMainBox.add_widget(Label(text="What Is it?", size_hint=(1,.20)))

    self.seedsWhatGrid = GridLayout(cols=2)

    for seedpack in self.seedArray:

        index = self.seedArray.index(seedpack)

        checkbox = CheckBox(size_hint=(.10,1), height=config.baseheight, group='default_seed')
        checkbox.self = self
        checkbox.func = 'useWhatSeed'
        checkbox.type = seedpack
        checkbox.bind(active=setDefaultSeed)
        self.seedsWhatGrid.add_widget(checkbox)

        button = Button(text=self.displayArray[index], size_hint=(.90,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans', font_size=config.basefont90)
        button.self = self
        button.pack = seedpack
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=useWhatSeed)
        self.seedsWhatGrid.add_widget(button)

    self.seedsMainBox.add_widget(self.seedsWhatGrid)

    self.seedsAItem.add_widget(self.seedsMainBox)

    return self.seedsAItem

# simple function to let outside calls grab a two part result by passing two pos
def getTwo(typeA, typeB):

    item = config.general['seed_type']

    seedList = {'adverb' : [], 'adjective' : [], 'verb' : [], 'noun' : []}
    filename = "." + os.sep + "resources" + os.sep + "panels" + os.sep + "seeds" + os.sep + item

    for item in seedList:
        mod = filename + "_" + item + ".py"
        seedList[item] = imp.load_source(item, mod)

    # verb noun
    aList = seedList[typeA].chart[0]
    bList  = seedList[typeB].chart[0]

    result = random.choice(aList) + " " + random.choice(bList)
    return result

def setDefaultSeed(checkbox, value):

    self = checkbox.self

    # first, get all the needed information
    check_func = checkbox.func
    check_type = checkbox.type

    # update config variables
    config.general['seed_func'] = check_func
    config.general['seed_type'] = check_type

    config.general['seed_alt_func'] = check_func
    config.general['seed_alt_type'] = check_type

    if check_func != 'useThreePartSeed':
        config.general['seed_subtype_pretty'] = "Seed"
        config.general['seed_alt_func'] = ''
    else:
        config.general['seed_subtype_pretty'] = "Desc"

    # now remove or add complex buttons as needed
    try:
        if config.general['seed_alt_func'] == '':
            self.seedButtonsBox.remove_widget(self.seedAlternateButton)
            self.seedButtonsBox.size_hint_y=1
    except:
        pass

    try:
        if config.general['seed_alt_func'] != '':
            self.seedButtonsBox.add_widget(self.seedAlternateButton)
            self.seedButtonsBox.size_hint_y=2
    except:
        pass

    self.seedButton.text = config.general['seed_subtype_pretty'].capitalize()

# standard Mythic style "verb noun"
def useTwoPartSeed(*args):
    try:
        self = args[0].self
        args[0].background_color = neutral
        item = args[0].pack
    except:
        self = args[0]
        item = args[1]

    seedList = {'adverb' : [], 'adjective' : [], 'verb' : [], 'noun' : []}
    filename = "." + os.sep + "resources" + os.sep + "panels" + os.sep + "seeds" + os.sep + item

    for item in seedList:
        mod = filename + "_" + item + ".py"
        seedList[item] = imp.load_source(item, mod)

    # verb noun
    verbList = seedList['verb'].chart[0]
    nounList  = seedList['noun'].chart[0]

    result = random.choice(verbList) + " " + random.choice(nounList)

    updateCenterDisplay(self, "[Seed] " + result, 'oracle')

# Location Crafter style; one is adverb adjective, the other is verb noun.
def useThreePartSeed(*args):
    try:
        args[0].background_color = neutral
        self = args[0].self
        item = args[0].pack
        subtype = args[0].subtype
    except:
        self = args[0]
        item = args[1]
        subtype = args[2]

    seedList = {'adverb' : [], 'adjective' : [], 'verb' : [], 'noun' : []}
    filename = "." + os.sep + "resources" + os.sep + "panels" + os.sep + "seeds" + os.sep + item

    for item in seedList:
        mod = filename + "_" + item + ".py"
        seedList[item] = imp.load_source(item, mod)

    adjList =  seedList['adjective'].chart[0]
    verbList =  seedList['verb'].chart[0]
    nounList  =  seedList['noun'].chart[0]
    advList =  seedList['adverb'].chart[0]

    if subtype == "adjective":
        # adverb adjective
        adverb = random.choice(advList)
        adjective = random.choice(adjList)
        result = "[Seed] " + adverb + " " + adjective
    else:
        # verb noun
        verb = random.choice(verbList)
        noun = random.choice(nounList)
        result = "[Seed] " + verb + " " + noun

    updateCenterDisplay(self, result, 'oracle')

# just get one element from each available list, adverb adjective verb noun
def useAllSeed(*args):
    try:
        args[0].background_color = neutral
        self = args[0].self
        item = args[0].pack
    except:
        self = args[0]
        item = args[1]

    seedList = {'adverb' : [], 'adjective' : [], 'verb' : [], 'noun' : []}
    filename = "." + os.sep + "resources" + os.sep + "panels" + os.sep + "seeds" + os.sep + item

    for item in seedList:
        mod = filename + "_" + item + ".py"
        seedList[item] = imp.load_source(item, mod)

    result = random.choice(seedList['adverb'].chart[0]) + ", " + random.choice(seedList['adjective'].chart[0]) + ", " + random.choice(seedList['verb'].chart[0]) + " " + random.choice(seedList['noun'].chart[0])

    updateCenterDisplay(self, "[Seed] " + result, 'oracle')

# result is a thing with a description -- adjective noun
def useWhatSeed(*args):
    try:
        self = args[0].self
        args[0].background_color = neutral
        item = args[0].pack
    except:
        self = args[0]
        item = args[1]

    seedList = {'adverb' : [], 'adjective' : [], 'verb' : [], 'noun' : []}
    filename = "." + os.sep + "resources" + os.sep + "panels" + os.sep + "seeds" + os.sep + item

    for item in seedList:
        mod = filename + "_" + item + ".py"
        seedList[item] = imp.load_source(item, mod)

    adjectiveList =  seedList['adjective'].chart[0]
    nounList  =  seedList['noun'].chart[0]

    result = random.choice(adjectiveList) + " " + random.choice(nounList)

    updateCenterDisplay(self, "[Seed] " + result, 'oracle')
