#!/usr/bin/env python
#-*- coding: utf-8 -*-
##-------------------------------------------------------------------------------------------------------------------------------------------
#  General logic
#
##-------------------------------------------------------------------------------------------------------------------------------------------

import imports
from imports import *
import config

import logicscen
from logicscen import *

#-------------------------------------------------------------------------------------------------------------------------------------------
# Basic
#-------------------------------------------------------------------------------------------------------------------------------------------

class ClickLabel(Button, Label):
    pass

class InputLabel(TextInput, Label):
    pass

def resetCenterDisplay(self, edit_mode):

    self.centerDisplayGrid.clear_widgets()

    config.textLabelArray = []

    config.textStatusLabelArray = []

    for i in config.textArray:
        updateCenterDisplay(self, i, config.textStatusArray[config.textArray.index(i)], True)

def updateCenterDisplay(self, text, status='result', reset=False):

    if len(text) <= 0:
        return

    edit_mode = config.general['edit_behavior']

    if text[:1] == "\n":
        text = text[1:]

    if reset == False:
        config.textArray.append(text)
        config.textStatusArray.append(status)

    base_text = text

    if status == "ephemeral":
        text = "[i][color=" + str(config.transitory_color) + "]" + text + "[/color][/i]"
    elif status == "query":
        text = "[b]" + text + "[/b]"
    elif status == "result":
        text = "[i]" + text + "[/i]"
    elif status == "oracle":
        text = "[b][i]" + text + "[/i][/b]"
    elif status == "italic":
        text = "[i]" + text + "[/i]"
    elif status == "bold":
        text = "[b]" + text + "[/b]"
    elif status == "color1":
        text = "[color=" + str(config.highlight_color) + "]" + text + "[/color]"
    elif status == "color2":
        text = "[color=" + str(config.alternate_color) + "]" + text + "[/color]"
    elif status == "bold_italic":
        text = "[b][i]" + text + "[/i][/b]"
    else:
        pass

    if edit_mode == "READ":
        # this mode is for reading the entire log, mechanics and all

        self.centerDisplayGrid.cols = 1

        label = ClickLabel(text=text, size_hint_y=None, font_size=config.maintextfont, font_name='Fantasque-Sans', background_normal='', background_down='', background_color=(0,0,0,0), background_color_down=accent2)
        label.text_size = (self.centerDisplayGrid.width, None)
        label.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        label.bind(on_release=storeBookmarkLabel)
        label.bind(on_ref_press=refPress)
        label.foreground_color=(1,1,1,1)
        label.markup = True
        label.self = self
        label.index = config.textArray.index(base_text)
        config.textLabelArray.append(label)

        self.centerDisplayGrid.add_widget(config.textLabelArray[-1])

    elif edit_mode == "PLAY":
        # this mode is used if you're prone to forgetting to change format type but don't wish to edit text

        self.centerDisplayGrid.cols = 2

        label = Label(text=text, size_hint_y=None, size_hint_x=.85, font_size=config.maintextfont, font_name='Fantasque-Sans', background_color=(0,0,0,0), foreground_color=styles.textcolor)
        label.text_size = (self.centerDisplayGrid.width, None)
        label.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        label.bind(on_release=storeBookmarkLabel)
        label.bind(on_ref_press=refPress)
        label.foreground_color=(1,1,1,1)
        label.markup = True
        label.self = self
        label.index = config.textArray.index(base_text)
        config.textLabelArray.append(label)

        label = ClickLabel(text=status, size_hint_y=None, size_hint_x=.15, height=12, font_size=config.basefont75, font_name='Fantasque-Sans')
        label.background_normal=''
        label.background_color=accent1
        label.background_down=''
        label.background_color_down=accent2
        label.bind(on_press=cycleText)
        label.markup = True
        config.textStatusLabelArray.append(label)

        self.centerDisplayGrid.add_widget(config.textLabelArray[-1])
        self.centerDisplayGrid.add_widget(config.textStatusLabelArray[-1])

    elif edit_mode == "CLEAN":
        # clean mode for reading just text; don't show mechanics or formatting tags

        self.centerDisplayGrid.cols = 1

        if status == "no_format":

            label = ClickLabel(text=text, size_hint_y=None, font_size=config.maintextfont, font_name='Fantasque-Sans', background_normal='', background_down='', background_color=(0,0,0,0), background_color_down=accent2)
            label.text_size = (self.centerDisplayGrid.width, None)
            label.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
            label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
            label.bind(on_release=storeBookmarkLabel)
            label.bind(on_ref_press=refPress)
            label.foreground_color=(1,1,1,1)
            label.markup = True
            label.index = config.textArray.index(base_text)
            config.textLabelArray.append(label)

            self.centerDisplayGrid.add_widget(config.textLabelArray[-1])

    elif edit_mode == "CEDIT":
        # editing mode for just text, no mechanics or formatting tags

        self.centerDisplayGrid.cols = 1

        if status == "no_format":

            label = TextInput(text=base_text, size_hint_y=None, font_size=config.maintextfont)
            label.text_size = (self.centerDisplayGrid.width, None)
            label.height = max(((len(label._lines)/4)+1) * label.line_height, config.general['basefontsize']*2)
            label.bind(focus=focusChangeText)
            label.background_color=(0,0,0,.5)
            label.foreground_color=(1,1,1,1)
            label.index = config.textArray.index(base_text)
            config.textLabelArray.append(label)

            self.centerDisplayGrid.add_widget(config.textLabelArray[-1])

    else:
        # full editing mode, text, mechanics, formatting

        self.centerDisplayGrid.cols = 2

        label = TextInput(text=base_text, size_hint_y=None, size_hint_x=.85, font_size=config.maintextfont)
        label.text_size = (self.centerDisplayGrid.width, None)
        label.height = max(((len(label._lines)/4)+1) * label.line_height, config.general['basefontsize']*2)
        label.bind(focus=focusChangeText)
        label.background_color=(0,0,0,.5)
        label.foreground_color=(1,1,1,1)
        #label.index = len(config.textLabelArray)
        label.index = config.textArray.index(base_text)
        config.textLabelArray.append(label)

        label = ClickLabel(text=status, size_hint_y=None, size_hint_x=.15, font_size=config.basefont75, font_name='Fantasque-Sans')
        label.background_normal=''
        label.background_color=accent1
        label.background_down=''
        label.background_color_down=accent2
        label.bind(on_press=cycleText)
        label.markup = True
        config.textStatusLabelArray.append(label)

        self.centerDisplayGrid.add_widget(config.textLabelArray[-1])
        self.centerDisplayGrid.add_widget(config.textStatusLabelArray[-1])

    try:
        self.centerDisplay.scroll_to(config.textLabelArray[-1])
    except:
        pass

