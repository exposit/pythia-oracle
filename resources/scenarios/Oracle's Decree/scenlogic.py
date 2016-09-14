#-*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------------------
# Oracle's Decree (Tutorial)
#
# This file contains scenario specific logic.
#
##---------------------------------------------------------------------------------------------------

from imports import *
import config


def test():
    print("hi from modlogic")

def overlandEncounter(self):

    roll = random.randint(0,9)

    result = config.scenario['overlandEncounterChart'][roll][0]

    if roll == 1 or roll == 4 or roll == 5 or roll == 6 or roll == 9:
        config.scenario['overlandEncounterChart'][roll][0] = "Water Shade"
        config.scenario['overlandEncounterChart'][roll][1] = "jump_meetshade"

    if result == "Water Shades":
        result = result + " [" + str(random.randint(1,2)) + "] "
        updateCenterDisplay(self, result, 'result')
    elif result == "Heelan Bandits":
        result = result + " [" + str(random.randint(1,3)) + "] "
        updateCenterDisplay(self, result, 'result')
    elif result == "Sand Sprites":
        result = result + " [" + str(random.randint(1,6)) + "] "
        updateCenterDisplay(self, result, 'result')

    refPress(config.textLabelArray[-1], config.scenario['overlandEncounterChart'][roll][1])

def setFishOrWater(self):
    config.scenario['fishattack'] = random.choice([True, False])

def setPetitioner(self):
    choice = random.choice([True, False])
    config.scenario['petitioner'] = choice
    return choice

def setTrueOrFalse(self):
    return random.choice([True, False])

def getProphecy(self):

    chart = [
        'It mumbles something you don\'t quite catch about \'appendix a\'.',
        'It sonorously intones a recipe for fish stew.',
        'It ponderously intones a mathematical formula for computing pi to four digits.',
        'It spouts a long list of items as if from a ledger of household goods.',
        'It recites a long poem on duty with no inflection.',
        'It recites a racy ode involving many water and flower allusions.',
        'It speaks for a moment, then falls silent. You\'re not sure, but you think it just insulted your parentage.',
    ]

    return random.choice(chart)
