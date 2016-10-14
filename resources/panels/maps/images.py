# -*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------------------
#
#  Images Panel
#
##---------------------------------------------------------------------------------------------------

import imports
from imports import *
import config

# set this to False to enable this panel
def exclude():
    return False

def onEnter(self):

    imgLabelArray = []
    # grab all images in the current directory's img folder
    if os.path.exists(config.curr_game_dir + "images"):
        images = glob.glob(config.curr_game_dir + "images" + os.sep + "*")
        for img in images:
            config.imgLabelArray.append( TextInput(text="", multiline=False, size_hint=(None, None), height=config.tallheight, font_size=config.basefont, font_name='Fantasque-Sans', background_color=neutral, foreground_color=styles.textcolor) )
            self.imgGrid.add_widget(config.imgLabelArray[-1])

            pic = Image(source=img, size_hint=(None, None))
            pic.size = pic.texture.size
            if pic.texture.width > self.imgAItem.width:
                ratio = self.imgAItem.width/pic.texture.width
                pic.width = self.imgAItem.width
                pic.height = pic.texture.height * ratio

            pic.height = pic.height - 50
            pic.width = pic.width - 50
            self.imgGrid.add_widget(pic)

            config.imgLabelArray.append( TextInput(text="", multiline=False, size_hint=(None, None), height=config.tallheight, font_size=config.basefont, font_name='Fantasque-Sans', background_color=neutral, foreground_color=styles.textcolor) )
            self.imgGrid.add_widget(config.imgLabelArray[-1])

            self.imgGrid.add_widget(Label(text="", size_hint=(None, None), height=config.tallheight))

        if len(config.imgTextArray) > 0:
            for i in range(len(config.imgTextArray)):
                if i <= len(config.imgLabelArray):
                    config.imgLabelArray[i].text = config.imgTextArray[i]
    else:
        self.imgAItem.parent.remove_widget(self.imgAItem)

def initPanel(self):

    self.imgAItem = AccordionItem(title='Images', background_normal='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', background_selected='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', min_space = config.aiheight)

    self.imgMainBox = BoxLayout(orientation='vertical')

    self.imgScroll = ScrollView(size_hint=(1, 1))

    self.imgGrid = GridLayout(cols=1, spacing=5, size_hint=(None, None))
    self.imgGrid.bind(minimum_height=self.imgGrid.setter('height'))
    self.imgGrid.bind(minimum_width=self.imgGrid.setter('width'))

    self.imgScroll.add_widget(self.imgGrid)
    self.imgMainBox.add_widget(self.imgScroll)
    self.imgAItem.add_widget(self.imgMainBox)

    return self.imgAItem
