#!/usr/bin/env python
#-*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------
#
#  Markdown -- fiction blocks only
#
##---------------------------------------------------------------------------------------

import imports
from imports import *
import config

def exclude():
    return False

def makeLogFile(self):

    logfile = config.curr_game_dir + "logs" + os.sep + "fiction.md"

    textArray, textStatusArray = getSourceMaterial()

    fictionStatusList = ["plain", "italic", "bold", "bold_italic", "color1", "color2"]

    result = "\n"
    for item in textArray:
        ti = textArray.index(item)
        item = item.rstrip()
        if textStatusArray[ti] in fictionStatusList:
            result = result + "\n"
            if textStatusArray[ti] == "italic":
                item = item.replace('\n', '*\n\n*')
                result = result + "\n*" + item + "*"
            elif textStatusArray[ti] == "bold":
                item = item.replace('\n', '**\n\n**')
                result = result + "\n**" + item + "**"
            elif textStatusArray[ti] == "bold_italic":
                item = item.replace('\n', '_**\n\n**_')
                result = result + "\n**_" + item + "_**"
            elif textStatusArray[ti] == "color1":
                item = item.replace('\n', '`\n\n`')
                result = result + "\n`" + item + "`"
            elif textStatusArray[ti] == "color2":
                item = item.replace('\n', '`\n\n`')
                result = result + "\n`" + item + "`"
            else:
                result = result + "\n" + item

    result = addYAML() + parseMarkup(result)

    with open(logfile, "w") as log_file:
        log_file.write(result)
