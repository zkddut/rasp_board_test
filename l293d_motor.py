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

def motor_configure(pin_en, pin_1a, pin_2a):
  MO_EN = pin_en
  MO_1A = pin_1a
  MO_2a = pin_2a
  GPIO.setmode(GPIO.BCM)
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

def anti_clockwise(val):
  GPIO.output(MO_1A, False)
  GPIO.output(MO_2A, True)
  GPIO.output(MO_EN, True)
  sleep(val)

def motor_stop():
  GPIO.output(MO_1A, False)
  GPIO.output(MO_2A, False)
  GPIO.output(MO_EN, False)

def main():
  print("Here we go! Press CTRL+C to exit")
  GPIO.setwarnings(False)
  GPIO.cleanup()
  motor_configure(MO_EN, MO_1A, MO_2A)
  button = Button(18)
  clock_wise_flag = 1
  try:
    while True:
      if button.is_pressed:
        print "Motor Start"
        if clock_wise_flag == 1:
          clockwise(3)
          clock_wise_flag = 0
        else:
          anti_clockwise(3)
          clock_wise_flag = 1
      else:
        motor_stop()
  except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO

if __name__=='__main__':
  main()


