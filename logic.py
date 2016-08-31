#!/usr/bin/env python
#-*- coding: utf-8 -*-
##-------------------------------------------------------------------------------------------------------------------------------------------
#  General logic
#
##-------------------------------------------------------------------------------------------------------------------------------------------

import imports
from imports import *
import config

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

    edit_mode = config.general['edit_behavior']

    if text[:1] == "\n":
        text = text[1:]

    if reset == False:
        config.textArray.append(text)
        config.textStatusArray.append(status)

    base_text = text

    if status == "ephemeral":
        text = "[i][color=" + str(config.transitory_color) + "]" + text + "[/color][/i]"
        # ideally this would not actually be added to the textArray, or at least not shown on load, but for now I'm leaving it as just a color change
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
        # this is the standard mode used for reading and playing

        self.centerDisplayGrid.cols = 1

        label = ClickLabel(text=text, size_hint_y=None, font_size=config.basefont, font_name='Fantasque-Sans', background_normal='', background_down='', background_color=(0,0,0,0), background_color_down=accent2)
        label.text_size = (self.centerDisplayGrid.width, None)
        label.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        label.bind(on_release=storeBookmarkLabel)
        label.foreground_color=(1,1,1,1)
        label.markup = True
        config.textLabelArray.append(label)

        self.centerDisplayGrid.add_widget(config.textLabelArray[-1])

    elif edit_mode == "PLAY":
        # this mode is used if you're prone to forgetting to change format type

        self.centerDisplayGrid.cols = 2

        label = Label(text=text, size_hint_y=None, size_hint_x=.85, font_size=config.basefont, font_name='Fantasque-Sans', background_color=(0,0,0,0), foreground_color=styles.textcolor)
        label.text_size = (self.centerDisplayGrid.width, None)
        label.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        label.bind(on_release=storeBookmarkLabel)
        label.foreground_color=(1,1,1,1)
        label.markup = True
        config.textLabelArray.append(label)

        label = ClickLabel(text=status, size_hint_y=None, size_hint_x=.15, height=12, font_size=10, font_name='Fantasque-Sans')
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
        # clean mode, don't show rolls

        if status == "no_format":

            self.centerDisplayGrid.cols = 1

            label = ClickLabel(text=text, size_hint_y=None, font_size=config.basefont, font_name='Fantasque-Sans', background_normal='', background_down='', background_color=(0,0,0,0), background_color_down=accent2)
            label.text_size = (self.centerDisplayGrid.width, None)
            label.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
            label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
            label.bind(on_release=storeBookmarkLabel)
            label.foreground_color=(1,1,1,1)
            label.markup = True
            config.textLabelArray.append(label)

            self.centerDisplayGrid.add_widget(config.textLabelArray[-1])

    else:
        # editing mode, which means everything is a text input & needs a status label

        self.centerDisplayGrid.cols = 2

        label = TextInput(text=base_text, size_hint_y=None, size_hint_x=.85)
        label.text_size = (self.centerDisplayGrid.width, None)
        label.bind(focus=focusChangeText)
        label.background_color=(0,0,0,.5)
        label.foreground_color=(1,1,1,1)
        config.textLabelArray.append(label)

        #label = ClickLabel(text=status, size_hint_y=None, size_hint_x=.25, height="30px", font_size=config.general['basefontsize'], font_name='Fantasque-Sans')
        label = ClickLabel(text=status, size_hint_y=None, size_hint_x=.15, font_size=10, font_name='Fantasque-Sans')
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

    label = TextInput(text=text, size_hint_y=None, size_hint_x=.75, multiline=False, height="30dp", font_size=config.basefont, font_name='Fantasque-Sans', background_color=(0,0,0,0), foreground_color=styles.textcolor)
    label.bind(focus=focusChangeThread)
    config.threadLabelArray.append(label)
    self.threadDisplayGrid.add_widget(config.threadLabelArray[-1])

    label = ClickLabel(text=status, size_hint_y=None, size_hint_x=.25, height="30dp", font_size=config.basefont, font_name='Fantasque-Sans')
    label.background_normal=''
    label.background_color=accent1
    label.background_down=''
    label.background_color_down=accent2
    label.bind(on_press=cycleThread)
    label.markup = True
    config.threadStatusLabelArray.append(label)
    self.threadDisplayGrid.add_widget(config.threadStatusLabelArray[-1])


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
        self.text = "Hide"
        config.threadStatusArray[config.threadStatusLabelArray.index(self)] = "Hide"
    elif self.text == "Hide":
        self.text = "Current"
        config.threadStatusArray[config.threadStatusLabelArray.index(self)] = "Current"
    else:
        self.text = "Current"
        config.threadStatusArray[config.threadStatusLabelArray.index(self)] = "Current"

    return True

