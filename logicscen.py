#!/usr/bin/env python
#-*- coding: utf-8 -*-
#---------------------------------------------------------------------------------------------------
# --> Logic to handle scenarios
#---------------------------------------------------------------------------------------------------

import imports
from imports import *
import config

import logic
from logic import *

def parseRefs(source):

    start_sep='[['
    end_sep=']]'
    result=[]
    tmp=source.split(start_sep)
    for par in tmp:
      if end_sep in par:
        result.append(par.split(end_sep)[0])

    for clause in result:
        action, text, link = clause.split('|')

        new = "[ref=" + action + "_" + link + "][color=" + config.link_color + "]" + text + "[/color][/ref]"

        source = source.replace("[[" + clause + "]]", new, 1)

    return source

def parseTextVariables(source):

    start_sep='<<'
    end_sep='>>'
    result=[]
    tmp=source.split(start_sep)
    for par in tmp:
      if end_sep in par:
        result.append(par.split(end_sep)[0])

    for clause in result:

        try:
            a = clause.split("if ")[0]
        except:
            a = clause

        try:
            if a.split('.')[0] == 'var':
                a = "config.scenario[\'" + a.split('.')[1] + "\']"
                a = eval(a)
        except:
            pass

        try:
            b = clause.split(" else ")[-1]
        except:
            b = ""

        try:
            if b.split('.')[0] == 'var':
                b = "config.scenario[\'" + b.split('.'[1]) + "\']"
                b = eval(b)
        except:
            pass

        try:
            condition = clause.split("if ")[1]
            condition = condition.split(" else ")[0]
        except:
            condition = ""

        try:
            condition = "config.scenario[\'" + condition + "\']"
            if eval(condition) == True:
                new = a
            else:
                new = b
        except:
            new = a

        source = source.replace("<<" + clause + ">>", new, 1)

    return source

def refPress(*args):

    self  = args[0].self
    label = args[0]
    subtype, text = args[1].split('_')
    subtype = subtype[:1]
    full = args[1]

    try:
        mod = config.curr_game_dir + "scenlogic.py"
        filename = mod.split('/')[-1]
        pyfile = filename.split('.')[0]
        modlogic = imp.load_source( pyfile, mod)
    except:
        pass

    if subtype == "d":

        block = config.scenario['block']
        #try:
        #    base = config.advDict[block][text]
        #except:
        base = config.scenario['descRefs'][text]

        try:
            eval("scenlogic." + base[3])(self)
        except:
            pass

        display = parseTextVariables(base[0])
        logic.updateCenterDisplay(self, display, base[1])

        if base[2] == 'repeatable':
            newtext = label.text
            colorList = re.findall('(?:[0-9a-fA-F]{3}){2}', newtext)
            for color in colorList:
                newtext = newtext.replace(color, config.visited_link_color)
            label.text = newtext
        else:
            newtext = label.text
            colorList = re.findall('(?:[0-9a-fA-F]{3}){2}', newtext)
            for color in colorList:
                newtext = newtext.replace(color, "")
            newtext = newtext.replace("[ref=" + full + "]", "")
            newtext = newtext.replace("[/ref]", "")
            newtext = newtext.replace("[/color]", "")
            label.text = newtext

        config.textArray[label.index] = label.text

    elif subtype == "t":

        block = config.scenario['block']
        try:
            base = config.advDict[block][text]
        except:
            base = config.scenario['toggleRefs'][text]

        if label.text == base[1]:
            label.text = base[2]
        else:
            label.text = base[1]

        config.textArray[label.index] = label.text

    elif subtype == "j":

        block = config.scenario['block']
        try:
            base = config.advDict[block][text]
        except:
            base = config.scenario['jumpRefs'][text]

        destination = base['jump']

        try:
            exitmsg = base['exitmsg']
        except:
            exitmsg = ""

        try:
            exitformat = base['exitformat']
        except:
            exitformat = "result"

        try:
            repeatable = base['repeatable']
        except:
            repeatable = "yes"

        try:
            pause = base['pause']
        except:
            pause = False

        config.scenario['block'] = destination

        exitmsg = parseTextVariables(exitmsg)
        logic.updateCenterDisplay(self, exitmsg, exitformat)

        # this was a jump; clear all older links
        for i in range(len(config.textLabelArray)):
            newtext = label.text
            colorList = re.findall('(?:[0-9a-fA-F]{3}){2}', newtext)
            for color in colorList:
                newtext = newtext.replace(color, "")
                newtext = newtext.replace("[ref=" + full + "]", "")
                newtext = newtext.replace("[/ref]", "")
                newtext = newtext.replace("[/color]", "")
                label.text = newtext

            config.textArray[label.index] = label.text

        if pause == False:
            showCurrentBlock(self)
        else:
            more = "[ref=f_showCurrentBlock][color=" + config.link_color + "]continue" + "[/color][/ref]"
            logic.updateCenterDisplay(self, more, 'italic')
    else:
        # this is a function
        for i in range(len(config.textLabelArray)):
            newtext = label.text
            colorList = re.findall('(?:[0-9a-fA-F]{3}){2}', newtext)
            for color in colorList:
                newtext = newtext.replace(color, "")
                newtext = newtext.replace("[ref=" + full + "]", "")
                newtext = newtext.replace("[/ref]", "")
                newtext = newtext.replace("[/color]", "")
                label.text = newtext

            config.textArray[label.index] = label.text

        eval(text)(self)

def showCurrentBlock(self, *args):

    block = config.scenario['block']
    result = ""
    count = 0
    for item in config.advDict[block]['text']:
        count = count + 1
        display = parseTextVariables(item[0])
        display = parseRefs(display)
        logic.updateCenterDisplay(self, display, item[1])

    self.scenarioTitleLabel.text = config.advDict[block]['title']

    showCurrentExits(self)

def showCurrentExits(self, *args):

    block = config.scenario['block']
    result = ""

    try:
        for item in config.advDict[block]['exits']:
            display = parseTextVariables(item[0])
            display = parseRefs(display)
            logic.updateCenterDisplay(self, display, item[1])
    except:
        try:
            for item in config.advDict[block]['exitlist']:
                display = '[[jump|' + config.advDict[block][item]['display'] + '|' + item + ']]'
                display = parseTextVariables(display)
                display = parseRefs(display)
                logic.updateCenterDisplay(self, display, config.advDict[block][item]['exitmsg'])
        except:
            pass