def cycleText(self, *args):
    if self.text == "color2":
        self.text = "ephemeral"
        config.textStatusArray[config.textStatusLabelArray.index(self)] = "ephemeral"
    elif self.text == "ephemeral":
        self.text = "result"
        config.textStatusArray[config.textStatusLabelArray.index(self)] = "result"
    elif self.text == "result":
        self.text = "query"
        config.textStatusArray[config.textStatusLabelArray.index(self)] = "query"
    elif self.text == "query":
        self.text = "oracle"
        config.textStatusArray[config.textStatusLabelArray.index(self)] = "oracle"
    elif self.text == "oracle":
        self.text = "no_format"
        config.textStatusArray[config.textStatusLabelArray.index(self)] = "no_format"
    elif self.text == "no_format":
        self.text = "italic"
        config.textStatusArray[config.textStatusLabelArray.index(self)] = "italic"
    elif self.text == "italic":
        self.text = "bold"
        config.textStatusArray[config.textStatusLabelArray.index(self)] = "bold"
    elif self.text == "bold":
        self.text = "bold_italic"
        config.textStatusArray[config.textStatusLabelArray.index(self)] = "bold_italic"
    elif self.text == "bold_italic":
        self.text = "color1"
        config.textStatusArray[config.textStatusLabelArray.index(self)] = "color1"
    elif self.text == "color1":
        self.text = "color2"
        config.textStatusArray[config.textStatusLabelArray.index(self)] = "color2"
    else:
        self.text = "no_format"
        config.textStatusArray[config.textStatusLabelArray.index(self)] = "no_format"

    return True

