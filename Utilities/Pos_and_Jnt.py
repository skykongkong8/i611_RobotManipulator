#!/usr/bin/python
# -*- coding: utf-8 -*-

from i611_MCS import *
from i611_extend import *
from teachdata import *
import sys

# Compatible with python 3
# class NoArgumentError(Exception):
#     def __init__(self):
#         super().__init__('No Argument Given!')

if __name__ == '__name__':
    rb = i611Robot()
    argument = sys.argv
    try:
        if len(argument) >= 2:
            argument = sys.argv[1]
            if argument == '-Joint2Position':
                pass
            elif argument == 'Position2Joint':
                try:
                    pass
                except:
                    print('Error : given position cannot be configured as joint because of singularity issue.')

        elif len(argument) < 2:
            print("No Argument Error!")
    except:
        print("Unknown Error!")
