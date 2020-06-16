from microbit import *
import radio
radio.config(length=50, channel=44)
radio.on()

bat = pin2.read_analog()
bat_volt = int(bat * 642 / 1023)
display.scroll("B" + str(bat_volt))

message = str(bat_volt)
radio.send(message)









