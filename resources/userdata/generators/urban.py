##-------------------------------------------------------------------------------------------------------------------------------------------
#  cities & actors panel
# -*- coding: utf-8 -*-
#
#
##-------------------------------------------------------------------------------------------------------------------------------------------

import imports
from imports import *
import config


def initPanel(self):

        urbanAItem = AccordionItem(title='Urban & Actors', background_selected='invisible.png', min_space=30)

        urbanMainBox = BoxLayout(orientation='vertical')

        urbanMainBox.add_widget(Label(text="Actors", size_hint=(1,1)))

        button = Button(text="Actor Age - Adult", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.function = "actorAgeAdult"
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=genericChartRoll)
        urbanMainBox.add_widget(button)

        button = Button(text="Actor Age - Any", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.function = "actorAgeAny"
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=genericChartRoll)
        urbanMainBox.add_widget(button)

        button = Button(text="Actor Gender", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.function = "actorGender"
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=genericChartRoll)
        urbanMainBox.add_widget(button)

        urbanAItem.add_widget(urbanMainBox)

        return urbanAItem

def genericChartRoll(*args):
    args[0].background_color = neutral
    self = args[0].self
    result = eval(args[0].function)()
    updateCenterDisplay(self, result)

#-------------------------------------------------------------------------------------------------------------------------------------------
# --> some 2d4 love
#-------------------------------------------------------------------------------------------------------------------------------------------

def actorGender():

    gender = random.choice(["male", "female"])

    return "[Gender] " + gender

def actorAgeAdult():

    chart = {
        2 : "Mid to late teens.",
        3 : "Nineteen or twenty.",
        4 : "Early twenties.",
        5 : "Mid-twenties.",
        6 : "Late twenties.",
        7 : "Thirties.",
        8 : "Forties.",
    }

    roll = random.randint(1,4) + random.randint(1,4)

    result = "[Age - Mature] " + chart[roll]

    return result

def actorAgeAny():

    chart = {
        2 : "Child.",
        3 : "Teen.",
        4 : "Young Adult.",
        5 : "Mature.",
        6 : "Middle-Aged.",
        7 : "Old.",
        8 : "Venerable.",
    }

    roll = random.randint(1,4) + random.randint(1,4)

    result = "[Age - Any] " + chart[roll]
    return result
