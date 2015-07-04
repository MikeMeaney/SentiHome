# Import stuff for the LCD
import time
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI
import Image
import ImageDraw
import ImageFont

# Import stuff for Hue Lifx

from phue import Bridge	##The Hue Api
import lifx ##The LIFX Api

# Make Connections to and pool Hue / lifx
# Create LIFX Connection
xLights = lifx.Lifx()

#Create Hue Connection
b = Bridge('192.168.0.45')
hLights = b.get_light_objects()
hGroups = b.get_group()

#Prime the display
# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))
disp.begin(contrast=40)
# Clear display.
disp.clear()
disp.display()

image = Image.new('1',(LCD.LCDWIDTH, LCD.LCDHEIGHT))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

# Draw a white filled box to clear the image.
draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)

i = 0;
for lh in hLights:
    print(lh.name)
    draw.text((0,i*10), lh.name, font=font)
    i += 1
    disp.image(image)
    disp.display()
