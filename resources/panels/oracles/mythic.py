#-*- coding: utf-8 -*-
##-----------------------------------------------------------------------------------------------------------------------------
#
# Mythic Panel
#
# Content from the Mythic Game Master Emulator (http://www.mythic.wordpr.com/page14/page9/page9.html) is used with the
# permission of the author under the condition that it not be used commercially.
#
# It is thus NOT released under the MIT license.
#
# If you wish to use only strictly MIT licensed content, delete this file and change the entries in the general dictionary and
# in config.py as follows:
#
# oracle = 'fu'
# oracle_func = 'fu'
# seed_func = 'useTwoPartSeed'
#
# Then remove everything between the 'mythic' comments in the general section of config.py.
#
# The python code is still under MIT wherever it doesn't conflict with the above.
#
#
##-----------------------------------------------------------------------------------------------------------------------------

import imports
from imports import *
import config

def exclude():
    return False

def onEnter(self):

    self.mythicContextSpinner.text = config.general['mythic_context']
    self.mythicGenreSpinner.text = config.general['mythic_genre']

    l = ToggleButtonBehavior.get_widgets('acting')
    for item in l:
        if item.text == config.general['mythic_current_acting']:
            item.state = 'down'
            item.background_color = accent2
    del l

    l = ToggleButtonBehavior.get_widgets('difficulty')
    for item in l:
        if item.text == config.general['mythic_current_difficulty']:
            item.state = 'down'
            item.background_color = accent2
    del l
    l = ToggleButtonBehavior.get_widgets('mythic')
    for item in l:
        if item.text == config.general['mythic_current_likeliness']:
            item.state = 'down'
            item.background_color = accent2
    del l

