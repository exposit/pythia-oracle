#!/usr/bin/env python
#-*- coding: utf-8 -*-
##-------------------------------------------------------------------------------------------------------------------------------------------
#  Module A (Test & Sample)
#
##-------------------------------------------------------------------------------------------------------------------------------------------
from imports import *
import config


def test():
    print("hi from advmod")

def Flee(self, *args):
    config.module['block'] = 'The End'
    showCurrentBlock(self, args)
