#!/usr/bin/python3

import time
import os 
import gpiod
from gpiod.line import Direction, Value, Bias, Edge

from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder

capturing = False

camera_a = Picamera2(0)
camera_a.configure(camera_a.create_video_configuration({"size":(1080,720)}))

camera_b = Picamera2(1)
camera_b.configure(camera_b.create_video_configuration({"size":(1080,720)}))

encodera = H264Encoder(1000000)
encoderb = H264Encoder(1000000)

fileA = "NoIR-video.mp4"
fileB = "IR-video.mp4"

def start_capturing():
    global capturing
    print("capture is on")
    capturing = True
    time.sleep(1)
    #catch errors and indicate LED
    camera_a.start_recording(encodera,fileA)
    camera_b.start_recording(encoderb,fileB)

def end_capturing():
    global capturing
    capturing = False
    print("capture is ended")
    time.sleep(1)
    #catch errors and indicate LED
    camera_a.stop_recording()
    camera_b.stop_recording()

#setup GPIO
LINE = 2
while True:
    with gpiod.request_lines(
        "/dev/gpiochip0",
        consumer="blink-example",
        config={
            LINE: gpiod.LineSettings(
                direction=Direction.INPUT,
            edge_detection=Edge.RISING,
            bias=Bias.PULL_UP
            )
        },
    ) as request:
        wait = True
        while wait:
            if request.wait_edge_events():
                print(request.get_value(LINE))
                time.sleep(1)
                wait = False
                if capturing == False:
                    start_capturing()
                else:
                    end_capturing()