from machine import Pin
import time

# Initialize touch module pin
touch = Pin(16, Pin.IN)

while True:
    if touch.value() == 1:
        print("Touch detected")
    else:
        print("No touch detected")
    time.sleep(0.1)
