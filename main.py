from oled import *
from dhtsense import *


def blinkled():
    from machine import Pin
    import time
    blueled = Pin(2, Pin.OUT)
    for i in range(3):
        blueled.high()
        time.sleep_ms(100)
        blueled.low()
        time.sleep_ms(100)
        blueled.high()


def start_ftp():
    import uftpd


blinkled()
start_ftp()
