# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 19:41:39 2024

@author: Gebruiker
Inspired by Nicolai Nielsen's tutorial video on YOLOv10
"""

import cv2
import os

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print ('Unable to access livestream.')

output_dir = 'output_img'
os.makedirs(output_dir, exist_ok=True)

img_counter = 0 

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    cv2.imshow('Swag', frame)
    
    key = cv2.waitKey(1)
    
    if key%256 == 27:
        print ("Closing...")
        break
    elif key%256 == 115:
        img_name = os.path.join(output_dir, "opencv_frame_{}.png".format(img_counter))
        cv2.imwrite(img_name, frame)
        print("{} saved!".format(img_name))
        img_counter += 1
        
cap.release()
cv2.destroyAllWindows()
    
    