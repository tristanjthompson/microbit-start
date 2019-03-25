from microbit import *
import radio
radio.on()
radio.config(channel=1)
radio.config(power=7)
waiting = "_"
display.show(waiting)

while True:
    incoming = radio.receive()
    if incoming is not None:
        display.show(incoming)
        print(incoming)
        sleep(500)
        display.show(waiting)