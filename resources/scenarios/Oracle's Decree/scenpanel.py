# -*- coding: utf-8 -*
#
# decree user defined panel for a scenario; will be called during main load and added to the oracle stack
#
# just add your own widgets to initPanel, add any needed logic below, and put this in the scenario folder,
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

    print("decree Oracle: updating my own widgets")

    # remember to modify the unique config for your scenario to include any necessary variables

    pass

# add your widgets in here; see the gui for examples
def initPanel(self):

    self.decreeAItem = AccordionItem(title='Oracle\'s Decree', background_selected= os.sep + 'resources' + os.sep + "ui_images" + os.sep + 'invisible.png', min_space=config.aiheight)

    self.decreeMainBox = BoxLayout(orientation='vertical')

    self.decreeMainBox.add_widget(Label(text="About This Adventure", size_hint=(1,1)))

    longtextA = "Oracle's Decree is based on a one page dungeon from http://blog.trilemma.com/, licensed under CC-BY-NC."
    longtextA = longtextA + "\nIt's a tutorial for intended to show off some of the scenario features of Pythia. It is site-based, though event-based adventures are equally feasible!"

    self.decreeMainBox.add_widget(Label(text=longtextA, size_hint=(1,1), markup=True))

    self.decreeMainBox.add_widget(Label(text="Things to Remember", size_hint=(1,1)))

    longtextB = "Pythia really shines when you put your own spin on things -- whenever you are presented with a scene or room, be sure to use all the tools at your disposal (oracles, generators, your own imagination) to flesh out the scene and determine what happens."
    longtextB = "Unlike a traditional CYOA or gamebook, you will be creating lots of content in between scenes or rooms. Interpret scenario options broadly or in the context of your own content."
    longtextB = longtextB + "\nIf a later experience doesn't reconcile well with the canon you've already created, feel free to use edit mode to change things up! Or go your own way -- it's up to you."

    self.decreeMainBox.add_widget(Label(text=longtextB, size_hint=(1,1), markup=True))

    self.decreeMainBox.add_widget(Label(text="Buttons", size_hint=(1,1)))

    button = Button(text="Hear a rumor", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=hearARumor)
    self.decreeMainBox.add_widget(button)

    button = Button(text="Encounters (every 12 miles)", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=overlandEncounter)
    self.decreeMainBox.add_widget(button)

    # this label is changed by a persistent variable on enter
    self.tempLabel = Label(text='This will be changed on enter!', size_hint=(1,.12))
    self.decreeMainBox.add_widget(self.tempLabel)

    # this button piggybacks on an existing function, in this case, rolling dice
    button = Button(text="1d1000", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=testFunction)
    self.decreeMainBox.add_widget(button)

    # this button does its own thing and but updates the center display as normal
    button = Button(text="Choice", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=testFunctionTwo)
    self.decreeMainBox.add_widget(button)

    # this button just prints hello
    button = Button(text="Hello", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=testFunctionThree)
    self.decreeMainBox.add_widget(button)

    self.decreeAItem.add_widget(self.decreeMainBox)

    return self.decreeAItem

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
    result = config.scenario['overlandEncounterChart'][roll][0]

    if roll == 2 or roll == 5 or roll == 6 or roll == 7 or roll == 10:
        config.scenario['overlandEncounterChart'][roll][0] = "Water Shades"

    if result == "Water Shades":
        result = result + " [" + str(random.randint(1,2)) + "] "
    elif result == "Heelan Bandits":
        result = result + " [" + str(random.randint(1,3)) + "] "
    elif result == "Sand Sprites":
        result = result + " [" + str(random.randint(1,6)) + "] "

    if result == "A field of Sand Domes":
        config.scenario['fishattack'] = random.choice([True, False])

    updateCenterDisplay(self, result, 'result')

    refPress(config.textLabelArray[-1], config.scenario['overlandEncounterChart'][roll][1])

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

# decree logic
def tertiaryFunction():
    return "world"
