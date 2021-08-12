#!/usr/bin/python
# -*- coding: utf-8 -*-

from teleoperation.teleoperation_manager import TeleoperationManager
from i611_MCS import *
from i611_extend import *
from i611_io import *
import sys

if __name__ == '__main__':
    manager = TeleoperationManager()
    rb = manager.initialization()
    argument = sys.argv

    cur_pos = manager.get_initialized_pos(rb)
    cur_jnt = rb.getjnt()

    try:

        if len(argument) == 1:
            # >> python main.py
            print("Set to code_control\n")
            # move_with_code(rb)

        elif len(argument) >= 2:
            if argument[1] == '-keyboard_RPY':
                # >> python main.py -RPY             
                manager.run_with_keyboard_RPY(cur_pos, rb)
            
            elif argument[1] == '-keyboard_JNT':
                manager.run_with_keyboard_JNT(cur_jnt, rb)

            elif argument[1] == '-command':
                # >> python main.py -command -(direction) -(offset_amount)
                if len(argument) >= 3:
                    manager.run_with_command(cur_pos, rb)
            else:
                print('Invalid argument input! Set to Default : move_with_keyboard_JNT\n')
                manager.run_with_keyboard_JNT(cur_pos, rb)

    except:
        manager.emergency_stop_everything()

    finally:
        print("Program Shutdown! Goodbye.\n")
        manager.terminator(rb)


