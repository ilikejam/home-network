# Copyright (c) 2017 Adafruit Industries
# Author: Tony DiCola & James DeVito
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!

import sys
import time
import subprocess

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

class Display:
    def __init__(self):
        # Create the I2C interface.
        i2c = busio.I2C(SCL, SDA)
        
        # Create the SSD1306 OLED class.
        # The first two parameters are the pixel width and pixel height.  Change these
        # to the right size for your display!
        disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
        
        # Clear display.
        disp.fill(0)
        disp.show()
        self.disp = disp
    
        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        self.width = disp.width
        self.height = disp.height
        self.image = Image.new('1', (self.width, self.height))
    
        # Get drawing object to draw on image.
        self.draw = ImageDraw.Draw(self.image)
    
        # Draw some shapes.
        # First define some constants to allow easy resizing of shapes.
        self.padding = 0
    
        self.back=0
        self.fore=127

    def display(self, message):
        print("Got message: " + message)
        sys.stdout.flush()
        fontpath = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
        fontsize = 28
        font = ImageFont.truetype(fontpath, fontsize)
        while (font.getsize(message)[0] > 128 or font.getsize(message)[1] > 32) and fontsize > 9:
            fontsize -= 1
            font = ImageFont.truetype(fontpath, fontsize)
        
        # Draw a black filled box to clear the image.
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=self.back)
        self.draw.text((0, self.padding+0), message, font=font, fill=self.fore)
        
        # Display image.
        self.disp.image(self.image)
        self.disp.show()
