from i611_MCS import *
from i611_extend import *
from constant_variables import *
import sys

class RobotArmTeleoperation_Command():
    def __init__(self, cur_pos):
        self.cur_pos = cur_pos
        self.pst_pos = None
        self.rb = i611Robot()

        self.offset_amount = OFFSET_AMOUNT
        self.msg = """
        Control Your i611 RobotArm in 3D World! (6 Directions)
        Suppose your endpoint is set to current plane, and control with WASDXHL keyboard input. 
        
        WARNING : BEWARE OF ENDPOINT ORIENTATION!
        WARNING : REMIND THAT THIS CONTROL SUPPORTS 6 DIRECTIONS, NOT 6 DOF!

        ---------------------------
        Moving around x-y plane:
            w
        a    s    d
            x
        
        Moving around z-axis:

        h (high)   l (low)
        
        CTRL-C to quit\n
        """

        self.e = """
        Communications Failed\n
        """