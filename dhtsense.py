import dht
import machine
import oled
import time


def temp():
    d.measure()
    return d.temperature()


def humid():
    d.measure()
    return d.humidity()


def displaytemp(temp, hum):
    t = str(temp)
    h = str(hum)
    oled.fill(0)
    oled.text(t, 0, 0)
    oled.text(h, 0, 10)
    oled.show()


def write_file_temp_hum():
    temperature = str(temp())
    time.sleep_ms(200)
    humidity = str(humid())
    data = []
    data.append(temperature)
    data.append(humidity)
    print(data)
    time.sleep_ms(200)
    displaytemp(temperature, humidity)
    time.sleep_ms(200)
    with open("dhtdata.txt", "w") as datafile:
        datafile.write("Temperature: {}\nHumidity: {}".format(data[0], data[1]))


d = dht.DHT22(machine.Pin(14))
print("dhtsense imported")
