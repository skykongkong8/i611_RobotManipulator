#!/usr/bin/python
# -*- coding: utf-8 -*-
# 라이브러리 가져오기
from i611_MCS import *
from i611_extend import *
from i611_io import *
import sys


def main():
    # i611 로봇 생성자
    rb = i611Robot()
    # 월드 좌표계 정의
    _BASE = Base()
    
    # 로봇과 연결 시작 초기화
    rb.open()
    # I/O 입출력 기능 초기화 (I/O 미사용시 생략 가능 )
    IOinit( rb )
    
    ## 3. 교시 포인트 설정 ######################
    p1 = Position( 95, -280, 425, -120, 84, -28 )
    p2 = Position( 95, -280, 240, 154, 80, -114 )
    p3 = Position( 300, -280, 240, 159, 86, -156 )
    p4 = p3.copy()
    p4.shift( dz=40 )
    j1 = Joint( 230, -1, -92, 90, 5, 89 )
    
    ## 4. 동작 조건 설정 ##################################
    #MotionParam 생성자에서 동작 조건 설정
    m = MotionParam( jnt_speed=10, lin_speed=70 )

    """
    DEFAULT = 5.0
    lin_speed : mm/s
    jnt_speed : % -> 단위가 없는 것을 보니 rad/s 으로 추정?
    """

    #MotionParam 형으로 동작 조건 설정
    rb.motionparam( m )
    
    ## 5. 로봇 동작 정의 ##############################
    # 작업 시작
    rb.home()
    rb.move( p1.offset(dz=30) )
    rb.line( p2, p3, p4 )
    rb.move( j1 )
    rb.home()
    ## 6. 종료 ######################################
    # 로봇과의 연결을 종료
    rb.close()
if __name__ == '__main__':
    main()


# Good news:
# Python 2.7 still supports sys.argv
