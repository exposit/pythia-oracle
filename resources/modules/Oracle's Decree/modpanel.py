# -*- coding: utf-8 -*
#
# sample user defined panel for a module; will be called during main load and added to the oracle stack
#
# just add your own widgets to initPanel, add any needed logic below, and put this in the module folder,
#
# check out logic.py for the expected formatting keywords
#
# Text content from the adventure "Oracle's Decree" is Copyright © 2015 Michael Prescott
# http://creativecommons.org/licenses/by-nc/3.0/
# Find more adventure locations at http://blog.trilemma.com
#

import imports
from imports import *
import config

def onEnter(self):

    modlogic.test()

    print("Sample Oracle: updating my own widgets")

    # remember to modify the unique config for your module to include any necessary variables

    pass

# add your widgets in here; see the gui for examples
def initPanel(self):

    self.sampleAItem = AccordionItem(title='Module A Panel', background_selected= os.sep + 'resources' + os.sep + "ui_images" + os.sep + 'invisible.png', min_space=config.aiheight)

    self.sampleMainBox = BoxLayout(orientation='vertical')

    self.sampleMainBox.add_widget(Label(text="Label", size_hint=(1,1)))

    button = Button(text="Hear a rumor", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=hearARumor)
    self.sampleMainBox.add_widget(button)

    button = Button(text="Encounters (every 12 miles)", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=overlandEncounter)
    self.sampleMainBox.add_widget(button)

    # this label is changed by a persistent variable on enter
    self.tempLabel = Label(text='This will be changed on enter!', size_hint=(1,.12))
    self.sampleMainBox.add_widget(self.tempLabel)

    # this button piggybacks on an existing function, in this case, rolling dice
    button = Button(text="1d1000", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=testFunction)
    self.sampleMainBox.add_widget(button)

    # this button does its own thing and but updates the center display as normal
    button = Button(text="Choice", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=testFunctionTwo)
    self.sampleMainBox.add_widget(button)

    # this button just prints hello
    button = Button(text="Hello", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=testFunctionThree)
    self.sampleMainBox.add_widget(button)

    self.sampleAItem.add_widget(self.sampleMainBox)

    return self.sampleAItem

# these functions catch events from the buttons up above and pass them to the appropriate logic functions

rumorList = ['In lost Pelaago, there is an oracle who knows all secrets.', 'Beyond the sands there is a fortress, last bastion against the scaled and treacherous Heelan.', 'There is a fortress out in the desert, used as a base by strange, lizard-like bandits.', 'In the desert, always carry holy water to sprinkle on your footsteps.']

def hearARumor(*args):
    self = args[0].self
    args[0].background_color = neutral
    updateCenterDisplay(self, '"' + random.choice(rumorList) + '"', 'bold')

def overlandEncounter(*args):
    self = args[0].self
    args[0].background_color = neutral

    #roll = random.randint(0,9)
    roll = 1
    result = config.modvar['overlandEncounterChart'][roll][0]

    if roll == 2 or roll == 5 or roll == 6 or roll == 7 or roll == 10:
        config.modvar['overlandEncounterChart'][roll][0] = "Water Shades"

    if result == "Water Shades":
        result = result + " [" + str(random.randint(1,2)) + "] "
    elif result == "Heelan Bandits":
        result = result + " [" + str(random.randint(1,3)) + "] "
    elif result == "Sand Sprites":
        result = result + " [" + str(random.randint(1,6)) + "] "

    if result == "A field of Sand Domes":
        config.modvar['fishattack'] = random.choice([True, False])

    updateCenterDisplay(self, result, 'result')

    refPress(config.textLabelArray[-1], config.modvar['overlandEncounterChart'][roll][1])

# this calls one of the main functions in logic.py instead of in this file
def testFunction(*args):
    self = args[0].self
    args[0].background_color = neutral
    updateCenterDisplay(self, rollDice(args[0].text), 'bold_italic')

# this just does stuff directly, no intermediary function
def testFunctionTwo(*args):
    self = args[0].self
    args[0].background_color = neutral
    chart = ["eenie", "meenie", "miney", "moe", "tiger"]
    # uncomment this to echo back the text in the text input
    #if len(self.textInput.text) > 0:
    #    updateCenterDisplay(self, self.textInput.text, 'bold_italic')
    updateCenterDisplay(self, random.choice(chart), 'oracle')

    # uncomment this to run the save routine
    #quicksave(self, config.curr_game_dir)

    # uncomment this to clear the main text input
    #self.textInput.text = ""

# this updates a label's text
def testFunctionThree(*args):
    args[0].background_color = neutral
    for arg in args:
        print arg
    args[0].self.tempLabel.text = "hello " + tertiaryFunction() + " " + str(random.randint(1,1000))

# sample logic
def tertiaryFunction():
    return "world"
