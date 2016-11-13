#!/usr/bin/env python
#-*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------
#
#  HTML
#     fiction: includes only fiction blocks
#     css: requires an html frame/blog ready
#
##---------------------------------------------------------------------------------------

import imports
from imports import *
import config

def exclude():
    return False

def makeLogFile(self):

    logfile = config.curr_game_dir + "logs" + os.sep + "fiction_css.html"

    textArray, textStatusArray = getSourceMaterial()

    fictionStatusList = ["plain", "italic", "bold", "bold_italic", "color1", "color2"]

    result = '\n<!-- actual adventure starts here -->'

    for item in textArray:
        ti = textArray.index(item)
        if textStatusArray[ti] in fictionStatusList:
            item = escapeHTML(item.rstrip())
            result = result + '\n<p id="fiction">' + item + "</p>"

    with open(logfile, "w") as log_file:
        log_file.write(result.encode('utf-8'))

    generateCSS()
