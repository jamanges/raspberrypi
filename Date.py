import RPi.GPIO as GPIO
import time

ledPin=11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin,GPIO.OUT)

month = int(float(time.strftime("%m")))

day = int(float(time.strftime("%d")))

while month > 0:
    global month
    GPIO.output(ledPin,GPIO.HIGH)
    time.sleep(.25)
    GPIO.output(ledPin,GPIO.LOW)
    time.sleep(.25)
    print month
    month = month - 1
 
time.sleep(2)

while day > 0:
    global day
    GPIO.output(ledPin,GPIO.HIGH)
    time.sleep(.25)
    GPIO.output(ledPin,GPIO.LOW)
    time.sleep(.25)
    print day
    day = day - 1
        
time.sleep(2)

