#!/usr/bin/env python
#-*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------
#
#  HTML
#     complete: includes all blocks except ephemeral
#     css: requires an html frame/blog ready
#     js: javascript toggles
#
##---------------------------------------------------------------------------------------

import imports
from imports import *
import config

def exclude():
    return True

def makeLogFile(self):

    logfile = config.curr_game_dir + "logs" + os.sep + "complete_css_js.html"

    textArray, textStatusArray = getSourceMaterial()

    fictionStatusList = ["plain", "italic", "bold", "bold_italic", "color1", "color2"]

    tempStatusArray = []
    tempArray = []
    result = ""

    for ti in range(len(textStatusArray)):
        if textStatusArray[ti] != "ephemeral" or config.show_ephemeral_in_logs == True:
            item = textArray[ti]
            item = escapeHTML(item.rstrip())
            if textStatusArray[ti] == "result":
                result = '\n<p id="mechanic" class="result">' + item + "</p>"
            elif textStatusArray[ti] == "query":
                result = '\n<p id="mechanic" class="query">' + item + "</p>"
            elif textStatusArray[ti] == "aside":
                result = '\n<p id="mechanic" class="aside">' + item + "</p>"
            elif textStatusArray[ti] == "oracle":
                result = '\n<p id="mechanic" class="oracle">' + item + "</p>"
            elif textStatusArray[ti] == "mechanic1":
                result = '\n<p id="mechanic" class="color1">' + item + "</p>"
            elif textStatusArray[ti] == "mechanic2":
                result = '\n<p id="mechanic" class="color2">' + item + "</p>"
            elif textStatusArray[ti] == "ephemeral":
                result = '\n<p id="mechanic" class="ephemeral">' + item + "</p>"
            else:
                result = '\n<p id="fiction">' + item + "</p>"

            tempArray.append(result)
            tempStatusArray.append(textStatusArray[ti])

    count = 0
    content_string = ""
    header_string = ""
    result = "<p>Press the toggle button to hide or show the mechanics.</p>"
    chunk = False

    for ti in range(len(tempStatusArray)):
        if tempStatusArray[ti] not in fictionStatusList and chunk == False:
            count = count + 1
            result = result + '\n<a id="myHeader' + str(count) + '" href="javascript:toggle2(\'myContent'  + str(count) + '\',\'myHeader' + str(count) + '\');" >collapse</a>'
            result = result + "\n<div id='myContent" + str(count) + "'>"
            result = result + tempArray[ti]
            content_string = content_string + "'myContent" + str(count) + "',"
            header_string = header_string + "'myHeader" + str(count) + "',"
            chunk = True
        elif tempStatusArray[ti] not in fictionStatusList and chunk == True:
            result = result + "\n" + tempArray[ti]
        elif tempStatusArray[ti] in fictionStatusList and chunk == True:
             result = result + "</div>\n" + tempArray[ti]
             chunk = False
        else:
            result = result + "\n" + tempArray[ti]
            chunk = False
            pass

    final = '<input type="button" value="Toggle All" onClick="toggle3([' + content_string + '], [' + header_string + ']);">'

    result = final + result

    with open(logfile, "w") as log_file:
        log_file.write(result.encode('utf-8'))

    generateCSS()
    generateJS()

def generateJS():

    script = ""
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

    logfile = config.curr_game_dir + "logs" + os.sep + "script.js"

    with open(logfile, "w") as log_file:
        log_file.write(script.encode('utf-8'))
