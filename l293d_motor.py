#!/usr/bin/python
import RPi.GPIO as GPIO
from gpiozero import LED, Button
from time import sleep

# Use L293D Chip to Control a motor
# Use BCM GPIO mode
# GPIO 5 -> 1,2E
# GPIO 6 -> 1A
# GPIO 13 -> 2A

MO_EN = 5
MO_1A = 6
MO_2A = 13

def motor_configure(en, 1a, 2a):
  MO_EN = en
  MO_1A = 1a
  MO_2a = 2a
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  button = Button(18)
  GPIO.setup(MO_EN, GPIO.OUT)
  GPIO.setup(MO_1A, GPIO.OUT)
  GPIO.setup(MO_2A, GPIO.OUT)
  mo_en = GPIO.PWM(MO_EN, 100)
  mo_en.start(0)

def motor_strength(stre):
  mo_en.ChangeDutyCycle(stre)

def clockwise(val):
  GPIO.output(MO_1A, True)
  GPIO.output(MO_2A, False)
  GPIO.output(MO_EN, True)
  sleep(val)

def anticlockwise():
  GPIO.output(MO_1A, False)
  GPIO.output(MO_2A, True)
  GPIO.output(MO_EN, True)
  sleep(val)

def motor_stop():
  GPIO.output(MO_1A, False)
  GPIO.output(MO_2A, False)
  GPIO.output(MO_EN, False)

print("Here we go! Press CTRL+C to exit")
motor_strength(50)
try:
  while True:
    if button.is_pressed:
      print "Motor Start"
      clockwise(3)
    else:
      motor_stop()
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
  GPIO.cleanup() # cleanup all GPIO

if __name__=='__main__':
  main()


