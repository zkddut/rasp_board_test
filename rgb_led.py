#!/usr/bin/python
import time
import RPi.GPIO as GPIO
from time import sleep

# RGB LED Module (TEST)

#Setup Active states
#Common Cathode RGB-LEDs (Cathode=Active Low)
LED_ENABLE = 0
LED_DISABLE = 1
RGB_ENABLE = 1
RGB_DISABLE = 0

#RGB CONFIG - Set GPIO Ports
RGB_RED = 17
RGB_GREEN = 27
RGB_BLUE = 22
RGB = [RGB_RED,RGB_GREEN,RGB_BLUE]
RGB_LED = []

def rgb_setup():
  #Set up the wiring
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)

  # Setup Ports
  for val in RGB:
    GPIO.setup(val, GPIO.OUT)
    RGB_LED.append(GPIO.PWM(val, 50))

def rgb_activate(colour):
  GPIO.output(colour, RGB_ENABLE)

def rgb_deactivate(colour):
  GPIO.output(colour, RGB_DISABLE)

def rgb_clear():
  for val in RGB:
    GPIO.output(val, RGB_DISABLE)
  for led in RGB_LED:
    led.stop()

def rgb_colour(colours):
  for colour, value in enumerate(colours):
    RGB_LED[colour].start(0)
    RGB_LED[colour].ChangeDutyCycle(value)

def main():
  rgb_setup()
  rgb_clear()
  rgb_activate(RGB_GREEN)
  rgb_activate(RGB_BLUE)
  time.sleep(3)
  rgb_clear()
  GPIO.cleanup()

if __name__=='__main__':
  main()
#End
