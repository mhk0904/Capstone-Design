#!/usr/bin/python3

import rospy
from std_msgs.msg import String

import cv2
import mediapipe as mp
import numpy as np

max_num_hands = 1
gesture = {
    0:'rock', 1:'one', 2:'two', 3:'three', 4:'four', 5:'paper',
    6:'six', 7:'rock', 8:'spiderman', 9:'scissors', 10:'ok',
}

# MediaPipe hands model
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Gesture recognition model
file = np.genfromtxt('/home/ko/catkin_ws/src/beginner_tutorials/src/gesture_train_test.csv', delimiter=',')
angle = file[:,:-1].astype(np.float32)
label = file[:, -1].astype(np.float32)
knn = cv2.ml.KNearest_create()
knn.train(angle, cv2.ml.ROW_SAMPLE, label)

cap = cv2.VideoCapture(0)

pub = rospy.Publisher('hand_position', String, queue_size=7)
rospy.init_node('CAM', anonymous=True)
rate = rospy.Rate(1) # 10hz

global val
val = None

with mp_hands.Hands(max_num_hands= max_num_hands, min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        ret, img = cap.read()
        if not ret:
            continue
        
        img = cv2.flip(img, 1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        result = hands.process(img)   
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        if result.multi_hand_landmarks is not None:
            for res in result.multi_hand_landmarks:
                joint = np.zeros((21, 3))
                for j, lm in enumerate(res.landmark):
                    joint[j] = [lm.x, lm.y, lm.z]

                # Compute angles between joints
                v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19],:] # Parent joint
                v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],:] # Child joint
                v = v2 - v1 # [20,3]
                # Normalize v
                v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

                # Get angle using arcos of dot product
                angle = np.arccos(np.einsum('nt,nt->n',
                    v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:], 
                    v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:])) # [15,]

                angle = np.degrees(angle) # Convert radian to degree

                # Inference gesture
                data = np.array([angle], dtype=np.float32)
                ret, results, neighbours, dist = knn.findNearest(data, 3)
                idx = int(results[0][0])

                # Draw gesture result
                if idx in gesture.keys():
                    cv2.putText(img, text=gesture[idx].upper(), org=(int(res.landmark[0].x * img.shape[1]), int(res.landmark[0].y * img.shape[0] + 20)), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 255, 255), thickness=2)
                    hello_str = "%s"  %gesture[idx].upper()
                    if hello_str != val:
                        val = hello_str    
                        pub.publish(hello_str)
                        rate.sleep()
                        rospy.loginfo(hello_str)

                    mp_drawing.draw_landmarks(img, res, mp_hands.HAND_CONNECTIONS, mp_drawing.DrawingSpec(color=(255,255,255),thickness=2 , circle_radius=4),
                    mp_drawing.DrawingSpec(color=(0,0,0),thickness=2 , circle_radius=2))

        cv2.imshow('Game', img)
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
