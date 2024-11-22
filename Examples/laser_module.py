from machine import Pin
import time

# Initialize laser pin
laser = Pin(26, Pin.OUT)

while True:
    laser.on()
    print("Laser on")
    time.sleep(1)
    laser.off()
    print("Laser off")
    time.sleep(1)
