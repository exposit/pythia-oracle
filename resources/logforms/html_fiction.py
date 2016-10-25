#!/usr/bin/env python
#-*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------
#
#  HTML - fiction blocks only
#
##---------------------------------------------------------------------------------------

import imports
from imports import *
import config

def exclude():
    return False

def makeLogFile(self):

    logfile = config.curr_game_dir + "logs" + os.sep + "fiction.html"

    textArray, textStatusArray = getSourceMaterial()

    fictionStatusList = ["plain", "italic", "bold", "bold_italic", "color1", "color2"]

    result = "\n<html>\n<head>\n<title>" + config.yaml['title'] + "</title>\n"
    style = '\n<style type="text/css">'
    style = style + "\n.italic {\nfont-style: italic;\n}"
    style = style + "\n.italicbold {\nfont-style: italic;font-weight: bold;\n}"
    style = style + "\n.bold {\nfont-weight: bold;\n}"
    style = style + "\n.color1 {\ncolor: #" + config.formats['highlight_color'] + ";\n}"
    style = style + "\n.color2 {\ncolor: #" + config.formats['alternate_color'] + ";\n}"
    style = style + "\n</style>\n"
    result = result + style + "</head>\n<body><!-- actual adventure starts here -->"
    # actual adventure content starts here
    for item in textArray:
        ti = textArray.index(item)
        if textStatusArray[ti] in fictionStatusList:
            status = textStatusArray[ti]
            if "\n" in item:
                item = item.replace('\n', '<br>')
            result = result + '\n<div class="' + status + '">' + item + "</div>"

    result = parseHTML(result)

    result = result +  "\n</body>\n</html>"

    with open(logfile, "w") as log_file:
        log_file.write(result)
