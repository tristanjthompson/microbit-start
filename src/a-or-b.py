from microbit import *

display.scroll("Press A or B")

while True:
    if button_a.was_pressed():
        display.show("A")
        sleep(1000)
    elif button_b.was_pressed():
        display.show("B")
        sleep(1000)
    
    display.show("?")