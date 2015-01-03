import RPi.GPIO as GPIO
import time


Code = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}
ledPin=11
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)

def dot():
    GPIO.output(ledPin,GPIO.HIGH)
    time.sleep(.2)
    GPIO.output(ledPin,GPIO.LOW)
    time.sleep(.2)

def dash():
    GPIO.output(ledPin,GPIO.HIGH)
    time.sleep(.5)
    GPIO.output(ledPin,GPIO.LOW)
    time.sleep(.2)
    
while True:
    input = raw_input('What would you like to encode? ')
    encoded = ""
    for letter in input:
        for code in Code[letter.upper()]:
            if code == '-':
                dash()
                encoded+=code
            elif code == '.':
                dot()
                encoded+=code
            else:
                time.sleep(.7)
                encoded+=code
    print encoded
        
