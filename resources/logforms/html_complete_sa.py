#!/usr/bin/env python
#-*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------
#
#  HTML
#     complete: includes all tags except ephemeral
#     sa: standalone web page
#
##---------------------------------------------------------------------------------------

import imports
from imports import *
import config

def exclude():
    return False

def makeLogFile(self):

    logfile = config.curr_game_dir + "logs" + os.sep + "complete_sa.html"

    textArray, textStatusArray = getSourceMaterial()

    result = '\n<html>\n<head>\n<title>' + 'title' + '</title>\n<link rel="stylesheet" type="text/css" href="style.css">\n</head>\n<body>\n<!-- actual adventure starts here -->'

    for item in textArray:
        ti = textArray.index(item)
        if textStatusArray[ti] != "ephemeral" or config.show_ephemeral_in_logs == True:
            item = escapeHTML(item.rstrip())
            if textStatusArray[ti] == "result":
                result = result + '\n<p id="mechanic" class="result">' + item + "</p>"
            elif textStatusArray[ti] == "query":
                result = result + '\n<p id="mechanic" class="query">' + item + "</p>"
            elif textStatusArray[ti] == "aside":
                result = result + '\n<p id="mechanic" class="aside">' + item + "</p>"
            elif textStatusArray[ti] == "oracle":
                result = result + '\n<p id="mechanic" class="oracle">' + item + "</p>"
            elif textStatusArray[ti] == "mechanic1":
                result = result + '\n<p id="mechanic" class="color1">' + item + "</p>"
            elif textStatusArray[ti] == "mechanic2":
                result = result + '\n<p id="mechanic" class="color2">' + item + "</p>"
            elif textStatusArray[ti] == "ephemeral":
                result = result + '\n<p id="mechanic" class="ephemeral">' + item + "</p>"
            else:
                result = result + '\n<p id="fiction">' + item + "</p>"

    result = result + "</body></html>"

    with open(logfile, "w") as log_file:
        log_file.write(result.encode('utf-8'))

    generateCSS()
