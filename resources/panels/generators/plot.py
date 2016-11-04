# -*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------------------
#  plot panel
#
#
##---------------------------------------------------------------------------------------------------

import imports
from imports import *
import config

def exclude():
    return False

def onEnter(self):
    try:
        for i in range(len(config.general['monsters'])):
            self.monsterFields[i].text = config.general['monsters'][i]
    except:
        config.general['monsters'] = ["","","","","",""]

    try:
        self.actSpinner.text = config.general['current_sequence']
    except:
        pass

    try:
        self.resolveLabel.text = str(config.general['resolve'])
    except:
        config.general['resolve'] = 0

def initPanel(self):

        self.plotAItem = AccordionItem(title='Plot & Monsters', background_normal='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', background_selected='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', min_space = config.aiheight)

        plotMainBox = BoxLayout(orientation='vertical')

        plotMainBox.add_widget(Label(text="General Plotting", size_hint=(1,.10), font_size=config.basefont90))

        #story seed
        self.premiseList = ["Somebody wants something but can't...", "The decision to do something...", "When someone moves to...", "Can someone who just wants...", "Two rivals...", "Two separate people, two separate agendas.", "Obsession!", "Plan complete...", "The story is about..", "The hero is..."]

        self.premiseSpinner = Spinner(
        text='Plot Premise',
        values=self.premiseList,
        background_normal='',
        background_color=accent1,
        background_down='',
        background_color_down=accent2,
        size_hint=(1,.25),
        )
        self.premiseSpinner.self = self
        self.premiseSpinner.bind(text=getPlotPrompt)
        plotMainBox.add_widget(self.premiseSpinner)

        button = Button(text="Plot Web", size_hint=(1,.25), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=getPlotWeb)
        plotMainBox.add_widget(button)

        button = Button(text="Plot Move", size_hint=(1,.15), background_normal='',
         background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont', font_size=config.basefont90)
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=getPlotMove)
        plotMainBox.add_widget(button)

        # scriptwriting system
        plotMainBox.add_widget(Label(text="Scriptwriting Framework", size_hint=(1,.10), font_size=config.basefont90))

        plotPlayBox = BoxLayout(orientation='horizontal', size_hint=(1,.2))

        # current scene spinner
        self.actList = ['Status Quo', 'Plot Point: Inciting Incident', 'Predicament', 'Plot Point: Lock In', 'First Obstacle', 'Higher Obstacle', 'Plot Point: First Culmination', 'Subplot', 'Highest Obstacle', 'Plot Point: Main Culmination', 'New Tension', 'Plot Point: Twist', 'Resolution', 'Epilogue']

        self.actSpinner = Spinner(
        text='Status Quo',
        values=self.actList,
        background_normal='',
        background_color=accent1,
        background_down='',
        background_color_down=accent2,
        size_hint=(.6,1),
        )
        self.actSpinner.self = self
        self.actSpinner.bind(text=updateConfig)
        plotPlayBox.add_widget(self.actSpinner)

        # Resolve tracker
        button = Button(text="-", size_hint=(.1,1))
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=releaseResolveDown)
        button.self = self
        plotPlayBox.add_widget(button)

        self.resolveLabel = Label(text="0", size_hint=(.2,1))
        plotPlayBox.add_widget(self.resolveLabel)

        button = Button(text="+", size_hint=(.1,1))
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=releaseResolveUp)
        button.self = self
        plotPlayBox.add_widget(button)

        plotMainBox.add_widget(plotPlayBox)

        button = Button(text="Get A Scene", size_hint=(1,.15), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=getPlayScene)
        plotMainBox.add_widget(button)

        #multipart scene list
        plotMainBox.add_widget(Label(text="Scene List", size_hint=(1,.10), font_size=config.basefont90))

        plotSceneBox = BoxLayout(orientation='horizontal', size_hint=(1,.15))

        button = Button(text="Make List", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=makeSceneList)
        plotSceneBox.add_widget(button)

        button = Button(text="Get Element", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=getSceneElement)
        plotSceneBox.add_widget(button)

        plotMainBox.add_widget(plotSceneBox)

        plotMainBox.add_widget(Label(text="Monsters", size_hint=(1,.10), font_size=config.basefont90))

        plotMonsterBox = GridLayout(cols=2, size_hint=(1,2))

        self.monsterFields = []

        for i in range(0,6):
            field = TextInput(text="", size_hint=(.90, None), font_size=config.basefont80)
            field.background_color=neutral
            field.foreground_color=(1,1,1,1)
            field.self = self
            field.bind(focus=focusChangeMonster)
            self.monsterFields.append(field)
            plotMonsterBox.add_widget(field)

            button = Button(text="New", size_hint=(.10, None), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
            button.field = field
            button.self = self
            button.bind(on_press=self.pressGenericButton)
            button.bind(on_release=getMonster)
            plotMonsterBox.add_widget(button)

        plotMainBox.add_widget(plotMonsterBox)

        button = Button(text="Copy Monsters To Main", size_hint=(1,.15), background_normal='',
         background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont', font_size=config.basefont90)
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=copyMonstersToMain)
        plotMainBox.add_widget(button)

        button = Button(text="Clear Monsters", size_hint=(1,.15), background_normal='',
         background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont', font_size=config.basefont90)
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=clearMonsters)
        plotMainBox.add_widget(button)

        self.plotAItem.add_widget(plotMainBox)

        return self.plotAItem

#---------------------------------------------------------------------------------------------------
# plotcrawl & wilderness panel button functions
#---------------------------------------------------------------------------------------------------

def miscChartRoll(*args):
    args[0].background_color = neutral
    self = args[0].self
    result = eval(args[0].function)()
    updateCenterDisplay(self, result)

def getSceneElement(button, *args):
    button.background_color = neutral
    self = button.self
    try:
        if len(config.general['scenes']) == 0:
            result = "No scenes found -- generate more!"
        else:
            result = config.general['scenes'][0]
            config.general['scenes'].remove(result)
        updateCenterDisplay(self, "[Scene] " + result)
    except:
        pass

active_plot_subjects = []

plot_subject = ['a hero', 'the enemy', 'an ally', 'common folk', 'a fire', 'the strong', 'the weak', 'a castle', 'a spy', 'a reward', 'a punishment', 'a bargain', 'a promise', 'a disaster', 'a lover', 'a danger', 'a monster', 'magic', 'love', 'secret']
plot_object = ['progress', 'setback', 'destruction', 'creation', 'truth', 'falsity', 'love', 'hate', 'twist', 'awaken', 'a celebration', 'ruin', 'defilement', 'retreat']
plot_bridge = ['causes', 'is', 'is', 'is', 'regards', 'experience', 'of', 'against', 'undergoes', 'overcome', 'twists', 'to', 'ruins', 'makes']
plot_end = ['triumphs', 'lost', 'fails', 'overcomes', 'wins', 'continues unchanged', 'endures', 'flees', 'defeated', 'undefeated', 'destroyed']

def makeSceneList(button, *args):
    button.background_color = neutral
    self = button.self

    output = []
    plot = []
    count = 0

    plot = plot + activateNoun(plot)

    final = map(None, *plot)

    output = []
    for i in final:
        for x in i:
            if x not in output and x != None:
                output.append(x)

    config.general['scenes'] = output

def activateNoun(plot):

    choice = random.choice(plot_subject)

    plot = getPlotList(choice, plot)

    return plot

def getPlotList(choice, plot):

    active_plot_subjects.append(choice)
    matches = []

    for item in plot_subject + plot_object:
        for link in plot_bridge:
            matches.append(choice + " (" + link + ") " + item)

    rand_iter = random.randint(1,max(min(config.max_plot_elements, len(matches)-1), 1))
    rand_smpl = [ matches[i] for i in sorted(random.sample(xrange(len(matches)), rand_iter)) ]

    rand_smpl.append(choice + " " + random.choice(plot_end))

    plot.append(rand_smpl)

    new_words = [x for x in plot_subject if x not in active_plot_subjects]

    if len(active_plot_subjects) < config.max_plot_subjects:
        if len(new_words) > 0:
            new_word = random.sample(new_words,1)[0]
            if new_word not in active_plot_subjects:
                plot = plot + getPlotList(new_word, plot)
        else:
            new_word = random.sample(plot_subject, 1)[0]
            if new_word not in active_plot_subjects:
                plot = plot + getPlotList(new_word, plot)

    return plot

# inspired by Apocalypse World & Simple World
def getPlotMove(*args):
    self = args[0].self
    args[0].background_color = neutral
    chart = {
       2 : "Deal harm.",
       3 : "Trade harm for harm.",
       4 : "Put someone in a high-stakes situation.",
       5 : "Turn their move back on them.",
       6 : "Change the world away from the expected in a subtle way.",
       7 : "Add or remove an NPC from the current scene or area.",
       8 : "Use one of their prized things, skills, or traits against them.",
       9 : "Change something off-screen or in the future.",
      10 : "Give them a difficult decision to make or present a dilemma.",
      11 : "Manipulate, alter, rescue, or reveal someone physically, emotionally, or mentally.",
      12 : "Place an emotional, physical, mental, or other type of barrier in the way.",
    }

    roll = random.randint(1,6) + random.randint(1,6)
    result = chart[roll]

    result = "[Plot Move] " + result

    updateCenterDisplay(self, result, 'result')

def focusChangeMonster(field, value):
    if value:
        pass
    else:
        try:
            self = field.self
            index = self.monsterFields.index(field)
            config.general['monsters'][index] = field.text
        except:
            pass

def getMonster(button, *args):

    self = button.self
    button.background_color = neutral
    field = button.field

    result = ""

    traits = random.sample(["rapacious", "violent", "depraved", "perverse", "hungry", "miserable", "insane", "degenerate", "incestuous/inbred", "obsessive", "magical", "superior", "chimeric", "mutated", "greedy", "generous", "hateful", "loving", "out of element", "fearful", "brave", "kind", "cruel", "vengeful"], 2)

    subtype =  random.sample(["vermin", "humanoid", "demihuman", "automaton or elemental", "magical beast", "plant", "mindless undead", "sentient undead", "insect", "demon ", "abomination", "beast"], 3)

    intelligence = random.choice(["low ", "high ", ""]) + random.choice(["none", "animal", "animal", "intelligent", "intelligent"])

    special_abilities = random.sample(["hits really hard", "has multiple attacks", "armored", "regenerates", "damage reduction", "spell-like ability resembling 1st level spell", "spell-like ability resembling 2nd level spell", "spell-like ability resembling 3rd level spell", "petrification attack", "poison attack", "ability to become insubstantial or incorporeal", "extremely stealthy", "breath attack", "immunity", "stunning attack", "paralyzing attack", "death attack", "draining attack", "telepathic"], 2)

    hd = random.randint(1,12)
    num = random.randint(1,12)

    # now parse stuff
    if "superior" in traits:
        traits[traits.index('superior')] = "superior (" + random.choice(["Str", "Dex", "Con", "Int", "Wis", "Cha"]) + ")"

    basetype = subtype[0]
    if "chimeric" in traits:
        basetype = subtype[0] + "-" + subtype[1]
    if "mutated" in traits:
        traits[traits.index('mutated')] = "mutated (" + subtype[2] + ")"

    rroll = random.randint(1,6)
    if rroll <= 2:
        special_abilities = "None"
    elif rroll == 6:
        special_abilities = ', '.join(special_abilities)
    else:
        special_abilities = special_abilities[0]

    if "mindless" in basetype:
        intelligence = "None"

    result = basetype + " (" + str(num) + ") Int: " + intelligence + " HD: " + str(hd) + " Traits: " + ", ".join(traits) + " SA: " + special_abilities

    field.text = result

    index = self.monsterFields.index(field)

    config.general['monsters'][index] = result

def copyMonstersToMain(button, *args):
    self = button.self
    button.background_color = neutral

    count = 0
    for item in config.general['monsters']:
        count = count + 1
        if len(item) > 0:
            updateCenterDisplay(self, "[" + str(count) + "] " + item, 'result')

def clearMonsters(button, *args):
    self = button.self
    button.background_color = neutral

    config.general['monsters'] = ["","","","","",""]

    for i in range(len(config.general['monsters'])):
        self.monsterFields[i].text = config.general['monsters'][i]

def getPlotPrompt(spinner, value):

    self = spinner.self

    result = []

    descList = ['surly', 'attractive', 'beautiful', 'ugly', 'handsome', 'hideous', 'deformed', 'maimed', 'scarred', 'pleasant', 'kind', 'charming', 'unhappy', 'sensual', 'naive', 'friendly', 'unfriendly', 'wealthy', 'poor', 'profligate', 'miserly', 'miserable', 'pathetic', 'vicious', 'violent', 'excitable', 'greedy', 'compassionate', 'selfless', 'repressed', 'louche', 'dissipated', 'weak', 'strong', 'fearless', 'fearful', 'haunted', 'happy-go-lucky', 'capable', 'calm', 'insolent', 'regal', 'stern', 'tempermental', 'mercurial', 'enraged', 'angry', 'infuriated', 'sorrowful', 'grief-stricken', 'depressed', 'optimistic', 'passionate', 'free-spirited', 'intense', 'obsessive', 'choleric', 'stolid', 'complacent', 'arrogant', 'haughty', 'bold', 'reckless', 'determined', 'guarded', 'paranoid', 'trusting', 'untrustworthy', 'tactless', 'disillusioned', 'graceful', 'outspoken', 'taciturn', 'reclusive', 'withdrawn', 'traumatized', 'skillful']

    subjList = ['mage', 'necromancer', 'sorcerer', 'wizard', 'diviner', 'seer', 'oracle', 'hunter', 'forester', 'poacher', 'ranger', 'outlaw', 'bandit', 'thief', 'rogue', 'burglar', 'jewel thief', 'assassin', 'thug', 'second story man', 'highwayman', 'grave robber', 'archaeologist', 'anatomist', 'doctor', 'scientist', 'academic', 'teacher', 'professor', 'sage', 'psychic', 'astrologer', 'vizier', 'chancellor', 'nobleman', 'gentleman', 'king', 'prince', 'queen', 'princess', 'gentewoman', 'lady', 'knight', 'spirit', 'ghost', 'phantom', 'vampire', 'werewolf', 'monster', 'fighter', 'warrior', 'soldier', 'demon hunter', 'wanderer', 'traveler', 'maiden', 'lad', 'merchant', 'shopkeeper', 'innkeeper', 'traitor', 'hermit', 'warlord', 'sorceress', 'shaman', 'healer', 'priest', 'acolyte', 'monk', 'baron', 'duke', 'serf', 'peasant', 'bartender', 'harlot', 'spy', 'adventurer', 'cleric', 'bard', 'entertainer', 'dancer', 'singer', 'musician', 'actor', 'actress', 'playwright', 'blacksmith', 'tinker', 'barbarian', 'alchemist', 'crafter', 'artisan', 'artist', 'butler', 'servant', 'enforcer', 'mercenary', 'pilgrim', 'arcane dabbler', 'mystic', 'beast tamer', 'youth', 'maid', 'virgin', 'innocent', 'libertine', 'rake', 'innocent victim of a curse', 'deserving victim of a curse', 'criminal', 'escapee', 'archer', 'madman', 'deserter', 'renegade', 'outcast', 'demon', 'devil']

    objList = ['wealth', 'treasure', 'power', 'an artifact', 'love', 'a love interest', 'a person who hates them', 'youth', 'immortality', 'fame', 'a delicacy', 'a rarity', 'the downfall of a rival', 'the death of an enemy', 'the disposal of a henchman', 'the disposal of a blackmailer', 'the resolution of a private matter', 'a place to call home', 'a lover', 'carnal pleasures', 'a reason to live', 'a child', 'an heir', 'a prize in their field', 'a rival\'s treasure', 'peace', 'forgiveness', 'revenge', 'the revelation of a secret', 'the burying of a sin', 'the disposal of an enemy', 'the ruin of an enemy', 'the love of a friend', 'to know the truth', 'to build something of lasting value', 'to make the world a better place', 'to cure a terrible disease', 'to make their mark', 'transformation', 'to improve', 'to experience everything', 'to indulge', 'freedom', 'freedom for a loved one', 'freedom for all', 'freedom from oppression', 'hope', 'a light against encroaching darkness']

    obsList = ['fame', 'infamy', 'poverty', 'wealth', 'death', 'reputation', 'distance', 'age', 'omens', 'rivalry', 'a foe', 'the owner', 'traps', 'infirmity', 'past crimes', 'hidden secrets', 'vile perversions', 'dark secrets', 'a noble burden', 'a duty', 'a sacred vow', 'a blood oath', 'a familial duty', 'a desperate bargain']

    targetSub = ['foe', 'rival', 'prisoner', 'reluctant ally', 'willing accomplice', 'naive innocent', 'group of bystanders'] + subjList
    actSub = ['seduce', 'betray', 'enslave', 'trick', 'impress', 'capture', 'entrap', 'coerce', 'murder', 'discard', 'poison', 'taint', 'transform', 'sacrifice', 'test the mettle of', 'test the faith of']

    p = ' a '

    acts = [x + p + y for x in actSub for y in targetSub ]

    actList = ['hire a surrogate', 'hire a patsy', 'hire muscle', 'hire a scholar', 'set a trap', 'prepare an ambush', 'send for an ally', 'scheme spitefully', 'post a reward', 'strike quickly', 'wait it out', 'act under cloak of night', 'seize an advantage', 'research', 'investigate', 'drown sorrows', 'get lost in', 'go for an extended trip', 'weather the storm', 'make sacrifices', 'order reprisals', 'encourage a rival', 'destroy a powerful artifact', 'establish a center for learning', 'build something', 'answer a call to arms', 'fulfil a sacred duty', 'pursue vengeance', 'pursue love', 'make a desperate bargain', 'dispose of all witnesses', 'satisfy jaded tastes', 'survive at all costs']

    ingList = ['fleeing', 'fighting', 'enduring', 'hiding', 'resisting', 'seeking', 'pursuing', 'looking for', 'hunting', 'facing']
    ing = random.sample(ingList, 2)

    eveList = ['someone taking a bath', 'a betrayal', 'a wedding', 'a murder', 'a confession' 'a funeral', 'a meal between enemies', 'a romantic assignation', 'a natural disaster', 'someone chasing someone else', 'someone scolding someone else', 'someone watching an event unfold', 'a dramatic reveal', 'a covert flirtation at a fancy event', 'a scandal breaking', 'a trial', 'a pleasant surprise', 'an unpleasant surprise', 'a vicious attack', 'a fight to the death', 'a fight for survival', 'a birthday preparation', 'the discovery of a long-lost relative', 'the discovery of a long-lost ruin', 'the discovery of a long-lost heir', 'the return of a black sheep', 'the loss of innocence', 'a secretive tryst', 'a bold move', 'the gleeful destruction of a foe', 'humiliation', 'gardening', 'tending to the wounded', 'a voyage']

    objSub = ["to " + x for x in actList]

    desc = random.sample(descList, 3)
    subj = random.sample(subjList, 3)
    eve = random.sample(eveList, 3)

    obj = []
    for i in range(3):
        l = random.choice([objList, objList + objSub])
        obj.append(random.choice(l))

    obs = random.sample(obsList, 3)

    act = random.sample(actList + acts, 1) + random.sample(actList, 1) + random.sample(actList + acts, 1)

    actor = [ y + " " + x for y, x in zip(desc, subj)]

    for i in range(len(actor)):
        if actor[i][:1] in "a i e o u":
            actor[i] = "an " + actor[i]
        else:
            actor[i] = "a " + actor[i]

    result.append(actor[0].capitalize() + " wants " + obj[0] + " but can't have it because of " + obs[0] + ", so will " + act[0] + " in order to " + act[1] + ".")

    result.append("The decision to " + act[0] + " by " + actor[0] + " sparks " + actor[1] + " to " + act[1] + ". This hurts " + actor[2] + " who is " + ing[0] + " " + obj[0] + ".")

    result.append("When " + actor[0] + " moves to " + act[0] + " " + ing[0] + " " + obj[0] + ", " + actor[1] + " plans to " + act[1] + ".")

    result.append("Can " + actor[0] + ", who just wants " + obj[0] + ", avoid " + obs[0] + " and " + act[0] + "?")

    result.append("Two rivals, " + actor[0] + " and " + actor[1] + ", both seek " + obj[0] + ". " + actor[2].capitalize() + " caught in the middle is " + ing[1] + " " + obj[1] + "-- and to " + act[0] + ".")

    result.append(actor[0].capitalize() + ", " + ing[0] + " " + obj[0] + ". " + actor[1].capitalize() + ", " + ing[1] + " " + obj[1] + ". Who will overcome " + obs[0] + " and " + obs[1] + " first?")

    result.append(actor[0].capitalize() + " is obsessed with " + actor[1] + ". Can " + actor[2] + " " + ing[0] + " " + obs[2] + " overcome " + obs[0] + " and " + obs[1] + "?")

    result.append(actor[0].capitalize() + " has completed a plan to " + act[0] + ". Now all that stands between them and " + obj[0] + " is " + actor[1] + " " + ing[1] + " " + obj[1] + " and " + actor[2] + " who wants to " + act[1] + ".")

    result.append("The story is about " + actor[0] + " " + ing[0] + " " + obs[0] + " and " + actor[1] + " " + ing[1] + " " + obs[1] + ". It starts with a plan to " + act[0] + " and ends with an attempt to " + act[2] + ". The theme is " + obs[2] + ".")

    result.append("The hero is " + actor[0] + " who suffers from " + obs[0] + ". The story begins with " + eve[0] + ", climaxes with " + eve[1] + ", and ends with " + eve[2] + ".")

    index = self.premiseList.index(value)

    result = result[index]
    updateCenterDisplay(self, result, 'result')

def getPlotWeb(button, *args):

    self = button.self
    button.background_color = neutral

    result = []

    descList = ['surly', 'attractive', 'beautiful', 'ugly', 'handsome', 'hideous', 'deformed', 'maimed', 'scarred', 'pleasant', 'kind', 'charming', 'unhappy', 'sensual', 'naive', 'friendly', 'unfriendly', 'wealthy', 'poor', 'profligate', 'miserly', 'miserable', 'pathetic', 'vicious', 'violent', 'excitable', 'greedy', 'compassionate', 'selfless', 'repressed', 'louche', 'dissipated', 'weak', 'strong', 'fearless', 'fearful', 'haunted', 'happy-go-lucky', 'capable', 'calm', 'insolent', 'regal', 'stern', 'tempermental', 'mercurial', 'enraged', 'angry', 'infuriated', 'sorrowful', 'grief-stricken', 'depressed', 'optimistic', 'passionate', 'free-spirited', 'intense', 'obsessive', 'choleric', 'stolid', 'complacent', 'arrogant', 'haughty', 'bold', 'reckless', 'determined', 'guarded', 'paranoid', 'trusting', 'untrustworthy', 'tactless', 'disillusioned', 'graceful', 'outspoken', 'taciturn', 'reclusive', 'withdrawn', 'traumatized', 'skillful']

    subjList = ['mage', 'necromancer', 'sorcerer', 'wizard', 'diviner', 'seer', 'oracle', 'hunter', 'forester', 'poacher', 'ranger', 'outlaw', 'bandit', 'thief', 'rogue', 'burglar', 'jewel thief', 'assassin', 'thug', 'second story man', 'highwayman', 'grave robber', 'archaeologist', 'anatomist', 'doctor', 'scientist', 'academic', 'teacher', 'professor', 'sage', 'psychic', 'astrologer', 'vizier', 'chancellor', 'nobleman', 'gentleman', 'king', 'prince', 'queen', 'princess', 'gentewoman', 'lady', 'knight', 'spirit', 'ghost', 'phantom', 'vampire', 'werewolf', 'monster', 'fighter', 'warrior', 'soldier', 'demon hunter', 'wanderer', 'traveler', 'maiden', 'lad', 'merchant', 'shopkeeper', 'innkeeper', 'traitor', 'hermit', 'warlord', 'sorceress', 'shaman', 'healer', 'priest', 'acolyte', 'monk', 'baron', 'duke', 'serf', 'peasant', 'bartender', 'harlot', 'spy', 'adventurer', 'cleric', 'bard', 'entertainer', 'dancer', 'singer', 'musician', 'actor', 'actress', 'playwright', 'blacksmith', 'tinker', 'barbarian', 'alchemist', 'crafter', 'artisan', 'artist', 'butler', 'servant', 'enforcer', 'mercenary', 'pilgrim', 'arcane dabbler', 'mystic', 'beast tamer', 'youth', 'maid', 'virgin', 'naive innocent', 'libertine', 'rake', 'innocent victim of a curse', 'deserving victim of a curse', 'criminal', 'escapee', 'archer', 'madman', 'deserter', 'renegade', 'outcast', 'demon', 'devil']

    conList = ['is sleeping with', 'is romancing', 'is seducing', 'is pursuing', 'is hunting', 'is working for', 'is conning', 'is bloodsworn to', 'is mortal enemies with', 'is rivals with', 'is afraid of', 'hates', 'loathes', 'loves', 'doesn\'t know of', 'knows a terrible secret about', 'is hiding a secret from', 'is partners in perversion with', 'is drinking buddies with', 'was beaten over an imagined slight by', 'was discarded by', 'is using', 'is tricking', 'is a client of', 'is chasing after', 'is trying to ruin', 'owes money to', 'fears replacement by', 'is attempting to convert']

    desc = random.sample(descList, 4)
    subj = random.sample(subjList, 4)
    con = random.sample(conList, 5)

    actor = [ y + " " + x for y, x in zip(desc, subj)]

    for i in range(len(actor)):
        if actor[i][:1] in "a i e o u":
            actor[i] = "an " + actor[i]
        else:
            actor[i] = "a " + actor[i]

    ractor = random.sample(actor[:3], 2)

    result = actor[0].capitalize() + " " + con[0] + " " + actor[1] + ". " + actor[1].capitalize() + " " + con[1] + " " + actor[2] + ". " + actor[2].capitalize() + " " + con[2] + " " + actor[0] + ". " + " " + actor[3].capitalize() + " " + con[3] + " " + ractor[0] + ". " + " " + actor[3].capitalize() + " " + con[4] + " " + ractor[1] + ". "

    updateCenterDisplay(self, result, 'result')

def getPlayScene(button, *args):
    button.background_color = neutral
    self = button.self

    sceneChart = ["Setting", "Atmosphere/Mood", "Introduction", "Exposition", "Transition", "Preparation", "Aftermath", "Investigation", "Revelation", "Recognition", "A Gift In Play", "Escape", "Pursuit", "Seduction", "Opposites Attract", "Reversal of Expectations", "Unexpected Visitor"]

    rroll = random.randint(1,100)

    if rroll <= 50:
        scene = random.choice(sceneChart)
    else:
        scene = random.sample(sceneChart, 2)
        scene = ' & '.join(scene)

    sceneTypeChart = ['Dream sequence', 'Montage', 'Flashback', 'Interlude', 'Straight', 'Straight', 'Interrupt', 'Obligatory']

    index = self.actList.index(self.actSpinner.text)
    if index <= 3:
        rroll = random.randint(0,7)
    elif index <= 9:
        rroll = max(random.randint(0,7), random.randint(0,7))
    else:
        rroll = max(random.randint(0,7), random.randint(0,7), random.randint(0,7))

    scenetype = sceneTypeChart[rroll]

    result = "[" + self.actSpinner.text + "] " + scene + ", " + scenetype + " (" + str(rroll+1) + ")"

    updateCenterDisplay(self, result, 'result')

def updateConfig(spinner, value):
    config.general['current_sequence'] = value

def releaseResolveUp(button, *args):
    button.background_color = neutral
    self = button.self
    config.general['resolve'] = config.general['resolve'] + 1
    self.resolveLabel.text = str(config.general['resolve'])

def releaseResolveDown(button, *args):
    button.background_color = neutral
    self = button.self
    config.general['resolve'] = config.general['resolve'] - 1
    self.resolveLabel.text = str(config.general['resolve'])
