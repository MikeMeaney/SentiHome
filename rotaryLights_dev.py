# Test script for selecting and toggling lights via rotary encoder
# Mike Meaney 2015

#Import stuff for the rotary encoder
import gaugette.rotary_encoder
import gaugette.switch

#Declare the pins for the rotary encoder
A_PIN  = 27
B_PIN  = 28
SW_PIN = 29

#Initiate the rotary encoder's worker
encoder = gaugette.rotary_encoder.RotaryEncoder.Worker(A_PIN, B_PIN)
encoder.start()
switch = gaugette.switch.Switch(SW_PIN)
last_state = None
clicks = 0
realClicks = 0

# Import stuff for Hue Lifx

from phue import Bridge ##The Hue Api
import lifx ##The LIFX Api

# Make Connections to and pool Hue / lifx
# Create LIFX Connection
#xLights = lifx.Lifx()

#Create Hue Connection
b = Bridge('192.168.0.45')
hLights = b.get_light_objects()
hGroups = b.get_group()

for hl in hLights:
    print (hl.name)

totalHues = len(hLights)
print ("Hue Lights" , totalHues)

#Do this stuff, for like, forever...
while True:
    delta = encoder.get_delta()
    

    if delta!=0:
#        print ("rotate %d " % delta)
        clicks += delta
        print (realClicks)
#        print (clicks)
#	print (clicks % 4)
	if clicks % 4 == 0:
#		print ("DERP, THAT'S ONE CLICK REALLY!!")
            realClicks = clicks /4
            print("-------------")
            print (realClicks)
            if realClicks >=totalHues or realClicks <= ~totalHues:
            	print("totalHues", totalHues)
            	print(realClicks)
            	realClicks = -1
            	clicks = -1
        print(hLights[realClicks].name)
        print("---------------")
	

    sw_state = switch.get_state()
    if sw_state != last_state:
        print ("switch %d" % sw_state)
        last_state = sw_state




