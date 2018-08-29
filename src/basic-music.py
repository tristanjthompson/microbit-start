from microbit import *
import music 

from microbit import *
import music 

tune = ["C4:4", "D4:4", "E4:4", "C4:4", "C4:4", "D4:4", "E4:4", "C4:4",
"E4:4", "F4:4", "G4:8", "E4:4", "F4:4", "G4:8"]

# NB - this needs croc clips connected to headphones to work
# "0" to the bottom of the jack
# "GND" to the top of the jack
music.play(tune)