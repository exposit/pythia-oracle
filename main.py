#!/usr/bin/env python
#-*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------
#  Main Screen
#
##---------------------------------------------------------------------------------------

from imports import *
import config

class ScrollableLabel(ScrollView):
    text = StringProperty('')

class MainScreen(Screen):

    def __init__(self,**kwargs):
        super (MainScreen, self).__init__(**kwargs)

##---------------------------------------------------------------------------------------
#  general
##---------------------------------------------------------------------------------------

        # set background; to have no background, delete or move the background images
        texture = ObjectProperty()

        #try:
        #    self.texture = Image(source='resources/bg_main/' + styles.curr_palette["name"].replace (" ", "_") + '_5.png').texture
        #    self.texture.wrap = 'repeat'
        #    self.texture.uvsize = (4, 4)

        #    with self.canvas:
        #        Rectangle(pos=(0,0), size=Window.size, texture=self.texture)
        #except:
        #    pass

        self.mainBox = BoxLayout(orientation="horizontal")
        self.add_widget(self.mainBox)

        # comment this out to return to default text input behavior, ie, enter while focused on main textinput does nothing
        Window.bind(on_key_down=self.key_action)

        Button.background_down=""

##---------------------------------------------------------------------------------------
#  SIDE PANEL - right horizontal stack
##---------------------------------------------------------------------------------------

        self.leftAccordion = Accordion(orientation='horizontal', size_hint=(.6, 1), min_space='28dp')
        self.mainBox.add_widget(self.leftAccordion)

