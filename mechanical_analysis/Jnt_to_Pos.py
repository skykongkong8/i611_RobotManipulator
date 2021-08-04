#!/usr/bin/python
# -*- coding: utf-8 -*-
from i611_MCS import *
from i611_extend import *
from i611_io import *


rb = i611Robot()
j1 = Joint(30,30,30,30,30,30)
p1 = rb.Joint2Position(j1)

print(p1)