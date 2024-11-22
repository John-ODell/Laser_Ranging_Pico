from machine import Pin, I2C
import time
import vl53l0x
import ssd1306

# Initialize I2C for VL53L0X and OLED (Dedicated Pins)
i2c_tof = I2C(0, scl=Pin(1), sda=Pin(0))
i2c_oled = I2C(1, scl=Pin(3), sda=Pin(2))

# Initialize VL53L0X
sensor = vl53l0x.VL53L0X(i2c_tof)

# Initialize OLED display
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c_oled)

# Initialize touch sensor pin
touch = Pin(16, Pin.IN)

# Initialize laser pin
laser = Pin(26, Pin.OUT)
laser.on() 

def display_message(lines):
    oled.fill(0)
    for i, line in enumerate(lines):
        oled.text(line, 0, i * 10)
    oled.show()

# Main loop observe how diplay_message is written 
running = True
paused_distance = 0
while True:
    if touch.value() == 1:
        running = not running
        if not running:
            paused_distance = sensor.read() * 0.00328084  # Ft conversion
            paused_distance_inches = sensor.read() * 0.0393701  # Inch Conversion
            display_message([
                "Distance",
                "Measured at",
                "{:.2f} ft".format(paused_distance),
                "{:.2f} in".format(paused_distance_inches)
            ])
        time.sleep(1) # Touch/Button Delay of 1 Second

    if running:
        distance = sensor.read() * 0.00328084 #ft conversion
        distance_inches = sensor.read() * 0.0393701 #Inch Conversion
        display_message([
            "Distance: {:.2f} ft".format(distance),
            "Distance: {:.2f} in".format(distance_inches)
        ])

    time.sleep(0.1)
