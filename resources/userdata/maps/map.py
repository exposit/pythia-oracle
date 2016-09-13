# -*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------------------
#
#  Basic Map Panel
#
##---------------------------------------------------------------------------------------------------

import imports
from imports import *
import config

# set this to False to enable this panel
def exclude():
    return False

def onEnter(self):
    print("Map panel: updating my own widgets")
    pass

# add your widgets in here; see the gui for examples
def initPanel(self):

    self.mapAItem = AccordionItem(title='Map', background_selected= os.sep + 'resources' + os.sep + "ui_images" + os.sep + 'invisible.png', min_space=config.aiheight)

    self.mapMainBox = BoxLayout(orientation='vertical')

    self.mapGrid = GridLayout(cols=15)
    mapLength = 5 * 5 * 3

    # two kinds of button; room button or direction button
    for i in range(mapLength):
        mapbutton = Button(text="", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans', font_size=config.basefont75)
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=testFunctionThree)
        self.mapMainBox.add_widget(button)

    # Button to spawn new map, maybe one to delete this map with confirmation
    button = Button(text="New Map", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    #button.bind(on_release=testFunctionThree)
    self.mapMainBox.add_widget(button)

    self.mapAItem.add_widget(self.mapMainBox)

    return self.mapAItem
