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


class RobotArmTeleoperation_Sample():
    def __init__(self, rb):
        self.figure_height = FIGURE_DEFAULT_HEIGHT
        self.figure_width = FIGURE_DEFAULT_WIDTH
        self.rb = rb
        self.mode = None
        self.msg = """
        Welcome to RobotArmTeleoperation Sample Moves mode!

        quick guide
            c : circle
            s : show off
            l : line
        
        """

    def draw_circle(self):
        StartJoint  = Joint(0, -30, -90, 0, -60, 0)
        StartPos = self.jnt2pos(StartJoint)
        StartSpeed  = MotionParam(jnt_speed = 45.0, lin_speed = 40.0, acctime = 0.4, dacctime = 0.4, overlap = 1.0, pose_speed = 80)
        self.set_motion_param(StartSpeed)
        self.do_move(StartJoint)

        try:
            p1 = StartPos.offset(dx = 100, dy = 50)
            p2 = StartPos.offset(dx = 50, dy = 200)

            # sample circle 1
            self.rb.circlemove(p1, p2, 0)
            self.do_move(StartPos)

            # sample circle 2
            self.rb.circlemove(p1, p2, 1)
            self.do_move(StartPos)

        except KeyboardInterrupt:
            self.rb_abort()
            print("Keyboard interrupt shutdown")


    def show_off(self):
        x_dist = 800
        z_dist = 100

        J1  = Joint(105, 45, 60, 0, 75, 45)
        P1  = self.rb.Joint2Position(J1)
        P1A = P1.offset(dz=z_dist)
        P2  = P1.offset(dx=-x_dist)
        P2A = P2.offset(dz=z_dist)
        
        m = MotionParam( jnt_speed=10, lin_speed=10, pose_speed=10, overlap = 30, ik_solver_option = 0x11111111 )
        self.rb.motionparam( m )
        
        do_move = self.rb.move
        do_move(J1)

        for _ in range(2):
            self.rb.sleep(1)
            self.rb.use_mt(False)
            do_move(P1)
            do_move(P1A)
            do_move(P2A)
            do_move(P2)
            do_move(P1)

            # Reverse Move
            self.rb.use_mt(True)
            do_move(P1)
            do_move(P1A)
            do_move(P2A)

            do_move(P2)
            do_move(P1)



    def draw_line(self):
        pass

    def set_motion_param(self, motion_param):
        self.rb.motionparam(motion_param)

    def do_move(self, joint_or_position):
        self.rb.move(joint_or_position)

    def jnt2pos(self, jnt):
        return self.rb.Joint2Position(jnt)

    def rb_abort(self):
        self.rb.abort()

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
        key_list = ['c', 's', 'l']

        """
        c : circle
        s : show-off
        l : line

        """
        
        while True:
            key = self.getKey()
            if key in key_list:
                break
        return key

    def mode_selection(self, key):
        if key == 'c':
            self.mode = C
        elif key == 's':
            self.mode = S
        elif key == 'l':
            self.mode = L
        else:
            self.mode = None

    def action(self):
        if self.mode == C:
            self.draw_circle()
        elif self.mode == S:
            self.show_off()
        elif self.mode == L:
            self.draw_line()