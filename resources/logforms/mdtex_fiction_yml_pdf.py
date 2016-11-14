#!/usr/bin/env python
#-*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------
#
#  Markdown
#     fiction: includes only fiction blocks
#     yml: uses a yaml Front Matter from config.txt
#     pdf: is ready to convert to pdf (or latex) via pandoc
#
##---------------------------------------------------------------------------------------

import imports
from imports import *
import config

def exclude():
    return False

def makeLogFile(self):

    logfile = config.curr_game_dir + "logs" + os.sep + "fiction_yml_pdf.md"

    textArray, textStatusArray = getSourceMaterial()

    YAML = config.yaml_for_pdf

    fictionStatusList = ["plain", "italic", "bold", "bold_italic", "color1", "color2"]

    result = ""
    for item in textArray:
        ti = textArray.index(item)
        item = item.rstrip()
        if textStatusArray[ti] in fictionStatusList:
            
            result = result + "\n"

            prefix_escapes = [ ['[i][b]', '\\textit{\\textbf{' ], ['[b][i]', '\\textbf{\\textit{'], ['[i]', '\\textit{'], ['[b]', '\\textbf{'] ]
            suffix_escapes = [ ['[/i][/b]', '}}'], ['[/b][/i]', '}}'], ['[/i]', '}'], ['[/b]',  '}'] ]

            for esc in prefix_escapes:
                if esc[0] in item:
                    item = item.replace(esc[0], esc[1] + "\plain{" )
            for esc in suffix_escapes:
                if esc[0] in item:
                    item = item.replace(esc[0], "}" + esc[1] )

            result = result + "\n" + item

    result = YAML + parseMarkup(result)
    result = result.lstrip()

    with open(logfile, "w") as log_file:
        log_file.write(result.encode('utf-8'))
