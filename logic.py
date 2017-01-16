#!/usr/bin/env python
#-*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------------------
#  General logic
#
##---------------------------------------------------------------------------------------------------

import imports
from imports import *
import config

import logicscen
from logicscen import *

#---------------------------------------------------------------------------------------------------
# Basic
#---------------------------------------------------------------------------------------------------

class ButtonBehaviorLabel(ButtonBehavior, Label):
    pass

class ButtonLabel(Button, Label):
    pass


def resetCenterDisplay(self, textArray=config.textArray, textStatusArray=config.textStatusArray):

    for i in range(len(textArray)):
        makeItemLabels(self, textArray[i], textStatusArray[i])
        addToCenterDisplay(self, textArray[i], textStatusArray[i])

def updateCenterDisplay(self, text, status='result'):

    #if len(config.textStatusArray) > 0:
    makeItemLabels(self, text, status)
    addToCenterDisplay(self, text, status)

    try:
        Window.set_title("Pythia-Oracle -- " + os.path.basename(os.path.normpath(config.curr_game_dir)) + " -- " + str(len(config.textArray)) + " blocks")
    except:
        pass

def swapBlock(block):

    self = block.self
    index = block.index
    status = config.textStatusArray[index]
    text = config.textArray[index]
    base_text = text

    is_bookmark_set = storeBookmarkLabel(block)
    if is_bookmark_set == True:
        return

    if block.__class__.__name__ == "ButtonBehaviorLabel":

        block.parent.remove_widget(block)

        box = GridLayout(cols=2, size_hint=(1,None))
        box.index = index

        field = TextInput(text=base_text, font_size=config.blockfont, size_hint_y=None, size_hint_x=None)
        field.bind(focus=focusChangeText)
        field.background_color=neutral
        field.foreground_color=(1,1,1,1)
        field.index = index
        field.self = self
        field.bind(height=box.setter('height'))
        box.add_widget(field)

        field.height = block.height + (field.line_height * 2)

        subbox = BoxLayout(orientation="vertical")
        subbox.index = index

        formBox = GridLayout(cols=4)
        insertList = [ 'i', 'b' ]
        for f in insertList:
            button = Button(text=f, font_size=config.blockstatusfont, font_name='maintextfont', size_hint_x=None, size_hint_y=1, background_normal='', background_color=accent1, background_down='', background_color_down=accent2 )
            button.width="20dp"
            button.bind(on_press=insertTextFormat)
            button.index = index
            button.self = self
            formBox.add_widget(button)

            button = Button(text="/" + f, font_size=config.blockstatusfont, font_name='maintextfont', size_hint_x=None, size_hint_y=1, background_normal='', background_color=accent1, background_down='', background_color_down=accent2 )
            button.width="20dp"
            button.bind(on_press=insertTextFormat)
            button.index = index
            button.self = self
            formBox.add_widget(button)

        subbox.add_widget(formBox)

        # these are for setting status
        if config.use_spinner_status == False:
            button = ButtonLabel(text=status, font_size=config.blockstatusfont, font_name='maintextfont', size_hint_x=None, size_hint_y=1, background_normal='', background_color=accent1, background_down='', background_color_down=accent2 )
            button.width="80dp"
            button.self = self
            button.bind(on_press=cycleText)
            button.index = index
            subbox.add_widget(button)

            field.width=self.centerDisplayGrid.width-button.width-20

        # this is a much cleaner solution instead of cycling, but takes a while
        if config.use_spinner_status == True:

            try:
                statusList = config.formats['status_tags']
            except:
                statusList = ['plain', 'aside', 'oracle', 'result', 'query', 'mechanic1', 'mechanic2', 'ephemeral']

            spinner = Spinner(
                # default value shown
                text=status,
                # available values
                values=statusList,
                background_normal='',
                background_color=accent1,
                background_down='',
                background_color_down=accent2,
                font_size=config.basefont60,
                size_hint_y=1,
                size_hint_x=None,
                width="80dp",
                )
            spinner.index = index
            spinner.self = self
            spinner.bind(text=reformatText)
            subbox.add_widget(spinner)

            field.width=self.centerDisplayGrid.width-spinner.width-20

        button = Button(text="done", font_size=config.blockstatusfont, font_name='maintextfont', size_hint_x=None, size_hint_y=1, background_normal='', background_color=accent1, background_down='', background_color_down=accent2 )
        button.width = "80dp"
        button.bind(on_press=swapBlock)
        button.index = index
        button.self = self
        subbox.add_widget(button)
        box.add_widget(subbox)

        config.textLabelArray[index] = box

    else:

        field = [x for x in config.textLabelArray[index].children if x.__class__.__name__ == "TextInput" ]

        config.textArray[index] = field[0].text

        formatted_text = parseText(field[0].text, status)

        block.parent.parent.parent.remove_widget(block.parent.parent)

        label = ButtonBehaviorLabel(text=formatted_text, size_hint=(1, None), font_size=config.blockfont, font_name='maintextfont', background_normal='', background_down='', background_color=(0,0,0,0), background_color_down=accent2)

        label.size = label.texture_size
        label.text_size = (self.centerDisplayGrid.width, None)
        label.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

        label.bind(on_release=swapBlock)
        label.bind(on_ref_press=refPress)
        label.foreground_color=(1,1,1,1)
        label.markup = True
        label.self = self
        label.index = index
        config.textLabelArray[index] = label
        label.padding_=50


    self.centerDisplayGrid.clear_widgets()

    for item in config.textLabelArray:
        self.centerDisplayGrid.add_widget(item)

