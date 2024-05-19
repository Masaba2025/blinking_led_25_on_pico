from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)

number = 0

while True:
    sleep(1)
    led.toggle()
    print("10 times {} is {}".format(number, 10*number))
    number = number + 1
    sleep(1)