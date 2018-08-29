from microbit import *

compass_points = ["S", "S", "W", "W", "W", "N", "N", "N", "E", "E", "E", "S"]

# Start calibrating
if not compass.is_calibrated():
    display.scroll("Calibrate? A", loop=True, wait=False)

    while True:
        if button_a.was_pressed():
            compass.calibrate()
            break
        elif button_b.was_pressed():
            break
            
style = ""

display.scroll("A=Needle, B=Letter", wait=False, loop=True)
while True:
    if button_a.was_pressed():
        style = "needle"
        break
    elif button_b.was_pressed():
        style = "letter"
        break
    

# Try to keep the compass pointed in (roughly) the correct direction
while True:
    sleep(100)
    
    if style == "needle":
        needle = ((15 - compass.heading()) // 30) % 12
        display.show(Image.ALL_CLOCKS[needle])
        sleep(500)
        display.show(" ")
    else:
        compass_point = compass.heading() // 30
        display.show(compass_points[compass_point])
        
    # display.scroll(compass_point, delay=50)
    # sleep(500)