def initPanel(self):

    self.mythicAItem = AccordionItem(title='Mythic Oracle', background_normal='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', background_selected='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', min_space = config.aiheight)

    mythicMainBox = BoxLayout(orientation='vertical')

    mythicSpinnerBox = GridLayout(cols=2, size_hint=(1,.2))

    mythicSpinnerBox.add_widget(Label(text="Context?", font_size=config.basefont90))
    mythicSpinnerBox.add_widget(Label(text="Genre?", font_size=config.basefont90))

    self.mythicContextSpinner = Spinner(
        text='The Adventure So Far',
        values=config.general['mythic_context_list'],
        background_normal='',
        background_color=accent1,
        background_down='',
        background_color_down=accent2,
        font_size=config.basefont90,
    )
    self.mythicContextSpinner.bind(text=setMythicContext)
    self.mythicContextSpinner.self = self
    mythicSpinnerBox.add_widget(self.mythicContextSpinner)

    self.mythicGenreSpinner = Spinner(
        text='Standard',
        values=config.general['mythic_genre_list'],
        background_normal='',
        background_color=accent1,
        background_down='',
        background_color_down=accent2,
        font_size=config.basefont90
    )

    self.mythicGenreSpinner.bind(text=setMythicGenre)
    self.mythicGenreSpinner.self = self
    mythicSpinnerBox.add_widget(self.mythicGenreSpinner)

    mythicMainBox.add_widget(mythicSpinnerBox)

    sceneButton = Button(text="Get Scene", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
    sceneButton.self = self
    sceneButton.bind(on_press=self.pressGenericButton)
    sceneButton.bind(on_release=releaseScene)
    mythicMainBox.add_widget(sceneButton)

    complexButton = Button(text="Get Complex Answer", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
    complexButton.self = self
    complexButton.bind(on_press=self.pressGenericButton)
    complexButton.bind(on_release=releaseComplex)
    mythicMainBox.add_widget(complexButton)

    matrixBox = GridLayout(cols=1)
    matrixBox.add_widget(Label(text='Oracle', size_hint=(1,.1), font_size=config.basefont90))

    likelyList = ["impossible", "no way", "very unlikely", "unlikely", "fifty-fifty", "somewhat likely", "likely", "very likely", "near sure", "sure thing", "must be"]

    for i in range(len(likelyList)):
        likelybtn = ToggleButton(text=likelyList[i], group='mythic', size_hint=(1,.15))
        likelybtn.self = self
        likelybtn.bind(on_press=toggledLikely)
        matrixBox.add_widget(likelybtn)

    mythicMainBox.add_widget(matrixBox)

    button = Button(text="Ask Oracle", size_hint=(1,.15), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=getMythicOracle)
    mythicMainBox.add_widget(button)

    opposedBox = GridLayout(cols=2)
    opposedBox.add_widget(Label(text='Acting', size_hint=(1,.15), font_size=config.basefont90))
    opposedBox.add_widget(Label(text='Difficulty', size_hint=(1,.15), font_size=config.basefont90))

    difficultyList = ['superhuman', 'awesome', 'incredible', 'exceptional', 'high', 'above average', 'average', 'below average', 'low', 'weak', 'minuscule']
    actingList = difficultyList

    for i in range(len(likelyList)):
        actingbtn = ToggleButton(text=actingList[i], group='acting', size_hint=(1,.15))
        actingbtn.self = self
        actingbtn.bind(on_press=toggledActing)
        opposedBox.add_widget(actingbtn)

        difficultybtn = ToggleButton(text=difficultyList[i], group='difficulty', size_hint=(1,.15))
        difficultybtn.self = self
        difficultybtn.bind(on_press=toggledDifficulty)
        opposedBox.add_widget(difficultybtn)

    mythicMainBox.add_widget(opposedBox)

    button = Button(text="Make Opposed Check", size_hint=(1,.15), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=getMythicOpposed)
    mythicMainBox.add_widget(button)

    mythicMainBox.add_widget(Label(text='Backstory', size_hint=(1,.1), font_size=config.basefont90))

    mythicBackBox = GridLayout(cols=2, size_hint=(1,.15))

    button = Button(text="Complete", background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=getSeveralBackstory)
    mythicBackBox.add_widget(button)

    button = Button(text="Single Event", background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=getSingleBackstory)
    mythicBackBox.add_widget(button)

    mythicMainBox.add_widget(mythicBackBox)

    self.mythicAItem.add_widget(mythicMainBox)

    return self.mythicAItem

#------------------------------------------------------------------------------------------------------------------------------
# Mythic Button Functions
#------------------------------------------------------------------------------------------------------------------------------

def releaseScene(*args):
    args[0].background_color = neutral
    new_text = rollUpScene()
    self = args[0].self
    updateCenterDisplay(self, new_text)

def getSeveralBackstory(*args):
    args[0].background_color = neutral
    self = args[0].self
    new_text = rollBackstoryNumber()
    updateCenterDisplay(self, new_text)

def getSingleBackstory(*args):
    args[0].background_color = neutral
    self = args[0].self
    new_text = rollBackstoryItem()
    updateCenterDisplay(self, "[Event] " + new_text)

def toggledLikely(button, *args):
    config.general['mythic_current_likeliness'] = button.text
    l = ToggleButtonBehavior.get_widgets('mythic')
    for item in l:
        if item.text == config.general['mythic_current_likeliness']:
            item.state = 'down'
            item.background_color = accent2
        else:
            item.background_color = neutral
    del l

def toggledDifficulty(button, *args):
    config.general['mythic_current_difficulty'] = button.text
    l = ToggleButtonBehavior.get_widgets('difficulty')
    for item in l:
        if item.text == config.general['mythic_current_difficulty']:
            item.state = 'down'
            item.background_color = accent2
        else:
            item.background_color = neutral
    del l

def toggledActing(button, *args):
    config.general['mythic_current_acting'] = button.text
    l = ToggleButtonBehavior.get_widgets('acting')
    for item in l:
        if item.text == config.general['mythic_current_acting']:
            item.state = 'down'
            item.background_color = accent2
        else:
            item.background_color = neutral
    del l

def setMythicGenre(spinner, text):
    config.general['mythic_genre'] = text
    self = spinner.self
    updateCenterDisplay(self, "Genre is now " + text + '.', 'result')

def setMythicContext(spinner, text):
    if text == "Start":
        config.general['mythic_context'] = text
        config.general["mythic_chaos_factor"] = 5
        if config.general['mythic_genre_list'].index(config.general['mythic_genre']) == 1:
            config.general["mythic_chaos_factor"] = 4
    else:
        config.general['mythic_context'] = text

def getMythicOracle(button, *args):
    button.background_color = neutral
    self = button.self

    if len(self.textInput.text) > 0:
        updateCenterDisplay(self, self.textInput.text, 'query')

    updateCenterDisplay(self,  mythic(), 'oracle')

    self.textInput.text = ""

def getMythicOpposed(button, *args):
    button.background_color = neutral
    self = button.self

    if len(self.textInput.text) > 0:
        updateCenterDisplay(self, self.textInput.text, 'query')

    acting = config.general['mythic_current_acting']
    difficulty = config.general['mythic_current_difficulty']

    updateCenterDisplay(self, mythicResisted(acting, difficulty), 'oracle')

    self.textInput.text = ""


def releaseComplex(button, *args):
    button.background_color = neutral
    self = button.self

    if len(self.textInput.text) > 0:
        updateCenterDisplay(self, self.textInput.text, 'query')

    updateCenterDisplay(self,  "[Mythic Complex] " + event_action() + " / " + event_subject(), 'oracle')

    self.textInput.text = ""

def useMythicComplex(self, *args):

    updateCenterDisplay(self,  "[Mythic Complex] " + event_action() + " / " + event_subject(), 'oracle')

#------------------------------------------------------------------------------------------------------------------------------
#--> mythic oracle
#------------------------------------------------------------------------------------------------------------------------------
def mythic():

    target = []
    chart = {
      "impossible" :       [[0,-20,77],[0,0,81],[0,0,81],[1,5,82],[1,5,82],[2,10,83],[3,15,84],[5,25,86],[10,50,91]],
      "no way"   :         [[0,0,81],[1,5,82],[1,5,82],[2,10,83],[3,15,84],[5,25,86],[7,35,88],[10,50,91],[15,75,96]],
      "very unlikely" :    [[1,5,82],[1,5,82],[2,10,83],[3,15,84],[5,25,86],[9,45,90],[10,50,91],[13,65,94],[16,85,97]],
      "unlikely" :         [[1,5,82],[2,10,83],[3,15,84],[4,20,85],[7,35,88],[10,50,91],[11,55,92],[15,75,96],[18,90,99]],
      "fifty-fifty" :      [[2,10,83],[3,15,84],[5,25,86],[7,35,88],[10,50,91],[13,65,94],[15,75,96],[16,85,97],[19,95,100]],
      "somewhat likely" :  [[4,20,85],[5,25,86],[9,45,90],[10,50,91],[13,65,94],[16,80,97],[16,85,97],[18,90,99],[19,95,100]],
      "likely" :           [[5,25,86],[7,35,88],[10,50,91],[11,55,92],[15,75,96],[16,85,97],[18,90,99],[19,95,100],[20,100,0]],
      "very likely" :      [[9,45,90],[10,50,91],[13,65,94],[15,75,96],[16,85,97],[18,90,99],[19,95,100],[19,95,100],[21,105,0]],
      "near sure" :        [[10,50,91],[11,55,92],[15,75,96],[16,80,97],[18,90,99],[19,95,100],[19,95,100],[20,100,0],[23,115,0]],
      "sure thing" :       [[11,55,92],[13,65,94],[16,80,97],[16,85,97],[18,90,99],[19,95,100],[19,95,100],[22,110,0],[25,125,0]],
      "must be" :          [[16,80,97],[16,85,97],[18,90,99],[19,95,100],[19,95,100],[20,100,0],[20,100,0],[26,130,0],[26,145,0]],
    }
    # may need to move this to a separate button
    #if complex == 1:
    #    result = rollUpScene()
    #    return result

    noun = config.general['mythic_current_likeliness']
    roll = random.randint(1, 100)
    adj_cf = config.general['mythic_chaos_factor'] - 1
    target = chart[noun][adj_cf]

    if roll <= target[0]:
        result = "[" + noun + ", " + str(roll) + "<=" + str(target[0]) + "] " + "Exceptional YES"
    elif roll <= target[1]:
        result =  "[" + noun + ", " + str(roll) + "<=" + str(target[1]) + "] " + "YES"
    elif roll >= target[2]:
        result =  "[" + noun + ", " + str(roll) + ">=" + str(target[2]) + "] " + "Exceptional NO"
    else:
        result =  "[" + noun + ", " + str(roll) + ">=" + str(target[1]) + "] " + "NO"

    rand_event = " "
    if config.general['mythic_use_random_event_rolls'] == True:
        rand_event = rollRandomEvent(roll)

    result = result + rand_event

    return result

event_focus = []
event_focus.append([
    [7, "Remote Event"],
    [21, "NPC Action"],
    [7, "Introduce a new NPC"],
    [10, "Move toward a thread"],
    [7, "Move away from a thread"],
    [3, "Close a thread"],
    [12, "PC negative"],
    [8, "PC positive"],
    [8, "Ambiguous event"],
    [9, "NPC negative"],
    [8, "NPC positive"],
])
event_focus.append([
    [10, "Horror - PC"],
    [13, "Horror - NPC"],
    [7, "Remote event"],
    [19, "NPC action"],
    [3, "New NPC"],
    [3, "Move toward a thread"],
    [7, "Move away from a thread"],
    [10, "PC negative"],
    [3, "PC positive"],
    [7, "Ambiguous event"],
    [15, "NPC negative"],
    [3, "NPC positive"],
])
event_focus.append([
    [16,"Action!"],
    [8, "Remote event"],
    [20, "NPC action"],
    [8, "New NPC"],
    [4, "Move toward a thread"],
    [8, "Move away from a thread"],
    [12, "PC negative"],
    [4, "PC positive"],
    [4, "Ambiguous event"],
    [12, "NPC negative"],
    [4, "NPC positive"],
])
event_focus.append([
    [8, "Remote event"],
    [12, "NPC action"],
    [12, "New NPC"],
    [20, "Move toward a thread"],
    [12, "Move away from a thread"],
    [8, "PC negative"],
    [8, "PC positive"],
    [8, "Ambiguous event"],
    [8, "NPC negative"],
    [4, "NPC positive"],
])
event_focus.append([
    [12, "Drop a bomb!"],
    [12, "Remote event"],
    [12, "NPC action"],
    [8, "New NPC"],
    [12, "Move toward a thread"],
    [4, "Move away from a thread"],
    [4, "Close a thread"],
    [8, "PC negative"],
    [8, "PC positive"],
    [12, "Ambiguous event"],
    [4, "NPC negative"],
    [4, "NPC positive"],
])
event_focus.append([
    [7, "Remote event"],
    [17, "NPC action"],
    [4, "PC NPC action"],
    [7, "New NPC"],
    [7, "Move toward a thread"],
    [3, "Move toward a PC thread"],
    [5, "Move away from a thread"],
    [2, "Move away from a PC thread"],
    [2, "Close thread"],
    [1, "Close PC thread"],
    [12, "PC negative"],
    [8, "PC positive"],
    [8, "Ambiguous event"],
    [7, "NPC negative"],
    [2, "PC NPC negative"],
    [7, "NPC positive"],
    [1, "PC NPC positive"],
])
event_focus.append([
    [12, "Thread escalates"],
    [4, "Remote event"],
    [14, "NPC action"],
    [12, "New NPC"],
    [4, "Move toward a thread"],
    [12, "Move away from a thread"],
    [14, "PC negative"],
    [8, "PC positive"],
    [4, "Ambiguous event"],
    [8, "NPC negative"],
    [8, "NPC positive"],
])

def event_action():
    action = ["Attainment", "Starting", "Neglect", "Fight", "Recruit", "Triumph", "Violate", "Oppose", "Malice", "Communicate", "Persecute", "Increase", "Decrease", "Abandon", "Gratify", "Inquire", "Antagonize", "Move", "Waste", "Truce", "Release", "Befriend", "Judge", "Desert", "Dominate", "Procrastinate", "Praise", "Separate", "Take", "Break", "Heal", "Delay", "Stop", "Lie", "Return", "Imitate", "Struggle", "Inform", "Bestow", "Postpone", "Expose", "Haggle", "Imprison", "Release", "Celebrate", "Develop", "Travel", "Block", "Harm", "Debase", "Overindulge", "Adjourn", "Adversity", "Kill", "Disrupt", "Usurp", "Create", "Betray", "Agree", "Abuse", "Oppress", "Inspect", "Ambush", "Spy", "Attach", "Carry", "Open", "Carelessness", "Ruin", "Extravagance", "Trick", "Arrive", "Propose", "Divide", "Refuse", "Mistrust", "Deceive", "Cruelty", "Intolerance", "Trust", "Excitement", "Activity", "Assist", "Care", "Negligence", "Passion", "Workhard", "Control", "Attract", "Failure", "Pursue", "Vengeance", "Proceedings", "Dispute", "Punish", "Guide", "Transform", "Overthrow", "Oppress", "Change"]

    return random.choice(action)

def event_subject():
    subject = ["Goals", "Dreams", "Environment", "Outside", "Inside", "Reality", "Allies", "Enemies", "Evil", "Good", "Emotions", "Opposition", "War", "Peace", "The innocent", "Love", "The spiritual", "The intellectual", "New ideas", "Joy", "Messages", "Energy", "Balance", "Tension", "Friendship", "The physical", "Project", "Pleasures", "Pain", "Possessions", "Benefits", "Plans", "Lies", "Expectations", "Legal matters", "Bureaucracy", "Business", "A path", "News", "Exterior factors", "Advice", "A plot", "Competition", "Prison", "Illness", "Food", "Attention", "Success", "Failure", "Travel", "Jealousy", "Dispute", "Home", "Investment", "Suffering", "Wishes", "Tactics", "Stalemate", "Randomness", "Misfortune", "Death", "Disruption", "Power", "A burden", "Intrigues", "Fears", "Ambush", "Rumor", "Wounds", "Extravagance", "A Representative", "Adversities", "Opulence", "Liberty", "Military", "The mundane", "Trials", "Masses", "Vehicle", "Art", "Victory", "Dispute", "Riches", "Status quo", "Technology", "Hope", "Magic", "Illusions", "Portals", "Danger", "Weapons", "Animals", "Weather", "Elements", "Nature", "The public", "Leadership", "Fame", "Anger", "Information"]

    return random.choice(subject).title()

def rollRandomEvent(roll):

    roll = int(roll)
    index = config.general['mythic_genre_list'].index(config.general['mythic_genre'])
    table = event_focus[index]
    limiter = 0
    doubledigit = False
    rand_event = False

    limiter = config.general["mythic_chaos_factor"]

    if roll > 10:
        firstdigit = [int(char) for char in str(roll)][0]
        lastdigit = [int(char) for char in str(roll)][1]

        if roll > 10 and firstdigit == lastdigit:
            doubledigit = True

        if index == 3 and doubledigit == True:
            rand_event = True
        elif firstdigit <= limiter and doubledigit == True:
            rand_event = True

    result = " "

    if rand_event == True:

        weighted = [item[1] for item in table for i in range(item[0])]

        focus = random.choice(weighted)
        action = event_action()
        subject = event_subject()
        result = "\n[RANDOM] " + focus + " \"" + action + " " + subject + "\""

    return result

backstory_number = [
    [8, 1],
    [17, 2],
    [26, 3],
    [20, 4],
    [15, 5],
    [10, 6],
    [4, 7],
]

backstory_focus = [
    [44, "New PC Character"],
    [24, "New PC Thread"],
    [16, "PC Negative"],
    [16, "PC Positive"],
]

def rollBackstoryNumber():

    table = backstory_number

    weighted = [item[1] for item in table for i in range(item[0])]

    number = random.choice(weighted)

    result = "[Backstory Events " + str(number) + "]"

    for i in range(number):
        result = result + "\n" + rollBackstoryItem()

    return result

def rollBackstoryItem():

    table = backstory_focus
    weighted = [item[1] for item in table for i in range(item[0])]

    focus = random.choice(weighted)
    action = event_action()
    subject = event_subject()
    result = "[FOCUS] " + focus + " \"" + action + " " + subject + "\""

    return result

#--> mythic resisted check
def mythicResisted(acting, difficulty):

    target = []
    chart = {
      "minuscule" :        [[0,-35,74],[0,-20,77],[0,-20,77],[0,0,81],[0,0,81],[1,5,82],[1,5,82],[2,10,83],[3,15,84],[5,25,86],[10,50,91]],
      "weak"   :           [[0,-15,78],[0,0,81],[0,0,81],[1,5,82],[1,5,82],[2,10,83],[3,15,84],[5,25,86],[7,35,88],[10,50,91],[15,75,96]],
      "low" :              [[0,-5,80],[1,5,82],[1,5,82],[1,5,82],[2,10,83],[3,15,84],[5,25,86],[9,45,90],[10,50,91],[13,65,94],[16,85,97]],
      "below average" :    [[0,0,81],[1,5,82],[1,5,82],[2,10,83],[3,15,84],[4,20,85],[7,35,88],[10,50,91],[11,55,92],[15,75,96],[18,90,99]],
      "average" :          [[1,5,82],[2,10,83],[2,10,83],[3,15,84],[5,25,86],[7,35,88],[10,50,91],[13,65,94],[15,75,96],[16,85,97],[19,95,100]],
      "above average" :    [[1,5,82],[3,15,84],[4,20,85],[5,25,86],[9,45,90],[10,50,91],[13,65,94],[16,80,97],[16,85,97],[18,90,99],[19,95,100]],
      "high" :             [[2,10,83],[4,20,85],[5,25,86],[7,35,88],[10,50,91],[11,55,92],[15,75,96],[16,85,97],[18,90,99],[19,95,100],[20,100,0]],
      "exceptional" :      [[3,15,84],[7,35,88],[9,45,90],[10,50,91],[13,65,94],[15,75,96],[16,85,97],[18,90,99],[19,95,100],[19,95,100],[21,105,0]],
      "incredible" :       [[4,20,85],[9,45,90],[10,50,91],[11,55,92],[15,75,96],[16,80,97],[18,90,99],[19,95,100],[19,95,100],[20,100,0],[23,115,0]],
      "awesome" :          [[5,25,86],[10,50,91],[11,55,92],[13,65,94],[16,80,97],[16,85,97],[18,90,99],[19,95,100],[19,95,100],[22,110,0],[25,125,0]],
      "superhuman" :       [[10,50,91],[15,75,96],[16,80,97],[16,85,97],[18,90,99],[19,95,100],[19,95,100],[20,100,0],[20,100,0],[26,130,0],[26,145,0]],
    }

    roll = random.randint(1, 100)

    difficultychart = ['superhuman', 'awesome', 'incredible', 'exceptional', 'high', 'above average', 'average', 'below average', 'low', 'weak', 'minuscule']

    target = chart[acting][difficultychart.index(difficulty)]

    preresult = "[" + acting + " vs " + difficulty + ", " + str(roll)

    if roll <= target[0]:
        result = "<=" + str(target[0]) + "] " + "Exceptional YES"
    elif roll <= target[1]:
        result =  "<=" + str(target[1]) + "] " + "YES"
    elif roll >= target[2]:
        result =  ">=" + str(target[2]) + "] " + "Exceptional NO"
    else:
        result =  ">=" + str(target[1]) + "] " + "NO"

    return preresult + result

#--> mythic scenes
def rollUpScene():

    index = config.general['mythic_genre_list'].index(config.general['mythic_genre'])
    table = event_focus[index]

    weighted = [item[1] for item in table for i in range(item[0])]

    focus = random.choice(weighted)
    action = event_action()
    subject = event_subject()

    if config.general['mythic_context'] == "Start":
        #-- this is the start of the adventure; let's set up some stuff
        # config.general["mythic_chaos_factor"] = 5
        context = "PCs (Start)"
        if index == 1:
            #config.general["mythic_chaos_factor"] = 4
            focus = "Ambiguous Event"
        elif index == 3:
            context = "The Mystery Is...?"
        elif index == 4:
            context = "Social"
    else:
        context = config.general['mythic_context']

    result = "[CONTEXT] " + context + "\n[FOCUS] " + focus + "\n[MEANING] " + action + " " + subject

    modroll = random.randint(1,10)
    altered = " "
    #--check for genre
    if index == 2:
       #--horror
        if modroll <= config.general["mythic_chaos_factor"] :
            if modroll <= 3 :
                altered = "\n[" + str(modroll) + "] Altered!"
            else:
                altered = "\n[" + str(modroll) + "] Interrupted!"


    else:
      #--standard
        if modroll <= config.general["mythic_chaos_factor"] :
           #--this is a changed scene
            if modroll % 2 == 0 :
               #--even
                altered = "\n[" + str(modroll) + "] Interrupted!"
            else:
                altered = "\n[" + str(modroll) + "] Altered!"

    result = result + altered
    scene_string = result

    return result

def setChaosFactor(target):

    target = target
    genre = config.general['mythic_genre_list'].index(config.general['mythic_genre'])
    cmin = 1
    cmax = 9

    if genre == 2: cmin = 4
    if genre == 3: cmin = 5
    if genre == 4: cmin = 3
    if genre == 7: cmin = 3

    if target == "up" or target == "u" or target == "+":
        if config.general['mythic_chaos_factor'] < 9:
          config.general['mythic_chaos_factor'] = config.general['mythic_chaos_factor'] + 1
          result = "\nChaos factor is now " + str(config.general['mythic_chaos_factor']) + "."
        else:
           result = "The chaos factor is already max."
    elif target == "down" or target == "d" or target == "-":
        if genre == 2:
            result = "\nChaos may not be reduced in this genre, only increased."
        elif config.general['mythic_chaos_factor'] > cmin:
          config.general['mythic_chaos_factor'] = config.general['mythic_chaos_factor'] - 1
          result = "\nChaos factor is now " + str(config.general['mythic_chaos_factor']) + "."
        else:
           result = "The chaos factor is already minimum."

    elif int(target) >= cmin and int(target) <= 9:
        config.general['mythic_chaos_factor'] = int(target)
        result = "\nChaos factor is now " + str(config.general['mythic_chaos_factor']) + "."
    else:
        result = "\nChaos factor is currently " + str(config.general['mythic_chaos_factor']) + ".\nTo change, enter a number between " + cmin + " and 9 on the variable panel."

    return result
