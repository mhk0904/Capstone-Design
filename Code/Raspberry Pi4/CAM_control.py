#!/usr/bin/env python3

#***********************************************************
#* Software License Agreement (BSD License)
#*
#*  Copyright (c) 2009, Willow Garage, Inc.
#*  All rights reserved.
#*
#*  Redistribution and use in source and binary forms, with or without
#*  modification, are permitted provided that the following conditions
#*  are met:
#*
#*   * Redistributions of source code must retain the above copyright
#*     notice, this list of conditions and the following disclaimer.
#*   * Redistributions in binary form must reproduce the above
#*     copyright notice, this list of conditions and the following
#*     disclaimer in the documentation and/or other materials provided
#*     with the distribution.
#*   * Neither the name of the Willow Garage nor the names of its
#*     contributors may be used to endorse or promote products derived
#*     from this software without specific prior written permission.
#*
#*  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#*  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#*  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
#*  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
#*  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
#*  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
#*  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#*  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#*  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
#*  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
#*  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#*  POSSIBILITY OF SUCH DAMAGE.
#***********************************************************

# Author: Blaise Gassend

import rospy
from std_msgs.msg import String
import sys
import os,time
from adafruit_servokit import ServoKit
import numpy as np

#i2c = busio.I2C(board.SCL, board.SDA)
#hat = adafruit_pca9685.PCA9685(i2c)
kit = ServoKit(channels=16)
global val
val = None


def servo(data):
    if data == "ROCK":
        kit.servo[0].angle = 0        
        kit.servo[2].angle = 150
        kit.servo[4].angle = 150
        kit.servo[7].angle = 150
        kit.servo[8].angle = 150
    
    if data == "ONE":
        kit.servo[0].angle = 0
        kit.servo[2].angle = 30
        kit.servo[4].angle = 150
        kit.servo[7].angle = 150
        kit.servo[8].angle = 150

    if data == "TWO":
        kit.servo[0].angle = 150
        kit.servo[2].angle = 30
        kit.servo[4].angle = 150
        kit.servo[7].angle = 150
        kit.servo[8].angle = 150
    
    if data == "THREE":
        kit.servo[0].angle = 0
        kit.servo[2].angle = 30
        kit.servo[4].angle = 30
        kit.servo[7].angle = 30
        kit.servo[8].angle = 150

    if data == "FOUR":
        kit.servo[0].angle = 0
        kit.servo[2].angle = 30
        kit.servo[4].angle = 30
        kit.servo[7].angle = 30
        kit.servo[8].angle = 30

    if data == "PAPER":
        kit.servo[0].angle = 150
        kit.servo[2].angle = 30
        kit.servo[4].angle = 30
        kit.servo[7].angle = 30
        kit.servo[8].angle = 30

    if data == "OK":
        kit.servo[0].angle = 30
        kit.servo[2].angle = 150
        kit.servo[4].angle = 30
        kit.servo[7].angle = 30
        kit.servo[8].angle = 30

    if data == "SIX":
        kit.servo[0].angle = 150
        kit.servo[2].angle = 150
        kit.servo[4].angle = 150
        kit.servo[7].angle = 150
        kit.servo[8].angle = 30

    if data == "SCISSORS":
        kit.servo[0].angle = 0
        kit.servo[2].angle = 30
        kit.servo[4].angle = 30
        kit.servo[7].angle = 150
        kit.servo[8].angle = 150

def callback(data):
    rospy.loginfo('%s',data.data)
    servo(data.data)


if __name__ == '__main__':
    argv = rospy.myargv()

    rospy.init_node('CAM', anonymous=True)
    rospy.Subscriber('hand_position', String, callback)
    #soundhandle = SoundClient()
    rospy.sleep(0.8)
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