def addToCenterDisplay(self, text, status):

    self.centerDisplayGrid.add_widget(config.textLabelArray[-1])

    jumpToIndex(self, len(config.textLabelArray)-1)


def makeItemLabels(self, text, status='result'):

    if len(text) <= 0:
        text = " "

    if text[:1] == "\n":
        text = text[1:]

    config.textArray.append(text)
    config.textStatusArray.append(status)

    base_text = text
    text = parseText(text, status)

    label = ButtonBehaviorLabel(text=text, size_hint=(1, None), font_size=config.blockfont, font_name='maintextfont', background_normal='', background_down='', background_color=(0,0,0,0), background_color_down=accent2)

    label.size = label.texture_size
    label.text_size = (self.centerDisplayGrid.width, None)
    label.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
    label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

    label.bind(on_release=swapBlock)
    label.bind(on_ref_press=refPress)
    label.foreground_color=(1,1,1,1)
    label.markup = True
    label.self = self
    label.index = len(config.textArray)-1
    config.textLabelArray.append(label)

def insertTextFormat(button):

    self = button.self
    index = button.index
    field = [x for x in config.textLabelArray[index].children if x.__class__.__name__ == "TextInput" ][0]

    format_to_insert = "[" + button.text + "]"

    # insert whatever the format box is into the field
    field.insert_text(format_to_insert)

    config.textArray[index] = field.text

def hideMechanicsBlocks(button):

    self = button.self
    button.background_color = neutral
    for unit in config.textLabelArray:
        if config.textStatusArray[unit.index] != "plain":
            self.centerDisplayGrid.remove_widget(unit)

def parseText(text, status):

    if status in config.formats:
        blockformat = config.formats[status]
        if blockformat == "color1":
            text = "[color=" + str(config.formats['highlight_color']) + "]" + text + "[/color]"
        elif blockformat == "color2":
            text = "[color=" + str(config.formats['alternate_color']) + "]" + text + "[/color]"
        elif blockformat == "color3":
            text = "[i][color=" + str(config.formats['transitory_color']) + "]" + text + "[/color][/i]"
        else:
            if blockformat == "bold":
                text = "[b]" + text + "[/b]"
            elif blockformat == "italic":
                text = "[i]" + text + "[/i]"
            elif blockformat == "bold_italic":
                text = "[b][i]" + text + "[/i][/b]"

    return text

# used by the spinner option
def reformatText(spinner, status):

    config.textStatusArray[spinner.index] = status
    text = config.textArray[spinner.index]
    text = parseText(text, status)
    config.textLabelArray[spinner.index].text = text

    return True

def cycleText(label, *args):

    status = label.text

    try:
        statusList = config.formats['status_tags']
    except:
        statusList = ['plain', 'aside', 'oracle', 'result', 'query', 'mechanic1', 'mechanic2', 'ephemeral']

    try:
        if statusList.index(status) == len(statusList)-1:
            status = statusList[0]
        else:
            status = statusList[statusList.index(status)+1]
    except:
        status = "plain"

    config.textStatusArray[label.index] = status
    label.text = status

    text = config.textArray[label.index]
    text = parseText(text, status)

    config.textLabelArray[label.index].text = text

    return True

# End of main text routines

def checkForTrigger(self):
    index = []
    fired = False
    for i in range(len(config.general['secrets'])):

        if config.general['secrets'][i][0] <= 0 and fired == False:
            # this trigger should Fire
            if config.general['secrets'][i][2] != 'Nothing.':
                updateCenterDisplay(self, "[Trigger (" + config.general['secrets'][i][1] + ")] " + config.general['secrets'][i][2], 'result')

            # remove the widget
            index.append(i)
            self.secretDisplayGrid.remove_widget(self.secretLabels[i])
            self.secretDisplayGrid.remove_widget(self.secretButtons[i])
            fired = True
        else:
            config.general['secrets'][i][0] = config.general['secrets'][i][0] - 1

    for i in index:
        # clear the trigger from config.general
        del config.general['secrets'][i]
        del self.secretLabels[i]
        del self.secretButtons[i]

def updateThreadDisplay(self, text, status):

    config.threadArray.append(text)
    config.threadStatusArray.append(status)

    label = TextInput(text=text, size_hint_y=None, size_hint_x=.88, multiline=False, font_size=config.threadfont, font_name='maintextfont', background_color=(0,0,0,0), foreground_color=styles.textcolor, height=config.threadheight)
    label.bind(focus=focusChangeThread)
    config.threadLabelArray.append(label)

    label = ButtonLabel(text=status, size_hint_y=None, size_hint_x=.15, font_size=config.threadstatusfont, font_name='maintextfont', height=config.threadheight)
    #label.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
    #label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
    label.background_normal=''
    label.background_color=accent1
    label.background_down=''
    label.background_color_down=accent2
    label.bind(on_press=cycleThread)
    label.markup = True
    config.threadStatusLabelArray.append(label)

    self.threadDisplayGrid.add_widget(config.threadLabelArray[-1])
    self.threadDisplayGrid.add_widget(config.threadStatusLabelArray[-1])

def cycleThread(label, *args):

    statusList = ['Current', 'Past', 'Major', 'Minor', 'Resolved', 'Abandoned', 'Success', 'Failure', 'Hide', 'BigQ']

    status = label.text

    try:
        if statusList.index(status) == len(statusList)-1:
            status = statusList[0]
        else:
            status = statusList[statusList.index(status)+1]
    except:
        status = 'Current'

    config.threadStatusArray[config.threadStatusLabelArray.index(label)] = status

    label.text = status

