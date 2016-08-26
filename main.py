#!/usr/bin/env python
#-*- coding: utf-8 -*-
##-------------------------------------------------------------------------------------------------------------------------------------------
#  Main Screen
#
##-------------------------------------------------------------------------------------------------------------------------------------------

from imports import *
import config

class ScrollableLabel(ScrollView):
    text = StringProperty('')

class MainScreen(Screen):

    def __init__(self,**kwargs):
        super (MainScreen, self).__init__(**kwargs)

##-------------------------------------------------------------------------------------------------------------------------------------------
#  general
##-------------------------------------------------------------------------------------------------------------------------------------------

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

##-------------------------------------------------------------------------------------------------------------------------------------------
#  SIDE PANEL - right horizontal stack
##-------------------------------------------------------------------------------------------------------------------------------------------

        self.leftAccordion = Accordion(orientation='horizontal', size_hint=(.6, 1), min_space=30)
        self.mainBox.add_widget(self.leftAccordion)

##-------------------------------------------------------------------------------------------------------------------------------------------
#  Center status across top
##-------------------------------------------------------------------------------------------------------------------------------------------

        self.centerBox = BoxLayout(orientation='vertical', padding=(10,10))

        self.statusBox = BoxLayout(orientation='horizontal', size_hint=(1,.05), padding=(10,10))

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
            btn = ToggleButton(text=str(i), group='bookmarks', font_size=config.general['basefontsize'], size_hint=(1,1), background_color=neutral, font_name='Fantasque-Sans', allow_no_selection=True)
            btn.bind(on_press=self.toggledBookmark)
            btn.value = i
            btn.index = -9
            self.bookmarkBox.add_widget(btn)

        self.clearBookmarkButton = ToggleButton(text="Clear", group='clear', font_size=config.general['basefontsize'], size_hint=(1,1), background_color=neutral, font_name='Fantasque-Sans', allow_no_selection=True)
        self.bookmarkBox.add_widget(self.clearBookmarkButton)

        self.statusBox.add_widget(self.bookmarkBox)

        self.editSpinner = Spinner(
            # default value shown
            text='EDIT',
            # available values
            values=['EDIT', 'PLAY', 'READ', 'CLEAN'],
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
            values=['PLAIN', 'CITE', 'BOLD', "COLOR1", "COLOR2"],
            background_normal='',
            background_color=accent1,
            background_down='',
            background_color_down=accent2,
            size_hint=(.2, 1),
            )

        self.enterSpinner.bind(text=self.toggleEnterBehavior)
        self.statusBox.add_widget(self.enterSpinner)

        self.centerBox.add_widget(self.statusBox)

##-------------------------------------------------------------------------------------------------------------------------------------------
#  Center text display
##-------------------------------------------------------------------------------------------------------------------------------------------

        self.centerBox.add_widget(Label(text="--------------------------------------------------------------------------", color=styles.textcolor, size_hint=(1,.04), font_name="Fantasque-Sans", font_size=config.general['basefontsize'] ))

        self.threadDisplay = ScrollView(size_hint=(1, .18))

        self.threadDisplayGrid = GridLayout(cols=2, spacing=10, size_hint_y=None, size_hint_x=1)
        self.threadDisplayGrid.bind(minimum_height = self.threadDisplayGrid.setter('height'))

        self.threadDisplay.add_widget(self.threadDisplayGrid)

        self.centerBox.add_widget(self.threadDisplay)

        self.centerBox.add_widget(Label(text="--------------------------------------------------------------------------", color=styles.textcolor, size_hint=(1,.04), font_name="Fantasque-Sans", font_size=config.general['basefontsize'] ))

        self.centerDisplay = ScrollView(size_hint=(1,.50))

        self.centerDisplayGrid = GridLayout(cols=1, spacing=10, size_hint_y=None, size_hint_x=1, padding=(10,10))
        self.centerDisplayGrid.bind(minimum_height = self.centerDisplayGrid.setter('height'))

        self.centerDisplay.add_widget(self.centerDisplayGrid)

        self.centerBox.add_widget(self.centerDisplay)

        self.textInputMainBox = BoxLayout(orientation='horizontal', size_hint=(1,.23))

        self.textInput = TextInput(text='', hint_text="",size_hint=(.7,1))
        self.textInput.bind(on_text_validate=self.text_entered)
        self.textInputMainBox.add_widget(self.textInput)

