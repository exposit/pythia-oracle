# -*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------------------
#
# PC Emulator Panel
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

    self.seedsAItem = AccordionItem(title='Seeds & Complex Answers', background_selected= os.sep + 'resources' + os.sep + "ui_images" + os.sep + 'invisible.png', min_space=config.aiheight)

    self.seedsMainBox = BoxLayout(orientation='vertical')

    self.seedsMainBox.add_widget(Label(text="Mythic Style", size_hint=(1,.15)))

    self.seedsTwoPartGrid = GridLayout(cols=2)

    self.seedArray = []

    seedfiles = glob.glob("." + os.sep + "resources" + os.sep + "panels" + os.sep + "seeds" + os.sep + "*.py")

    for item in seedfiles:
        waste, filename = item.rsplit(os.sep, 1)
        filename, ext = filename.rsplit('_', 1)
        self.seedArray.append(filename)

    self.seedArray = list(set(self.seedArray))

    for seedpack in self.seedArray:

        # checkbox for making default
        checkbox = CheckBox(size_hint_y=None, size_hint=(.10,.20), height=config.baseheight, group='default_seed')
        checkbox.self = self
        checkbox.func = 'useTwoPartSeed'
        checkbox.type = seedpack
        checkbox.bind(active=setDefaultSeed)
        self.seedsTwoPartGrid.add_widget(checkbox)

        button = Button(text=seedpack, size_hint=(.90,.20), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=useTwoPartSeed)
        self.seedsTwoPartGrid.add_widget(button)

    self.seedsMainBox.add_widget(self.seedsTwoPartGrid)

    self.seedsMainBox.add_widget(Label(text="Location Crafter Style", size_hint=(1,.15)))

    self.seedsTitleGrid = GridLayout(cols=3, size_hint=(1,.150))
    self.seedsTitleGrid.add_widget(Label(text="X", size_hint=(.10,1)))
    self.seedsTitleGrid.add_widget(Label(text="Description", size_hint=(.45,1)))
    self.seedsTitleGrid.add_widget(Label(text="Action", size_hint=(.45,1)))
    self.seedsMainBox.add_widget(self.seedsTitleGrid)

    self.seedsThreePartGrid = GridLayout(cols=3)

    for seedpack in self.seedArray:

        # checkbox for defaults
        checkbox = CheckBox(size_hint_y=None, size_hint=(.10,.20), height=config.baseheight, group='default_seed')
        checkbox.self = self
        checkbox.func = 'useThreePartSeed'
        checkbox.type = seedpack
        checkbox.bind(active=setDefaultSeed)
        self.seedsThreePartGrid.add_widget(checkbox)

        button = Button(text=seedpack, size_hint=(.45,.20), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans', font_size=config.basefont90)
        button.self = self
        button.subtype = "adjective"
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=useThreePartSeed)
        self.seedsThreePartGrid.add_widget(button)

        button = Button(text=seedpack, size_hint=(.45,.20), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans', font_size=config.basefont90)
        button.self = self
        button.subtype = "verb"
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=useThreePartSeed)
        self.seedsThreePartGrid.add_widget(button)

    self.seedsMainBox.add_widget(self.seedsThreePartGrid)

    self.seedsMainBox.add_widget(Label(text="One Big List", size_hint=(1,.15)))

    self.seedsAllGrid = GridLayout(cols=4)

    for seedpack in self.seedArray:

        checkbox = CheckBox(size_hint_y=None, size_hint=(.10,.20), height=config.baseheight, group='default_seed')
        checkbox.self = self
        checkbox.func = 'useAllSeed'
        checkbox.type = seedpack
        checkbox.bind(active=setDefaultSeed)
        self.seedsAllGrid.add_widget(checkbox)

        button = Button(text=seedpack, size_hint=(.90,.20), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=useAllSeed)
        self.seedsAllGrid.add_widget(button)

    self.seedsMainBox.add_widget(self.seedsAllGrid)

    self.seedsMainBox.add_widget(Label(text="What Is It?", size_hint=(1,.15)))

    self.seedsWhatGrid = GridLayout(cols=2)

    for seedpack in self.seedArray:

        checkbox = CheckBox(size_hint_y=None, size_hint=(.10,.20), height=config.baseheight, group='default_seed')
        checkbox.self = self
        checkbox.func = 'useWhatSeed'
        checkbox.type = seedpack
        checkbox.bind(active=setDefaultSeed)
        self.seedsAllGrid.add_widget(checkbox)

        button = Button(text=seedpack, size_hint=(.90,.20), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.self = self
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
        item = args[0].text
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
        item = args[0].text
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
        item = args[0].text
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
        item = args[0].text
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

    #updateCenterDisplay(self, "[" + string.capwords(item) + " What] " + result, 'oracle')
    updateCenterDisplay(self, "[Seed] " + result, 'oracle')

oldseedArray = {
    # general lists off the top of my head; pretty vanilla and bland
    'generic' : {
        'adjective' : ['peaceful', 'beautiful', 'kind', 'calm', 'stoic', 'meaningful', 'trivial', 'bland', 'spicy', 'fiesty', 'cruel', 'ugly', 'quarrelsome', 'paired', 'alone', 'edgy', 'endless', 'loved', 'loving', 'hated', 'hating', 'despised', 'secretive', 'open', 'stoic', 'veiled', 'plainspoken', 'honorable', 'dishonorable', 'trustworthy', 'untrustworthy', 'insane', 'clear', 'scary', 'calming'],
        'adverb' : ['likely', 'ruinously', 'hardly', 'ghostly', 'markedly', 'extremely', 'very', 'unlikely', 'open', 'closed', 'worse', 'better', 'freely', 'guardedly'],
        'verb' : ['accelerate', 'accumulate', 'acquire', 'adjust', 'adopt', 'advance', 'align', 'alter', 'anger', 'anticipate', 'assist', 'assume', 'bestow', 'carry', 'change', 'clarify', 'command', 'commit', 'conclude', 'consider', 'construct', 'control', 'convince', 'couple', 'determine', 'discover', 'disregard', 'divert', 'divide', 'draw', 'dream', 'edgy', 'educate', 'emphasize', 'enable', 'enchain', 'encourage', 'endless', 'enjoy', 'enrage', 'enter', 'entrance', 'eviscerate', 'examine', 'exchange', 'execute', 'exhaust', 'experience', 'facilitate', 'fascinate', 'feint', 'guess', 'impassion', 'improvise', 'inflame', 'inflate', 'interest', 'involve', 'justify', 'keep', 'ken', 'locate', 'loosen', 'lose', 'love', 'mend', 'mesmerize', 'motivate', 'murder', 'negotiate', 'nurture', 'obscure', 'overcome', 'penalize', 'quarter', 'question', 'refuse', 'reject', 'renegotiate', 'revenge', 'run', 'share', 'simplify', 'spy', 'squelch', 'stoic', 'strengthen', 'substitute', 'synthesize', 'teach', 'tighten', 'track', 'transition', 'trap', 'triumph', 'tumble', 'unify', 'unveil', 'weaken', 'withdraw'],
        'noun' : ['addiction', 'air', 'ally', 'armor', 'art', 'beyond', 'blood', 'bravery', 'change', 'class', 'cold', 'common', 'compassion', 'consumption', 'couple', 'cowardice', 'death', 'disaster', 'dispassion', 'displeasure', 'earth', 'earth', 'elements', 'emotions', 'enemy', 'fatigue', 'focus', 'foreign', 'forgiveness', 'freedom', 'friend', 'friendship', 'fury', 'future', 'grief', 'hatred', 'health', 'home', 'honor', 'hope', 'hot', 'ideas', 'illness', 'insanity', 'instinct', 'integrity', 'jewel', 'journey', 'joy', 'key', 'kin', 'location', 'love', 'luxuries', 'master', 'moderation', 'monster', 'moon', 'music', 'near', 'necessities', 'neighbor', 'obsession', 'passion', 'past', 'path', 'physical', 'possessions', 'power', 'priceless', 'quarry', 'quest', 'rain', 'reason', 'regret', 'reserves', 'rubbish', 'sex', 'shine', 'skill', 'sorrow', 'stalemate', 'star', 'status quo', 'stoicism', 'sun', 'survival', 'task', 'tool', 'trap', 'uncontrollable', 'unknowable', 'value', 'vengeance', 'violence', 'water', 'wealth', 'weapons', 'whimsy', 'work', 'veil', 'passage'],
        },
}