# sort and hide threads
def clearThread(self, *args):

    downList = ["Resolved", "Success", "Failure", "Past", "Abandoned"]
    upList = ['Major', 'Current', 'BigQ']

    topList = []
    midList = []
    bottomList = []
    hideList = []

    for i in range(len(config.threadStatusArray)):

        status = config.threadStatusArray[i]

        if status in downList:
            bottomList.append(i)
        elif status in upList:
            topList.append(i)
        elif status == "Hide":
            hideList.append(i)
        else:
            midList.append(i)

    for i in hideList:
        self.threadDisplayGrid.remove_widget(config.threadLabelArray[i])
        self.threadDisplayGrid.remove_widget(config.threadStatusLabelArray[i])

    for i in topList:
        self.threadDisplayGrid.remove_widget(config.threadLabelArray[i])
        self.threadDisplayGrid.remove_widget(config.threadStatusLabelArray[i])
        self.threadDisplayGrid.add_widget(config.threadLabelArray[i])
        self.threadDisplayGrid.add_widget(config.threadStatusLabelArray[i])

    for i in midList:
        self.threadDisplayGrid.remove_widget(config.threadLabelArray[i])
        self.threadDisplayGrid.remove_widget(config.threadStatusLabelArray[i])
        self.threadDisplayGrid.add_widget(config.threadLabelArray[i])
        self.threadDisplayGrid.add_widget(config.threadStatusLabelArray[i])

    for i in bottomList:
        self.threadDisplayGrid.remove_widget(config.threadLabelArray[i])
        self.threadDisplayGrid.remove_widget(config.threadStatusLabelArray[i])
        self.threadDisplayGrid.add_widget(config.threadLabelArray[i])
        self.threadDisplayGrid.add_widget(config.threadStatusLabelArray[i])

def updateActorDisplay(self, text, status):

    config.actorArray.append(text)
    config.actorStatusArray.append(status)

    tag, text, sep = getActorTag(text)

    label = TextInput(text=tag, size_hint_y=None, size_hint_x=1, font_size=config.actortagfont, font_name='maintextfont', background_color=(0,0,0,0), foreground_color=styles.textcolor, multiline=False, height=config.actortagheight)
    label.bind(focus=focusChangeActorTitle)
    label.self = self
    self.actorDisplayGrid.add_widget(label)
    label.index = len(config.actorLabelArray)

    label = TextInput(text=text, size_hint_y=None, size_hint_x=1, font_size=config.actorfont, font_name='maintextfont', background_color=(0,0,0,0), foreground_color=styles.textcolor)
    label.bind(focus=focusChangeActor)
    label.height = 200
    label.tag = tag
    label.sep = sep
    label.index = len(config.actorLabelArray)
    config.actorLabelArray.append(label)

    self.actorDisplayGrid.add_widget(config.actorLabelArray[-1])

    label = ButtonLabel(text=status, size_hint_y=None, size_hint_x=1, font_size=config.actorstatusfont, font_name='maintextfont',)
    label.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
    #label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
    label.bind(on_press=cycleActor)
    label.background_normal=''
    label.background_color=accent1
    label.background_down=''
    label.background_color_down=accent2
    label.markup = True
    config.actorStatusLabelArray.append(label)

    self.actorDisplayGrid.add_widget(config.actorStatusLabelArray[-1])

def cycleActor(label, *args):

    statusList = ['Past', 'In Party', 'Retired', 'Deceased', 'Remote', 'Unknown', 'Hide', 'Current']

    status = label.text

    try:
        if statusList.index(status) == len(statusList)-1:
            status = statusList[0]
        else:
            status = statusList[statusList.index(status)+1]
    except:
        status = 'Current'

    config.actorStatusArray[config.actorStatusLabelArray.index(label)] = status

    label.text = status

    return True

# I don't think this is hooked in
def showActor(self, *args):
    for i in range(len(config.actorStatusArray)):
        if config.actorStatusArray[i] == "Hide":
            self.actorDisplayGrid.add_widget(config.actorLabelArray[i])
            self.actorDisplayGrid.add_widget(config.actorStatusLabelArray[i])

# this is called only on a save
def clearActor(self, *args):
    for i in range(len(config.actorStatusArray)):
        if config.actorStatusArray[i] == "Hide":
            self.actorDisplayGrid.remove_widget(config.actorLabelArray[i])
            self.actorDisplayGrid.remove_widget(config.actorStatusLabelArray[i])

def focusChangeActor(field, value):
    if value:
        pass
    else:
        text = field.tag + field.sep + " " + field.text[0].lower() + field.text[1:]
        config.actorArray[field.index] = text

def focusChangeActorTitle(field, value):
    if value:
        pass
    else:
        label = config.actorLabelArray[field.index]
        label.tag = field.text
        text = field.text + label.sep + " " + label.text[0].lower() + label.text[1:]
        config.actorArray[field.index] = text
        updateActorIndex(field.self)

def focusChangeThread(label, value):
    if value:
        pass
    else:
        config.threadArray[config.threadLabelArray.index(label)] = label.text

def focusChangeText(field, value):
    if value:
        pass
    else:
        config.textArray[field.index] = field.text

        # if the text height has changed by more than two lines
        old_height = field.height
        new_height = max( (len(field._lines) + 1) * field.line_height, config.formats['basefontsize']*2 )

        if abs(old_height - new_height) > field.line_height*2:
            field.height = new_height

