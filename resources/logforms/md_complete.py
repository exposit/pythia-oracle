#!/usr/bin/env python
#-*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------
#
#  Markdown -- includes all mechanics except ephemeral
#
##---------------------------------------------------------------------------------------

import imports
from imports import *
import config

def exclude():
    return False

def makeLogFile(self):

    logfile = config.curr_game_dir + "logs" + os.sep + "complete.md"

    textArray, textStatusArray = getSourceMaterial()

    result = "\n"
    for item in textArray:
        ti = textArray.index(item)
        item = item.strip()
        if textStatusArray[ti] != "ephemeral":
            result = result + "\n"
            if textStatusArray[ti] == "italic" or textStatusArray[ti] == "result" or textStatusArray[ti] == "aside":
                item = item.replace('\n', '*\n\n*')
                result = result + "\n*" + item + "*"
            elif textStatusArray[ti] == "bold" or textStatusArray[ti] == "query":
                item = item.replace('\n', '**\n\n**')
                result = result + "\n**" + item + "**"
            elif textStatusArray[ti] == "bold_italic" or textStatusArray[ti] == "oracle":
                item = item.replace('\n', '_**\n\n**_')
                result = result + "\n**_" + item + "_**"
            elif textStatusArray[ti] == "color1" or textStatusArray[ti] == "mechanic1":
                item = item.replace('\n', '`\n\n`')
                result = result + "\n`" + item + "`"
            elif textStatusArray[ti] == "color2" or textStatusArray[ti] == "mechanic2":
                item = item.replace('\n', '`\n\n`')
                result = result + "\n`" + item + "`"
            else:
                result = result + "\n" + item

    # now any in block tags
    result = parseMarkup(result)

    with open(logfile, "w") as log_file:
        log_file.write(result)
