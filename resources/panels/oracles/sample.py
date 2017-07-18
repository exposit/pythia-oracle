# -*- coding: utf-8 -*self
#
# sample user defined panel
#
# just add your own widgets to initPanel, add any needed logic below, and put this in the panels folder,
# in whichever of the two folders applies (generator or oracle)
#
# check out logic.py for the expected formatting keywords
#

import imports
from imports import *
import config

# set this to False to enable this panel
def exclude():
    return True

def onEnter(self):
    print("Sample Oracle: updating my own widgets")
    try:
        self.tempLabel.text = str(config.user['holder'])
    except:
        self.tempLabel.text = "No variable found -- this time!"
        config.user['holder'] = "But now it is!"
    pass

# add your widgets in here; see the gui for examples
def initPanel(self):

    self.sampleAItem = AccordionItem(title='Sample', background_normal='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', background_selected='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', min_space = config.aiheight)

    self.sampleMainBox = BoxLayout(orientation='vertical')

    self.sampleMainBox.add_widget(Label(text="Label", size_hint=(1,1)))

    # this label is changed by a persistent variable on enter
    self.tempLabel = Label(text='This will be changed on enter!', size_hint=(1,.12))
    self.sampleMainBox.add_widget(self.tempLabel)

    # this button piggybacks on an existing function, in this case, rolling dice
    button = Button(text="1d1000", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=testFunction)
    self.sampleMainBox.add_widget(button)

    # this button does its own thing and but updates the center display as normal
    button = Button(text="Choice", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=testFunctionTwo)
    self.sampleMainBox.add_widget(button)

    # this button just prints hello
    button = Button(text="Hello", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=testFunctionThree)
    self.sampleMainBox.add_widget(button)

    self.sampleAItem.add_widget(self.sampleMainBox)

    return self.sampleAItem

# these functions catch events from the buttons up above and pass them to the appropriate logic functions

# this calls one of the main functions in logic.py instead of in this file
def testFunction(*args):
    self = args[0].self
    args[0].background_color = neutral
    updateCenterDisplay(self, rollDice(args[0].text), 'result')

# this just does stuff directly, no intermediary function
def testFunctionTwo(*args):
    self = args[0].self
    args[0].background_color = neutral
    chart = ["eenie", "meenie", "miney", "moe", "tiger"]
    # uncomment this to echo back the text in the text input
    #if len(self.textInput.text) > 0:
    #    updateCenterDisplay(self, self.textInput.text, 'result')
    updateCenterDisplay(self, random.choice(chart), 'oracle')

    # uncomment this to run the save routine
    #quicksave(self, config.curr_game_dir)

    # uncomment this to clear the main text input
    #self.textInput.text = ""

# this updates a label's text
def testFunctionThree(*args):
    args[0].background_color = neutral
    for arg in args:
        print(arg)
    args[0].self.tempLabel.text = "hello " + tertiaryFunction() + " " + str(random.randint(1,1000))

# sample logic
def tertiaryFunction():
    return "world"
