from microbit import *

# display.scroll("Press A or B")

while True:
    display.scroll("A or B?", delay=100, wait=False, loop=True)
    while True:
        if button_a.was_pressed():
            display.show("A")
            sleep(1000)
            break
        elif button_b.was_pressed():
            display.show("B")
            sleep(1000)
            break