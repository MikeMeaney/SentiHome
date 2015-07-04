# Mike Meaney 2015 calitexaco.com
# sentiHome All On / Off Demo
print("------------  sentiHome Every Thing Button --------------")
from phue import Bridge	##The Hue Api
import lifx ##The LIFX Api
import RPi.GPIO as GPIO # GPIO Api
from time import sleep

outPin = 18
inPin = 13
toggle = False

# Config GPIOs
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(outPin, GPIO.OUT)
GPIO.setup(inPin, GPIO.IN)
GPIO.output(outPin,0)

# Config PWM pin
pwm = GPIO.PWM(18, 100)
pwm.start(0)

# Create LIFX Connection
xLights = lifx.Lifx()

#Create Hue Connection
b = Bridge('192.168.0.45')
hLights = b.get_light_objects()

# Print the LifX Lights
print('--- LIFX ---')
print(xLights)

print('--- HUE ----')
for lh in hLights:
	print(lh)

def allHueOff(h): # Pass in Hue Lights Array

    for hl in h:
        hl.on = False
    print("All off")

    for x in range(0,100):
        pwm.ChangeDutyCycle(x)
        sleep(0.01)
        
def allHueOn(h): # Pass in Hue Lights Array    

    for hl in h:
        hl.on = True
        hl.brightness = 254
        hl.hue = 15000
    print("All on")
    
    for x in range(0,101):
        pwm.ChangeDutyCycle(100-x)
        sleep(0.01)

while True:
    GPIO.wait_for_edge(inPin, GPIO.FALLING)
    print("Button Pressed")
    
    if toggle == True:
        allHueOn(hLights)
        toggle = False
        print("Toggle False")
    else:
        allHueOff(hLights)
        toggle = True
        print("Toggle True")
 
        GPIO.wait_for_edge(inPin, GPIO.RISING)
        print("Button Released")
GPIO.cleanup()
