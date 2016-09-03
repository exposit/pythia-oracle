# -*- coding: utf-8 -*-
##-------------------------------------------------------------------------------------------------------------------------------------------
# FU Oracle Panel
#
#
##-------------------------------------------------------------------------------------------------------------------------------------------

import imports
from imports import *
import config

def exclude():
    return False

def onEnter(self):
    pass

def initPanel(self):

        self.fuAItem = AccordionItem(title='FU & Weighted Oracle', background_selected= os.sep + 'resources' + os.sep + "ui_images" + os.sep + 'invisible.png', min_space="28dp")

        self.fuMainBox = BoxLayout(orientation='vertical')

        self.fuMainBox.add_widget(Label(text='FU Oracle', size_hint=(1,.12)))

        button = Button(text="0", size_hint=(1,.12), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.modifier = "none"
        button.count = 0
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=fuRoll)
        self.fuMainBox.add_widget(button)
        self.fuSubBox = GridLayout(cols=5)

        self.fuSubBox.add_widget(Label(text="Pos", size_hint=(1,.12)))
        for i in range(1,5):
            button = Button(text="+" + str(i), size_hint=(1,.12), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
            button.modifier = "positive"
            button.count = i
            button.self = self
            button.bind(on_press=self.pressGenericButton)
            button.bind(on_release=fuRoll)
            self.fuSubBox.add_widget(button)

        self.fuSubBox.add_widget(Label(text="Neg", size_hint=(1,.12)))
        for i in range(1,5):
            button = Button(text="-" + str(i), size_hint=(1,.12), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
            button.modifier = "negative"
            button.count = i
            button.self = self
            button.bind(on_press=self.pressGenericButton)
            button.bind(on_release=fuRoll)
            self.fuSubBox.add_widget(button)

        self.fuMainBox.add_widget(self.fuSubBox)

        self.fuMainBox.add_widget(Label(text="---", halign="center", size_hint=(1,.12)))

        self.fuMainBox.add_widget(Label(text='Drama Rolls', size_hint=(1,.12)))
        button = Button(text="How Much...?", size_hint=(1,.25), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.function = "howMuchWeighted"
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=howMuch)
        self.fuMainBox.add_widget(button)

        self.fuMainBox.add_widget(Label(text="How's It Going?", size_hint=(1,.12)))
        self.fuDramaBox = GridLayout(cols=2)
        dramaRollList = ["chaotic", "same old", "kinda good", "kinda bad", "great", "terrible"]
        self.fuDramaBox.add_widget(Label(text="Good/Bad"))
        self.fuDramaBox.add_widget(Label(text="Yes/No"))
        for i in dramaRollList:
            button = Button(text=i, size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
            button.bind(on_press=self.pressGenericButton)
            button.bind(on_release=dramaChartRoll)
            button.subtype="Good/Bad"
            button.self = self
            self.fuDramaBox.add_widget(button)

            button = Button(text=i, size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
            button.bind(on_press=self.pressGenericButton)
            button.bind(on_release=dramaChartRoll)
            button.subtype="Yes/No"
            button.self = self
            self.fuDramaBox.add_widget(button)

        self.fuMainBox.add_widget(self.fuDramaBox)

        self.fuAItem.add_widget(self.fuMainBox)

        return self.fuAItem

#-------------------------------------------------------------------------------------------------------------------------------------------
# FU Button Functions
#-------------------------------------------------------------------------------------------------------------------------------------------

def fuRoll(*args):
    args[0].background_color = neutral
    self = args[0].self
    if len(self.textInput.text) > 0:
        updateCenterDisplay(self, self.textInput.text, 'query')
    updateCenterDisplay(self, fu(args[0].count, args[0].modifier), 'oracle')
    self.textInput.text = ""

def dramaChartRoll(*args):
    args[0].background_color = neutral
    self = args[0].self
    if len(self.textInput.text) > 0:
        updateCenterDisplay(self, self.textInput.text, 'query')
    result = dramaRoll(args[0].text, args[0].subtype)
    updateCenterDisplay(self, result)
    self.textInput.text = ""

def howMuch(*args):
    args[0].background_color = neutral
    self = args[0].self
    if len(self.textInput.text) > 0:
        updateCenterDisplay(self, self.textInput.text, 'query')
    updateCenterDisplay(self, howMuchWeighted(), 'result')
    self.textInput.text = ""

#-------------------------------------------------------------------------------------------------------------------------------------------
# --> FU Oracle Functions
#-------------------------------------------------------------------------------------------------------------------------------------------

# FU
# http://creativecommons.org/licenses/by/3.0/
# This function is based on FU: The Freeform/Universal RPG (found at http://nathanrussell.net/fu), by Nathan Russell, and licensed for our use under the Creative
# Commons Attribution 3.0 Unported license (http://creativecommons.org/licenses/by/3.0/).
def fu(count=0, modifier="none"):
    rolls = []
    odds = []
    evens = []
    count = count+1
    roll_string = ""
    ands = ""
    if modifier == "none":
        mod = "0"
    else:
        mod = "+"
    for i in range(count):
        roll = random.randint(1,6)
        if roll % 2 == 0:
            evens.append(roll)
        else:
            odds.append(roll)
        roll_string = roll_string + str(roll) + " "

    if modifier == "negative":
        mod = "-"
        if len(odds) > 0:
            roll_result = min(odds)
            if odds.count(roll_result) > 1:
                ands = " ...and " + str(odds.count(roll_result) - 1) + "x extra 'ands'!"
        else:
            roll_result = min(evens)
            if evens.count(roll_result) > 1:
                ands = " ...and " + str(evens.count(roll_result) - 1) + "x extra 'ands'!"
    else:
        if len(evens) > 0:
            roll_result = max(evens)
            if evens.count(roll_result) > 1:
                ands = " ...and " + str(evens.count(roll_result) - 1) + "x extra 'ands'!"
        else:
            roll_result = max(odds)
            if odds.count(roll_result) > 1:
                ands = " ...and " + str(odds.count(roll_result) - 1) + "x extra 'ands'!"
    chart = {
        6 : "Yes, and...",
        4 : "Yes.",
        2 : "Yes, but...",
        5 : "No, but...",
        3 : "No.",
        1 : "No, and...",
    }

    return "[FU" + mod + ": " + roll_string + "] " + chart[roll_result] + ands

# END FU

def howMuchWeighted():
    chart = {
        2 : "Almost entirely.",
        3 : "A lot.",
        4 : "More than expected.",
        5 : "A moderate amount.",
        6 : "Less than expected.",
        7 : "A little.",
        8 : "Scarcely any.",
    }

    roll = random.randint(1,4) + random.randint(1,4)

    result = "[How Much?] " + chart[roll]
    return result

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
    return "[Drama @" + text + "] " + result
