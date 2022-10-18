#!/usr/bin/env python3

import time

from gpiozero import Button
from gpiozero import LED

from aiy.pins import PIN_A
from aiy.pins import LED_1

led = LED(LED_1)
button = Button(PIN_A) # , hold_time=1

print("LED on, waiting 2s...")
led.on()
time.sleep(2)
print("LED off! Waiting for button...")
led.off()

count = 0
now_pressed = 0
previously_pressed = 1
really_pressed = 0

while True:
    now_pressed = button.is_pressed
    if now_pressed == previously_pressed:
        count = count + 1
        if count == 5:
            really_pressed = now_pressed
    else:
        previously_pressed = now_pressed
        count = 0

    if really_pressed:
        print("Button pressed, LED on!")
        led.on()
    else:
        print("Button unpressed, LED off.")
        led.off()
