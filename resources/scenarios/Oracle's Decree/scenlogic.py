#!/usr/bin/env python
#-*- coding: utf-8 -*-
##-------------------------------------------------------------------------------------------------------------------------------------------
#  Module A (Test & Sample)
#
##-------------------------------------------------------------------------------------------------------------------------------------------
from imports import *
import config


def test():
    print("hi from modlogic")

def Flee(self, *args):
    config.module['block'] = 'The End'
    showCurrentBlock(self)

def overlandEncounter(self):

    roll = random.randint(0,9)
    roll=0

    result = config.scenario['overlandEncounterChart'][roll][0]

    if roll == 2 or roll == 5 or roll == 6 or roll == 7 or roll == 10:
        config.scenario['overlandEncounterChart'][roll][0] = "Water Shade"
        config.scenario['overlandEncounterChart'][roll][1] = "jump_meetshade"

    if result == "Water Shades":
        result = result + " [" + str(random.randint(1,2)) + "] "
    elif result == "Heelan Bandits":
        result = result + " [" + str(random.randint(1,3)) + "] "
    elif result == "Sand Sprites":
        result = result + " [" + str(random.randint(1,6)) + "] "

    # set a variable on entering this event
    #if result == "A field of Sand Domes":
    #    config.scenario['fishattack'] = random.choice([True, False])

    updateCenterDisplay(self, result, 'result')

    refPress(config.textLabelArray[-1], config.scenario['overlandEncounterChart'][roll][1])

def setFishOrWater(self):
    config.scenario['fishattack'] = random.choice([True, False])
