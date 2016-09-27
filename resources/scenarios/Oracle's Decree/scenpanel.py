# -*- coding: utf-8 -*
#
# Oracle's Decree Tutorial panel
#
# This will be called during main load and added to the oracle stack
#
# Text content from the adventure "Oracle's Decree" is Copyright © 2015 Michael Prescott
# http://creativecommons.org/licenses/by-nc/3.0/
# Find more adventure locations at http://blog.trilemma.com
#

import imports
from imports import *
import config

def exclude(self):
    return False

def onEnter(self):

    scenlogic.test()
    print("Oracle\'s Decree: updating my own widgets")
    pass

# add your widgets in here; see the gui for examples
def initPanel(self):

    self.decreeAItem = AccordionItem(title='Oracle\'s Decree', background_normal='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', background_selected='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', min_space = config.aiheight)

    self.decreeMainBox = BoxLayout(orientation='vertical')

    self.decreeMainBox.add_widget(Label(text="About This Adventure", size_hint=(1,1), font_size=config.basefont90))

    textList = ["Oracle's Decree text is Copyright © 2015 Michael Prescott, from http://blog.trilemma.com/ and licensed under CC-BY-NC.", "This is a tutorial intended to demonstrate some of the scenario features of Pythia."]

    for item in textList:
        label = Label(text=item, size_hint=(1,1), markup=True, font_name="Fantasque-Sans", font_size=config.basefont80)
        label.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        self.decreeMainBox.add_widget(label)

    self.decreeMainBox.add_widget(Label(text="Things to Keep In Mind", size_hint=(1,1), font_size=config.basefont90))

    textList = ["Unlike a traditional CYOA or gamebook, Pythia scenarios expect and encourage you to generate content within each scene or room.", "While you can play through a scenario straight, it will be more fun if you use all the tools at your disposal to flesh out each scene.", "You should interpret scenario options and exits broadly or in the context of your own content.", "If a later experience doesn't reconcile well with the canon you've already created, feel free to use edit mode to change things up! Or just go your own way -- it's up to you."]

    for item in textList:
        label = Label(text=item, size_hint=(1,1), markup=True, font_name="Fantasque-Sans", font_size=config.basefont80)
        label.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1] + 10))
        label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        self.decreeMainBox.add_widget(label)

    self.decreeMainBox.add_widget(Label(text="Buttons", size_hint=(1,1), font_size=config.basefont90))

    button = Button(text="Hear a rumor", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans', font_size=config.basefont80)
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=hearARumor)
    self.decreeMainBox.add_widget(button)

    item="If you get stuck, want to go back somewhere, or go off course and want to get back to the scenario, use the buttons below."
    label = Label(text=item, size_hint=(1,1), markup=True, font_name="Fantasque-Sans", font_size=config.basefont80)
    label.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1] + 10))
    label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
    self.decreeMainBox.add_widget(label)

    button = Button(text="List of Scenes", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name="Fantasque-Sans", font_size=config.basefont80)
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=listScenes)
    self.decreeMainBox.add_widget(button)

    button = Button(text="Safe Spot", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name="Fantasque-Sans", font_size=config.basefont80)
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=moveToStart)
    self.decreeMainBox.add_widget(button)

    self.decreeAItem.add_widget(self.decreeMainBox)

    return self.decreeAItem

# these functions catch events from the buttons up above and pass them to the appropriate logic functions

rumorList = ['In lost Pelaago, there is an oracle who knows all secrets.', 'Beyond the sands there is a fortress, last bastion against the scaled and treacherous Heelan.', 'There is a fortress out in the desert, used as a base by strange, lizard-like bandits.', 'In the desert, always carry holy water to sprinkle on your footsteps.']

def hearARumor(*args):
    self = args[0].self
    args[0].background_color = neutral
    updateCenterDisplay(self, '"' + random.choice(rumorList) + '"', 'bold')

def moveToStart(*args):
    self = args[0].self
    args[0].background_color = neutral
    safeexit = parseRefs("A door appears, leading to [[jump|safety|findstarsleigh]].")
    updateCenterDisplay(self, safeexit , 'bold')

def listScenes(*args):
    self = args[0].self
    args[0].background_color = neutral
    result = ""
    for key in config.scenario['jumpRefs']:
        result = result + "     " + "[[jump|" + key + "|" + key + "]]"
    scenes = parseRefs(result)
    updateCenterDisplay(self, scenes , 'bold')