def updateThreadDisplay(self, text, status):

    config.threadArray.append(text)
    config.threadStatusArray.append(status)

    label = TextInput(text=text, size_hint_y=None, size_hint_x=.90, multiline=False, height=config.baseheight, font_size=config.basefont90, font_name='Fantasque-Sans', background_color=(0,0,0,0), foreground_color=styles.textcolor)
    label.bind(focus=focusChangeThread)
    config.threadLabelArray.append(label)
    self.threadDisplayGrid.add_widget(config.threadLabelArray[-1], len(self.threadDisplayGrid.children))

    label = ClickLabel(text=status, size_hint_y=None, size_hint_x=.10, height=config.baseheight, font_size=config.basefont75, font_name='Fantasque-Sans')
    label.background_normal=''
    label.background_color=accent1
    label.background_down=''
    label.background_color_down=accent2
    label.bind(on_press=cycleThread)
    label.markup = True
    config.threadStatusLabelArray.append(label)
    self.threadDisplayGrid.add_widget(config.threadStatusLabelArray[-1], len(self.threadDisplayGrid.children))


def cycleThread(self, *args):
    # current -> major -> minor -> past -> resolved -> abandoned -> removed -> current
    if self.text == "Current":
        self.text = "Major"
        config.threadStatusArray[config.threadStatusLabelArray.index(self)] = "Major"
    elif self.text == "Major":
        self.text = "Minor"
        config.threadStatusArray[config.threadStatusLabelArray.index(self)] = "Minor"
    elif self.text == "Minor":
        self.text = "Past"
        config.threadStatusArray[config.threadStatusLabelArray.index(self)] = "Past"
    elif self.text == "Past":
        self.text = "Resolved"
        config.threadStatusArray[config.threadStatusLabelArray.index(self)] = "Resolved"
    elif self.text == "Resolved":
        self.text = "Abandoned"
        config.threadStatusArray[config.threadStatusLabelArray.index(self)] = "Abandoned"
    elif self.text == "Abandoned":
        self.text = "Don't Show"
        config.threadStatusArray[config.threadStatusLabelArray.index(self)] = "Don't Show"
    elif self.text == "Don't Show":
        self.text = "Current"
        config.threadStatusArray[config.threadStatusLabelArray.index(self)] = "Current"
    else:
        self.text = "Current"
        config.threadStatusArray[config.threadStatusLabelArray.index(self)] = "Current"

    return True

# call this on a new thread added; plenty of time to change our minds
def clearThread(self, *args):
    for i in range(len(config.threadStatusArray)):
        if config.threadStatusArray[i] == "Don't Show":
            self.threadDisplayGrid.remove_widget(config.threadLabelArray[i])
            self.threadDisplayGrid.remove_widget(config.threadStatusLabelArray[i])

def updateActorDisplay(self, text, status):

    config.actorArray.append(text)
    config.actorStatusArray.append(status)

    label = Label(text=' ', size_hint_y=None, size_hint_x=1, font_size=config.basefont80, height=config.basefont80, font_name='Fantasque-Sans',)
    self.actorDisplayGrid.add_widget(label)

    label = TextInput(text=text, size_hint_y=None, size_hint_x=1, height=config.octupleheight, font_size=config.basefont, font_name='Fantasque-Sans', background_color=(0,0,0,0), foreground_color=styles.textcolor)
    label.bind(focus=focusChangeActor)
    label.text_size = (self.actorDisplayGrid.width, None)
    label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
    label.markup = True
    config.actorLabelArray.append(label)

    self.actorDisplayGrid.add_widget(config.actorLabelArray[-1])

    label = ClickLabel(text=status, size_hint_y=None, size_hint_x=1, font_size=config.basefont80, height=config.basefont80, font_name='Fantasque-Sans',)
    label.bind(on_press=cycleActor)
    label.background_normal=''
    label.background_color=accent1
    label.background_down=''
    label.background_color_down=accent2
    label.markup = True
    config.actorStatusLabelArray.append(label)

    self.actorDisplayGrid.add_widget(config.actorStatusLabelArray[-1])

    label = Label(text=' ', size_hint_y=None, size_hint_x=1, font_size=config.basefont80, height=config.basefont80, font_name='Fantasque-Sans',)
    self.actorDisplayGrid.add_widget(label)

