#!/usr/bin/env python
#-*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------
#
#  Markdown -- includes all mechanics except ephemeral and a full YAML header from this file
#
##---------------------------------------------------------------------------------------

import imports
from imports import *
import config

def exclude():
    return False

def makeLogFile(self):

    logfile = config.curr_game_dir + "logs" + os.sep + "complete_yaml_pdf.md"

    textArray, textStatusArray = getSourceMaterial()

    YAML = config.yaml

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
                # this needs to be parsed properly
                prefix_escapes = [ ['[i][b]', '\\textit{\\textbf{' ], ['[b][i]', '\\textbf{\\textit{'], ['[i]', '\\textit{'], ['[b]', '\\textbf{'] ]
                suffix_escapes = [ ['[/i][/b]', '}}'], ['[/b][/i]', '}}'], ['[/i]', '}'], ['[/b]',  '}'] ]
                #print(item)
                for esc in prefix_escapes:
                    if esc[0] in item:
                        item = item.replace(esc[0], esc[1] + "\plain{" )
                for esc in suffix_escapes:
                    if esc[0] in item:
                        item = item.replace(esc[0], "}" + esc[1] )
                #print(item)

                result = result + "\n" + item

    # now any in block tags
    result = YAML + parseMarkup(result)

    with open(logfile, "w") as log_file:
        log_file.write(result.encode('utf-8'))
