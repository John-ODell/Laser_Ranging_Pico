# To help understand how this works visit the base example and library at
# https://github.com/kevinmcaleer/vl53l0x/blob/master/tof_test.py
from machine import Pin, I2C
from vl53l0x import VL53L0X

print("setting up i2c")
sda = Pin(0)
scl = Pin(1)
id = 0

i2c = I2C(id=id, sda=sda, scl=scl)

print(i2c.scan())
tof = VL53L0X(i2c)
 
budget = tof.measurement_timing_budget_us
print("Budget was:", budget)
tof.set_measurement_timing_budget(40000)

tof.set_Vcsel_pulse_period(tof.vcsel_period_type[0], 12)
tof.set_Vcsel_pulse_period(tof.vcsel_period_type[1], 8)

while True:
# Start ranging
    print(tof.ping()-50, "mm")