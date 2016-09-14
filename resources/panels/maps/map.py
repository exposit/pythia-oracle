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

    self.mapTitle = TextInput(text="", size_hint=(1,.10), font_size=config.basefont, background_color=(0,0,0,.5), foreground_color=(1,1,1,1), multiline=False)
    self.mapTitle.self = self
    self.mapMainBox.add_widget(self.mapTitle)

    self.mapScroll = ScrollView(size_hint=(1, 1))

    self.mapGrid = GridLayout(cols=21, rows=21, spacing=5, size_hint=(None, None))
    self.mapGrid.bind(minimum_height=self.mapGrid.setter('height'))
    self.mapGrid.bind(minimum_width=self.mapGrid.setter('width'))

    count = -1
    for i in range(441):
        subtype = ""
        ind = i % 21
        if ind == 0:
            count = count + 1

        if count % 2 == 0:
            subtype = "arrow"
            button = Button(text="", size_hint=(None,None), size=('20dp', '20dp'), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Cormorant', font_size=config.tallheight)
            button.self = self
            button.subtype = subtype
            button.bind(on_press=self.pressGenericButton)
            button.bind(on_release=changeDir)
        else:
            if ind % 2 != 0:
                subtype = "room"
                button = TextInput(text="", size_hint=(None,None), size=('40dp', '40dp'), font_size=config.basefont75, background_color=(0,0,0,.5), foreground_color=(1,1,1,1))
                button.self = self
                button.subtype = "room"
                #roomArray.append(button)
            else:
                subtype = "arrow"
                button = Button(text="", size_hint=(None,None), size=('20dp', '20dp'), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Cormorant', font_size=config.tallheight)
                button.self = self
                button.subtype = subtype
                button.bind(on_press=self.pressGenericButton)
                button.bind(on_release=changeDir)

        self.mapGrid.add_widget(button)
        config.tempMapArray.append(button)

    self.mapScroll.add_widget(self.mapGrid)
    self.mapMainBox.add_widget(self.mapScroll)

    button = Button(text="Save Map", size_hint=(1,.10), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=saveMap)
    self.mapMainBox.add_widget(button)

    tempVals = []
    for i in config.mapArray:
        tempVals.append(i)

    self.mapSpinner = Spinner(
    text='Blank',
    values=tempVals,
     size_hint=(1,.10),
    )
    self.mapSpinner.self = self
    self.mapSpinner.bind(text=loadMap)

    self.mapMainBox.add_widget(self.mapSpinner)

    button = Button(text="New Map", size_hint=(1,.10), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=makeNewMap)
    self.mapMainBox.add_widget(button)

    self.mapAItem.add_widget(self.mapMainBox)

    return self.mapAItem

def changeDir(button, *args):

    button.background_color = neutral
    self = button.self
    newtext = button.text

    dirList = ["←","↖","↑","↗","→","↘","↓","↙","↔","↕","✕"]

    try:
        index = dirList.index(newtext)
    except:
        index = 0

    if index < len(dirList)-1:
        newtext = dirList[index+1]
    else:
        newtext = dirList[0]

    button.text = str(newtext)
    saveMap(self)

def makeNewMap(source):

    try:
        self = source.self
        source.background_color = neutral
    except:
        self = source

    saveMap(self)

    for i in config.tempMapArray:
        i.text = ""

    self.mapTitle.text = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

def loadMap(spinner, value):

    self = spinner.self

    makeNewMap(self)

    for i in range(len(config.mapArray[value])):
        config.tempMapArray[i].text = config.mapArray[value][i]

    self.mapTitle.text = value

def saveMap(source):

    try:
        self = source.self
        source.background_color = neutral
    except:
        self = source

    if self.mapTitle.text == "":
        self.mapTitle.text = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

    maptitle = self.mapTitle.text

    config.mapArray[maptitle] = []

    for element in config.tempMapArray:
        config.mapArray[maptitle].append(element.text)

    tempVals = []
    for i in config.mapArray:
        tempVals.append(i)
    self.mapSpinner.values = tempVals
