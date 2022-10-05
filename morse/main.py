from machine import Pin
import utime
led = Pin(25, Pin.OUT)

morseCode={' ': '/', 'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}

def flash(on,off):
    led.high()
    utime.sleep(on)
    led.low()
    utime.sleep(off)
    
def flashMorse(morseMsg):
    for i in morseMsg:
        if (i=="."):
            flash(0.1,0.1)
        if (i=="-"):
            flash(0.4,0.1)
        if (i=="/"):
            utime.sleep(0.8)
        if (i==" "):
            utime.sleep(0.4)
            
def strToMorse(msg):
    morse=""
    for i in msg.lower():
        morse+=morseCode[i]+" "
    return(morse)

msg="hello world"
morseMsg=strToMorse(msg)

while True:
    flashMorse(morseMsg)
    utime.sleep(3)

