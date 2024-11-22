Laser Ranging Pico by John O'Dell

!!!!CAUTION!!! THIS SKETCH IS FOR 18+ OR ADULT SUPERVISION

THIS SKETCH INCLUDES USING LASERS. NEVER POINT A LASER AT ANOTHER PERSON, AND ALWAYS USE EYE PROTECTION WHEN WORKER WITH LASERS, NO MATTER THE SIZE. https://www.osha.gov/laser-hazards/hazards

I AM NOT RESPONSIBLE FOR ANY INJURY, DAMAGE, OR LOSS THAT MAY OCCUR FROM THE USE OF THIS PROJECT. USE AT YOUR OWN RISK.

Thank You and huge kudos to https://github.com/kevinmcaleer/vl53l0x for the vl53l0x library and base example.

Items need

    - Raspberry Pi Pico 2
    - vl53lxx Time-of-Flight Module
    - Laser Module
    - .96 OLED screen
    - Touch sensor
        - OR a button/input sensor
    - Thonny IDE https://thonny.org/

vl53lxx Module 

Pin Outs (Dedicated Pins)

    SDA -> GPIO 1
    SCL/SCK -> GPIO 0
    VCC -> 3.3v
    GND -> GND
    (only pins needed)

Save the example "vl53l0x.py" to your device (named respectivly) L not one/1

Open the example "tof_test" and press the green arrows

    In your serial shell you will see in mm the distance return

Troubleshooting

    - Make sure you have the right pins
    - Don't use the other pins on the module
    - Use the GPIO 0 and GPIO 1 
    - It is not being covered, there must be an open line of sight

Laser Module

Pin Outs (Non-Dedicated)

    S -> GPIO 26 
    VCC -> 3.3v
    GND -> GND

Open the example "laser_module" and press the green arrow

    The laser will turn on and off every other second.
        - press the red stop sign while the laser in the off time to stop
        - or run "laser_off.py"
            - change to laser.on() for the opposite

Troubleshooting

    - make sure the wires are correct
    - you have enough power for your laser module

.96 OLED Screen
Save the example "ssd1306.py" to your device (named respectivly) 

Pin Outs (Dedicated pins)
    SDA -> GPIO 2
    SCL/SCK -> GPIO 3
    VCC -> 3.3v
    GND -> GND

Open the example "oled_init.py" and press the green arrows

    - on the oled screen "hello world" should be displayed

Troubleshooting

    - Make sure your sda and scl/sck pins are not mixed
    - You are in I2C 1 not 0
        - for a bad SCL pin error run "screen_scan.py"

Touch Sensor (If you do not have one, replace with a button or another type of input sensor)

Pin Outs (Non Dedicated)

    IO -> GPIO 16
    VCC -> 3.3v
    GND -> GND

Open the example "touch_module.py" and press the green arrow

    - on the serial shell it will print when the button is pressed or not at a high sample rate
    - touch on the front and back to understand the sensitivity
    - if not using a a touch module, make sure you get a bool a value

Troubleshooting

    - Make sure you have not switched the ground and vcc
    - GPIO 16 is the 10th down on the left side (facing the usb port)
    - change the sleep time if needed for a non touch model


----- Laser Ranger Pico -----

Open the example "laser_ranger.py" and press the green arrow

    - to have this run on boot, rename the example to "boot.py" when saving to the device
    - you must have saved the two provided files to your device
        - ssd1306.py
        - vl53l0x.py (L not one/1)
    - The distance is shown in feet and inches in real time and printed to the OLED screen with the laser guiding to what is being measured
    - Pressing the touch module (or choice of input sensor) will stop the measurment at what is currently being measured
    - Pressing the touch module again will restart the real time measurement.

Troubleshooting

    - The laser is for guiding and not part of the ranging module, the accuracy will depend on your callibration
    - There is a sleep time on the button of 1 second (time.sleep(1)). This causes a small delay between presses and what is shown on the OLED screen, feel free to change this.
    - The ranging module measures in mm, feel free to change the conversions
    - /n does not create a new line, observe the code to write new text to the screen
    
Please contact me with any questions or comments.