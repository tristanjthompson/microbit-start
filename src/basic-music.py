from microbit import *
import music 

tune = ["C4:4", "D4:4", "E4:4", "C4:4", "C4:4", "D4:4", "E4:4", 
        "C4:4", "E4:4", "F4:4", "G4:8", "E4:4", "F4:4", "G4:8"]
        
tt = Image("99900:"
           "09000:"
           "00000:"
           "00999:"
           "00090")

# NB - this needs croc clips connected to headphones to work
# "0" to the bottom of the jack
# "GND" to the top of the jack
while True:
    while True:
        # while True:
        display.show("A")
        sleep(350)
        display.show("B")
        sleep(350)
        if button_a.was_pressed():
            break
        elif button_b.was_pressed():
            break
    display.show(Image.MUSIC_QUAVERS)
    # display.show(tt)
    music.play(tune)