def cycleActor(self, *args):
    if self.text == "Current":
        self.text = "Past"
        config.actorStatusArray[config.actorStatusLabelArray.index(self)] = "Past"
    elif self.text == "Past":
        self.text = "In Party"
        config.actorStatusArray[config.actorStatusLabelArray.index(self)] = "In Party"
    elif self.text == "In Party":
        self.text = "Retired"
        config.actorStatusArray[config.actorStatusLabelArray.index(self)] = "Retired"
    elif self.text == "Retired":
        self.text = "Deceased"
        config.actorStatusArray[config.actorStatusLabelArray.index(self)] = "Deceased"
    elif self.text == "Deceased":
        self.text = "Remote"
        config.actorStatusArray[config.actorStatusLabelArray.index(self)] = "Remote"
    elif self.text == "Remote":
        self.text = "Unknown"
        config.actorStatusArray[config.actorStatusLabelArray.index(self)] = "Unknown"
    elif self.text == "Unknown":
        self.text = "Don't Show"
        config.actorStatusArray[config.actorStatusLabelArray.index(self)] = "Don't Show"
    else:
        self.text = "Current"
        config.actorStatusArray[config.actorStatusLabelArray.index(self)] = "Current"
    return True

def showActor(self, *args):
    for i in range(len(config.actorStatusArray)):
        if config.actorStatusArray[i] == "Hide":
            self.actorDisplayGrid.add_widget(config.actorLabelArray[i])
            self.actorDisplayGrid.add_widget(config.actorStatusLabelArray[i])

def clearActor(self, *args):
    for i in range(len(config.actorStatusArray)):
        if config.actorStatusArray[i] == "Don't Show":
            self.actorDisplayGrid.remove_widget(config.actorLabelArray[i])
            self.actorDisplayGrid.remove_widget(config.actorStatusLabelArray[i])

def focusChangeActor(self, value):
    if value:
        pass
    else:
        config.actorArray[config.actorLabelArray.index(self)] = self.text

def focusChangeThread(self, value):
    if value:
        pass
    else:
        config.threadArray[config.threadLabelArray.index(self)] = self.text

def focusChangeText(self, value):
    if value:
        pass
    else:
        config.textArray[self.index] = self.text

#-------------------------------------------------------------------------------------------------------------------------------------------
# save/load functions
#-------------------------------------------------------------------------------------------------------------------------------------------
def saveconfig(self, gamedir):
    try:
        tempDict = {}
        tempDict['general'] = config.general
        tempDict['user'] = config.user
        tempDict['scenario'] = config.scenario

        f = open(gamedir + 'config.txt', 'w')
        json.dump(tempDict, f)
        f.close()
    except:
        print("Saving configuration file failed.")

def loadconfig(self, gamedir):
    #try:
        f = open(gamedir + 'config.txt', 'r')
        tempDict = json.load(f)
        for i in tempDict['general']:
            config.general[i] = tempDict['general'][i]
        for i in tempDict['user']:
            config.user[i] = tempDict['user'][i]
        for i in tempDict['scenario']:
            config.scenario[i] = tempDict['scenario'][i]
        f.close()
    #except:
    #    saveconfig(self, gamedir)

def quicksave(self, gamedir):

    f = open(gamedir + 'main.txt', 'w')
    json.dump(config.textArray, f)
    f.close()

    f = open(gamedir + 'main_status.txt', 'w')
    json.dump(config.textStatusArray, f)
    f.close()

    f = open(gamedir + 'threads.txt', 'w')
    json.dump(config.threadArray, f)
    f.close()

    f = open(gamedir + 'threads_status.txt', 'w')
    json.dump(config.threadStatusArray, f)
    f.close()

    f = open(gamedir + 'actors.txt', 'w')
    json.dump(config.actorArray, f)
    f.close()

    f = open(gamedir + 'actors_status.txt', 'w')
    json.dump(config.actorStatusArray, f)
    f.close()

    f = open(gamedir + 'tracks.txt', 'w')
    tempArray = []
    for i in range(len(config.trackLabelArray)):
        tempArray.append([config.trackLabelArray[i].text, config.trackStatusLabelArray[i].active])
    json.dump(tempArray, f)
    f.close

    f = open(gamedir + 'pcs.txt', 'w')
    tempArray = []
    for i in range(len(config.pcKeyLabelArray)):
        tempArray.append([config.pcKeyLabelArray[i].text, config.pcValueLabelArray[i].text])
    json.dump(tempArray, f)
    f.close

    updateCleanMarkdown()
    updateCleanHTML()
    updateCollapseHTML()

    saveconfig(self, gamedir)

