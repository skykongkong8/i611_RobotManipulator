#!/usr/bin/python
# -*- coding: utf-8 -*-
from i611_MCS import *
from i611_extend import *
from i611_io import *


rb = i611Robot()
rb.home()

home_pos = rb.getpos()
"""
Quick remind:

rb.getpos()
teachdata.get_pos()
cell.get_position()
"""
# j1 = Joint(30,30,30,30,30,30)
# p1 = rb.Joint2Position(j1)

print(home_pos)