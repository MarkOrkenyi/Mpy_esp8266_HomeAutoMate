def checkoled():
    oled.fill(1)
    oled.show()
    time.sleep_ms(500)
    oled.fill(0)
    oled.show()
    oled.text(".",0,0)
    oled.text(".",128,64)
    oled.show()
def text(text,posx,posy):
    oled.text(text,posx,posy)
def fill(value):
    oled.fill(value)
def show():
    oled.show()
def currenttime():
    rtc = machine.RTC()
    oled.text("Current time is: {}:{}:{}".format(rtc.datetime()[4],rtc.datetime()[5],rtc.datetime()[6]))
import time
import ssd1306
import machine
i2c = machine.I2C(-1, machine.Pin(5), machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
print("Display initialized")