def quickload(self, gamedir):

    try:
        f = open(gamedir + 'main.txt', 'r')
        x = open(gamedir + 'main_status.txt', 'r')
        tempArray = json.load(f)
        tempStatusArray = json.load(x)
        for i in tempArray:
            curr_index = tempArray.index(i)
            updateCenterDisplay(self, i, tempStatusArray[curr_index])
        self.centerDisplay.scroll_to(config.textLabelArray[-1])
        f.close()
        x.close()
    except:
        updateCenterDisplay(self, "The adventure begins...", 'italic')

    try:
        f = open(gamedir + 'threads.txt', 'r')
        x = open(gamedir + 'threads_status.txt', 'r')
        tempTable = []
        tempStatusTable = []

        for i in json.load(f):
            tempTable.append(i)

        for z in json.load(x):
            tempStatusTable.append(z)

        for m in range(len(tempTable)):
            updateThreadDisplay(self, tempTable[m], tempStatusTable[m])
        f.close()
        x.close()
    except:
        pass

    try:
        f = open(gamedir + 'actors.txt', 'r')
        x = open(gamedir + 'actors_status.txt', 'r')
        tempTable = []
        tempStatusTable = []

        for i in json.load(f):
            tempTable.append(i)

        for z in json.load(x):
            tempStatusTable.append(z)

        for m in range(len(tempTable)):
            updateActorDisplay(self, tempTable[m], tempStatusTable[m])
        f.close()
        x.close()
    except:
        pass

    try:
        f = open(gamedir + 'tracks.txt', 'r')
        tempTable = []
        for i in json.load(f):
            tempTable.append(i)

        for x in range(len(tempTable)):
            config.trackLabelArray[x].text = tempTable[x][0]
            config.trackStatusLabelArray[x].active = tempTable[x][1]
        f.close()
    except:
        pass

    try:
        f = open(gamedir + 'pcs.txt', 'r')
        tempTable = []
        for i in json.load(f):
            tempTable.append(i)

        for x in range(len(tempTable)):
            config.pcKeyLabelArray[x].text = tempTable[x][0]
            config.pcValueLabelArray[x].text = tempTable[x][1]
        f.close()
    except:
        pass

def makeBackup():
    saveFiles = '.' + os.sep + 'saves' + os.sep
    timestamp =  'save_{:%Y-%m-%d-%H-%M-%S}'.format(datetime.datetime.now())
    backupZip = zipfile.ZipFile('.' + os.sep + 'backups' + os.sep + timestamp + '.zip', 'w')
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
    #for i in range(len(config.textArray)):
    #    if label.text == config.textArray[i]:
    #        index = i
    l = ToggleButtonBehavior.get_widgets('bookmarks')
    for button in l:
        if button.state == "down":
            button.index = index
            button.state = 'normal'
            button.text = str(index)
            config.general['bookmarks'][button.value] = index
    del l

def updateCleanMarkdown():
    try:
        with open(config.curr_game_dir + "log_clean.md", "w") as log_file:
            result = "\n"
            for item in config.textArray:
                ti = config.textArray.index(item)
                item = item.rstrip()
                if config.textStatusArray[ti] != "ephemeral":
                    if config.textStatusArray[ti] == "italic" or config.textStatusArray[ti] == "result":
                        item = item.replace('\n', '*\n*')
                        result = result + "\n*" + item + "*"
                    elif config.textStatusArray[ti] == "bold" or config.textStatusArray[ti] == "query":
                        item = item.replace('\n', '**\n**')
                        result = result + "\n**" + item + "**"
                    elif config.textStatusArray[ti] == "bold_italic" or config.textStatusArray[ti] == "oracle":
                        item = item.replace('\n', '_**\n**_')
                        result = result + "\n**_" + item + "_**"
                    elif config.textStatusArray[ti] == "color1":
                        item = item.replace('\n', '`\n`')
                        result = result + "\n`" + item + "`"
                    elif config.textStatusArray[ti] == "color2":
                        item = item.replace('\n', '`\n`')
                        result = result + "\n`" + item + "`"
                    else:
                        result = result + "\n" + item
            log_file.write(result)
    except:
        pass