def getActorTag(text):

    tag = " "
    remainder = text

    sepList = [',', ':', '  ', '\n', '.']

    for sep in sepList:
        if sep in text:
            tag, remainder = text.split(sep, 1)
            if len(remainder) > 0:
                break

    tag = tag[:25]
    remainder = remainder.strip()
    if len(remainder) > 0:
        remainder =  remainder[0].upper() + remainder[1:]
    else:
        remainder = text

    #print(tag, remainder)

    return tag, remainder, sep

def updateActorIndex(self):

    self.actorIndexDisplayGrid.clear_widgets()

    tagArray = []
    tagDict = {}

    for item in config.actorArray:
        tag, remainder, sep = getActorTag(item)
        tagArray.append(tag)
        tagDict[tag] = item

    tagArray.sort()

    for tag in tagArray:

        item = tagDict[tag]

        button = Button(text=tag, size_hint=(1,None), halign='center', background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='maintextfont', font_size=config.actortagfont, multiline=False, height=config.actortagheight)
        button.value = config.actorArray.index(item)
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=self.jumpToActor)
        self.actorIndexDisplayGrid.add_widget(button)

def focusChangePC(field, value):
    try:
        self = field.self
        nameList = []
        for pc in range(len(config.pcKeyLabelArray)):
            name = [i for i in config.pcKeyLabelArray[pc] if i.text=="Name"]
            nn = [i for i in config.pcKeyLabelArray[pc] if i.text=="NN"]
            nick = [i for i in config.pcKeyLabelArray[pc] if i.text=="Nick"]

            if nick:
                index = config.pcKeyLabelArray[pc].index(nick[0])
                nameList.append(config.pcValueLabelArray[pc][index].text.strip("\""))
            elif nn:
                index = config.pcKeyLabelArray[pc].index(nn[0])
                nameList.append(config.pcValueLabelArray[pc][index].text.strip("\""))
            elif name:
                index = config.pcKeyLabelArray[pc].index(name[0])
                nameList.append(config.pcValueLabelArray[pc][index].text.strip("\""))
            else:
                nameList.append("")

        for i in range(len(self.pcPanelsList)):
            if len(nameList[i]) > 0:
                self.pcPanelsList[i].title = nameList[i]
    except:
        if config.debug == True:
            print("[focusChangePC] Unexpected error:", sys.exc_info())

#---------------------------------------------------------------------------------------------
# save/load functions
#---------------------------------------------------------------------------------------------

def saveconfig(self, gamedir):
    try:
        tempDict = {}
        tempDict['general'] = config.general
        tempDict['user'] = config.user
        tempDict['scenario'] = config.scenario
        tempDict['formats'] = config.formats

        f = open(gamedir + 'config.txt', 'w')
        json.dump(tempDict, f)
        f.close()
    except:
        if config.debug == True:
            print("[saveconfig] Unexpected error:", sys.exc_info())

def loadconfig(self, gamedir):

    try:

        with open(gamedir + 'config.txt', 'r') as config_file:
            tempDict = json.load(config_file)

        sectionList = ['general', 'formats', 'user', 'scenario']

        for section in sectionList:
            for key, value in tempDict[section].iteritems():
                eval("config." + section)[key] = value

    except:
        # no config, make a new one
        if config.debug == True:
            print("[CONFIG] Remaking configuration file for save game: " + gamedir)
        f = file(config.curr_game_dir + "config.txt", "w")
        saveconfig(self, config.curr_game_dir)

def quicksave(self, gamedir):

    if config.manual_edit_mode == True:
        print("Game not saved because manual_edit_mode is set to True.")
        return False

    tempArray = []

    for i in range(len(config.textArray)):
        if "\n\n" in config.textArray[i]:
            paragraphs = config.textArray[i].split('\n\n')
            for block in paragraphs:
                tempArray.append([block, config.textStatusArray[i]])
        else:
            tempArray.append([config.textArray[i], config.textStatusArray[i]])

    with open(gamedir + 'main.txt', 'w') as mainfile:
        json.dump(tempArray, mainfile)

    if os.path.isfile(gamedir + 'main_status.txt'):
        os.remove(gamedir + 'main_status.txt')

    tempArray = []
    for i in range(len(config.threadArray)):
        tempArray.append([config.threadArray[i], config.threadStatusArray[i]])

    with open(gamedir + 'threads.txt', 'w') as threadfile:
        json.dump(tempArray, threadfile)

    if os.path.isfile(gamedir + 'threads_status.txt'):
        os.remove(gamedir + 'threads_status.txt')

    tempArray = []
    for i in range(len(config.actorArray)):
        tempArray.append([config.actorArray[i], config.actorStatusArray[i]])

    with open(gamedir + 'actors.txt', 'w') as actorfile:
        json.dump(tempArray, actorfile)

    if os.path.isfile(gamedir + 'actors_status.txt'):
        os.remove(gamedir + 'actors_status.txt')

    f = open(gamedir + 'tracks.txt', 'w')
    tempArray = []
    for i in range(len(config.trackLabelArray)):
        tempArray.append([config.trackLabelArray[i].text, config.trackStatusLabelArray[i].active])
    json.dump(tempArray, f)
    f.close

    f = open(gamedir + 'pcs.txt', 'w')
    tempArray = []
    for pc in range(len(config.pcKeyLabelArray)):
        tempArray.append([])
        for i in range(len(config.pcKeyLabelArray[pc])):
            key = config.pcKeyLabelArray[pc][i].text
            val = config.pcValueLabelArray[pc][i].text
            tempArray[pc].append([key,val])

    json.dump(tempArray, f)
    f.close

    f = open(gamedir + 'maps.txt', 'w')
    maps = {}
    try:
        maps['ddmaps'] = config.mapArray
    except:
        pass

    try:
        maps['gmaps'] = config.gmapArray
    except:
        pass

    json.dump(maps, f)
    f.close()

    # images are saved in the main config file
    if os.path.exists(gamedir + "images"):
        config.user['image_labels'] = []
        for i in range(len(config.imgLabelArray)):
            config.user['image_labels'].append(config.imgLabelArray[i].text)

    saveconfig(self, gamedir)

