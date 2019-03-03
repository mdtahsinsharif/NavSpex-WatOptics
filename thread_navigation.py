import sys
import os
sys.path.insert(0, os.getcwd() + '/Software/WatOptics_firmware/hardware_testing/barcode-scanner')
import barcode_scanner_video


def thread_navigate():
    barcode_scanner_video.scan_barcode();
    