#!/usr/bin/env python
#-*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------
#
#  HTML -- includes all mechanics except ephemeral
#
##---------------------------------------------------------------------------------------

import imports
from imports import *
import config

def exclude():
    return False

def makeLogFile(self):

    logfile = config.curr_game_dir + "logs" + os.sep + "complete.html"

    textArray, textStatusArray = getSourceMaterial()

    result = "\n<html>\n<head>\n<title>" + config.yaml['title'] + "</title>\n"
    style = '\n<style type="text/css">'
    style = style + "\n.italic {\nfont-style: italic;\n}"
    style = style + "\n.italicbold {\nfont-style: italic;font-weight: bold;\n}"
    style = style + "\n.bold {\nfont-weight: bold;\n}"
    style = style + "\n.highlightcolor {\ncolor: #" + config.formats['highlight_color'] + ";\n}"
    style = style + "\n.alternatecolor {\ncolor: #" + config.formats['alternate_color'] + ";\n}"
    style = style + "\n</style>\n"
    result = result + style + "</head>\n<body><!-- actual adventure starts here -->"
    # actual adventure content starts here
    for item in textArray:
        ti = textArray.index(item)
        if textStatusArray[ti] != "ephemeral":
            if "\n" in item:
                item = item.replace('\n', '<br>')
            if textStatusArray[ti] == "result":
                result = result + '\n<div class="mechanic"><div class="italic">' + item + "</div></div>"
            elif textStatusArray[ti] == "query":
                result = result + '\n<div class="mechanic"><div class="bold">' + item + "</div></div>"
            elif textStatusArray[ti] == "aside":
                result = result + '\n<div class="mechanic"><div class="italic">' + item + "</div></div>"
            elif textStatusArray[ti] == "oracle":
                result = result + '\n<div class="mechanic"><div class="italicbold">' + item + "</div></div>"
            elif textStatusArray[ti] == "mechanic1":
                result = result + '\n<div class="mechanic"><div class="highlightcolor">' + item + "</div></div>"
            elif textStatusArray[ti] == "mechanic2":
                result = result + '\n<div class="mechanic"><div class="alternatecolor">' + item + "</div></div>"
            else:
                if textStatusArray[ti] == "italic":
                    result = result + '\n<div class="italic">' + item + "</div></div>"
                elif textStatusArray[ti] == "bold":
                    result = result + '\n<div class="bold">' + item + "</div></div>"
                elif textStatusArray[ti] == "bold_italic":
                    result = result + '\n<div class="bold_italic">' + item + "</div></div>"
                elif textStatusArray[ti] == "color1":
                    result = result + '\n<div class="color1">' + item + "</div></div>"
                elif textStatusArray[ti] == "color2":
                    result = result + '\n<div class="color2">' + item + "</div></div>"
                else:
                    result = result + '\n<div class="normal">' + item + "</div></div>"

        result = parseHTML(result)

    result = result + "\n</body>\n</html>"

    with open(logfile, "w") as log_file:
        log_file.write(result.encode('utf-8'))