def quickload(self, gamedir):

    # MAIN FILE
    # first, are we still using the old two file save set up?
    success = False
    try:
        with open(gamedir + 'main.txt', 'r') as mainfile, open(gamedir + 'main_status.txt', 'r') as statusfile:
            textArray = json.load(mainfile)
            textStatusArray = json.load(statusfile)
        success = True
    except:
        pass

    # are we using a one file save game version?
    if success == False:
        try:
            with open(gamedir + 'main.txt', 'r') as mainfile:
                tempArray = json.load(mainfile)
        except ValueError as err:
            if config.debug == True:
                print(err)

        try:
            textArray = []
            textStatusArray = []
            for i in range(len(tempArray)):
                textArray.append(tempArray[i][0])
                textStatusArray.append(tempArray[i][1])
        except:
            if config.debug == True:
                traceback.print_exc()

    tempTextArray = []
    tempStatusArray = []

    try:

        for i in range(len(textArray)):
            if "\n\n" in textArray[i]:
                paragraphs = textArray[i].split('\n\n')
                for block in paragraphs:
                    tempTextArray.append(block)
                    tempStatusArray.append(textStatusArray[i])
            else:
                tempTextArray.append(textArray[i])
                tempStatusArray.append(textStatusArray[i])

        if config.debug == True:
            print("[DEBUG] Total Blocks In Main Text: " + str(len(tempTextArray)))

        resetCenterDisplay(self, tempTextArray, tempStatusArray)

    except:
        if config.debug == True:
            print("[quickload Main] Unexpected error:", sys.exc_info())

    if len(tempTextArray) == 0:
        if config.manual_edit_mode == False:
            print("should be updating with tab")
            updateCenterDisplay(self, "The adventure begins...", 'italic')

    if config.manual_edit_mode == True:
        updateCenterDisplay(self, "WARNING: MANUAL EDIT MODE is ON and text will not be saved.", 'color3')

    # THREADS
    success = False
    try:
        with open(gamedir + 'threads.txt', 'r') as mainfile, open(gamedir + 'threads_status.txt', 'r') as statusfile:
            threadArray = json.load(mainfile)
            threadStatusArray = json.load(statusfile)
        success = True
    except:
        pass

    if success == False:
        try:
            with open(gamedir + 'threads.txt', 'r') as mainfile:
                tempArray = json.load(mainfile)

            threadArray = []
            threadStatusArray = []
            for i in range(len(tempArray)):
                threadArray.append(tempArray[i][0])
                threadStatusArray.append(tempArray[i][1])

        except:
            if config.debug == True:
                print("opening single file failed")

    try:
        for i in range(len(threadArray)):
            updateThreadDisplay(self, threadArray[i], threadStatusArray[i])
    except:
        if config.debug == True:
            print("[quickload Threads] Unexpected error:", sys.exc_info())

    # ACTORS
    success = False
    try:
        with open(gamedir + 'actors.txt', 'r') as mainfile, open(gamedir + 'actors_status.txt', 'r') as statusfile:
            actorArray = json.load(mainfile)
            actorStatusArray = json.load(statusfile)
        success = True
    except:
        pass

    if success == False:
        try:
            with open(gamedir + 'actors.txt', 'r') as mainfile:
                tempArray = json.load(mainfile)

            actorArray = []
            actorStatusArray = []
            for i in range(len(tempArray)):
                actorArray.append(tempArray[i][0])
                actorStatusArray.append(tempArray[i][1])

        except:
            if config.debug == True:
                print("opening single file failed")

    try:
        for i in range(len(actorArray)):
            updateActorDisplay(self, actorArray[i], actorStatusArray[i])
    except:
        if config.debug == True:
            print("[quickload Actors] Unexpected error:", sys.exc_info())

    # TRACKED INFO
    try:
        with open(gamedir + 'tracks.txt', 'r') as filename:
            tempTable= json.load(filename)

        for x in range(len(tempTable)):
            config.trackLabelArray[x].text = tempTable[x][0]
            config.trackStatusLabelArray[x].active = tempTable[x][1]
    except:
        if config.debug == True:
            print("[quickload Tracks] Unexpected error:", sys.exc_info())


    # CHARACTER SHEETS
    try:
        with open(gamedir + 'pcs.txt', 'r') as f:
            tempArray = json.load(f)

        for pc in range(len(tempArray)):
            for x in range(len(config.pcKeyLabelArray[pc])):
                config.pcKeyLabelArray[pc][x].text = tempArray[pc][x][0]
                config.pcValueLabelArray[pc][x].text = tempArray[pc][x][1]
    except:
        if config.debug == True:
            print("[quickload PCs] Unexpected error:", sys.exc_info())

    # MAPS
    try:
        with open(gamedir + 'maps.txt', 'r') as filename:
            maps = json.load(filename)

        config.mapArray = maps['ddmaps']

        tempVals = []
        for i in config.mapArray:
            tempVals.append(i)
        self.mapSpinner.values = tempVals

    except:
        pass

    try:
        with open(gamedir + 'maps.txt', 'r') as filename:
            maps = json.load(filename)

        config.gmapArray = maps['gmaps']

        tempVals = []
        for i in config.gmapArray:
            tempVals.append(i)
        self.gmapSpinner.values = tempVals

    except:
        pass