def updateCleanHTML():
    try:
        with open(config.curr_game_dir + "log_standard.html", "w") as log_file:
            result = "\n<html>\n<head>\n<title>" + config.curr_title + "</title>\n"
            style = '\n<style type="text/css">'
            style = style + "\n.italic {\nfont-style: italic;\n}"
            style = style + "\n.italicbold {\nfont-style: italic;font-weight: bold;\n}"
            style = style + "\n.bold {\nfont-weight: bold;\n}"
            style = style + "\n.highlightcolor {\ncolor: #" + config.highlight_color + ";\n}"
            style = style + "\n.alternatecolor {\ncolor: #" + config.alternate_color + ";\n}"
            style = style + "\n</style>\n"
            result = result + style + "</head>\n<body><!-- actual adventure starts here -->"
            # actual adventure content starts here
            for item in config.textArray:
                ti = config.textArray.index(item)
                if config.textStatusArray[ti] != "ephemeral":
                    if config.textStatusArray[ti] == "italic" or config.textStatusArray[ti] == "result":
                        result = result + '\n<div class="mechanic"><div class="italic">' + item + "</div></div>"
                    elif config.textStatusArray[ti] == "bold" or config.textStatusArray[ti] == "query":
                        result = result + '\n<div class="mechanic"><div class="bold">' + item + "</div></div>"
                    elif config.textStatusArray[ti] == "bold_italic" or config.textStatusArray[ti] == "oracle":
                        result = result + '\n<div class="mechanic"><div class="italicbold">' + item + "</div></div>"
                    elif config.textStatusArray[ti] == "color1":
                        result = result + '\n<div class="mechanic"><div class="highlightcolor">' + item + "</div></div>"
                    elif config.textStatusArray[ti] == "color2":
                        result = result + '\n<div class="mechanic"><div class="alternatecolor">' + item + "</div></div>"
                    else:
                        result = result + '\n<div class="normal">' + item + "</div></div>"

            result = result +  "\n</body>\n</html>"
            log_file.write(result)
    except:
        pass

