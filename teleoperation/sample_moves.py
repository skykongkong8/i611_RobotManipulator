#!/usr/bin/python
# -*- coding: utf-8 -*-

from i611_MCS import *
from i611_extend import *
from constant_variables import *


class RobotArmTeleoperation_Sample():
    def __init__(self, rb):
        self.figure_height = FIGURE_DEFAULT_HEIGHT
        self.figure_width = FIGURE_DEFAULT_WIDTH
        self.rb = rb
        self.msg = """
        Welcome to RobotArmTeleoperation Sample Moves mode!
        """

    def set_motion_param(self, motion_param):
        self.rb.motionparam(motion_param)

    def draw_line(self):
        pass

    def draw_circle(self):
        StartJoint  = Joint(0, -30, -90, 0, -60, 0)
        StartSpeed  = MotionParam(jnt_speed = 45.0, lin_speed = 40.0, acctime = 0.4, dacctime = 0.4, overlap = 1.0, pose_speed = 80)
        self.set_motion_param(StartSpeed)

        self.rb.move(StartJoint)

    def draw_square(self):
        pass