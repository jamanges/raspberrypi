import RPi.GPIO as GPIO
import time
import pywapi

bluePin = 15
greenPin = 12
redPin = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)

weather = pywapi.get_weather_from_weather_com('47401')

temp = int(weather['current_conditions']['feels_like'])

print temp

while True:
    input = raw_input('Zip Code: ')
    weather = pywapi.get_weather_from_weather_com(input)
    temp = int(weather['current_conditions']['feels_like'])
    print temp
    if temp <= 5:
        GPIO.output(bluePin,GPIO.HIGH)
        time.sleep(.9)
        GPIO.output(bluePin,GPIO.LOW)
    elif temp <= 13:
        GPIO.output(greenPin,GPIO.HIGH)
        time.sleep(.9)
        GPIO.output(greenPin,GPIO.LOW)
    else:
        GPIO.output(redPin,GPIO.HIGH)
        time.sleep(.9)
        GPIO.output(redPin,GPIO.LOW)
    