def updateCollapseHTML():

    try:
        tempStatusArray = []
        tempArray = []

        for i in range(len(config.textStatusArray)):
            if config.textStatusArray[i] != "ephemeral":
                if config.textStatusArray[i] == "italic" or config.textStatusArray[i] == "result":
                    result = '\n<p class="italic">' + config.textArray[i] + "</p>\n"
                elif config.textStatusArray[i] == "bold" or config.textStatusArray[i] == "query":
                    result = '\n<p class="bold">' + config.textArray[i] + "</p>\n"
                elif config.textStatusArray[i] == "bold_italic" or config.textStatusArray[i] == "oracle":
                    result = '\n<p class="italicbold">' + config.textArray[i] + "</p>\n"
                elif config.textStatusArray[i] == "color1":
                    result = '\n<p class="highlightcolor">' + config.textArray[i] + "</p>\n"
                elif config.textStatusArray[i] == "color2":
                    result = '\n<p class="alternatecolor">' + config.textArray[i] + "</p>\n"
                else:
                    result = '\n<p class="normal">' + config.textArray[i] + "</p>\n"
                tempArray.append(result)
                tempStatusArray.append(config.textStatusArray[i])

        with open(config.curr_game_dir + "log_ind_collapsible.html", "w") as log_file:
            count = 0
            bracket = "\n<html>\n<head>\n<title>" + config.curr_title + "</title>\n"
            script = '<script>'
            script = script + '\nfunction toggle2(showHideDiv, switchTextDiv) {'
            script = script + '\n	 var ele = document.getElementById(showHideDiv);'
            script = script + '\n	 var text = document.getElementById(switchTextDiv);'
            script = script + '\n	 if(ele.style.display == "block") {'
            script = script + '\n    		ele.style.display = "none";'
            script = script + '\n		text.innerHTML = "show";'
            script = script + '\n  	}'
            script = script + '\n	 else {'
            script = script + '\n		ele.style.display = "block";'
            script = script + '\n		text.innerHTML = "hide";'
            script = script + '\n	}'
            script = script + '\n}'
            script = script + '\nfunction toggle3(contentDiv, controlDiv) {'
            script = script + '\n        if (contentDiv.constructor == Array) {'
            script = script + '\n                for(i=0; i < contentDiv.length; i++) {'
            script = script + '\n                     toggle2(contentDiv[i], controlDiv[i]);'
            script = script + '\n                }'
            script = script + '\n        }'
            script = script + '\n        else {'
            script = script + '\n               toggle2(contentDiv, controlDiv);'
            script = script + '\n        }'
            script = script + '\n}'
            script = script + '</script>'
            style = '\n<style type="text/css">'
            style = style + "\n.italic {\nfont-style: italic;\n}"
            style = style + "\n.italicbold {\nfont-style: italic;font-weight: bold;\n}"
            style = style + "\n.bold {\nfont-weight: bold;\n}"
            style = style + "\n.highlightcolor {\ncolor: #" + config.highlight_color + ";\n}"
            style = style + "\n.alternatecolor {\ncolor: #" + config.alternate_color + ";\n}"
            style = style + "\n</style>\n"
            bracket = bracket + "</head>\n<body><!-- actual adventure starts here -->"

            content_string = ""
            header_string = ""
            result = ""
            chunk = False
            if tempStatusArray[0] != 'no_format':
                count = count + 1
                result = result + '\n<a id="myHeader' + str(count) + '" href="javascript:toggle2(\'myContent'  + str(count) + '\',\'myHeader' + str(count) + '\');" >hide</a>'
                result = result + "\n<div id='myContent" + str(count) + "'>"
                content_string = content_string + "'myContent" + str(count) + "',"
                header_string = header_string + "'myHeader" + str(count) + "',"
                chunk = True

            for ti in range(len(tempStatusArray)):
                if tempStatusArray[ti] != "no_format" and chunk == False:
                    count = count + 1
                    result = result + '\n<a id="myHeader' + str(count) + '" href="javascript:toggle2(\'myContent'  + str(count) + '\',\'myHeader' + str(count) + '\');" >collapse</a>'
                    result = result + "\n<div id='myContent" + str(count) + "'>"
                    result = result + tempArray[ti]
                    content_string = content_string + "'myContent" + str(count) + "',"
                    header_string = header_string + "'myHeader" + str(count) + "',"
                    chunk = True
                elif tempStatusArray[ti] != "no_format" and chunk == True:
                    result = result + "\n" + tempArray[ti]
                elif tempStatusArray[ti] == "no_format" and chunk == True:
                     result = result + "</div>\n" + tempArray[ti]
                     chunk = False
                else:
                    result = result + "\n" + tempArray[ti]
                    chunk = False
                    pass

            final = bracket + script + style

            final = final + '<input type="button" value="Toggle All" onClick="toggle3([' + content_string + '], [' + header_string + ']);">'

            final = final + result
            final = final +  "\n</body>\n</html>"
            log_file.write(final)
    except:
        pass

def rollDice(text):

    results = "Please use standard dice notation, ie, 1d10."

    if len(text) > 0:
        try:
            count, sides = text.split("d")
        except:
            count = 1
            sides = 100
        # are we repeating?
        try:
            sides, reps = sides.split("x")
        except:
            reps = 1

        results = "Rolling " + str(count) + "d" + str(sides) + " " + str(reps) + " times."
        for m in range(int(reps)):
            resultArray = []
            result = 0
            resultstring = " "
            if int(count) and int(sides):
                for i in range(int(count)):
                    x = random.randint(1,int(sides))
                    resultArray.append(x)
                    result = result + x
                    resultstring = resultstring + " " + str(x)
            results = results + "\n[" + resultstring + "  ] " + str(result)

    return results