def makeBackup(subtype):

    if config.backup_limit >= 1:
        path = '.' + os.sep + 'backups'
        files = os.listdir(path)
        zipfiles = [f for f in files if f[-3:] == "zip"]
        for i in range(len(zipfiles)):
            zipfiles[i] = os.path.join(path, zipfiles[i])
        if len(zipfiles) >= config.backup_limit:
            zipfiles = sorted(zipfiles, key=os.path.getctime)
            oldest = zipfiles[0]
            os.remove(oldest)

    if config.backup_limit >= 0:
        saveFiles = '.' + os.sep + 'saves' + os.sep
        timestamp =  '{:%Y-%m-%d-%H-%M-%S}'.format(datetime.datetime.now())
        backupZip = zipfile.ZipFile('.' + os.sep + 'backups' + os.sep + timestamp + "_" + subtype + '.zip', 'w')
        for dirname, subdirs, files in os.walk(saveFiles):
            backupZip.write(dirname)
            for filename in files:
                backupZip.write(os.path.join(dirname, filename))
        backupZip.close()

def storeBookmarkLabel(label):
    try:
        index = label.index
    except:
        index = -9

    bset = False
    l = ToggleButtonBehavior.get_widgets('bookmarks')
    for button in l:
        if button.state == "down":
            button.index = index
            button.state = 'normal'
            button.text = str(index)
            config.general['bookmarks'][button.value] = index
            bset = True
    del l

    return bset


def parseTextForDice(text):

    roll_results = []

    words = text.split(' ')
    for word in words:
        if any(ext in word for ext in ["1","2","3","4","5","6","7","8","9","0"]):
            if any(ext in word for ext in ['.', '!', ',', '?', ':', ';', '-']):
                word = word[:-1]
            result = rollDice(word)
            if result != "Please use standard dice notation, ie, 1d10 or 2d6x3 or 2d8+6.":
                roll_results.append(result)

    if len(roll_results) == 0:
        return False

    return '\n'.join(roll_results)


def rollDice(text):

    results = "Please use standard dice notation, ie, 1d10 or 2d6x3 or 2d8+6."
    count = 1
    sides = 100
    reps = 1
    mod = 0

    if len(text) > 0:
        try:
            count, sides = text.split("d")
        except:
            return results

        try:
            sides, reps = sides.split("x")
        except:
            pass

        if reps > 1:
            try:
                reps, mod = reps.split("+")
            except:
                pass
        else:
            try:
                sides, mod = sides.split("+")
            except:
                pass

        try:
            sides = int(sides)
            count = int(count)
        except:
            return results

        try:
            reps = int(reps)
        except:
            pass

        try:
            mod = int(mod)
        except:
            pass

        results = "Rolling " + str(count) + "d" + str(sides) + " " + str(reps) + " times."
        for m in range(int(reps)):
            resultArray = []
            result = 0
            resultstring = " "
            if int(count) and int(sides):
                if config.general['use_dice_qualities'] == True:
                    qualifiers = random.sample(config.user['resolution_qualifiers'], min(int(count), len(config.user['resolution_qualifiers'])))
                for i in range(int(count)):
                    x = random.randint(1,int(sides))
                    resultArray.append(x)
                    result = result + x
                    resultstring = resultstring + " " + str(x)
                    if config.general['use_dice_qualities'] == True:
                        try:
                            resultstring = resultstring + " (" + qualifiers[i] + ")"
                        except:
                            resultstring = resultstring + " (" + random.choice(config.user['resolution_qualifiers']) + ")"

            total = ""
            if mod > 0:
                total = " + " + str(mod) + " = " + str(result + mod)
            results = results + "\n[" + resultstring + "  ] " + str(result) + total

    return results

def rollOREDice(text):

    try:
        uplim = int(text)
    except:
        return "Please enter a number in the main text input for your dice pool."

    resultList = []
    rawList = []
    matchList = []
    waste = ""
    match_string = ""

    for x in range(0, 11):
        resultList.append(0)

    for x in range(0, uplim):
        resultList.append(0)
        result = random.randint(1,10)
        rawList.append(result)
        resultList[result] = resultList[result] + 1

    result_string = "[" + ', '.join(str(x) for x in rawList) + "] Matches: "

    for x in range(0, len(resultList)):
        if resultList[x] > 1:
            match_string = match_string + " %d x %d  " % (resultList[x], x)
        if resultList[x] == 1:
            waste = waste + str(x) + ", "

    if len(match_string) == 0:
        match_string = "NONE"

    result_string = result_string + match_string + " Waste: %s" % (waste)

    return result_string

#---------------------------------------------------------------------------------------------------
# --> Random choosers from player defined lists
#---------------------------------------------------------------------------------------------------

def getRandomActor(key="All"):

    textarray = []
    result = "[Random actor, key: " + key + "] " + "No results found."

    for i in range(len(config.actorArray)):
        textarray.append( config.actorArray[i] + " (" + config.actorStatusArray[i] + ")" )

    if key == "All" and len(textarray) > 0:
        result = "[Random actor, key: " + key + "] " + random.choice(textarray)
    else:
        matching = [s for s in textarray if key in s]

        if len(matching) > 0:
            result = "[Random actor, key: " + key + "] " + random.choice(matching)

    return result

