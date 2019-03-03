import sys
import os
sys.path.insert(0, os.getcwd() + '/Software/WatOptics_firmware/hardware_testing/barcode-scanner')
import barcode_scanner_video
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2

def thread_navigate():
    barcode_scanner_video.scan_barcode();
    