# -*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------------------
#
# FU Oracle Panel
#
##---------------------------------------------------------------------------------------------------
import imports
from imports import *
import config

def exclude():
    return False

def onEnter(self):
    pass

def initPanel(self):

    self.fuAItem = AccordionItem(title='FU & How\'s It Going', background_normal='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', background_selected='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', min_space = config.aiheight)

    self.fuMainBox = BoxLayout(orientation='vertical')

    #self.fuMainBox.add_widget(Label(text='Oracle', size_hint=(1,0.10)))

    fuTextList = [
        'almost certain', 'very probable', 'probable', 'likely', 'possibly', 'even odds', 'doubtful', 'somewhat unlikely', 'probably not', 'improbable', 'almost certainly not' ]

    fuOddsList = ['99%', '97%', '94%', '88%', '75%', '50%', '25%', '12%', '6%', '3%', '1%']

    self.fuSubBox = BoxLayout(orientation='horizontal', size_hint=(1,.6))

    self.fuTextSubBox = BoxLayout(orientation='vertical')
    self.fuModSubBox = BoxLayout(orientation='vertical', size_hint_x=.25)
    self.fuOddsSubBox = BoxLayout(orientation='vertical', size_hint_x=.25)

    count = 6
    modifier="none"
    oddsButtons = []
    for i in range(len(fuTextList)):
        count = count - 1
        if count > 0:
            modifier = "positive"
        elif count == 0:
            modifier = "none"
        else:
            modifier = "negative"

        button = Button(text=fuTextList[i], background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans', font_size=config.basefont90, size_hint=(1,1))
        button.count = count
        button.modifier = modifier
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=fuRoll)
        self.fuTextSubBox.add_widget(button)

        button = Button(text=str(count), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans', size_hint=(1,1))
        button.modifier = modifier
        button.count = count
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=fuRoll)
        self.fuModSubBox.add_widget(button)

        button = Button(text=fuOddsList[i], background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans', size_hint=(1,1))
        button.modifier = modifier
        button.count = count
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=fuRoll)
        oddsButtons.append(button)
        self.fuOddsSubBox.add_widget(button)

    self.fuSubBox.add_widget(self.fuTextSubBox)
    self.fuSubBox.add_widget(self.fuModSubBox)
    #self.fuSubBox.add_widget(self.fuOddsSubBox)

    self.fuMainBox.add_widget(self.fuSubBox)

    self.oddsButton = Button(text="show the odds", background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans', font_size=config.basefont75, size_hint_y=0.05)
    self.oddsButton.self = self
    self.oddsButton.bind(on_press=self.pressGenericButton)
    self.oddsButton.bind(on_release=toggleOdds)
    self.fuMainBox.add_widget(self.oddsButton)

    button = Button(text="How Much...?", background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans', size_hint_y=0.07)
    button.function = "howMuchWeighted"
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=howMuch)
    self.fuMainBox.add_widget(button)

    dramaRollList = ["chaotic", "same old", "kinda good", "kinda bad", "great", "terrible"]

    self.fuMainBox.add_widget(Label(text="How's It Going?", size_hint_y=0.07, font_size=config.basefont90))
    self.fuDramaBox = GridLayout(cols=2, size_hint_y=.3)

    self.fuDramaBox.add_widget(Label(text="Good/Bad"))
    self.fuDramaBox.add_widget(Label(text="Yes/No"))

    for i in dramaRollList:
        button = Button(text=i, background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans', font_size=config.basefont90,)
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=dramaChartRoll)
        button.subtype="Good/Bad"
        button.self = self
        self.fuDramaBox.add_widget(button)

        button = Button(text=i, background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans', font_size=config.basefont90,)
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=dramaChartRoll)
        button.subtype="Yes/No"
        button.self = self
        self.fuDramaBox.add_widget(button)

    self.fuMainBox.add_widget(self.fuDramaBox)

    button = Button(text="Chaos Oracle", background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans', font_size=config.basefont90, size_hint=(1,.07))
    button.function = "getChaosOracle"
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=chaosOracleRoll)
    self.fuMainBox.add_widget(button)

    button = Button(text="Plot Move", size_hint=(1,.07), background_normal='',
     background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans', font_size=config.basefont90)
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=getPlotMove)
    self.fuMainBox.add_widget(button)

    self.fuMainBox.add_widget(Label(text="But/And Clarifier", halign="center", size_hint_y=0.07, font_size=config.basefont90))

    butCardBox = GridLayout(cols=4, size_hint=(1,.07))
    butLabels = ['yes but', 'no and', 'no but', 'yes and']
    for i in range(0,4):
        button = Button(text=butLabels[i], background_normal='',
         background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans', font_size=config.basefont90)
        button.self = self
        button.subtype = i
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=abulafiaButCards)
        butCardBox.add_widget(button)

    self.fuMainBox.add_widget(butCardBox)

    self.fuMainBox.add_widget(Label(text="Random Events", halign="center", size_hint_y=0.07, font_size=config.basefont90))

    self.randomEventTypeSpinner = Spinner(
    text='Random',
    values=['Action', 'Social', 'Weird', 'World', 'Plot', 'Random'],
    background_normal='',
    background_color=accent1,
    background_down='',
    background_color_down=accent2,
    size_hint_y=0.07
    )
    self.randomEventTypeSpinner.self = self
    self.fuMainBox.add_widget(self.randomEventTypeSpinner)

    self.fuMainBox.add_widget(Label(text="How Is This Scene Going So Far?", halign="center", size_hint_y=0.06, font_size=config.basefont75))

    self.fuRandomEventBox = GridLayout(cols=2, size_hint=(1,.20))

    button = Button(text='random', background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans', font_size=config.basefont80, size_hint=(1,.07))
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=randomChartRoll)
    button.subtype="Random Event"
    button.self = self
    button.link = self.randomEventTypeSpinner
    self.fuMainBox.add_widget(button)

    for i in dramaRollList:
        button = Button(text=i, background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans', font_size=config.basefont80,)
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=randomChartRoll)
        button.subtype="Random Event"
        button.self = self
        button.link = self.randomEventTypeSpinner
        self.fuRandomEventBox.add_widget(button)

    self.fuMainBox.add_widget(self.fuRandomEventBox)

    self.fuAItem.add_widget(self.fuMainBox)

    return self.fuAItem

#---------------------------------------------------------------------------------------------------# FU Button Functions
#---------------------------------------------------------------------------------------------------
def chaosOracleRoll(*args):
    args[0].background_color = neutral
    self = args[0].self

    result = getChaosOracle()

    if len(self.textInput.text) > 0:
        updateCenterDisplay(self, self.textInput.text, 'query')

    updateCenterDisplay(self, result, "oracle")
    self.textInput.text = ""

def fuRoll(*args):
    args[0].background_color = neutral
    self = args[0].self
    if len(self.textInput.text) > 0:
        updateCenterDisplay(self, self.textInput.text, 'query')
    updateCenterDisplay(self, fu(args[0].count, args[0].modifier, args[0].text), 'oracle')
    self.textInput.text = ""

def dramaChartRoll(*args):
    args[0].background_color = neutral
    self = args[0].self
    if len(self.textInput.text) > 0:
        updateCenterDisplay(self, self.textInput.text, 'query')
    result = dramaRoll(args[0].text, args[0].subtype)
    if random.randint(1,10) == 1:
        result = result + "\n" + randomEventRoll("Random", "Random")
    updateCenterDisplay(self, result)
    self.textInput.text = ""

def randomChartRoll(*args):
    args[0].background_color = neutral
    self = args[0].self
    if len(self.textInput.text) > 0:
        updateCenterDisplay(self, self.textInput.text, 'query')
    result = randomEventRoll(args[0].text, args[0].link.text)
    updateCenterDisplay(self, result)
    self.textInput.text = ""

def howMuch(*args):
    args[0].background_color = neutral
    self = args[0].self
    if len(self.textInput.text) > 0:
        updateCenterDisplay(self, self.textInput.text, 'query')
    updateCenterDisplay(self, howMuchWeighted(), 'result')
    self.textInput.text = ""

def toggleOdds(button, *args):
    self = button.self
    button.background_color = neutral

    if self.oddsButton.text == "show the odds":
        self.fuSubBox.add_widget(self.fuOddsSubBox)
        self.oddsButton.text = "don't show the odds"
    else:
        self.fuSubBox.remove_widget(self.fuOddsSubBox)
        self.oddsButton.text = "show the odds"

#---------------------------------------------------------------------------------------------------# --> FU Oracle Functions
#---------------------------------------------------------------------------------------------------
# FU
# http://creativecommons.org/licenses/by/3.0/
# This function is based on FU: The Freeform/Universal RPG (found at http://nathanrussell.net/fu), by Nathan Russell, and licensed for our use under the Creative
# Commons Attribution 3.0 Unported license (http://creativecommons.org/licenses/by/3.0/).
def fu(count=0, modifier="none", text="0"):
    rolls = []
    odds = []
    evens = []
    count = abs(count)
    count = count+1

    roll_string = ""
    ands = ""

    for i in range(count):
        roll = random.randint(1,6)
        if roll % 2 == 0:
            evens.append(roll)
        else:
            odds.append(roll)
        roll_string = roll_string + str(roll) + " "

    if modifier == "negative":
        if len(odds) > 0:
            roll_result = min(odds)
            if odds.count(roll_result) > 1:
                ands = " ...and " + str(odds.count(roll_result) - 1) + " extra 'ands'!"
        else:
            roll_result = min(evens)
            if evens.count(roll_result) > 1:
                ands = " ...and " + str(evens.count(roll_result) - 1) + " extra 'ands'!"
    else:
        if len(evens) > 0:
            roll_result = max(evens)
            if evens.count(roll_result) > 1:
                ands = " ...and " + str(evens.count(roll_result) - 1) + " extra 'ands'!"
        else:
            roll_result = max(odds)
            if odds.count(roll_result) > 1:
                ands = " ...and " + str(odds.count(roll_result) - 1) + " extra 'ands'!"
    chart = {
        6 : "Yes, and...",
        4 : "Yes.",
        2 : "Yes, but...",
        5 : "No, but...",
        3 : "No.",
        1 : "No, and...",
    }

    random_event = ""
    rroll = random.randint(1,20)
    if rroll == 1:
        random_event = "\n... and something unexpected happens!"

    return "[" + text + ": " + roll_string + "] " + chart[roll_result] + ands + random_event

# END FU

def howMuchWeighted():
    chart = {
        2 : "Almost entirely or far more than expected.",
        3 : "A lot or a lot more than expected.",
        4 : "More than expected.",
        5 : "A moderate amount or as expected.",
        6 : "Less than expected.",
        7 : "A little or much less than expected.",
        8 : "Scarcely any.",
    }

    roll = random.randint(1,4) + random.randint(1,4)

    result = "[How Much?] " + chart[roll]
    return result

# based on drama roll
def randomEventRoll(text, event_type="Random"):

    if event_type == "Random":
        event_type = random.choice(['Action', 'Social', 'Weird', 'World', 'Plot'])

    if text == "random":
        text = random.choice(["chaotic", "same old", "kinda good", "kinda bad", "great", "terrible"])

    if event_type == "Action":
        chart = [
          "A bomb drops, literally or figuratively.",
          "An unexpected enemy attacks from ambush.",
          "Someone looking for a fight appears.",
          "Someone is being mugged or murdered or something else noisy nearby.",
          "Badly wounded person appears or is discovered, being chased or stalked.",
          "An unexpected ally appears.",
          ]
    elif event_type == "Social":
        chart = [
          "A bomb drops, figuratively.",
          "A powerful, dangerous, or humiliating secret or weakness is revealed."
          "An embarrassing, revealing or damaging secret or weakness is revealed.",
          "An unexpected ally makes a move.",
          "Someone unexpectedly falls in love with or discovers great esteem for someone else.",
          "Someone isn't who they seem or switches motivations, ambitions, or goals suddenly.",
          ]
    elif event_type == "Weird":
        chart = [
          "A chaos bomb drops, literally or figuratively.",
          "Magical effect occurs, to the hero or an ally's detriment.",
          "Magical effect occurs, to everyone's detriment.",
          "Someone is compelled to act out of character or to feel a certain way.",
          "Wild coincidence aids the hero -- at a cost.",
          "Something changes in an utterly improbable way.",
          ]
    elif event_type == "Plot":
        chart = [
          "New or random actor becomes important or comes into play.",
          "Random thread becomes important or comes into play.",
          "New actor.",
          "New thread.",
          "New or random actor and random thread are linked.",
          "Something happens to a random or logical ally.",
          ]
    else:
        chart = [
          "Natural disaster.",
          "Fire breaks out.",
          "An actor's long term plans begin to bear fruit.",
          "An actor's long term plans go awry.",
          "A hidden enemy is revealed.",
          "Someone dies or is very badly injured off-screen.",
          ]

    roll = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    if roll == 3:
        event = chart[0]
    elif roll <= 6:
        event = chart[1]
    elif roll <= 10:
        event = chart[2]
    elif roll <= 14:
        event = chart[3]
    elif roll <= 17:
        event = chart[4]
    elif roll == 18:
        event = chart[5]

    chart = ["disastrously bad.", "bad.", "bad with some good.", "good with some bad.", "good.", "spectacularly good."]
    if text == "chaotic":
        result = random.choice(chart)
    elif text == "same old":
        roll = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
        if roll == 3:
            result = chart[0]
        elif roll <= 6:
            result = chart[1]
        elif roll <= 10:
            result = chart[2]
        elif roll <= 14:
            result = chart[3]
        elif roll <= 17:
            result = chart[4]
        elif roll == 18:
            result = chart[5]
    elif text == "kinda good":
        roll = random.randint(1,6) + random.randint(1,6)
        if roll == 2:
            result = chart[0]
        elif roll <= 4:
            result = chart[1]
        elif roll <= 6:
            result = chart[2]
        elif roll <= 9:
            result = chart[3]
        elif roll <= 11:
            result = chart[4]
        elif roll == 12:
            result = chart[5]
    elif text == "kinda bad":
        roll = random.randint(1,6) + random.randint(1,6)
        if roll == 2:
            result = chart[0]
        elif roll <= 4:
            result = chart[1]
        elif roll <= 7:
            result = chart[2]
        elif roll <= 9:
            result = chart[3]
        elif roll <= 11:
            result = chart[4]
        elif roll == 12:
            result = chart[5]
    elif text == "great":
        rollArray = []
        rollArray.append(random.randint(0,5))
        rollArray.append(random.randint(0,5))
        roll = max(rollArray)
        result = chart[roll]
    elif text == "terrible":
        rollArray = []
        rollArray.append(random.randint(0,5))
        rollArray.append(random.randint(0,5))
        roll = min(rollArray)
        result = chart[roll]

    second = ""
    if random.randint(1,20) == 1:
        second = "\nCombined with...\n" + randomEventRoll(text, event_type="Random")

    return "[Random Event] Context: " + event_type + "! " + event + " This is " + result + second

# from http://abominablefancy.blogspot.com/2015/04/dice-hows-it-going.html
def dramaRoll(text, subtype):

    if subtype == "Good/Bad":
        chart = ["Disastrously bad.", "Bad", "Bad with some good.", "Good with some bad.", "Good.", "Spectacularly good."]
    else:
        chart = ["No, and...", "No.", "No, but...", "Yes, but...", "Yes.", "Yes, and..."]

    if text == "chaotic":
        result = random.choice(chart)
    elif text == "same old":
        roll = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
        if roll == 3:
            result = chart[0]
        elif roll <= 6:
            result = chart[1]
        elif roll <= 10:
            result = chart[2]
        elif roll <= 14:
            result = chart[3]
        elif roll <= 17:
            result = chart[4]
        elif roll == 18:
            result = chart[5]
    elif text == "kinda good":
        roll = random.randint(1,6) + random.randint(1,6)
        if roll == 2:
            result = chart[0]
        elif roll <= 4:
            result = chart[1]
        elif roll <= 6:
            result = chart[2]
        elif roll <= 9:
            result = chart[3]
        elif roll <= 11:
            result = chart[4]
        elif roll == 12:
            result = chart[5]
    elif text == "kinda bad":
        roll = random.randint(1,6) + random.randint(1,6)
        if roll == 2:
            result = chart[0]
        elif roll <= 4:
            result = chart[1]
        elif roll <= 7:
            result = chart[2]
        elif roll <= 9:
            result = chart[3]
        elif roll <= 11:
            result = chart[4]
        elif roll == 12:
            result = chart[5]
    elif text == "great":
        rollArray = []
        rollArray.append(random.randint(0,5))
        rollArray.append(random.randint(0,5))
        roll = max(rollArray)
        result = chart[roll]
    elif text == "terrible":
        rollArray = []
        rollArray.append(random.randint(0,5))
        rollArray.append(random.randint(0,5))
        roll = min(rollArray)
        result = chart[roll]
    return "[Drama] " + result

# chaos oracle, for no other reason than I love it and have no place else for it
def getChaosOracle(*args):

    chart = {
        2 : "No, and, and",
        3 : "No, and, but",
        4 : "No, and",
        5 : "No",
        6 : "No, but",
        7 : "Whatever result would be most interesting or roll a random event.",
        8 : "Yes, but",
        9 : "Yes",
        10 : "Yes, and",
        11 : "Yes, and, but",
        12 : "Yes, and, and",
    }
    roll = random.randint(1,6) + random.randint(1,6)
    result = chart[roll]

    result = "[Chaos " + str(roll) + "] " + result

    return result

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

# http://www.random-generator.com/index.php?title=But_Cards
def abulafiaButCards(*args):
    self = args[0].self
    subtype = args[0].subtype
    args[0].background_color = neutral

    statementList = ["an inconvenient attraction is struck", "in order to do it, you’ll have to do something else first", "it breaks the alignment of things", "it costs someone you care about, something they care about", "it costs you something dear", "it means closing the door on a future opportunity", "it only provides a temporary solution. It won’t last that long", "it takes longer than you thought it would", "it works a little too well", "it’s quiet … too quiet", "what you want isn’t what you need", "you can’t do it by yourself", "you get seriously hurt", "YOU TOTALLY ALMOST DIE OMG", "you’re not even supposed to be here", "your beloved is lost",]
    questionList = ["didn’t it seem a little too easy? What’s really going on, here", "is it not by the path you thought", "what does it mean for someone else", "what does it mean for the enemy", "what is that person doing over there", "what really made you want it", "why is that character acting so strangely", "why now", "why you"]
    positiveList = ["a clue reveals itself", "something unrelated but useful also occurs", "you earn a reward", "you learn something about your enemies in the process", "you learn something about yourself in the process", "you make a fast friend", "your style and panache are duly noted"]

    statement = random.choice(statementList)
    positive = random.choice(positiveList)

    coin = random.randint(1,2)
    if coin == 1:
        everything = random.choice(questionList) + "?"
    else:
        everything = random.choice(statementList) + "."

    resultList = [
        "But " + everything,
        "And " + statement + ".",
        "But " + positive + ".",
        "And " + positive + ".",
    ]

    updateCenterDisplay(self, resultList[subtype], 'result' )