def getRandomThread(key="All"):

    textarray = []
    result = "[Random thread, key: " + key  + "] No results found."

    for i in range(len(config.threadLabelArray)):
        textarray.append(config.threadLabelArray[i].text + ", " + config.threadStatusLabelArray[i].text)

    if key == "All" and len(textarray) > 0:
        result = "[Random thread, key: " + key  + "] " + random.choice(textarray)
    else:
        matching = [s for s in textarray if key in s]

        if len(matching) > 0:
            result = "[Random thread, key: " + key  + " ] " + random.choice(matching)

    return result

def getRandomPC(key="Name"):

    textarray = []

    for k in range(len(config.pcKeyLabelArray)):
        for i in range(len(config.pcKeyLabelArray[k])):
            textarray.append(config.pcKeyLabelArray[k][i].text + ": " + config.pcValueLabelArray[k][i].text)

    matching = [s for s in textarray if key in s]

    if len(matching) > 0:
        result = "[Random Major Character, key: " + key  + " ] " + random.choice(matching)
    else:
        result = "[Random Major Character, key: " + key  + " ] "  + "No results found."

    return result

def getRandomTrack(key="Active"):

    textarray = []
    matching = []
    result = "[Random track, key: " + key + " ] " + "No results found."
    for i in range(len(config.trackLabelArray)):
        status = "Inactive"
        if config.trackStatusLabelArray[i].active == True:
            status = "Active"
        textarray.append(config.trackLabelArray[i].text + " (" + status + ")")

    if key == "Active":
        for i in range(len(config.trackLabelArray)):
            if config.trackStatusLabelArray[i].active == True:
                matching.append(config.trackLabelArray[i].text)
    else:
        matching = [s for s in textarray if key in s]

    if len(matching) > 0:
        result = "[Random track, key: " + key  + " ] " + random.choice(matching)

    return result

# find
def findText(self, search_string):
    # list comprehension on config.textArray
    search_terms = [search_string.lower(), search_string.capitalize(), search_string]

    resultList = []

    for term in search_terms:
        resultList = resultList + [s for s in config.textArray if term in s]

    config.general['findList'] = list(set(resultList))
    config.general['findIndex'] = 0

    self.findButton.text = "find: " + str(len(config.general['findList']))

    # get the index of the first element
    element = ""
    if len(config.general['findList']) > 0:
        element = config.general['findList'][0]

    if len(element) > 0:
        index = config.textArray.index(element)
    else:
        return "No results found."

    jumpToIndex(self, index)

def jumpToNext(self):

    try:
        if config.general['findIndex'] == len(config.general['findList'])-1:
            config.general['findIndex'] = 0
        else:
            config.general['findIndex'] = config.general['findIndex'] + 1

        element = config.general['findList'][config.general['findIndex']]
        index = config.textArray.index(element)
        jumpToIndex(self, index)
    except:
        pass

def jumpToIndex(self, index):

    if index == -1 or index == 0:
        self.centerDisplay.scroll_to(self.centerDisplay.children[index])
    else:
        self.centerDisplay.scroll_to(config.textLabelArray[index])

# weighted choosers
def chooseWeighted(value, text, form):
    result_string = ""
    result = "Please enter a comma-separated list in one line that has at least as many options as needed. Excess options will be ignored."
    try:
        if value == 1:
            # 2d4
            index = 2
            chart = {}
            result_string = ""
            result = text.split(", ")
            for i in result:
                chart[index] = i
                index = index + 1
            roll = random.randint(1,4) + random.randint(1,4)
            result = chart[roll]
            for key,value in chart.items():
                result_string = result_string + "[" + str(key) + "] " + value + " "
        elif value == 2:
            # 2d6
            index = 2
            chart = {}
            result_string = ""
            result = text.split(", ")
            for i in result:
                chart[index] = i
                index = index + 1
            roll = random.randint(1,6) + random.randint(1,6)
            result = chart[roll]
            for key,value in chart.items():
                result_string = result_string + str(key) + ": " + value + " "
        elif value == 3:
            # 3:2:1
            roll = random.randint(1,6)
            chart = text.split(", ")
            result_string = "3: " + chart[0] + " 2: " + chart[1] + " 1: " + chart[2]
            if roll <= 3:
                result = chart[0]
                roll = 3
            elif roll <= 5:
                result = chart[1]
                roll = 2
            elif roll == 6:
                result = chart[2]
                roll = 1
        else:
            result_string = text
            if value == 0:
                result = random.choice(text.split(", "))
            elif value == 4:
                result = ', '.join(random.sample(text.split(", "), 2))
            elif value == 5:
                result = ', '.join(random.sample(text.split(", "), 3))
            elif value == 6:
                result = ', '.join(random.sample(text.split(", "), 4))
            elif value == 7:
                result = ', '.join(random.sample(text.split(", "), 5))
            roll = "Choice"

        return str(result_string), str(result), str(form), str(roll)

    except:
        return str(result_string), str(result), str("ephemeral"), str("0")

# ---------------------------
# Shared Functions for Logs
# ---------------------------

def getSourceMaterial():

    textArray = []
    textStatusArray = []

    with open(config.curr_game_dir + 'main.txt', 'r') as mainfile:
        tempArray = json.load(mainfile)

    for i in range(len(tempArray)):
        textArray.append(tempArray[i][0])
        textStatusArray.append(tempArray[i][1])

    return textArray, textStatusArray

