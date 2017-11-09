# -*- coding: utf-8 -*self
#
# skeleton user defined panel
#
# Rename this file something unique, like "monsters.py"; don't change anything else in this file.
# Then make a text file named the same as this file with "_data.txt" at the end, like "monsters_data.txt".
# The *_data file will hold all of your custom data.
#
# A button will be generated for each section in the data file; pressing it will return one option
# from those provided in the data file.
#
#    A line starting with "##" will be considered a button label
#    A line starting with "#" will be ignored as a comment
#    Anything else is considered part of the list of options to choose from for that section.
#
# Look at the skeleton_data.txt for an example.
#

import imports
from imports import *
import config

# set this to False to enable this panel
def exclude():
    return False

def onEnter(self):
    #print("Skeleton Data loading...")
    pass

# add your widgets in here; see the gui for examples
def initPanel(self):

    try:
        vari = os.path.realpath(__file__).split(os.sep)[-1].split('.')[0]
        title = vari.title()
    except:
        title = "Custom"

    self.skeletonAItem = AccordionItem(title=title, background_normal='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', background_selected='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', min_space = config.aiheight)

    self.skeletonMainBox = BoxLayout(orientation='vertical')

    #self.skeletonMainBox.add_widget(Label(text="Label", size_hint=(1,1)))

    try:

        fname = "." + os.sep + "resources" + os.sep + "panels" + os.sep + "custom" + os.sep + vari + "_data.txt"

        with open(fname) as f:
            self.content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        self.content = [x.strip() for x in self.content]
        self.content = [x for x in self.content if x]
    except:
        self.content = []
        pass

    for line in self.content:
        if "##" in line:
            # this button does its own thing and but updates the center display as normal
            button = Button(text=line.replace("##", ""), size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
            button.self = self
            button.source = self.content.index(line)
            button.bind(on_press=self.pressGenericButton)
            button.bind(on_release=getElement)
            self.skeletonMainBox.add_widget(button)

    self.skeletonAItem.add_widget(self.skeletonMainBox)

    return self.skeletonAItem

# these functions catch events from the buttons up above

def getElement(*args):
    self = args[0].self
    args[0].background_color = neutral
    source = args[0].source

    buttondata = []

    tmpcontent = self.content[source:]

    for line in tmpcontent:
        if "##" in line and len(buttondata) == 0:
            # this is the first label
            pass
        elif "##" in line:
            # this is the end of this chunk
            break
        elif "#" in line:
            # this is a comment; ignore it
            pass
        else:
            # this is content
            buttondata.append(line)

    if len(buttondata) > 0:
        chart = buttondata

    updateCenterDisplay(self, random.choice(chart), 'oracle')
