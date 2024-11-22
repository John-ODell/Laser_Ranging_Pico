from machine import Pin
import time

# Initialize laser pin
laser = Pin(26, Pin.OUT)

while True:
    laser.off()
    print("Laser off")
