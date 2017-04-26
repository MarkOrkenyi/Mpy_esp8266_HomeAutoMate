# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
import gc
import webrepl


def connectwifi(SSID="codecool-student", Password="student@ccess2015"):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, Password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


def disable_AP():
    import network
    ap = network.WLAN(network.AP_IF)
    ap.active(False)


disable_AP()
webrepl.start()
gc.collect()


print('Enter "connectwifi(SSID,Password)" to connect to another network')