##-------------------------------------------------------------------------------------------------------------------------------------------
#  Center text submit buttons & text input
##-------------------------------------------------------------------------------------------------------------------------------------------

        self.submitButtonsBox = BoxLayout(orientation='vertical', size_hint=(.23,1))

        self.textInputMainBox.add_widget(self.submitButtonsBox)

        self.questionSubmitButton = Button(text="???",size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.questionSubmitButton.bind(on_press=self.pressGenericButton)
        self.questionSubmitButton.bind(on_release=self.releaseQuestion)
        self.submitButtonsBox.add_widget(self.questionSubmitButton)

        self.complexButton = Button(text="Complex", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.complexButton.bind(on_press=self.pressGenericButton)
        self.complexButton.bind(on_release=self.releaseComplex)
        self.submitButtonsBox.add_widget(self.complexButton)

        self.playerSubmitButton = Button(text="Direct",size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.playerSubmitButton.bind(on_press=self.pressGenericButton)
        self.playerSubmitButton.bind(on_release=self.releasePlayer)
        self.submitButtonsBox.add_widget(self.playerSubmitButton)

        self.dmSubmitButton = Button(text="Aside",size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.dmSubmitButton.bind(on_press=self.pressGenericButton)
        self.dmSubmitButton.bind(on_release=self.releaseDM)
        self.submitButtonsBox.add_widget(self.dmSubmitButton)

        self.rollSubmitButton = Button(text="Roll Dice",size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.rollSubmitButton.bind(on_press=self.pressGenericButton)
        self.rollSubmitButton.bind(on_release=self.releaseRoll)
        self.submitButtonsBox.add_widget(self.rollSubmitButton)

        self.threadSubmitButton = Button(text="Add Thread",size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.threadSubmitButton.bind(on_press=self.pressGenericButton)
        self.threadSubmitButton.bind(on_release=self.releaseThread)
        self.submitButtonsBox.add_widget(self.threadSubmitButton)

        self.addActorButton = Button(text="Add Actor", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.addActorButton.bind(on_press=self.pressGenericButton)
        self.addActorButton.bind(on_release=self.releaseAddActor)
        self.submitButtonsBox.add_widget(self.addActorButton)

        self.centerBox.add_widget(self.textInputMainBox)

##-------------------------------------------------------------------------------------------------------------------------------------------
#  center footer box
##-------------------------------------------------------------------------------------------------------------------------------------------

        self.footerBox = GridLayout(cols=4, size_hint=(1,.10))
        self.centerBox.add_widget(self.footerBox)

        # box for random selectors
        self.selectorBox = GridLayout(cols=2)

        self.randomTrackButton = Button(text="Random\nTrack", halign='center', font_size=config.general['basefontsize']*.75, background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.randomTrackButton.bind(on_press=self.pressGenericButton)
        self.randomTrackButton.bind(on_release=self.releaseRandomTrack)
        self.selectorBox.add_widget(self.randomTrackButton)

        self.randomPCButton = Button(text="Random\nPC", halign='center', font_size=config.general['basefontsize']*.75, background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.randomPCButton.bind(on_press=self.pressGenericButton)
        self.randomPCButton.bind(on_release=self.releaseRandomPC)
        self.selectorBox.add_widget(self.randomPCButton)

        self.randomActorButton = Button(text="Random\nActor", halign='center', font_size=config.general['basefontsize']*.75, background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.randomActorButton.bind(on_press=self.pressGenericButton)
        self.randomActorButton.bind(on_release=self.releaseRandomActor)
        self.selectorBox.add_widget(self.randomActorButton)

        self.randomThreadButton = Button(text="Random\nThread", halign='center', font_size=config.general['basefontsize']*.75, background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.randomThreadButton.bind(on_press=self.pressGenericButton)
        self.randomThreadButton.bind(on_release=self.releaseRandomThread)
        self.selectorBox.add_widget(self.randomThreadButton)

        self.footerBox.add_widget(self.selectorBox)

        # pick one
        self.pickOneBox = GridLayout(cols=2)

        self.listButton = Button(text="Pick One\nList", halign="center", font_size=config.general['basefontsize']*.75, size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        self.listButton.bind(on_press=self.pressGenericButton)
        self.listButton.bind(on_release=self.chooseFromList)
        self.listButton.value = 0
        self.pickOneBox.add_widget(self.listButton)

        self.listButton = Button(text="Pick One\n2d4", halign="center", font_size=config.general['basefontsize']*.75, size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        self.listButton.bind(on_press=self.pressGenericButton)
        self.listButton.bind(on_release=self.chooseFromList)
        self.listButton.value = 1
        self.pickOneBox.add_widget(self.listButton)

        self.listButton = Button(text="Pick One\n3d6", halign="center", font_size=config.general['basefontsize']*.75, size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        self.listButton.bind(on_press=self.pressGenericButton)
        self.listButton.bind(on_release=self.chooseFromList)
        self.listButton.value = 2
        self.pickOneBox.add_widget(self.listButton)

        self.listButton = Button(text="Pick One\n3:2:1", halign="center", font_size=config.general['basefontsize']*.75, size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        self.listButton.bind(on_press=self.pressGenericButton)
        self.listButton.bind(on_release=self.chooseFromList)
        self.listButton.value = 3
        self.pickOneBox.add_widget(self.listButton)

        self.footerBox.add_widget(self.pickOneBox)

        # dice presets
        self.dicePresetsBox = GridLayout(cols=4)

        self.button = Button(text="d8", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.button.bind(on_press=self.pressGenericButton)
        self.button.bind(on_release=self.releasePresetDice)
        self.dicePresetsBox.add_widget(self.button)

        self.button = Button(text="2d8", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.button.bind(on_press=self.pressGenericButton)
        self.button.bind(on_release=self.releasePresetDice)
        self.dicePresetsBox.add_widget(self.button)

        self.button = Button(text="d20", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans', font_size=config.general['basefontsize'])
        self.button.bind(on_press=self.pressGenericButton)
        self.button.bind(on_release=self.releasePresetDice)
        self.dicePresetsBox.add_widget(self.button)

        self.button = Button(text="d100", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans', font_size=config.general['basefontsize'])
        self.button.bind(on_press=self.pressGenericButton)
        self.button.bind(on_release=self.releasePresetDice)
        self.dicePresetsBox.add_widget(self.button)

        self.button = Button(text="d4", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.button.bind(on_press=self.pressGenericButton)
        self.button.bind(on_release=self.releasePresetDice)
        self.dicePresetsBox.add_widget(self.button)

        self.button = Button(text="d6", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.button.bind(on_press=self.pressGenericButton)
        self.button.bind(on_release=self.releasePresetDice)
        self.dicePresetsBox.add_widget(self.button)

        self.button = Button(text="2d6", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.button.bind(on_press=self.pressGenericButton)
        self.button.bind(on_release=self.releasePresetDice)
        self.dicePresetsBox.add_widget(self.button)

        self.button = Button(text="3d6", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.button.bind(on_press=self.pressGenericButton)
        self.button.bind(on_release=self.releasePresetDice)
        self.dicePresetsBox.add_widget(self.button)

        self.footerBox.add_widget(self.dicePresetsBox)

        # system buttons, ie, help and save
        self.systemBox = BoxLayout(orientation='vertical')

        self.saveButton = Button(text="Save", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.saveButton.bind(on_press=self.pressGenericButton)
        self.saveButton.bind(on_release=self.releaseSave)
        self.systemBox.add_widget(self.saveButton)

        self.helpButton = Button(text="Help", background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.helpButton.bind(on_release=self.showHelp)
        self.systemBox.add_widget(self.helpButton)

        self.footerBox.add_widget(self.systemBox)

        self.helpBox = GridLayout(cols=1, padding=(10,10))

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
            self.helpBox.add_widget(label)

        self.helpPopup = Popup(title='Help',
            content=self.helpBox,
            size_hint=(None, None), size=(550, 500),
            auto_dismiss=True)

        self.mainBox.add_widget(self.centerBox)

##-------------------------------------------------------------------------------------------------------------------------------------------
#  SIDE PANEL - right horizontal stack for trackers
##-------------------------------------------------------------------------------------------------------------------------------------------

        self.rightAccordion = Accordion(orientation='horizontal', size_hint=(.6, 1), min_space=30)
        self.mainBox.add_widget(self.rightAccordion)

##-------------------------------------------------------------------------------------------------------------------------------------------
#  PC panel
##-------------------------------------------------------------------------------------------------------------------------------------------

        self.pcAItem = AccordionItem(title='PC & Party Tracker', background_selected='resources/ui_images/invisible.png', min_space=30)

        self.pcMainBox = BoxLayout(orientation='vertical')

        self.pcTitleGrid = GridLayout(cols=2, spacing=5, size_hint=(1,.05))
        label = Label(text="Key", halign="center", size_hint_x=.25, font_size=config.general['basefontsize'], font_name='Fantasque-Sans', background_color=(0,0,0,.5), foreground_color=styles.textcolor)
        self.pcTitleGrid.add_widget(label)
        label = Label(text="Value", halign="center", size_hint_x=.75, font_size=config.general['basefontsize'], font_name='Fantasque-Sans', background_color=(0,0,0,.5), foreground_color=styles.textcolor)
        self.pcTitleGrid.add_widget(label)

        self.pcMainBox.add_widget(self.pcTitleGrid)

        self.pcDisplay = ScrollView(size_hint=(1, 1))
        self.pcDisplayGrid = GridLayout(cols=2, spacing=5, size_hint_y=None, size_hint_x=1)
        self.pcDisplayGrid.bind(minimum_height = self.pcDisplayGrid.setter('height'))

        for i in range(1,30):

            label = TextInput(text="", multiline=False, height="30px", size_hint_y=None, size_hint_x=.25, font_size=config.general['basefontsize'], font_name='Fantasque-Sans', background_color=(0,0,0,.5), foreground_color=styles.textcolor)
            label.text_size = (self.pcDisplayGrid.width, None)
            label.value = i
            label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
            config.pcKeyLabelArray.append(label)

            self.pcDisplayGrid.add_widget(config.pcKeyLabelArray[-1])

            label = TextInput(text="", multiline=False, height="30px", size_hint_y=None, size_hint_x=.75, font_size=config.general['basefontsize'], font_name='Fantasque-Sans', background_color=(0,0,0,.5), foreground_color=styles.textcolor)
            label.text_size = (self.pcDisplayGrid.width, None)
            label.value = i
            label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
            config.pcValueLabelArray.append(label)

            self.pcDisplayGrid.add_widget(config.pcValueLabelArray[-1])

        self.pcDisplay.add_widget(self.pcDisplayGrid)

        self.pcMainBox.add_widget(self.pcDisplay)

        self.pcAItem.add_widget(self.pcMainBox)

        self.rightAccordion.add_widget(self.pcAItem)

##-------------------------------------------------------------------------------------------------------------------------------------------
#  actor panel
##-------------------------------------------------------------------------------------------------------------------------------------------

        self.actorsAItem = AccordionItem(title='Actor Tracker', background_selected='resources/ui_images/invisible.png', min_space=30)

        self.actorMainBox = BoxLayout(orientation='vertical')

        self.actorDisplay = ScrollView(size_hint=(1, 1))
        self.actorDisplayGrid = GridLayout(cols=2, spacing=5, size_hint_y=None, size_hint_x=1)
        self.actorDisplayGrid.bind(minimum_height = self.actorDisplayGrid.setter('height'))
        self.actorDisplay.add_widget(self.actorDisplayGrid)

        self.actorMainBox.add_widget(self.actorDisplay)

        self.actorsAItem.add_widget(self.actorMainBox)

        self.rightAccordion.add_widget(self.actorsAItem)

#-------------------------------------------------------------------------------------------------------------------------------------------
# tracks & scratchpad panel
#-------------------------------------------------------------------------------------------------------------------------------------------

        self.tracksAItem = AccordionItem(title='Tracks, Status, Notes', background_selected='/resources/ui_images/invisible.png', min_space=30)

        self.tracksMainBox = BoxLayout(orientation='vertical')

        self.trackTitleGrid = GridLayout(cols=2, spacing=5, size_hint=(1,.10))

        label = Label(text="Status/Condition/Track", size_hint_x=.90, font_size=config.general['basefontsize'], font_name='Fantasque-Sans', background_color=(0,0,0,.5), foreground_color=styles.textcolor)
        label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        self.trackTitleGrid.add_widget(label)
        label = Label(text="On?", size_hint_x=.10, font_size=config.general['basefontsize'], font_name='Fantasque-Sans', background_color=(0,0,0,.5), foreground_color=styles.textcolor)
        self.trackTitleGrid.add_widget(label)

        self.tracksMainBox.add_widget(self.trackTitleGrid)

        self.trackDisplay = ScrollView(size_hint=(1, 1))
        self.trackDisplayGrid = GridLayout(cols=2, spacing=5, size_hint_y=None, size_hint_x=1)
        self.trackDisplayGrid.bind(minimum_height = self.trackDisplayGrid.setter('height'))

        for i in range(1,30):

            label = TextInput(text="", multiline=False, height="30px", size_hint_y=None, size_hint_x=.90, font_size=config.general['basefontsize'], font_name='Fantasque-Sans', background_color=(0,0,0,.5), foreground_color=styles.textcolor)
            label.text_size = (self.trackDisplayGrid.width, None)
            label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
            config.trackLabelArray.append(label)

            self.trackDisplayGrid.add_widget(config.trackLabelArray[-1])

            label = CheckBox(size_hint_y=None, size_hint_x=.10, height="30px", color=[1, 1, 1, 4])
            label.background_checkbox_normal="./resources/ui_images/checkbox_off.png"
            label.background_checkbox_down="./resources/ui_images/checkbox_on.png"
            config.trackStatusLabelArray.append(label)

            self.trackDisplayGrid.add_widget(config.trackStatusLabelArray[-1])

        self.trackDisplay.add_widget(self.trackDisplayGrid)

        self.tracksMainBox.add_widget(self.trackDisplay)

        self.tracksAItem.add_widget(self.tracksMainBox)

        self.rightAccordion.add_widget(self.tracksAItem)

##-------------------------------------------------------------------------------------------------------------------------------------------
#  holder panel for generators
##-------------------------------------------------------------------------------------------------------------------------------------------

        self.generatorAccordionItem = AccordionItem(title='Generators', background_selected='/resources/ui_images/invisible.png', min_space=30)

        self.generatorStackAccordion = Accordion(orientation='vertical', size_hint=(1, 1), min_space=30)

        self.generatorAccordionItem.add_widget(self.generatorStackAccordion)

        self.leftAccordion.add_widget(self.generatorAccordionItem)

##-------------------------------------------------------------------------------------------------------------------------------------------
#  holder panel for oracles
##-------------------------------------------------------------------------------------------------------------------------------------------

        self.oracleAccordionItem = AccordionItem(title='Oracles', background_selected='/resources/ui_images/invisible.png', min_space=30)

        self.oracleStackAccordion = Accordion(orientation='vertical', size_hint=(1, 1), min_space=30)

        self.oracleAccordionItem.add_widget(self.oracleStackAccordion)

        self.leftAccordion.add_widget(self.oracleAccordionItem)

##-------------------------------------------------------------------------------------------------------------------------------------------
#  custom generator panels
##-------------------------------------------------------------------------------------------------------------------------------------------

        self.panelsBox = BoxLayout(orientation="vertical")
        for i in gen_module:
            methodToCall = getattr( i, 'initPanel' )
            self.generatorStackAccordion.add_widget(methodToCall(self))


##-------------------------------------------------------------------------------------------------------------------------------------------
#  custom oracle panels
##-------------------------------------------------------------------------------------------------------------------------------------------

        self.panelsBox = BoxLayout(orientation="vertical")
        for i in oracle_module:
            methodToCall = getattr( i, 'initPanel' )
            self.oracleStackAccordion.add_widget(methodToCall(self))

#-----------------------------------------
### Functions
#-----------------------------------------

# testing
    def text_entered(self, *args):
        for arg in args:
            print(arg)

#-------------------------------------------------------------------------------------------------------------------------------------------
# miscellaneous functions
#-------------------------------------------------------------------------------------------------------------------------------------------

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
                elif config.general['enter_behavior'] == "BOLD":
                    updateCenterDisplay(self, new_text, "bold")
                elif config.general['enter_behavior'] == "EMCITE":
                    updateCenterDisplay(self, new_text, "bold_italic")
                elif config.general['enter_behavior'] == "COLOR1":
                    updateCenterDisplay(self, new_text, "color1")
                elif config.general['enter_behavior'] == "COLOR2":
                    updateCenterDisplay(self, new_text, "color2")
                else:
                    updateCenterDisplay(self, new_text, "no_format")

            quicksave(self, config.curr_game_dir)
            self.textInput.text = ""
            return True

    def pressGenericButton(self, *args):
        args[0].background_color = accent2

    def releaseSave(self, *args):
        args[0].background_color = neutral
        quicksave(self, config.curr_game_dir)
        saveconfig(self, config.curr_game_dir)
        updateCenterDisplay(self, "Content and configuration saved.", 'ephemeral')

    # generic function calls
    def miscChartRoll(self, *args):
        args[0].background_color = neutral
        #result = eval(args[0].text)()
        result = eval(args[0].function)()
        updateCenterDisplay(self, result)

#-------------------------------------------------------------------------------------------------------------------------------------------
# submit text input buttons
#-------------------------------------------------------------------------------------------------------------------------------------------

    def releaseQuestion(self, *args):
        args[0].background_color = neutral
        if len(self.textInput.text) > 0:
            updateCenterDisplay(self, self.textInput.text, 'query')
        updateCenterDisplay(self, fu(0), 'oracle')
        self.textInput.text = ""
        quicksave(self, config.curr_game_dir)

    def releaseComplex(self, *args):
        args[0].background_color = neutral
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
        if len(self.textInput.text) > 0:
            self.addActorButton.background_color = neutral
            new_text = self.textInput.text
            updateActorDisplay(self, new_text, 'Current')
            updateCenterDisplay(self, "[New Actor] " + new_text, 'italic')
            quicksave(self, config.curr_game_dir)
        self.textInput.text = ""

#-------------------------------------------------------------------------------------------------------------------------------------------
# center status bar
#-------------------------------------------------------------------------------------------------------------------------------------------

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
            self.clearBookmarkButton.state = 'normal'
        else:
            if button.index >= 0:
                self.centerDisplay.scroll_to(config.textLabelArray[button.index])
                button.state = 'normal'

#-------------------------------------------------------------------------------------------------------------------------------------------
# center footer bar
#-------------------------------------------------------------------------------------------------------------------------------------------

    def releaseRandomThread(self, *args):
        args[0].background_color = neutral
        text = self.textInput.text.capitalize()
        filterList = ["Major", "Minor", "Past", "Resolved", "Abandoned", "Hide", "Current"]
        if text in filterList:
            curr_index = filterList.index(text)
            updateCenterDisplay(self, getRandomThread(filterList[curr_index]))
        else:
            updateCenterDisplay(self, getRandomThread("All"))
        self.textInput.text = ""

    def releaseRandomActor(self, *args):
        args[0].background_color = neutral
        text = self.textInput.text.capitalize()
        filterList = ["Past", "In party", "Retired", "Deceased", "Remote", "Hide", "Current"]
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
        try:
            if value == 1:
                # 2d4
                index = 2
                chart = {}
                result = self.textInput.text.split(", ")
                for i in result:
                    chart[index] = i
                    index = index + 1
                roll = random.randint(1,4) + random.randint(1,4)
                result = chart[roll]
            elif value == 2:
                # 3d6
                index = 3
                chart = {}
                result = self.textInput.text.split(", ")
                for i in result:
                    chart[index] = i
                    index = index + 1

                roll = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
                result = chart[roll]
            elif value == 3:
                # 3:2:1
                roll = random.randint(1,6)
                chart = self.textInput.text.split(", ")
                if roll <= 3:
                    result = chart[0]
                elif roll <= 4:
                    result = chart[1]
                elif roll <= 5:
                    result = chart[2]
            else:
                result = self.textInput.text.split(", ")
                result = random.choice(self.textInput.text.split(", "))

            updateCenterDisplay(self, "[Options] " + self.textInput.text, 'query')
            updateCenterDisplay(self, "[Result] " + result)
            self.textInput.text = ""

        except:
            updateCenterDisplay(self, "Please enter a comma-separated list on one line.", 'ephemeral')

    def showHelp(self, *args):
        self.helpPopup.open()

#-------------------------------------------------------------------------------------------------------------------------------------------
# heartbeat functions
#-------------------------------------------------------------------------------------------------------------------------------------------

    def on_enter(self):

        quickload(self, config.curr_game_dir)

        loadconfig(self, config.curr_game_dir)

        # now update variable widgets
        try:
            # general
            self.enterSpinner.text = str(config.general["enter_behavior"])
            self.editSpinner.text = str(config.general["edit_behavior"])

            l = ToggleButtonBehavior.get_widgets('bookmarks')
            for i in range(len(l)):
                l[i].index = config.general['bookmarks'][i]
            del l

            updateCleanMarkdown()
            updateCleanHTML()

        except:
            print("Variables loaded but widgets not updated")
