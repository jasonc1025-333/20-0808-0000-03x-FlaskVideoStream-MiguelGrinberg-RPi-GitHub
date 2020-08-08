#!/usr/bin/env python3
##jwc o #!/usr/bin/env python2

# jwc from: ~/01-Jwc/03t-StsPilot-MarkOrion/STS-PiLot

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 09:44:23 2017

@author: Mark Dammer

This file contains basic configuration and all former global variables
"""
# Configuration
width = 320 # Video width requested from camera
height = 240 # Video height requested from camera
video_src = 0 # OpenCV video source for camera_cv.py
pi_hflip = True # Flip Picamera image horizontally
pi_vflip = True # Flip Picamera image vertically
cv_hflip = False # Flip OpenCV camera image horizontally
cv_vflip = False # Flip OpenCV camera image vertically

# Global values
camera_detected = True
camera_active = True
camera = None
stream = None
video_status = True
video_fps = 0
brakes = False
chocks = False
blue = False
yellow = False
green = False
watchdog_Alive_Bool = True
watchdog_Start_On_Bool = True
watchdog_Cycles_Now = 20
timeout_Cycles_MAX = 10
left_motor = 0
right_motor = 0
servo_01_Pan_Degrees = 90
servo_02_Tilt_Degrees = 90
servo_03_Degrees = 0
servo_04_Degrees = 0
temp = 0
