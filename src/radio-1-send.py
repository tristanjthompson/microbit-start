from microbit import *
import radio
radio.on()
radio.config(channel=1)
radio.config(power=7)
josh_name = "A A A"
tristan_name = "B B B"
info = "AB"

display.show(info, wait=False, loop=True)
while True:
        if button_a.was_pressed():
            radio.send(josh_name)
            display.scroll("Sent")
            display.show(info, wait=False, loop=True)
        
        if button_b.was_pressed():
            radio.send(tristan_name)
            display.scroll("Sent")
            display.show(info, wait=False, loop=True)