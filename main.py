#!/usr/bin/python
# -*- coding: utf-8 -*-
from teleoperation.robotarm_teleoperation_command import RobotArmTeleoperation_Command
from teleoperation.robotarm_teleoperation_keyboard import RobotArmTeleoperation_Keyboard
from i611_MCS import *
from i611_extend import *
from i611_io import *
import sys


def initialization():
    rb = i611Robot()
    _BASE = Base()
    rb.open()
    rb.home()
    IOinit( rb )

    return rb


def move_with_code(rb):
    """Set positions from data"""
    p1 = Position( 95, -280, 425, -120, 84, -28 )
    p2 = Position( 95, -280, 240, 154, 80, -114 )
    p3 = Position( 300, -280, 240, 159, 86, -156 )
    p4 = p3.copy()
    p4.shift( dz=40 )
    j1 = Joint( 230, -1, -92, 90, 5, 89 )
    
    """Customize jnt and lin speed"""
    m = MotionParam( jnt_speed=10, lin_speed=70 )
    rb.motionparam( m )

    """
    DEFAULT = 5.0
    jnt_speed : % -> 단위가 없는 것을 보니 rad/s 으로 추정?
    lin_speed : mm/s
    """
    
    """Start"""
    rb.home()
    rb.move( p1.offset(dz=30) )
    rb.line( p2, p3, p4 )
    rb.move( j1 )
    rb.home()

    # rb.close()

def move_with_keyboard(cur_pos, rb):
    key_teleop = RobotArmTeleoperation_Keyboard(cur_pos, rb)
    print(key_teleop.msg)
    while True:
        try:
            key = key_teleop.ready_for_keyboard_input()
            pos_candidate = key_teleop.make_new_position(key)
            new_pos = key_teleop.return_position(pos_candidate)
            rb.move(new_pos)
            # rb.line(key_teleop.cur_pos, new_pos)
            # rb.optline(key_teleop.cur_pos, new_pos)

            key_teleop.pst_pos = key_teleop.cur_pos
            key_teleop.cur_pos = new_pos
        except KeyboardInterrupt:
            print("keyboard interrupt abort!")
        except:
            print(key_teleop.e)

def move_with_command(cur_pos, rb):
    cmd_teleop = RobotArmTeleoperation_Command(cur_pos, rb)
    print(cmd_teleop.msg)
    while True:
        try:
            pass
        except:
            print(cmd_teleop.e)

def get_initialized_pos(rb):
    cur_pos = rb.getpos()
    
    if cur_pos != Position():
        rb.home()
        cur_pos = rb.getpos()
    return cur_pos

def terminator(rb):
    flag = rb.home()
    if not flag:
        print('Error : manipulator failed to come back home position!')
    rb.close()

# def emergency_stop_everything(rb):
#     rb.abort()

if __name__ == '__main__':
    rb = initialization()
    argument = sys.argv

    cur_pos = get_initialized_pos(rb)
    cur_jnt = rb.getjnt()

    try:

        if len(argument) == 1:
            print("Set to code_control")
            # move_with_code(rb)
        elif len(argument) == 2:
            if argument[1] == '-keyboard':                
                move_with_keyboard(cur_pos, rb)
            elif argument[1] == '-command':
                move_with_command(cur_pos, rb)
            else:
                print('Invalid argument input! Set to Default : move_with_keyboard')
                move_with_keyboard(cur_pos, rb)

    except:
        pass

    finally:
        terminator(rb)


