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

    self.mapAItem = AccordionItem(title='Diagram Map', background_normal='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', background_selected='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', min_space = config.aiheight)

    self.mapMainBox = BoxLayout(orientation='vertical')

    self.mapTitleBox = BoxLayout(orientation='horizontal', size_hint=(1,.07))

    self.mapTitle = TextInput(text="", size_hint=(.75,1), font_size=config.basefont, background_color=(0,0,0,.5), foreground_color=(1,1,1,1), multiline=False)
    self.mapTitle.self = self
    self.mapTitleBox.add_widget(self.mapTitle)

    button = Button(text="Save", size_hint=(.25,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=saveMap)
    self.mapTitleBox.add_widget(button)

    self.mapMainBox.add_widget(self.mapTitleBox)

    self.mapScroll = ScrollView(size_hint=(1, 1))

    self.mapGrid = GridLayout(cols=21, spacing=5, size_hint=(None, None))
    self.mapGrid.bind(minimum_height=self.mapGrid.setter('height'))
    self.mapGrid.bind(minimum_width=self.mapGrid.setter('width'))

    makeGrid(self, self.mapGrid)

    self.mapScroll.add_widget(self.mapGrid)
    self.mapMainBox.add_widget(self.mapScroll)

    self.mapNavBox = BoxLayout(orientation='horizontal', size_hint=(1,.15))

    tempVals = []
    for i in config.mapArray:
        tempVals.append(i)

    self.mapSpinner = Spinner(
    text='Blank',
    values=tempVals,
     size_hint=(.75,1),
    )
    self.mapSpinner.self = self
    self.mapSpinner.bind(text=loadMap)

    self.mapNavBox.add_widget(self.mapSpinner)

    navList = [
        ['NW', -.2, +.2 ],
        ['N',    0, +.2 ],
        ['NE', +.2, +.2 ],
        ['W',  -.2,   0 ],
        [' ',    0,   0 ],
        ['E',  +.2,   0 ],
        ['SW', -.2, -.2 ],
        ['S',    0, -.2 ],
        ['SE', +.2, -.2 ],
    ]

    self.mapNavGrid = GridLayout(cols=3, size_hint=(.25,1))
    for i in range(9):
        button = Button(text=navList[i][0], size=(10,10), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.self = self
        button.adjx = navList[i][1]
        button.adjy = navList[i][2]
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=moveMap)
        self.mapNavGrid.add_widget(button)

    self.mapNavBox.add_widget(self.mapNavGrid)

    self.mapMainBox.add_widget(self.mapNavBox)

    button = Button(text="New Map", size_hint=(1,.10), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=makeNewMap)
    self.mapMainBox.add_widget(button)

    button = Button(text="Full Map", size_hint=(1,.10), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=fullMapPopup)
    self.mapMainBox.add_widget(button)

    self.miniMapButton = Button(text="Show Minimap", size_hint=(1,.10), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    self.miniMapButton.self = self
    self.miniMapButton.bind(on_press=self.pressGenericButton)
    self.miniMapButton.bind(on_release=toggleMiniMap)
    self.mapMainBox.add_widget(self.miniMapButton)

    self.miniMapGrid = GridLayout(cols=21)

    self.mapAItem.add_widget(self.mapMainBox)

    self.displayMapGrid = GridLayout(cols=21, spacing=5, size_hint=(1, 1))

    # popup for showing the map
    self.displayPopup = Popup(title='Map',
        content=self.displayMapGrid,
        size_hint=(None, None))
    self.displayPopup.self = self
    self.displayPopup.bind(on_open=copyMapToDisplay)
    self.displayPopup.bind(on_dismiss=saveAsPng)
    self.displayPopup.size=(800, 800)

    return self.mapAItem

def makeGrid(self, holder):

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
                button = TextInput(text="", size_hint=(None,None), size=('40dp', '40dp'), font_size=config.basefont75, background_color=(0,0,0,.5), foreground_color=(1,1,1,1), halign="center", valign="center")
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

        holder.add_widget(button)

        config.tempMapArray.append(button)

def changeDir(button, *args):

    button.background_color = neutral
    self = button.self
    newtext = button.text

    dirList = ["X","↔","↕","←","↖","↑","↗","→","↘","↓","↙"]

    try:
        index = dirList.index(newtext)
    except:
        index = 0

    if index < len(dirList)-1:
        newtext = dirList[index+1]
    else:
        newtext = dirList[0]

    button.text = str(newtext)
    #saveMap(self)

def makeNewMap(source):

    try:
        self = source.self
        source.background_color = neutral
    except:
        self = source

    #saveMap(self)

    for i in config.tempMapArray:
        i.text = ""

    self.mapTitle.text = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

def loadMap(spinner, value):

    self = spinner.self

    makeNewMap(self)

    for i in range(len(config.mapArray[value])):
        config.tempMapArray[i].text = config.mapArray[value][i]

    self.mapTitle.text = value

    genMiniMap(self)

def saveMap(source):

    try:
        self = source.self
        source.background_color = neutral
    except:
        self = source

    if self.mapTitle.text == "":
        self.mapTitle.text = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

    maptitle = self.mapTitle.text
    #print("Maptitle", maptitle)

    config.mapArray[maptitle] = []

    for element in config.tempMapArray:
        config.mapArray[maptitle].append(element.text)

    quicksave(self, config.curr_game_dir)

    tempVals = []
    for i in config.mapArray:
        tempVals.append(i)
    self.mapSpinner.values = tempVals

    genMiniMap(self)

def moveMap(*args):

    args[0].background_color = neutral
    self = args[0].self
    adjx = args[0].adjx
    adjy = args[0].adjy

    currx = self.mapScroll.scroll_x
    curry = self.mapScroll.scroll_y

    newx = currx + adjx
    newy = curry + adjy

    if newx > 1:
        newx = 1.
    elif newx < 0:
        newx = 0.

    if newy > 1:
        newy = 1.
    elif newy < 0:
        newy = 0.

    self.mapScroll.scroll_x = newx
    self.mapScroll.scroll_y = newy

def toggleMiniMap(*args):

    args[0].background_color = neutral
    self = args[0].self

    if args[0].text == 'Show Minimap':

        args[0].text = 'Close Minimap'

        genMiniMap(self)

        self.mapMainBox.add_widget(self.miniMapGrid)

    else:
        args[0].text = 'Show Minimap'
        self.mapMainBox.remove_widget(self.miniMapGrid)

def genMiniMap(self):

    self.miniMapGrid.clear_widgets()

    for button in config.tempMapArray:
        if button.text == "":
            text = " "
        else:
            if button.subtype == 'arrow':
                text = button.text
            else:
                text = button.text[:1]
        label = Label(text=text, font_name='Cormorant', font_size=config.basefont90)
        self.miniMapGrid.add_widget(label)

def fullMapPopup(button, *args):
    button.background_color = neutral
    self = button.self
    self.displayPopup.open()

def copyMapToDisplay(popup):
    # populate grid properly
    self = popup.self

    for i in config.tempMapArray:
        i.parent.remove_widget(i)
        self.displayMapGrid.add_widget(i)

def saveAsPng(popup):

    self = popup.self

    # save png
    if self.mapTitle.text == "":
        maptitle = "unknown"
    else:
        maptitle = self.mapTitle.text

    self.displayMapGrid.export_to_png(config.curr_game_dir + "dd_" + maptitle + ".png")

    for i in config.tempMapArray:
        i.parent.remove_widget(i)
        self.mapGrid.add_widget(i)
