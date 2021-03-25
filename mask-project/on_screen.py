import cv2
from mss import mss
import numpy as np
from PIL import Image
from maskdetector import MaskDetector

sct = mss()
mon = {'top': 0, 'left': 0, 'width': 1200, 'height': 800}

def get_screen_frame():
    raw = np.array(sct.grab(mon))
    cvt = cv2.cvtColor(raw, cv2.COLOR_BGRA2BGR)
    return cvt


detector = MaskDetector()

detector.set_input_capture(get_screen_frame)
detector.loop()