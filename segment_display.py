#!/usr/bin/env python
#================================================
#
#       Drive 7-segment-display with 74HC595.
#
#       You need 3 control pin for this driver using configure() method
#       Call display(digit=[0-9], dp=[0,1]) to effect output
#
#=================================================

import RPi.GPIO as GPIO
from time import sleep

class SegmentDisplay:
  def __init__(self, name):
    self.name = name
    self.digit = None
    self.dp = None
    # Serial data input pin
    self.ds = None
    # Time sequence input of storage register. On the rising edge, data in the shift register moves into memory register.
    self.st_cp = None
    # Time sequence input of shift register. On the rising edge, the data in shift register moves successively one bit, i.e. data in Q1 moves to Q2, and so forth. While on the falling edge, the data in shift register remain unchanged.
    self.sh_cp = None
    self.display_map = {
        #pin  g,f,e,d,c,b,a
        None:(0,0,0,0,0,0,0),
        0   :(0,1,1,1,1,1,1),
        1   :(0,0,0,0,1,1,0),
        2   :(1,0,1,1,0,1,1),
        3   :(1,0,0,1,1,1,1),
        4   :(1,1,0,0,1,1,0),
        5   :(1,1,0,1,1,0,1),
        6   :(1,1,1,1,1,0,0),
        7   :(0,0,0,0,1,1,1),
        8   :(1,1,1,1,1,1,1),
        9   :(1,1,0,0,1,1,1)
    }

  def configure(self, ds, st_cp, sh_cp):
    self.ds = ds
    self.st_cp = st_cp
    self.sh_cp = sh_cp
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.ds, GPIO.OUT)
    GPIO.setup(self.st_cp, GPIO.OUT)
    GPIO.setup(self.sh_cp, GPIO.OUT)
    GPIO.output(self.ds, GPIO.LOW)
    GPIO.output(self.st_cp, GPIO.LOW)
    GPIO.output(self.sh_cp, GPIO.LOW)

  def convert_to_hc595_input(self):
    if (self.digit >= 0 and self.digit <= 9):
      valid_digit = self.digit
    else:
      valid_digit = None
    display_value = list(self.display_map[valid_digit])
    if (self.dp == 1):
      display_value.insert(0,1)
    else:
      display_value.insert(0,0)
    return (display_value)

  def hc595_shift_in(self, dat):
    # shift in the data to hc595
    for bit in range(0, 8):
      GPIO.output(self.ds, dat[bit])
      GPIO.output(self.sh_cp, GPIO.HIGH)
      sleep(0.001)
      GPIO.output(self.sh_cp, GPIO.LOW)

  def hc595_out(self):
    GPIO.output(self.st_cp, GPIO.HIGH)
    sleep(0.001)
    GPIO.output(self.st_cp, GPIO.LOW)

  def display(self, digit, dp):
    self.digit = digit
    self.dp = dp
    self.hc595_shift_in(self.convert_to_hc595_input())
    self.hc595_out()

  def reset(self):
    self.hc595_shift_in([0,0,0,0,0,0,0,0])
    self.__init__(self.name)
    self.hc595_out
    GPIO.cleanup()

def main():
  print("Here we go! Press CTRL+C to exit")
  GPIO.setwarnings(False)
  GPIO.cleanup()

  seg_display = SegmentDisplay("mySegDisplay")
  seg_display.configure(12, 16, 20)

  for i in range(10):
    seg_display.display(i, 0)
    print("Display Value: ", i)
    sleep(1)
  seg_display.display(None, 1)
  print("Display dp")
  sleep(1)
  seg_display.reset()

if __name__=='__main__':
  main()
