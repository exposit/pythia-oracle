#!/usr/bin/env python
#-*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------
#
#  HTML - includes all mechanics except ephemeral and a javascript toggle
#
##---------------------------------------------------------------------------------------

import imports
from imports import *
import config

def exclude():
    return False

# everything in the main file except ephemeral in markdown
def makeLogFile(self):

    logfile = config.curr_game_dir + "logs" + os.sep + "complete_collapsible.html"

    textArray, textStatusArray = getSourceMaterial()

    fictionStatusList = ["plain", "italic", "bold", "bold_italic", "color1", "color2"]
    tempStatusArray = []
    tempArray = []

    for i in range(len(textStatusArray)):
        if textStatusArray[i] != "ephemeral":

            item = textArray[i]
            if "\n" in item:
                item = item.replace('\n', '<br>')

            if textStatusArray[i] == "result":
                result = '\n<p class="italic">' + item + "</p>\n"
            elif textStatusArray[i] == "aside":
                result = '\n<p class="italic">' + item + "</p>\n"
            elif textStatusArray[i] == "query":
                result = '\n<p class="bold">' + item + "</p>\n"
            elif textStatusArray[i] == "oracle":
                result = '\n<p class="italicbold">' + item + "</p>\n"
            elif textStatusArray[i] == "mechanic1":
                result = '\n<p class="highlightcolor">' + item + "</p>\n"
            elif textStatusArray[i] == "mechanic2":
                result = '\n<p class="alternatecolor">' + item + "</p>\n"
            else:
                if textStatusArray[i] == "italic":
                    result = '\n<p class="italic">' + item + "</p>\n"
                elif textStatusArray[i] == "bold":
                    result = '\n<p class="bold">' + item + "</p>\n"
                elif textStatusArray[i] == "bold_italic":
                    result = '\n<p class="italicbold">' + item + "</p>\n"
                elif textStatusArray[i] == "color1":
                    result = '\n<p class="highlightcolor">' + item + "</p>\n"
                elif textStatusArray[i] == "color2":
                    result = '\n<p class="alternatecolor">' + item + "</p>\n"
                else:
                    result = '\n<p class="normal">' + item + "</p>\n"

            tempArray.append(result)
            tempStatusArray.append(textStatusArray[i])

    count = 0
    bracket = "\n<html>\n<head>\n<title>" + config.yaml['title'] + "</title>\n"
    script = '<script>'
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
    script = script + '</script>'
    style = '\n<style type="text/css">'
    style = style + "\n.italic {\nfont-style: italic;\n}"
    style = style + "\n.italicbold {\nfont-style: italic;font-weight: bold;\n}"
    style = style + "\n.bold {\nfont-weight: bold;\n}"
    style = style + "\n.highlightcolor {\ncolor: #" + config.formats['highlight_color'] + ";\n}"
    style = style + "\n.alternatecolor {\ncolor: #" + config.formats['alternate_color'] + ";\n}"
    style = style + "\n</style>\n"
    bracket = bracket + "</head>\n<body><!-- actual adventure starts here -->"

    content_string = ""
    header_string = ""
    result = ""
    chunk = False
    if tempStatusArray[0] not in fictionStatusList:
        count = count + 1
        result = result + '\n<a id="myHeader' + str(count) + '" href="javascript:toggle2(\'myContent'  + str(count) + '\',\'myHeader' + str(count) + '\');" >hide</a>'
        result = result + "\n<div id='myContent" + str(count) + "'>"
        content_string = content_string + "'myContent" + str(count) + "',"
        header_string = header_string + "'myHeader" + str(count) + "',"
        chunk = True

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

    result = parseHTML(result)

    final = bracket + script + style

    final = final + '<input type="button" value="Toggle All" onClick="toggle3([' + content_string + '], [' + header_string + ']);">'

    result = final + result
    result = result +  "\n</body>\n</html>"

    with open(logfile, "w") as log_file:
        log_file.write(result.encode('utf-8'))
