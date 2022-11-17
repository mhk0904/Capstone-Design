#!/usr/bin/env python3
import rospy
import string

from std_msgs.msg import String
import sys
import os,time
import adafruit_servokit
import numpy as np

#i2c = busio.I2C(board.SCL, board.SDA)
#hat = adafruit_pca9685.PCA9685(i2c)
kit = adafruit_servokit.ServoKit(channels=16)
global val
val = None

def callback(data):
    #rospy.loginfo('%s', data.data)
    finger = (data.data).split(',')

    Thumb_finger = int(finger[0])
    if Thumb_finger < 30:
        Thumb_finger = 30
    elif Thumb_finger > 170:
        Thumb_finger = 170
    else:
        Thumb_finger = Thumb_finger
    
    Index_finger = int(finger[1])
    if Index_finger < 30:
        Index_finger = 30
    elif Index_finger > 170:
        Index_finger = 170
    else:
        Index_finger = Index_finger

    Middle_finger = int(finger[2])
    if Middle_finger < 30:
        Middle_finger = 30
    elif Middle_finger > 170:
        Middle_finger = 170
    else:
        Middle_finger = Middle_finger

    Ring_finger = int(finger[3])
    if Ring_finger < 30:
        Ring_finger = 30
    elif Ring_finger > 170:
        Ring_finger = 170
    else:
        Ring_finger = Ring_finger
    
    little_finger = int(finger[4])
    if little_finger < 30:
        little_finger = 30
    elif little_finger > 170:
        little_finger = 170
    else:
        little_finger = little_finger

    kit.servo[0].angle = 180 - Thumb_finger
    kit.servo[2].angle = Index_finger
    kit.servo[4].angle = Middle_finger
    kit.servo[7].angle = Ring_finger
    kit.servo[8].angle = little_finger

    rospy.loginfo('%d, %d, %d, %d, %d', int(finger[0]),int(finger[1]),int(finger[2]),int(finger[3]),int(finger[4]))


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', String, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()


# text = '123, 200'
# strings = text.split(',')
# print(strings)
# value1 = int(strings[0])
# value2 = int(strings[1])
# print(value1)
# print(value2)
