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

class RobotJoints():
    def __init__(self):
        pass

class RobotJointTeleoperation_Keyboard():

    #########################################################
    #Get keyboard input, Return new, and compatible position#
    #########################################################

    def __init__(self, cur_jnt,rb):
        self.cur_jnt = cur_jnt
        self.rb = rb
        self.mode = J1J2 #DEFAULT = J1J2

        self.offset_amount = OFFSET_AMOUNT
        self.msg = """
        Control Your i611 RobotArm in 3D World! (6 Directions)
        Suppose your endpoint is set to current plane, and control with WASDXHL keyboard input. 
        
        WARNING : BEWARE OF ENDPOINT ORIENTATION!
        WARNING : REMIND THAT THIS CONTROL IS IDENTICAL TO JOG STICK CONTROL!
        _________________________________
        |    Joint Control:             |
        |        w                      |
        |    a   s   d                  |
        |        d                      |
        |                               |
        |   Chmod:                      |
        |    u   : Joint 1 & Joint 2    |
        |    j   : Joint 3 & Joint 4    |
        |    m   : Joint 5 & Joint 6    |
        |_______________________________|
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
        key_list = ['w', 'a', 's', 'd', 'x', 'u', 'j', 'm']
        
        while True:
            key = self.getKey()
            if key in key_list:
                break
        return key

    def j1j2(self, key, joint):
        try:
            if key == 'w':
                joint.shift(dj2 = self.offset_amount)
            
            elif key == 'a':
                joint.shift(dj1 = -self.offset_amount)
            
            elif key == 'd':
                joint.shift(dj1 = self.offset_amount)

            elif key == 'x':
                joint.shift(dj2 = -self.offset_amount)

            elif key == 's':
                pass

            elif key == 'u':
                self.mode = J1J2

            elif key == 'j':
                self.mode = J3J4

            elif key == 'm':
                self.mode = J5J6
            return joint

        except:
            print("Unknown Error : set to home")
            return joint.clear()

    def j3j4(self,key, joint):
        try:
            if key == 'w':
                joint.shift(dj4 = self.offset_amount)
            
            elif key == 'a':
                joint.shift(dj3 = -self.offset_amount)
            
            elif key == 'd':
                joint.shift(dj3 = self.offset_amount)

            elif key == 'x':
                joint.shift(dj4 = -self.offset_amount)

            elif key == 's':
                pass

            elif key == 'u':
                self.mode = J1J2

            elif key == 'j':
                self.mode = J3J4

            elif key == 'm':
                self.mode = J5J6
            return joint

        except:
            print("Unknown Error : set to home")
            return joint.clear()

    def j5j6(self, key, joint):
        try:
            if key == 'w':
                joint.shift(dj6 = self.offset_amount)
            
            elif key == 'a':
                joint.shift(dj5 = -self.offset_amount)
            
            elif key == 'd':
                joint.shift(dj5 = self.offset_amount)

            elif key == 'x':
                joint.shift(dj6 = -self.offset_amount)

            elif key == 's':
                pass

            elif key == 'u':
                self.mode = J1J2

            elif key == 'j':
                self.mode = J3J4

            elif key == 'm':
                self.mode = J5J6
            return joint

        except:
            print("Unknown Error : set to home")
            return joint.clear()


    def make_new_joint(self, key):
        """Formulate new position with keyboard input"""
        joint = self.cur_jnt
        if self.mode == J1J2:
            return self.j1j2(key, joint)
        elif self.mode == J3J4:
            return self.j3j4(key, joint)
        elif self.mode == J5J6:
            return self.j5j6(key, joint)