##---------------------------------------------------------------------------------------
#  Center status across top
##---------------------------------------------------------------------------------------

        self.centerBox = BoxLayout(orientation='vertical', padding=(10,10))

        self.statusBox = BoxLayout(orientation='horizontal', size_hint=(1,.07), padding=(10,10))

        self.trackBox = BoxLayout(orientation="horizontal", size_hint=(.25,1))

        self.trackDownButton = Button(text="-", size_hint=(.5,1), background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.trackDownButton.bind(on_press=self.pressGenericButton)
        self.trackDownButton.bind(on_release=self.releaseTrackerDown)
        self.trackBox.add_widget(self.trackDownButton)

        self.trackLabel = Label(text="0")
        self.trackBox.add_widget(self.trackLabel)

        self.trackUpButton = Button(text="+", size_hint=(.5,1), background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.trackUpButton.bind(on_press=self.pressGenericButton)
        self.trackUpButton.bind(on_release=self.releaseTrackerUp)
        self.trackBox.add_widget(self.trackUpButton)

        self.statusBox.add_widget(self.trackBox)

        self.bookmarkBox = BoxLayout(orientation="horizontal", size_hint=(.75,1))
        for i in range(0,5):
            btn = ToggleButton(text="-", group='bookmarks', font_size=config.basefont, size_hint=(1,1), background_color=neutral, font_name='Fantasque-Sans', allow_no_selection=True)
            btn.bind(on_press=self.toggledBookmark)
            btn.value = i
            btn.index = -9
            self.bookmarkBox.add_widget(btn)

        self.clearBookmarkButton = ToggleButton(text="Clear", group='clear', font_size=config.basefont, size_hint=(1,1), background_color=neutral, font_name='Fantasque-Sans', allow_no_selection=True)
        self.bookmarkBox.add_widget(self.clearBookmarkButton)
        self.clearBookmarkButton.bind(on_press=self.pressGenericButton)

        self.statusBox.add_widget(self.bookmarkBox)

        self.editSpinner = Spinner(
            # default value shown
            text=config.general['edit_behavior'],
            # available values
            values=['PLAY', 'READ', 'CLEAN', 'CEDIT', 'EDIT'],
            background_normal='',
            background_color=accent1,
            background_down='',
            background_color_down=accent2,
            size_hint=(.15, 1),
            )

        self.editSpinner.bind(text=self.toggleLabelToInput)
        self.statusBox.add_widget(self.editSpinner)

        self.enterSpinner = Spinner(
            # default value shown
            text='PLAIN',
            # available values
            values=['PLAIN', 'CITE', 'BOLD', "COLOR1", "COLOR2", "NONE"],
            background_normal='',
            background_color=accent1,
            background_down='',
            background_color_down=accent2,
            size_hint=(.2, 1),
            )

        self.enterSpinner.bind(text=self.toggleEnterBehavior)
        self.statusBox.add_widget(self.enterSpinner)

        self.centerBox.add_widget(self.statusBox)

##---------------------------------------------------------------------------------------
#  Center text display
##---------------------------------------------------------------------------------------

        #self.centerBox.add_widget(Label(text="---------------------", color=styles.textcolor, size_hint=(1,.04), font_name="Fantasque-Sans", font_size=config.basefont ))

        self.threadButtonBox = GridLayout(cols=2, spacing=5, size_hint=(1,.05))

        self.button = Button(text="copy to main window", size_hint=(1,.03), background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans', font_size=config.basefont75)
        self.button.bind(on_press=self.pressGenericButton)
        self.button.bind(on_release=self.copyThreadsToMain)
        self.threadButtonBox.add_widget(self.button)

        self.randomThreadButton = Button(text="random thread", halign='center', font_size=config.basefont75, background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.randomThreadButton.bind(on_press=self.pressGenericButton)
        self.randomThreadButton.bind(on_release=self.releaseRandomThread)
        self.threadButtonBox.add_widget(self.randomThreadButton)

        self.centerBox.add_widget(self.threadButtonBox)

        self.threadDisplay = ScrollView(size_hint=(1,.30))

        self.threadDisplayGrid = GridLayout(cols=2, spacing=10, size_hint_y=None, size_hint_x=1,  padding=(10,10))
        self.threadDisplayGrid.bind(minimum_height = self.threadDisplayGrid.setter('height'))

        self.threadDisplay.add_widget(self.threadDisplayGrid)

        self.centerBox.add_widget(self.threadDisplay)

        #self.centerBox.add_widget(Label(text="---------------------", color=styles.textcolor, size_hint=(1,.04), font_name="Fantasque-Sans", font_size=config.basefont ))

        self.titleBarBox = BoxLayout(orientation='horizontal', size_hint=(1,.05))

        self.button = Button(text="top", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans', font_size=config.basefont75)
        self.button.bind(on_press=self.pressGenericButton)
        self.button.bind(on_release=self.jumpToTop)
        self.titleBarBox.add_widget(self.button)

        self.centerBox.add_widget(self.titleBarBox)

        self.centerDisplay = ScrollView(size_hint=(1,1))

        self.centerDisplayGrid = GridLayout(cols=1, spacing=10, size_hint_y=None, size_hint_x=1, padding=(10,10))
        self.centerDisplayGrid.bind(minimum_height = self.centerDisplayGrid.setter('height'))

        self.centerDisplay.add_widget(self.centerDisplayGrid)

        self.centerBox.add_widget(self.centerDisplay)

##---------------------------------------------------------------------------------------
#  main text input & control panel
##---------------------------------------------------------------------------------------

        self.controlBox = BoxLayout(orientation='horizontal', size_hint=(1,.45))

        self.textInputMainBox = BoxLayout(orientation='vertical')

        self.textInput = TextInput(text='', hint_text="", size_hint=(1,1))
        #self.textInput.bind(on_text_validate=self.text_entered)
        self.textInputMainBox.add_widget(self.textInput)

##---------------------------------------------------------------------------------------
#  center footer box
##---------------------------------------------------------------------------------------

        self.footerBox = GridLayout(rows=2)

        # system buttons, ie, About and save
        self.saveButton = Button(text="Save", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.saveButton.bind(on_press=self.pressGenericButton)
        self.saveButton.bind(on_release=self.releaseSave)

        self.AboutButton = Button(text="About", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.AboutButton.bind(on_release=self.showAbout)

        # box for adding threads & actors
        self.threadSubmitButton = Button(text="Add\nThread", halign='center', size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans', font_size=config.basefont90)
        self.threadSubmitButton.bind(on_press=self.pressGenericButton)
        self.threadSubmitButton.bind(on_release=self.releaseThread)

        self.addActorButton = Button(text="Add\nActor", halign='center', size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans', font_size=config.basefont90)
        self.addActorButton.bind(on_press=self.pressGenericButton)
        self.addActorButton.bind(on_release=self.releaseAddActor)

        # pick one
        self.listButton1 = Button(text="Pick One\nList", halign="center", font_size=config.basefont75, size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        self.listButton1.bind(on_press=self.pressGenericButton)
        self.listButton1.bind(on_release=self.chooseFromList)
        self.listButton1.value = 0

        self.listButton2 = Button(text="Pick One\n2d4", halign="center", font_size=config.basefont75, size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        self.listButton2.bind(on_press=self.pressGenericButton)
        self.listButton2.bind(on_release=self.chooseFromList)
        self.listButton2.value = 1

        self.listButton3 = Button(text="Pick One\n3d6", halign="center", font_size=config.basefont75, size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        self.listButton3.bind(on_press=self.pressGenericButton)
        self.listButton3.bind(on_release=self.chooseFromList)
        self.listButton3.value = 2

        self.listButton4 = Button(text="Pick One\n3:2:1", halign="center", font_size=config.basefont75, size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        self.listButton4.bind(on_press=self.pressGenericButton)
        self.listButton4.bind(on_release=self.chooseFromList)
        self.listButton4.value = 3

        # dice presets
        self.button1 = Button(text="1d8", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.button1.bind(on_press=self.pressGenericButton)
        self.button1.bind(on_release=self.releasePresetDice)

        self.button2 = Button(text="2d8", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.button2.bind(on_press=self.pressGenericButton)
        self.button2.bind(on_release=self.releasePresetDice)

        self.button3 = Button(text="3d8", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.button3.bind(on_press=self.pressGenericButton)
        self.button3.bind(on_release=self.releasePresetDice)

        self.button4 = Button(text="1d20", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans', font_size=config.basefont80)
        self.button4.bind(on_press=self.pressGenericButton)
        self.button4.bind(on_release=self.releasePresetDice)

        self.button5 = Button(text="1d100", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans', font_size=config.basefont80)
        self.button5.bind(on_press=self.pressGenericButton)
        self.button5.bind(on_release=self.releasePresetDice)

        self.button6 = Button(text="1d4", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.button6.bind(on_press=self.pressGenericButton)
        self.button6.bind(on_release=self.releasePresetDice)

        self.button7 = Button(text="1d6", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.button7.bind(on_press=self.pressGenericButton)
        self.button7.bind(on_release=self.releasePresetDice)

        self.button8 = Button(text="2d6", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.button8.bind(on_press=self.pressGenericButton)
        self.button8.bind(on_release=self.releasePresetDice)

        self.button9 = Button(text="3d6", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.button9.bind(on_press=self.pressGenericButton)
        self.button9.bind(on_release=self.releasePresetDice)

        self.button0 = Button(text="1d10", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.button0.bind(on_press=self.pressGenericButton)
        self.button0.bind(on_release=self.releasePresetDice)


        # row one
        self.footerBox.add_widget(self.saveButton)
        self.footerBox.add_widget(self.threadSubmitButton)
        self.footerBox.add_widget(self.listButton1)
        self.footerBox.add_widget(self.listButton2)
        self.footerBox.add_widget(self.button1)
        self.footerBox.add_widget(self.button2)
        self.footerBox.add_widget(self.button3)
        self.footerBox.add_widget(self.button4)
        self.footerBox.add_widget(self.button5)

        self.footerBox.add_widget(self.AboutButton)
        self.footerBox.add_widget(self.addActorButton)
        self.footerBox.add_widget(self.listButton3)
        self.footerBox.add_widget(self.listButton4)
        self.footerBox.add_widget(self.button6)
        self.footerBox.add_widget(self.button7)
        self.footerBox.add_widget(self.button8)
        self.footerBox.add_widget(self.button9)
        self.footerBox.add_widget(self.button0)

        # About box popup
        self.AboutBox = GridLayout(cols=1, padding=(10,10))

        text = []
        text.append("Make a new game, push buttons, enter text, push more buttons, let me know if anything crashes. Back up your save folder frequently in case of boom. Have fun!")
        text.append("")
        text.append("Drama chart & How's It Going rolls from Joel Priddy @ http://abominablefancy.blogspot.com; go there for more neat stuff!")
        text.append("")
        text.append("The FU oracle is based on FU: The Freeform/Universal RPG (found at http://nathanrussell.net/fu), by Nathan Russell, and licensed for our use under the Creative Commons Attribution 3.0 Unported license (http://creativecommons.org/licenses/by/3.0/).")
        text.append("")
        text.append("Pythia (this program) is licensed under MIT.\nGithub (user name exposit, repo pythia-oracle) for more information.")
        for entry in text:
            label = Label(text=entry)
            label.size = label.texture_size
            label.text_size = (500,None)
            self.AboutBox.add_widget(label)

        self.AboutPopup = Popup(title='About',
            content=self.AboutBox,
            size_hint=(None, None), size=(550, 500),
            auto_dismiss=True)

        self.textInputMainBox.add_widget(self.footerBox)

        self.controlBox.add_widget(self.textInputMainBox)

##---------------------------------------------------------------------------------------
#  Center text submit buttons
##---------------------------------------------------------------------------------------

        self.submitButtonsBox = BoxLayout(orientation='vertical', size_hint=(.23,1))

        self.questionSubmitButton = Button(text="???", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.questionSubmitButton.bind(on_press=self.pressGenericButton)
        self.questionSubmitButton.bind(on_release=self.releaseQuestion)
        self.submitButtonsBox.add_widget(self.questionSubmitButton)

        self.complexButton = Button(text="Complex", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.complexButton.bind(on_press=self.pressGenericButton)
        self.complexButton.bind(on_release=self.releaseComplex)
        self.submitButtonsBox.add_widget(self.complexButton)

        self.playerSubmitButton = Button(text="Direct", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.playerSubmitButton.bind(on_press=self.pressGenericButton)
        self.playerSubmitButton.bind(on_release=self.releasePlayer)
        self.submitButtonsBox.add_widget(self.playerSubmitButton)

        self.dmSubmitButton = Button(text="Aside", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.dmSubmitButton.bind(on_press=self.pressGenericButton)
        self.dmSubmitButton.bind(on_release=self.releaseDM)
        self.submitButtonsBox.add_widget(self.dmSubmitButton)

        self.rollSubmitButton = Button(text="Roll Dice", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.rollSubmitButton.bind(on_press=self.pressGenericButton)
        self.rollSubmitButton.bind(on_release=self.releaseRoll)
        self.submitButtonsBox.add_widget(self.rollSubmitButton)

        # scenario buttons go here, if a scenario is loaded
        self.scenarioButtonList = []
        button = Button(text="show scene", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=self.showBlock)
        self.scenarioButtonList.append(button)

        button = Button(text="show exits", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=self.showExits)
        self.scenarioButtonList.append(button)

        self.controlBox.add_widget(self.submitButtonsBox)

        self.centerBox.add_widget(self.controlBox)

        self.mainBox.add_widget(self.centerBox)

##---------------------------------------------------------------------------------------
#  SIDE PANEL - right horizontal stack for trackers
##---------------------------------------------------------------------------------------

        self.rightAccordion = Accordion(orientation='horizontal', size_hint=(.6, 1), min_space = config.aiheight)
        self.mainBox.add_widget(self.rightAccordion)

##---------------------------------------------------------------------------------------
#  PC panel
##---------------------------------------------------------------------------------------

        self.pcAItem = AccordionItem(title='PC & Party Tracker', background_selected=os.sep + 'resources' + os.sep + 'ui_images' + os.sep + 'invisible.png', min_space = config.aiheight)

        self.pcMainBox = BoxLayout(orientation='vertical')

        self.pcButtonBox = GridLayout(cols=2, spacing=5, size_hint=(1,.05))

        self.button = Button(text="copy to main window", size_hint=(1,.05), background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans', font_size=config.basefont75)
        self.button.bind(on_press=self.pressGenericButton)
        self.button.bind(on_release=self.copyPCsToMain)
        self.pcButtonBox.add_widget(self.button)

        self.randomPCButton = Button(text="random PC", halign='center', font_size=config.basefont75, background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.randomPCButton.bind(on_press=self.pressGenericButton)
        self.randomPCButton.bind(on_release=self.releaseRandomPC)
        self.pcButtonBox.add_widget(self.randomPCButton)

        self.pcMainBox.add_widget(self.pcButtonBox)

        self.pcTitleGrid = GridLayout(cols=2, spacing=5, size_hint=(1,.05))
        label = Label(text="Key", halign="center", size_hint_x=.25, font_size=config.basefont90, font_name='Fantasque-Sans', background_color=(0,0,0,.5), foreground_color=styles.textcolor)
        self.pcTitleGrid.add_widget(label)
        label = Label(text="Value", halign="center", size_hint_x=.75, font_size=config.basefont90, font_name='Fantasque-Sans', background_color=(0,0,0,.5), foreground_color=styles.textcolor)
        self.pcTitleGrid.add_widget(label)

        self.pcMainBox.add_widget(self.pcTitleGrid)

        self.pcDisplay = ScrollView(size_hint=(1, 1))
        self.pcDisplayGrid = GridLayout(cols=2, spacing=5, size_hint_y=None, size_hint_x=1)
        self.pcDisplayGrid.bind(minimum_height = self.pcDisplayGrid.setter('height'))

        for i in range(1,30):

            if i <= 14:
                ml = False
                ht = config.tallheight
                fs = config.basefont90
            else:
                ml = True
                ht = config.tripleheight
                fs = config.basefont90

            label = TextInput(text="", multiline=ml, size_hint_y=None, size_hint_x=.25, height=ht, font_size=fs, font_name='Fantasque-Sans', background_color=(0,0,0,.5), foreground_color=styles.textcolor)
            #label.text_size = (self.pcDisplayGrid.width, None)
            label.value = i
            #label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
            config.pcKeyLabelArray.append(label)

            self.pcDisplayGrid.add_widget(config.pcKeyLabelArray[-1])

            label = TextInput(text="", multiline=ml, size_hint_y=None, size_hint_x=.75, height=ht, font_size=fs, font_name='Fantasque-Sans', background_color=(0,0,0,.5), foreground_color=styles.textcolor)
            label.text_size = (self.pcDisplayGrid.width, None)
            label.value = i
            #label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
            config.pcValueLabelArray.append(label)

            self.pcDisplayGrid.add_widget(config.pcValueLabelArray[-1])

        self.pcDisplay.add_widget(self.pcDisplayGrid)

        self.pcMainBox.add_widget(self.pcDisplay)

        self.pcAItem.add_widget(self.pcMainBox)

        self.rightAccordion.add_widget(self.pcAItem)

##---------------------------------------------------------------------------------------
#  actor panel
##---------------------------------------------------------------------------------------

        self.actorAItem = AccordionItem(title='Actor Tracker', background_selected=os.sep + 'resources' + os.sep + 'ui_images' + os.sep + 'invisible.png', min_space = config.aiheight)

        self.actorMainBox = BoxLayout(orientation='vertical')

        self.actorButtonBox = GridLayout(cols=2, spacing=5, size_hint=(1,.05))

        self.button = Button(text="copy to main window", size_hint=(1,.05), background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans', font_size=config.basefont75)
        self.button.bind(on_press=self.pressGenericButton)
        self.button.bind(on_release=self.copyActorToMain)
        self.actorButtonBox.add_widget(self.button)

        self.randomActorButton = Button(text="random actor", halign='center', font_size=config.basefont75, background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.randomActorButton.bind(on_press=self.pressGenericButton)
        self.randomActorButton.bind(on_release=self.releaseRandomActor)
        self.actorButtonBox.add_widget(self.randomActorButton)

        self.actorMainBox.add_widget(self.actorButtonBox)

        self.actorMainBox.add_widget(Label(text="Actors", halign="center", size_hint=(1,.05), font_size=config.basefont90))
        self.actorDisplay = ScrollView(size_hint=(1, 1))
        self.actorDisplayGrid = GridLayout(cols=1, spacing=5, size_hint_y=None, size_hint_x=1)
        self.actorDisplayGrid.bind(minimum_height = self.actorDisplayGrid.setter('height'))
        self.actorDisplay.add_widget(self.actorDisplayGrid)

        self.actorMainBox.add_widget(self.actorDisplay)

        self.actorAItem.add_widget(self.actorMainBox)

        self.rightAccordion.add_widget(self.actorAItem)

#---------------------------------------------------------------------------------------
# tracks & scratchpad panel
#---------------------------------------------------------------------------------------

        self.tracksAItem = AccordionItem(title='Tracks, Status, Notes', background_selected=os.sep + 'resources' + os.sep + 'ui_images' + os.sep + 'invisible.png', min_space = config.aiheight)

        self.tracksMainBox = BoxLayout(orientation='vertical')

        self.trackButtonBox = GridLayout(cols=2, spacing=5, size_hint=(1,.05))

        self.button = Button(text="copy to main window", size_hint=(1,.05), background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans', font_size=config.basefont75)
        self.button.bind(on_press=self.pressGenericButton)
        self.button.bind(on_release=self.copyTracksToMain)
        self.trackButtonBox.add_widget(self.button)

        self.randomTrackButton = Button(text="random track", halign='center', font_size=config.basefont75, background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.randomTrackButton.bind(on_press=self.pressGenericButton)
        self.randomTrackButton.bind(on_release=self.releaseRandomTrack)
        self.trackButtonBox.add_widget(self.randomTrackButton)

        self.tracksMainBox.add_widget(self.trackButtonBox)

        self.trackTitleGrid = GridLayout(cols=2, spacing=5, size_hint=(1,.10))

        label = Label(text="Status/Condition/Track", size_hint_x=.90, font_size=config.basefont90, font_name='Fantasque-Sans', background_color=(0,0,0,.5), foreground_color=styles.textcolor)
        label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        self.trackTitleGrid.add_widget(label)
        label = Label(text="On?", size_hint_x=.10, font_size=config.basefont90, font_name='Fantasque-Sans', background_color=(0,0,0,.5), foreground_color=styles.textcolor)
        self.trackTitleGrid.add_widget(label)

        self.tracksMainBox.add_widget(self.trackTitleGrid)

        self.trackDisplay = ScrollView(size_hint=(1, 1))
        self.trackDisplayGrid = GridLayout(cols=2, spacing=5, size_hint_y=None, size_hint_x=1)
        self.trackDisplayGrid.bind(minimum_height = self.trackDisplayGrid.setter('height'))

        for i in range(1,30):

            label = TextInput(text="", multiline=False, size_hint_y=None, size_hint_x=.90, height=config.tallheight, font_size=config.basefont, font_name='Fantasque-Sans', background_color=(0,0,0,.5), foreground_color=styles.textcolor)
            config.trackLabelArray.append(label)

            self.trackDisplayGrid.add_widget(config.trackLabelArray[-1])

            label = CheckBox(size_hint_y=None, size_hint_x=.10, color=[1, 1, 1, 4], height=config.baseheight)
            label.background_checkbox_normal="." + os.sep + "resources" + os.sep + "ui_images" + os.sep + "checkbox_off.png"
            label.background_checkbox_down="." + os.sep + "resources" + os.sep + "ui_images" + os.sep + "checkbox_on.png"
            config.trackStatusLabelArray.append(label)

            self.trackDisplayGrid.add_widget(config.trackStatusLabelArray[-1])

        self.trackDisplay.add_widget(self.trackDisplayGrid)

        self.tracksMainBox.add_widget(self.trackDisplay)

        self.tracksAItem.add_widget(self.tracksMainBox)

        self.rightAccordion.add_widget(self.tracksAItem)

##---------------------------------------------------------------------------------------
#  holder panel for maps
##---------------------------------------------------------------------------------------

        self.mapAccordionItem = AccordionItem(title='Maps', background_selected= os.sep + 'resources' + os.sep + "ui_images" + os.sep + 'invisible.png', min_space = config.aiheight)

        self.mapStackAccordion = Accordion(orientation='vertical', size_hint=(1,1), min_space = config.aiheight)

        self.mapAccordionItem.add_widget(self.mapStackAccordion)

        self.leftAccordion.add_widget(self.mapAccordionItem)

##---------------------------------------------------------------------------------------
#  holder panel for generators
##---------------------------------------------------------------------------------------

        self.generatorAccordionItem = AccordionItem(title='Generators', background_selected= os.sep + 'resources' + os.sep + "ui_images" + os.sep + 'invisible.png', min_space = config.aiheight)

        self.generatorStackAccordion = Accordion(orientation='vertical', size_hint=(1,1), min_space = config.aiheight)

        self.generatorAccordionItem.add_widget(self.generatorStackAccordion)

        self.leftAccordion.add_widget(self.generatorAccordionItem)

##---------------------------------------------------------------------------------------
#  holder panel for oracles
##---------------------------------------------------------------------------------------

        self.oracleAccordionItem = AccordionItem(title='Oracles', background_selected= os.sep + 'resources' + os.sep + "ui_images" + os.sep + 'invisible.png', min_space = config.aiheight)

        self.oracleStackAccordion = Accordion(orientation='vertical', size_hint=(1,1), min_space = config.aiheight)

        self.oracleAccordionItem.add_widget(self.oracleStackAccordion)

        self.leftAccordion.add_widget(self.oracleAccordionItem)

##---------------------------------------------------------------------------------------
#  custom generator panels
##---------------------------------------------------------------------------------------

        #self.panelsBox = BoxLayout(orientation="vertical")
        for i in gen_module:
            methodToCall = getattr( i, 'initPanel' )
            self.generatorStackAccordion.add_widget(methodToCall(self))


##---------------------------------------------------------------------------------------
#  custom oracle panels
##---------------------------------------------------------------------------------------

        #self.panelsBox = BoxLayout(orientation="vertical")
        for i in oracle_module:
            methodToCall = getattr( i, 'initPanel' )
            self.oracleStackAccordion.add_widget(methodToCall(self))

##---------------------------------------------------------------------------------------
#  custom maps panels
##---------------------------------------------------------------------------------------

        #self.panelsBox = BoxLayout(orientation="vertical")
        for i in map_module:
            methodToCall = getattr( i, 'initPanel' )
            self.mapStackAccordion.add_widget(methodToCall(self))

#-----------------------------------------
### Functions
#-----------------------------------------

# testing
    def text_entered(self, *args):
        for arg in args:
            print(arg)

#---------------------------------------------------------------------------------------
# miscellaneous functions
#---------------------------------------------------------------------------------------

# trap for enter keystrokes in main input box so 'enter' submits text
    def key_action(self, *args):
        #print "got a key event: %s" % list(args)
        #print(self.textInput.text, self.textInput.focus)
        if args[1] == 13 and self.textInput.focus == True:
            #print("Defocus and send text.")
            if len(self.textInput.text) > 0:
                new_text = self.textInput.text
                if config.general['enter_behavior'] == "CITE":
                    updateCenterDisplay(self, new_text, "italic")
                    quicksave(self, config.curr_game_dir)
                    self.textInput.text = ""
                    return True
                elif config.general['enter_behavior'] == "BOLD":
                    updateCenterDisplay(self, new_text, "bold")
                    quicksave(self, config.curr_game_dir)
                    self.textInput.text = ""
                    return True
                elif config.general['enter_behavior'] == "EMCITE":
                    updateCenterDisplay(self, new_text, "bold_italic")
                    quicksave(self, config.curr_game_dir)
                    self.textInput.text = ""
                    return True
                elif config.general['enter_behavior'] == "COLOR1":
                    updateCenterDisplay(self, new_text, "color1")
                    quicksave(self, config.curr_game_dir)
                    self.textInput.text = ""
                    return True
                elif config.general['enter_behavior'] == "COLOR2":
                    updateCenterDisplay(self, new_text, "color2")
                    quicksave(self, config.curr_game_dir)
                    self.textInput.text = ""
                    return True
                elif config.general['enter_behavior'] == "PLAIN":
                    updateCenterDisplay(self, new_text, "no_format")
                    quicksave(self, config.curr_game_dir)
                    self.textInput.text = ""
                    return True
                else:
                    pass

    def pressGenericButton(self, *args):
        args[0].background_color = accent2

    def releaseSave(self, *args):
        args[0].background_color = neutral
        quicksave(self, config.curr_game_dir)
        saveconfig(self, config.curr_game_dir)
        updateCenterDisplay(self, "Content and configuration saved.", 'ephemeral')
        clearActor(self, *args)
        clearThread(self, *args)

    # generic function calls
    def miscChartRoll(self, *args):
        args[0].background_color = neutral
        #result = eval(args[0].text)()
        result = eval(args[0].function)()
        updateCenterDisplay(self, result)

    def showBlock(self, *args):
        args[0].background_color = neutral
        showCurrentBlock(self)

    def showExits(self, *args):
        args[0].background_color = neutral
        showCurrentExits(self)

#---------------------------------------------------------------------------------------
# PC, threads, tracks, & actor panel copy functions
#---------------------------------------------------------------------------------------

    def copyTracksToMain(self, *args):
        args[0].background_color = neutral
        result = ""
        for i in range(len(config.trackLabelArray)):
            if len(config.trackLabelArray[i].text) > 0:
                result = result + "\n" + config.trackLabelArray[i].text
                if config.trackStatusLabelArray[i].active:
                    result = result + " [X]"
        result = "[Tracked] " + result
        updateCenterDisplay(self, result, "color2")

    def copyActorToMain(self, *args):
        args[0].background_color = neutral
        result = ""
        for i in range(len(config.actorArray)):
            result = result + "\n" + config.actorArray[i] + " [" + config.actorStatusArray[i] + "]"
        result = "[Actors] " + result
        updateCenterDisplay(self, result, "color2")

    def copyPCsToMain(self, *args):
        args[0].background_color = neutral
        result = ""
        for i in range(len(config.pcKeyLabelArray)):
            if len(config.pcKeyLabelArray[i].text) > 0:
                result = result + "\n" + config.pcKeyLabelArray[i].text + ": " + config.pcValueLabelArray[i].text
        result = "[PC] " + result
        updateCenterDisplay(self, result, "color2")

    def copyThreadsToMain(self, *args):
        args[0].background_color = neutral
        result = ""
        for i in range(len(config.threadArray)):
            result = result + "\n" + config.threadArray[i] + " [" + config.threadStatusArray[i] + "]"
        result = "[Threads] " + result
        updateCenterDisplay(self, result, "color2")

#---------------------------------------------------------------------------------------
# submit text input buttons
#---------------------------------------------------------------------------------------

    def releaseQuestion(self, *args):
        args[0].background_color = neutral
        if len(self.textInput.text) > 0:
            updateCenterDisplay(self, self.textInput.text, 'query')

        index = 99
        for i in range(len(oracle_module)):
            if oracle_module[i].__name__ == config.scenario['oracle']:
                index = i

        if index < 99:
            methodToCall = getattr( oracle_module[index], config.scenario['oracle_func'] )
            answer = methodToCall()
        else:
            answer = "No oracle found."

        updateCenterDisplay(self, answer, 'oracle')
        self.textInput.text = ""
        quicksave(self, config.curr_game_dir)

    def releaseComplex(self, *args):
        args[0].background_color = neutral
        if len(self.textInput.text) > 0:
            updateCenterDisplay(self, self.textInput.text, 'query')
        updateCenterDisplay(self,  "[Complex] " + complex_action() + " " + complex_subject(), 'oracle')
        quicksave(self, config.curr_game_dir)
        self.textInput.text = ""

    def releaseRoll(self, *args):
        self.rollSubmitButton.background_color = neutral
        updateCenterDisplay(self, rollDice(self.textInput.text), 'bold_italic')
        quicksave(self, config.curr_game_dir)
        self.textInput.text = ""

    def releasePlayer(self, *args):
        self.playerSubmitButton.background_color = neutral
        if len(self.textInput.text) > 0:
            new_text = self.textInput.text
            updateCenterDisplay(self, new_text, 'no_format')
            quicksave(self, config.curr_game_dir)
        self.textInput.text = ""

    def releaseDM(self, *args):
        self.dmSubmitButton.background_color = neutral
        if len(self.textInput.text) > 0:
            new_text = self.textInput.text
            updateCenterDisplay(self, new_text, "italic")
            quicksave(self, config.curr_game_dir)
        self.textInput.text = ""

    def releaseThread(self, *args):
        self.threadSubmitButton.background_color = neutral
        if len(self.textInput.text) > 0:
            new_text = "" + self.textInput.text + ""
            updateThreadDisplay(self, new_text, "Current")
            updateCenterDisplay(self, "[New Thread] " + new_text, 'italic')
            quicksave(self, config.curr_game_dir)
        self.textInput.text = ""

    def releaseAddActor(self, *args):
        self.addActorButton.background_color = neutral
        if len(self.textInput.text) > 0:
            new_text = self.textInput.text
            updateActorDisplay(self, new_text, 'Current')
            updateCenterDisplay(self, "[New Actor] " + new_text, 'italic')
            quicksave(self, config.curr_game_dir)
        self.textInput.text = ""

#---------------------------------------------------------------------------------------
# center status bar
#---------------------------------------------------------------------------------------

    def releaseTrackerUp(self, *args):
        args[0].background_color = neutral
        config.general['tracker'] = config.general['tracker'] + 1
        self.trackLabel.text = str(config.general['tracker'])

    def releaseTrackerDown(self, *args):
        args[0].background_color = neutral
        config.general['tracker'] = config.general['tracker'] - 1
        self.trackLabel.text = str(config.general['tracker'])

    def toggleEnterBehavior(self, spinner, text):
        config.general['enter_behavior'] = text

    def toggleLabelToInput(self, spinner, text):
        config.general['edit_behavior'] = text
        resetCenterDisplay(self, text)

    def toggledBookmark(self, button):
        if self.clearBookmarkButton.state == 'down':
            button.index = -9
            button.state = 'normal'
            config.general['bookmarks'][button.value] = -9
            button.text = '-'
            self.clearBookmarkButton.state = 'normal'
        else:
            if button.index >= 0:

                try:
                    for item in config.textLabelArray:
                        if config.textArray[button.index] in item.text:
                            self.centerDisplay.scroll_to(item)
                except:
                    pass
                    #updateCenterDisplay(self, "That bookmark is not available in this mode.", 'ephemeral')

                button.state = 'normal'

    def jumpToTop(self, button):
        button.background_color = neutral
        if button.text == "top":
            button.text = "bottom"
            self.centerDisplay.scroll_to(config.textLabelArray[0])
        else:
            button.text = "top"
            self.centerDisplay.scroll_to(config.textLabelArray[-1])

#---------------------------------------------------------------------------------------
# center footer bar
#---------------------------------------------------------------------------------------

    def releaseRandomThread(self, *args):
        args[0].background_color = neutral
        text = self.textInput.text.capitalize()
        filterList = ["Major", "Minor", "Past", "Resolved", "Abandoned", "Don't Show", "Current"]
        if text in filterList:
            curr_index = filterList.index(text)
            updateCenterDisplay(self, getRandomThread(filterList[curr_index]))
        else:
            updateCenterDisplay(self, getRandomThread("All"))
        self.textInput.text = ""

    def releaseRandomActor(self, *args):
        args[0].background_color = neutral
        text = self.textInput.text.capitalize()
        filterList = ["Past", "In party", "Retired", "Deceased", "Remote", "Don't Show", "Current"]
        if text in filterList:
            curr_index = filterList.index(text)
            updateCenterDisplay(self, getRandomActor(filterList[curr_index]))
        else:
            updateCenterDisplay(self, getRandomActor("All"))
        self.textInput.text = ""

    def releaseRandomPC(self, *args):
        args[0].background_color = neutral
        if len(self.textInput.text) > 0:
            updateCenterDisplay(self, getRandomPC(self.textInput.text))
        else:
            updateCenterDisplay(self, getRandomPC())
        self.textInput.text = ""

    def releaseRandomTrack(self, *args):
        args[0].background_color = neutral
        if len(self.textInput.text) > 0:
            updateCenterDisplay(self, getRandomTrack(self.textInput.text))
        else:
            updateCenterDisplay(self, getRandomTrack())
        self.textInput.text = ""

    def releasePresetDice(self, *args):
        args[0].background_color = neutral
        updateCenterDisplay(self, rollDice(args[0].text), 'bold_italic')
        quicksave(self, config.curr_game_dir)
        self.textInput.text = ""

    def chooseFromList(self, *args):
        args[0].background_color = neutral
        value = args[0].value
        pick = args[0].text.split('\n')
        pick = pick[1]
        if len(self.textInput.text) > 0:
            result_string, result, form, roll = chooseWeighted(value, self.textInput.text, "result")
            if len(result_string) > 0:
                updateCenterDisplay(self, "[" + pick + " Options] " + result_string, 'query')
                updateCenterDisplay(self, "[" + roll + "] " + result, form)
            else:
                updateCenterDisplay(self, "Please enter a comma-separated list in one line that has at least as many options as needed.", 'ephemeral')
        self.textInput.text = ""

    def showAbout(self, *args):
        self.AboutPopup.open()

#---------------------------------------------------------------------------------------
# heartbeat functions
#---------------------------------------------------------------------------------------

    def on_enter(self):

        loadconfig(self, config.curr_game_dir)
        quickload(self, config.curr_game_dir)

        # now update variable widgets
        try:
            # general
            self.enterSpinner.text = str(config.general["enter_behavior"])
            self.editSpinner.text = str(config.general["edit_behavior"])

            l = ToggleButtonBehavior.get_widgets('bookmarks')
            for i in range(len(l)):
                if config.general['bookmarks'][i] >= 0:
                    l[i].index = config.general['bookmarks'][i]
                    l[i].text = str(config.general['bookmarks'][i])
                else:
                    l[i].text = '-'
            del l

            self.trackLabel.text = str(config.general['tracker'])
        except:
            pass

        try:
            #panel specific
            for i in gen_module:
                methodToCall = getattr( i, 'onEnter' )
                methodToCall(self)

            for i in oracle_module:
                methodToCall = getattr( i, 'onEnter' )
                methodToCall(self)
        except:
            pass

        if config.scenario['active'] == True:

            if config.scenario['use_core'] == False:
                self.generatorStackAccordion.remove_widget(self.actorsAItem)
                self.generatorStackAccordion.remove_widget(self.hexAItem)
                self.mapStackAccordion.remove_widget(self.mapAItem)

            if config.scenario['use_oracle'] == False:
                self.oracleStackAccordion.remove_widget(self.fuAItem)
                self.submitButtonsBox.remove_widget(self.questionSubmitButton)

            # scenario logic - required
            mod = config.curr_game_dir + "scenlogic.py"
            filename = mod.split('/')[-1]
            pyfile = filename.split('.')[0]
            scenlogic = imp.load_source( pyfile, mod)

            # scenario oracle/info panel - required
            mod = config.curr_game_dir + "scenpanel.py"
            filename = mod.split('/')[-1]
            pyfile = filename.split('.')[0]
            scenpanel = imp.load_source( pyfile, mod)

            self.oracleStackAccordion.add_widget(scenpanel.initPanel(self))

            # scenario map panel - optional
            try:
                mod = config.curr_game_dir + "scenmap.py"
                filename = mod.split('/')[-1]
                pyfile = filename.split('.')[0]
                scenmap = imp.load_source( pyfile, mod)

                self.mapStackAccordion.add_widget(scenmap.initPanel(self))
            except:
                pass

            # scenario generator panel - optional
            try:
                mod = config.curr_game_dir + "scengen.py"
                filename = mod.split('/')[-1]
                pyfile = filename.split('.')[0]
                scengen = imp.load_source( pyfile, mod)

                self.generatorStackAccordion.add_widget(scengen.initPanel(self))
            except:
                pass

            with open(config.curr_game_dir + "scenario.txt", "r") as f:
                config.advDict = json.load(f)

            for button in self.scenarioButtonList:
                self.submitButtonsBox.add_widget(button)

            block = config.scenario['block']

            self.scenarioTitleLabel = Button(text=config.advDict[block]['title'], size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans', font_size=config.basefont75)
            self.titleBarBox.add_widget(self.scenarioTitleLabel)

            if len(config.textLabelArray) == 1:
                config.advDict[block]['shown'] == 99
                showCurrentBlock(self)
                saveconfig(self, config.curr_game_dir)

        updateCleanMarkdown()
        updateCleanHTML()
        updateCollapseHTML()
