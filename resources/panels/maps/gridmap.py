# -*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------------------
#
#  Grid Map Panel
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

    self.gmapAItem = AccordionItem(title='Grid Map', background_normal='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', background_selected='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', min_space = config.aiheight)

    self.gmapMainBox = BoxLayout(orientation='vertical')

    self.gmapTitleBox = BoxLayout(orientation='horizontal', size_hint=(1,.07))

    self.gmapTitle = TextInput(text="", size_hint=(.75,1), font_size=config.basefont, background_color=(0,0,0,.5), foreground_color=(1,1,1,1), multiline=False)
    self.gmapTitle.self = self
    self.gmapTitleBox.add_widget(self.gmapTitle)

    button = Button(text="Save", size_hint=(.25,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=saveMap)
    self.gmapTitleBox.add_widget(button)

    self.gmapMainBox.add_widget(self.gmapTitleBox)

    self.gmapScroll = ScrollView(size_hint=(1, 1))

    self.gmapGrid = GridLayout(cols=26, spacing=5, size_hint=(None, None))
    self.gmapGrid.bind(minimum_height=self.gmapGrid.setter('height'))
    self.gmapGrid.bind(minimum_width=self.gmapGrid.setter('width'))

    count = -1
    for i in range(26*24):

        button = TextInput(text="", size_hint=(None,None), size=('25dp', '25dp'), font_size=config.basefont75, background_color=(0,0,0,1), foreground_color=(1,1,1,1), halign="center", valign="center")
        button.self = self
        button.count = 0
        self.gmapGrid.add_widget(button)
        button.bind(focus=changeColor)
        button.bind(text=changeText)
        config.tempGmapArray.append(button)

    self.gmapScroll.add_widget(self.gmapGrid)
    self.gmapMainBox.add_widget(self.gmapScroll)

    self.gmapNavBox = BoxLayout(orientation='horizontal', size_hint=(1,.15))

    tempVals = []
    for i in config.gmapArray:
        tempVals.append(i)

    self.gmapSpinner = Spinner(
    text='Blank',
    values=tempVals,
     size_hint=(.75,1),
    )
    self.gmapSpinner.self = self
    self.gmapSpinner.bind(text=loadMap)

    self.gmapNavBox.add_widget(self.gmapSpinner)

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

    self.gmapNavGrid = GridLayout(cols=3, size_hint=(.25,1))
    for i in range(9):
        button = Button(text=navList[i][0], size=(10,10), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.self = self
        button.adjx = navList[i][1]
        button.adjy = navList[i][2]
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=moveMap)
        self.gmapNavGrid.add_widget(button)

    self.gmapNavBox.add_widget(self.gmapNavGrid)

    self.gmapMainBox.add_widget(self.gmapNavBox)

    button = Button(text="New Map", size_hint=(1,.10), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=makeNewMap)
    self.gmapMainBox.add_widget(button)

    button = Button(text="Full Map", size_hint=(1,.10), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=fullMapPopup)
    self.gmapMainBox.add_widget(button)

    self.miniMapButton = Button(text="Show Minimap", size_hint=(1,.10), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    self.miniMapButton.self = self
    self.miniMapButton.bind(on_press=self.pressGenericButton)
    self.miniMapButton.bind(on_release=toggleMiniMap)
    self.gmapMainBox.add_widget(self.miniMapButton)

    self.miniMapGrid = GridLayout(cols=26)

    self.gmapAItem.add_widget(self.gmapMainBox)

    # popup for showing the full map
    self.displayGmapGrid = GridLayout(cols=26, spacing=5, size_hint=(1, 1))

    self.displayGmapPopup = Popup(title='Map',
        content=self.displayGmapGrid,
        size_hint=(None, None))
    self.displayGmapPopup.self = self
    self.displayGmapPopup.bind(on_open=copyMapToDisplay)
    self.displayGmapPopup.bind(on_dismiss=saveAsPng)
    self.displayGmapPopup.size=(800, 800)

    return self.gmapAItem

def changeColor(field, value):
    if value:
        if field.background_color == [0,0,0,1]:
            field.background_color = [1,1,1,1]
            field.foreground_color = [0,0,0,1]
        else:
            field.foreground_color = [1,1,1,1]
            field.background_color = [0,0,0,1]
        #genMiniMap(field.self)
        #saveMap(field.self)
    else:
        pass

def changeText(*args):
    pass

def makeNewMap(source):

    try:
        self = source.self
        source.background_color = neutral
    except:
        self = source

    if len(self.gmapTitle.text) > 0:
        saveMap(self)

    for i in config.tempGmapArray:
        i.text = ""
        i.background_color = [0,0,0,1]

    self.gmapTitle.text = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

def loadMap(spinner, value):

    self = spinner.self

    makeNewMap(self)

    for i in range(len(config.gmapArray[value])):
        config.tempGmapArray[i].text = config.gmapArray[value][i][0]
        config.tempGmapArray[i].background_color = config.gmapArray[value][i][1]

    self.gmapTitle.text = value

    genMiniMap(self)

def saveMap(source):

    try:
        self = source.self
        source.background_color = neutral
    except:
        self = source

    if self.gmapTitle.text == "":
        self.gmapTitle.text = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

    maptitle = self.gmapTitle.text

    config.gmapArray[maptitle] = []

    for element in config.tempGmapArray:
        config.gmapArray[maptitle].append([element.text, element.background_color])

    quicksave(self, config.curr_game_dir)

    tempVals = []
    for i in config.gmapArray:
        tempVals.append(i)
    self.gmapSpinner.values = tempVals

    genMiniMap(self)

def moveMap(*args):

    args[0].background_color = neutral
    self = args[0].self
    adjx = args[0].adjx
    adjy = args[0].adjy

    currx = self.gmapScroll.scroll_x
    curry = self.gmapScroll.scroll_y

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

    self.gmapScroll.scroll_x = newx
    self.gmapScroll.scroll_y = newy

def toggleMiniMap(*args):

    args[0].background_color = neutral
    self = args[0].self

    if args[0].text == 'Show Minimap':

        args[0].text = 'Close Minimap'

        genMiniMap(self)

        self.gmapMainBox.add_widget(self.miniMapGrid)

    else:
        args[0].text = 'Show Minimap'
        self.gmapMainBox.remove_widget(self.miniMapGrid)

def genMiniMap(self):

    self.miniMapGrid.clear_widgets()

    for field in config.tempGmapArray:
        if field.text == "":
            text = " "
        else:
            text = field.text[:1]

        fgcolor = field.foreground_color
        bgcolor = field.background_color

        button = Button(text=text, font_name='Cormorant', font_size=config.basefont90, background_color=bgcolor, color=fgcolor, size=(10,10))

        self.miniMapGrid.add_widget(button)

def fullMapPopup(button, *args):
    button.background_color = neutral
    self = button.self
    self.displayGmapPopup.open()

def copyMapToDisplay(popup):
    # populate grid properly
    self = popup.self

    for i in config.tempGmapArray:
        i.parent.remove_widget(i)
        self.displayGmapGrid.add_widget(i)

def saveAsPng(popup):

    self = popup.self

    # save png
    if self.gmapTitle.text == "":
        maptitle = "unknown"
    else:
        maptitle = self.gmapTitle.text

    self.displayGmapGrid.export_to_png(config.curr_game_dir + "grid_" + maptitle + ".png")

    for i in config.tempGmapArray:
        i.parent.remove_widget(i)
        self.gmapGrid.add_widget(i)