# call this on a new thread added; plenty of time to change our minds
def clearThread(self, *args):
    for i in range(len(config.threadStatusArray)):
        if config.threadStatusArray[i] == "Hide":
            self.threadDisplayGrid.remove_widget(config.threadLabelArray[i])
            self.threadDisplayGrid.remove_widget(config.threadStatusLabelArray[i])

def updateActorDisplay(self, text, status):

    config.actorArray.append(text)
    config.actorStatusArray.append(status)

    label = TextInput(text=text, size_hint_y=None, size_hint_x=.75, font_size=config.basefont, font_name='Fantasque-Sans', background_color=(0,0,0,0), foreground_color=styles.textcolor)
    label.bind(focus=focusChangeActor)
    label.text_size = (self.actorDisplayGrid.width, None)
    label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
    label.markup = True
    config.actorLabelArray.append(label)

    self.actorDisplayGrid.add_widget(config.actorLabelArray[-1])

    label = ClickLabel(text=status, size_hint_y=None, size_hint_x=.25, font_size=config.basefont, font_name='Fantasque-Sans',)
    label.bind(on_press=cycleActor)
    label.background_normal=''
    label.background_color=accent1
    label.background_down=''
    label.background_color_down=accent2
    label.markup = True
    config.actorStatusLabelArray.append(label)

    self.actorDisplayGrid.add_widget(config.actorStatusLabelArray[-1])

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
        self.text = "Hide"
        config.actorStatusArray[config.actorStatusLabelArray.index(self)] = "Hide"
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
        if config.actorStatusArray[i] == "Hide":
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
        config.textArray[config.textLabelArray.index(self)] = self.text

#-------------------------------------------------------------------------------------------------------------------------------------------
# save/load functions
#-------------------------------------------------------------------------------------------------------------------------------------------
def saveconfig(self, gamedir):
    try:
        tempDict = {}
        tempDict['general'] = config.general
        tempDict['user'] = config.user

        f = open(gamedir + 'config.txt', 'w')
        simplejson.dump(tempDict, f)
        f.close()
    except:
        print("Saving configuration file failed.")

def loadconfig(self, gamedir):
    try:
        f = open(gamedir + 'config.txt', 'r')
        tempDict = simplejson.load(f)
        for i in tempDict['general']:
            config.general[i] = tempDict['general'][i]
        for i in tempDict['user']:
            config.user[i] = tempDict['user'][i]
    except:
        saveconfig(self, gamedir)

def quicksave(self, gamedir):

    f = open(gamedir + 'main.txt', 'w')
    simplejson.dump(config.textArray, f)
    f.close()

    f = open(gamedir + 'main_status.txt', 'w')
    simplejson.dump(config.textStatusArray, f)
    f.close()

    f = open(gamedir + 'threads.txt', 'w')
    simplejson.dump(config.threadArray, f)
    f.close()

    f = open(gamedir + 'threads_status.txt', 'w')
    simplejson.dump(config.threadStatusArray, f)
    f.close()

    f = open(gamedir + 'actors.txt', 'w')
    simplejson.dump(config.actorArray, f)
    f.close()

    f = open(gamedir + 'actors_status.txt', 'w')
    simplejson.dump(config.actorStatusArray, f)
    f.close()

    f = open(gamedir + 'tracks.txt', 'w')
    tempArray = []
    for i in range(len(config.trackLabelArray)):
        tempArray.append([config.trackLabelArray[i].text, config.trackStatusLabelArray[i].active])
    simplejson.dump(tempArray, f)
    f.close

    f = open(gamedir + 'pcs.txt', 'w')
    tempArray = []
    for i in range(len(config.pcKeyLabelArray)):
        tempArray.append([config.pcKeyLabelArray[i].text, config.pcValueLabelArray[i].text])
    simplejson.dump(tempArray, f)
    f.close

    saveconfig(self, gamedir)

    clearThread(self)
    clearActor(self)

