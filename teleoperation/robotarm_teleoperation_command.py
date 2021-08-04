#!/usr/bin/python
# -*- coding: utf-8 -*-

from i611_MCS import *
from i611_extend import *
from constant_variables import *
import sys

class RobotArmTeleoperation_Command():
    def __init__(self, cur_pos, rb, argument):
        self.cur_pos = cur_pos
        self.pst_pos = None
        self.rb = rb
        self.argument = argument
        self.offset_amount = OFFSET_AMOUNT
        self.msg = """
        Control Your i611 RobotArm in 3D World! (6 Directions)
        Suppose your endpoint is set to current plane, and control with WASDXHL keyboard input. 
        
        WARNING : BEWARE OF ENDPOINT ORIENTATION!
        WARNING : REMIND THAT THIS CONTROL SUPPORTS 6 DIRECTIONS, NOT 6 DOF!

        command guide:

        [axis control]
        +x -x
        +y -y
        +z -z

        [additional control]
        -home
        -undo

        CTRL-C to quit\n
        """

        self.e = """
        Communications Failed\n
        """
        self.count = 0

    def set_offset_amount(self):
        argument = self.argument
        if len(argument) <= 3:
            pass
        elif len(argument) == 4:
            if type(argument[3]) == int or type(argument[3]) ==float:
                self.offset_amount = argument[3]
        print("offset amount set to {}". format(self.offset_amount))
        
    def make_new_position(self):
        """Formulate new position with keyboard input"""
        position = self.cur_pos        
        argument = self.argument
        try:
            if argument == '+y':
                position.shift(dy = self.offset_amount)
            
            elif argument == '-x':
                position.shift(dx = -self.offset_amount)
            
            elif argument == '+x':
                position.shift(dx = self.offset_amount)

            elif argument == '-y':
                position.shift(dy = -self.offset_amount)

            elif argument == '-home':
                # BEWARE OF S : THIS INITIALIZES THE POSITION VALUE
                position = self.rb.home()

            elif argument == '+z':
                position.shift(dz = self.offset_amount)

            elif argument == '-z':
                position.shift(dz = -self.offset_amount)
            
            elif argument == '-undo':
                if self.pst_pos:
                    position = self.pst_pos
                else:
                    print('There is no past position!')
        except:
            print("Unknown Error : set to past position")
            return self.pst_pos
        finally:
            return position

    def check_position(self, position):
        """If joint configuration exists, such configuration is compatible"""
        try:
            check_joint = self.rb.Position2Joint(position)
        except:
            print('Physical Error : Current robot does not support required position.')
            self.cur_pos = self.pst_pos
            return False
        return True

    def return_position(self, position):
        """Only returns promised position"""
        if self.check_position(position):
            return position
        else:
            return self.cur_pos