def parseMarkup(result):

    result = result.replace('[i]', '_')
    result = result.replace('[/i]', '_')
    result = result.replace('[b]', '**')
    result = result.replace('[/b]', '**')
    result = result.replace('[u]', '<u>')
    result = result.replace('[/u]', '</u>')
    result = result.replace('[s]', '<s>')
    result = result.replace('[/s]', '</s>')
    result = result.replace('[sub]', '<sub>')
    result = result.replace('[/sub]', '</sub>')
    result = result.replace('[sup]', '<sup>')
    result = result.replace('[/sup]', '</sup>')
    result = result.replace('---', '\n***\n')

    return result

def escapeHTML(result):

    escapes = [ ['&', '&amp;'], ['<=', ' &le; '], ['>=', ' &ge; '], ['<', ' &lt; '], ['>', ' &gt; '], ['\n', '<br>'], ['[i]', '<i>'], ['[/i]', '</i>'], ['[b]', '<b>'] , ['[/b]', '</b>'], ['[u]', '<u>'], ['[/u]', '</u>'], ['[s]', '<s>'], ['[/s]', '</s>'], ['[sub]', '<sub>'], ['[/sub]', '</sub>'], ['[sup]', '<sup>'], ['[/sup]', '</sup>'], ['<p>', '\n<p>'] ]

    for pair in escapes:
        result = result.replace(pair[0], pair[1])

    return result


def generateCSS():

    css_string = "/* styles for styling Pythia play logs generated with the css logforms */\n/* Mechanic has sub-classes corresponding to Pythia format tags. Fiction just has sub tags like <i> and <b> so shouldn't need special styling unless you want to. */ \n\n#mechanic { opacity: 0.5; } \n#mechanic.result { font-style: italic; } \n#mechanic.query { font-weight: bold; } \n#mechanic.aside { font-style: italic; } \n#mechanic.oracle { font-weight: bold; font-style: italic; } \n#mechanic.mechanic1 { color: #" + config.formats['highlight_color']  + "; } \n#mechanic.mechanic2 { color: #" + config.formats['alternate_color']  + "; } \n#mechanic.ephemeral { color: #" + config.formats['transitory_color']  + "; }\n#fiction { opacity: 1.0; }"

    logfile = config.curr_game_dir + "logs" + os.sep + "style.css"

    with open(logfile, "w") as log_file:
        log_file.write(css_string.encode('utf-8'))

# here's full 100 item Mythic-Style lists; I don't think these are tied in right now
def seed_action():
    chart = ['accelerate', 'accumulate', 'acquire', 'adjust', 'adopt', 'advance', 'align', 'alter', 'anger', 'anticipate', 'assist', 'assume', 'bestow', 'carry', 'change', 'clarify', 'command', 'commit', 'conclude', 'consider', 'construct', 'control', 'convince', 'couple', 'determine', 'discover', 'disregard', 'divert', 'divide', 'draw', 'dream', 'edgy', 'educate', 'emphasize', 'enable', 'enchain', 'encourage', 'endless', 'enjoy', 'enrage', 'enter', 'entrance', 'eviscerate', 'examine', 'exchange', 'execute', 'exhaust', 'experience', 'facilitate', 'fascinate', 'feint', 'guess', 'impassion', 'improvise', 'inflame', 'inflate', 'interest', 'involve', 'justify', 'keep', 'ken', 'locate', 'loosen', 'lose', 'love', 'mend', 'mesmerize', 'motivate', 'murder', 'negotiate', 'nurture', 'obscure', 'overcome', 'penalize', 'quarter', 'question', 'refuse', 'reject', 'renegotiate', 'revenge', 'run', 'share', 'simplify', 'spy', 'squelch', 'stoic', 'strengthen', 'substitute', 'synthesize', 'teach', 'tighten', 'track', 'transition', 'trap', 'triumph', 'tumble', 'unify', 'unveil', 'weaken', 'withdraw']

    return random.choice(chart)

def seed_subject():
    chart = ['addiction', 'air', 'ally', 'armor', 'art', 'beyond', 'blood', 'bravery', 'change', 'class', 'cold', 'common', 'compassion', 'consumption', 'couple', 'cowardice', 'death', 'disaster', 'dispassion', 'displeasure', 'earth', 'earth', 'elements', 'emotions', 'enemy', 'fatigue', 'focus', 'foreign', 'forgiveness', 'freedom', 'friend', 'friendship', 'fury', 'future', 'grief', 'hatred', 'health', 'home', 'honor', 'hope', 'hot', 'ideas', 'illness', 'insanity', 'instinct', 'integrity', 'jewel', 'journey', 'joy', 'key', 'kin', 'location', 'love', 'luxuries', 'master', 'moderation', 'monster', 'moon', 'music', 'near', 'necessities', 'neighbor', 'obsession', 'passion', 'past', 'path', 'physical', 'possessions', 'power', 'priceless', 'quarry', 'quest', 'rain', 'reason', 'regret', 'reserves', 'rubbish', 'sex', 'shine', 'skill', 'sorrow', 'stalemate', 'star', 'status quo', 'stoicism', 'sun', 'survival', 'task', 'tool', 'trap', 'uncontrollable', 'unknowable', 'value', 'vengeance', 'violence', 'water', 'wealth', 'weapons', 'whimsy', 'work']

    return random.choice(chart)
