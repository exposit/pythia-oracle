#!/usr/bin/env python
#-*- coding: utf-8 -*-
##-------------------------------------------------------------------------------------------------------------------------------------------
#  Imports
#
##-------------------------------------------------------------------------------------------------------------------------------------------

# General Python
import os
import time
import random
import math
import simplejson
import glob
import string

# Kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition, NoTransition, SlideTransition, SwapTransition, FadeTransition, FallOutTransition, RiseInTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.core.text import LabelBase
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.behaviors import ToggleButtonBehavior

from kivy.uix.image import Image
from kivy.graphics import *
from kivy.properties import ObjectProperty, ListProperty

from kivy.uix.dropdown import DropDown
from kivy.uix.splitter import Splitter
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.slider import Slider
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup

from kivy.graphics.svg import Svg
from kivy.lang import Builder
from kivy.uix.filechooser import FileChooserListView

from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty

import imp

# font & color
import styles
from styles import *

# logic files
import logic
from logic import *

# extra panels -- generators
try:
    userpanels = glob.glob("." + os.sep + "resources" + os.sep + "userdata" + os.sep + "generators" + os.sep + "*.py")
    gen_module = []
    for panel in userpanels:
        filename = panel.split('/')[-1]
        pyfile = filename.split('.')[0]
        potential = imp.load_source( pyfile, panel)
        if potential.exclude() == False:
            gen_module.append(potential)
except:
    pass

# extra panels -- oracles
try:
    userpanels = glob.glob("." + os.sep + "resources" + os.sep + "userdata" + os.sep + "oracles" + os.sep + "*.py")
    oracle_module = []
    for panel in userpanels:
        filename = panel.split('/')[-1]
        pyfile = filename.split('.')[0]
        potential = imp.load_source( pyfile, panel)
        if potential.exclude() == False:
            oracle_module.append(potential)
except:
    pass

random.seed()

for font in KIVY_FONTS:
    LabelBase.register(**font)