#-------------------------------------------------------------------------------------------------------------------------------------------
# --> Random choosers from player defined lists
#-------------------------------------------------------------------------------------------------------------------------------------------

def getRandomActor(key="All"):

    textarray = []
    result = "[Random actor, key: " + key + "] " + "No results found."

    for i in range(len(config.actorLabelArray)):
        textarray.append(config.actorLabelArray[i].text + ", " + config.actorStatusLabelArray[i].text)

    if key == "All" and len(textarray) > 0:
        result = "[Random actor, key: " + key + "] " + random.choice(textarray)
    else:
        matching = [s for s in textarray if key in s]

        if len(matching) > 0:
            result = "[Random actor, key: " + key + "] " + random.choice(matching)

    return result

def getRandomThread(key="All"):

    exclusion = False
    if key[:1] == "!":
        # this is a exclusion search
        exclusion = True
        key = key[1:]

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

    exclusion = False
    if key[:1] == "!":
        # this is a exclusion search
        exclusion = True
        key = key[1:]

    textarray = []

    for i in range(len(config.pcKeyLabelArray)):
        textarray.append(config.pcKeyLabelArray[i].text + ": " + config.pcValueLabelArray[i].text)

    matching = [s for s in textarray if key in s]

    if len(matching) > 0:
        result = "[Random PC, key: " + key  + " ] " + random.choice(matching)
    else:
        result = "[Random PC, key: " + key  + " ] "  + "No results found."

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

# weighted choosers
def chooseWeighted(value, text, form):
    result_string = ""
    result = "Please enter a comma-separated list in one line that has at least as many options as needed."
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
            # 3d6
            index = 3
            chart = {}
            result_string = ""
            result = text.split(", ")
            for i in result:
                chart[index] = i
                index = index + 1
            roll = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
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
            for element in text.split(", "):
                result_string = result_string + element + ", "
            result = random.choice(text.split(", "))
            roll = "Choice"

        return str(result_string), str(result), str(form), str(roll)

    except:
        return str(result_string), str(result), str("ephemeral"), str("0")

# simple action/subject lists to help answer complex questions
def complex_action():
    chart = ['accelerate', 'accumulate', 'acquire', 'adjust', 'adopt', 'advance', 'align', 'alter', 'anticipate', 'assist', 'bestow', 'carry', 'change', 'clarify', 'command', 'commit', 'conclude', 'consider', 'construct', 'control', 'convince', 'determine', 'discover', 'disregard', 'divert', 'divide', 'educate', 'emphasize', 'enable', 'enrage', 'enter', 'eviscerate', 'examine', 'exchange', 'execute', 'exhaust', 'experience', 'facilitate', 'fascinate', 'guess', 'impassion', 'improvise', 'inflate', 'interest', 'involve', 'justify', 'locate', 'loosen', 'lose', 'love', 'mend', 'mesmerize', 'motivate', 'murder', 'negotiate', 'nurture', 'obscure', 'overcome', 'penalize', 'question', 'refuse', 'reject', 'renegotiate', 'revenge', 'run', 'share', 'simplify', 'spy', 'squelch', 'strengthen', 'substitute', 'synthesize', 'teach', 'tighten', 'track', 'transition', 'trap', 'triumph', 'tumble', 'unify', 'unveil', 'weaken', 'withdraw']

    return random.choice(chart)

def complex_subject():
    chart = ['addiction', 'ally', 'armor', 'art', 'boss', 'change', 'class', 'common', 'compassion', 'death', 'disaster', 'earth', 'elements', 'emotions', 'emotions', 'enemy', 'fatigue', 'focus', 'friend', 'friendship', 'fury', 'future', 'hatred', 'home', 'hope', 'honor', 'instinct', 'integrity', 'key', 'kin', 'location', 'love', 'luxuries', 'monster', 'moon', 'music', 'necessities', 'neighbor', 'obsession', 'past', 'passion', 'path', 'physical', 'possessions', 'power', 'quarry', 'reserves', 'sex', 'stalemate', 'star', 'status quo', 'sun', 'survival', 'task', 'value', 'vengeance', 'violence', 'wealth', 'weapons', 'work']

    return random.choice(chart)
