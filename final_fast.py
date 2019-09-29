from adafruit_circuitplayground.express import cpx
# Circuit Playground Express Data Time/Light Intensity/Temp
# Log data to a spreadsheet on-screen
# Open Spreadsheet beforehand and position to start (A,1)
# Use slide switch to start and stop sensor readings
# Time values are seconds since board powered on (relative time)

import time
from digitalio import DigitalInOut, Direction, Pull
import analogio
import board
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import adafruit_thermistor

# Switch to quickly enable/disable


# light level

# temperature


# Set the keyboard object!
# Sleep for a bit to avoid a race condition on some systems
time.sleep(1)
kbd = Keyboard()
layout = KeyboardLayoutUS(kbd)  # US is only current option...

print("Time\tLight\tTemperature\tX\tY\tZ")  # Print column headers

def slow_write(string):   # Typing should not be too fast for
    for c in string:      # the computer to be able to accept
        layout.write(c)
        time.sleep(0.2)   # use 1/5 second pause between characters

while True:
    if cpx.switch:    # If the slide switch is on, don't log
        continue

    cpx.red_led = True
    x, y, z = cpx.acceleration
    R = 0
    G = 0
    B = 0
    cpx.pixels.fill(((R + abs(int(x))), (G + abs(int(y))), (B + abs(int(z)))))
    output = "%0.1f\t%d\t%0.1f\t%0.2f\t%0.2f\t%0.2f" % (time.monotonic(), cpx.light, cpx.temperature ,x,y,z)
    print(output)
    cpx.red_led = False
    if cpx.temperature>34:
        cpx.pixels.fill((255,0,0))
        cpx.play_tone(262, 1)
        cpx.play_tone(294, 1)

    # Change 0.1 to whatever time you need between readings
    #time.sleep(0.1)