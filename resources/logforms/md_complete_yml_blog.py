#!/usr/bin/env python
#-*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------
#
#  Markdown
#     complete: includes all blocks except ephemeral
#     yml: uses a yaml Front Matter from config.txt
#     blog: ready for jekyll or similar
#
##---------------------------------------------------------------------------------------

import imports
from imports import *
import config

def exclude():
    return False

def makeLogFile(self):

    logfile = config.curr_game_dir + "logs" + os.sep + "complete_yml_blog.md"

    textArray, textStatusArray = getSourceMaterial()

    YAML = config.yaml_for_markdown

    result = ""
    for item in textArray:
        ti = textArray.index(item)
        item = item.strip()
        if textStatusArray[ti] != "ephemeral":
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
    result = YAML + parseMarkup(result)
    result = result.lstrip()

    with open(logfile, "w") as log_file:
        log_file.write(result.encode('utf-8'))
