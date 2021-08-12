#!/usr/bin/python
# -*- coding: utf-8 -*-
from .sample_moves import RobotArmTeleoperation_Sample
from .robotarm_teleoperation_command import RobotArmTeleoperation_Command
from .robotarm_teleoperation_keyboard_RPY import RobotArmTeleoperation_Keyboard
from .robotarm_teleoperation_keyboard_JNT import RobotJointTeleoperation_Keyboard
from i611_MCS import *
from i611_extend import *
from i611_io import *
import sys

class TeleoperationManager:
    def initialization(self):
        rb = i611Robot()
        _BASE = Base()
        rb.open()
        rb.home()
        IOinit( rb )

        return rb


    def run_with_code(self, rb):
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

    def run_with_keyboard_RPY(self, cur_pos, rb):
        key_teleop = RobotArmTeleoperation_Keyboard(cur_pos, rb)
        print(key_teleop.msg)
        while True:
            print("Waiting for keyboard input...\n")
            try:
                key = key_teleop.ready_for_keyboard_input()
                pos_candidate = key_teleop.make_new_position(key)
                new_pos = key_teleop.return_position(pos_candidate)

                #Check  path
                rb.move(new_pos)
                # rb.line(key_teleop.cur_pos, new_pos)
                # rb.optline(key_teleop.cur_pos, new_pos)

                # Position Update
                key_teleop.pst_pos = key_teleop.cur_pos
                key_teleop.cur_pos = new_pos
            except KeyboardInterrupt:
                print("keyboard interrupt abort!\n")
                break
            except:
                print(key_teleop.e)
                break

    def run_with_keyboard_JNT(self, cur_jnt, rb):
        key_teleop = RobotJointTeleoperation_Keyboard(cur_jnt, rb)
        print(key_teleop.msg)
        while True:
            print("Waiting for keyboard input...\n")
            try:
                key = key_teleop.ready_for_keyboard_input()
                new_jnt = key_teleop.make_new_joint(key)

                rb.move(new_jnt)
                key_teleop.cur_jnt = new_jnt
            except KeyboardInterrupt:
                print('KeyboardInterrupt abort!\n')
                break
            except:
                print(key_teleop.e)
                break

    def run_with_command(self, cur_pos, rb):
        cmd_teleop = RobotArmTeleoperation_Command(cur_pos, rb, sys.argv[2])
        print(cmd_teleop.msg)
        while True:
            try:
                cmd_teleop.set_offset_amount()
                pos_candidate = cmd_teleop.make_new_position()
                new_pos = cmd_teleop.return_position(pos_candidate)

                rb.move(new_pos)

                # Position Update
                cmd_teleop.pst_pos = cmd_teleop.cur_pos
                cmd_teleop.cur_pos = new_pos
            except:
                print(cmd_teleop.e)

    def run_sample_moves(self):
        samplemove_teleop = RobotArmTeleoperation_Sample()
        print(samplemove_teleop.msg)
        while True:
            try:
                key = samplemove_teleop.ready_for_keyboard_input()
                samplemove_teleop.mode_selection(key)
                samplemove_teleop.action()
            except:
                print("Invalid Key Error!")


    def get_initialized_pos(self,rb):
        cur_pos = rb.getpos()
        
        if cur_pos != Position():
            rb.home()
            cur_pos = rb.getpos()
        return cur_pos

    def terminator(rb):
        flag = rb.home()
        if not flag:
            print('Error : manipulator failed to come back home position!\n')
        rb.close()

    def emergency_stop_everything(rb):
        rb.abort()  