def quickload(self, gamedir):

    f = open(gamedir + 'main.txt', 'r')
    x = open(gamedir + 'main_status.txt', 'r')
    try:
        tempArray = simplejson.load(f)
        tempStatusArray = simplejson.load(x)
        for i in tempArray:
            curr_index = tempArray.index(i)
            updateCenterDisplay(self, i, tempStatusArray[curr_index])
        self.centerDisplay.scroll_to(config.textLabelArray[-1])
    except:
        updateCenterDisplay(self, "The adventure begins...", 'italic')
    f.close()
    x.close()

    f = open(gamedir + 'threads.txt', 'r')
    x = open(gamedir + 'threads_status.txt', 'r')
    try:

        tempTable = []
        tempStatusTable = []

        for i in simplejson.load(f):
            tempTable.append(i)

        for z in simplejson.load(x):
            tempStatusTable.append(z)

        for m in range(len(tempTable)):
            updateThreadDisplay(self, tempTable[m], tempStatusTable[m])

    except:
        pass
    f.close()
    x.close()

    f = open(gamedir + 'actors.txt', 'r')
    x = open(gamedir + 'actors_status.txt', 'r')
    try:

        tempTable = []
        tempStatusTable = []

        for i in simplejson.load(f):
            tempTable.append(i)

        for z in simplejson.load(x):
            tempStatusTable.append(z)

        for m in range(len(tempTable)):
            updateActorDisplay(self, tempTable[m], tempStatusTable[m])

    except:
        pass
    f.close()
    x.close()

    f = open(gamedir + 'tracks.txt', 'r')
    try:
        tempTable = []
        for i in simplejson.load(f):
            tempTable.append(i)
            #print(i)

        for x in range(len(tempTable)):
            config.trackLabelArray[x].text = tempTable[x][0]
            config.trackStatusLabelArray[x].active = tempTable[x][1]
    except:
        pass
    f.close()


    try:
        f = open(gamedir + 'pcs.txt', 'r')
        tempTable = []
        for i in simplejson.load(f):
            tempTable.append(i)

        for x in range(len(tempTable)):
            config.pcKeyLabelArray[x].text = tempTable[x][0]
            config.pcValueLabelArray[x].text = tempTable[x][1]
        f.close()
    except:
        pass

def storeBookmarkLabel(label):
    for i in range(len(config.textLabelArray)):
        if label.text == config.textLabelArray[i].text:
            index = i
    l = ToggleButtonBehavior.get_widgets('bookmarks')
    for button in l:
        if button.state == "down":
            button.index = index
            button.state = 'normal'
            config.general['bookmarks'][button.value] = index
    del l

def updateCleanMarkdown():
    try:
        with open(config.curr_game_dir + "human_readable_log.md", "w") as log_file:
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
                    elif config.textStatusArray[ti] == "no_format":
                        result = result + "\n" + item
                    else:
                        item = item.replace('\n', '`\n`')
                        result = result = "\n`" + item + "`"
            log_file.write(result)
    except:
        pass

def updateCleanHTML():
    try:
        test = ""
        with open(config.curr_game_dir + "human_readable_log.htm", "w") as log_file:
            result = "\n<html>\n<head>\n<title>" + test + "</title>\n</head>\n<body>"
            for item in config.textArray:
                item = item.rstrip()
                ti = config.textArray.index(item)
                if config.textStatusArray[ti] != "ephemeral":
                    if config.textStatusArray[ti] == "italic" or config.textStatusArray[ti] == "result":
                        result = result + "\n<p><i>" + item + "</i></p>"
                    elif config.textStatusArray[ti] == "bold" or config.textStatusArray[ti] == "query":
                        result = result + "\n<p><b>" + item + "</b></p>"
                    elif config.textStatusArray[ti] == "bold_italic" or config.textStatusArray[ti] == "oracle":
                        result = result + "\n<p><b><i>" + item + "</i></b></p>"
                    elif config.textStatusArray[ti] == "no_format":
                        result = result + "\n<p>" + item + "</p>"
                    else:
                        result = result = "\n<p text=\"rgb(0,0,255)\">" + item + "</p>"
            result = result +  "</body>\n</html>"
            log_file.write(result)
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

    print(list(textarray))
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

# simple action/subject lists to help answer complex questions, off the top of my head, could be a lot longer/more
def complex_action():
    chart = [
        "accumulate", "align", "divert", "divide", "construct", "synthesize", "command", "facilitate", "penalize",
        "run", "convince", "motivate", "share", "enable", "assist", "unify", "acquire", "involve", "determine", "locate",
        "examine", "track", "lose", "discover", "alter", "question", "negotiate", "renegotiate", "exchange", "accelerate", "execute",
        "anticipate", "commit", "trap", "unveil", "emphasize", "simplify", "transition", "overcome", "improvise", "clarify",
        "obscure", "eviscerate", "experience", "teach", "substitute", "tighten", "loosen", "strengthen", "weaken", "withdraw",
        "advance", "nurture", "squelch", "adjust", "justify", "murder", "love", "mesmerize", "revenge", "mend", "control", 'enrage',
        'educate', 'adopt', 'reject', 'consider', 'disregard'
    ]
    return random.choice(chart)

def complex_subject():
    chart = [
        "friend", "enemy", "ally", "lover", "home", "monster", "location", "work", "boss", "emotions", "physical", "reserves", "task", "future",
        "past", "vengeance", "possessions", "music", "art", "sex", "survival", "necessities", "luxuries", "weapons", "armor", "fatigue", "honor",
        "integrity", "violence", "compassion", "sun", "moon", "value", 'neighbor', 'kin', 'fury', 'emotions', "quarry", "focus", "addiction", "obsession"
    ]
    return random.choice(chart)
