#!/usr/bin/python
# -*- coding: utf-8 -*-

from i611_MCS import *
from i611_extend import *
from constant_variables import *
import sys
import os
import select
if os.name == 'nt':
    import msvcrt
else:  
    import tty
    import termios


class RobotArmTeleoperation_Keyboard():

    #########################################################
    #Get keyboard input, Return new, and compatible position#
    #########################################################

    def __init__(self, cur_pos,rb):
        self.cur_pos = cur_pos
        self.pst_pos = None
        self.rb = rb

        self.offset_amount = OFFSET_AMOUNT
        self.msg = """
        Control Your i611 RobotArm in 3D World! (6 Directions)
        Suppose your endpoint is set to current plane, and control with WASDXHL keyboard input. 
        
        WARNING : BEWARE OF ENDPOINT ORIENTATION!
        WARNING : REMIND THAT THIS CONTROL SUPPORTS 6 DIRECTIONS, NOT 6 DOF!

       _____________________________
       | Moving around x-y plane:  |
       |     w                     |
       | a   s   d                 |
       |     x                     |
       |                           |
       | Moving around z-axis:     |
       |                           |
       | h (high)   l (low)        |
       |                           |
       | u (undo)                  |
       |___________________________|
        
        CTRL-C to quit\n
        """

        self.e = """
        Communications Failed\n
        """
 
    def getKey(self):
        """Recognize keyboard input"""
        # windows
        if os.name == 'nt':
            if sys.version_info[0] >= 3: # just-in-case python 3+
                return msvcrt.getch().decode()
            else:
                return msvcrt.getch() # python 2.7

        # just-in-case linux-like os
        tty.setraw(sys.stdin.fileno())
        rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
        if rlist:
            key = sys.stdin.read(1)
            return key
        else:
            key = ''
            return key
    

    def ready_for_keyboard_input(self):
        """Get keyboard input"""
        key_list = ['w', 'a', 's', 'd', 'x', 'h', 'l', 'u']
        
        while True:
            key = self.getKey()
            if key in key_list:
                break
        return key

    def make_new_position(self, key):
        """Formulate new position with keyboard input"""
        position = self.cur_pos
        
        try:
            if key == 'w':
                position.shift(dy = self.offset_amount)
            
            elif key == 'a':
                position.shift(dx = -self.offset_amount)
            
            elif key == 'd':
                position.shift(dx = self.offset_amount)

            elif key == 'x':
                position.shift(dy = -self.offset_amount)

            elif key == 's':
                # BEWARE OF S : THIS INITIALIZES THE POSITION VALUE
                position = self.rb.home()

            elif key == 'h':
                position.shift(dz = self.offset_amount)

            elif key == 'l':
                position.shift(dz = -self.offset_amount)
            
            elif key == 'u':
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
