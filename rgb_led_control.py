#!/usr/bin/python

# Test program to show the use of libraries
import time
import rgb_led as RGBLED
from random import randint

def main():
  print "Setup the RGB module"
  RGBLED.rgb_setup()
  print "Switch on RGB"

  for i in range(100):
    colours = [randint(0,1) for i in range(3)]
    RGBLED.rgb_colour(colours)
    print "RED: {} GREEN: {} BLUE: {}".format(colours[0], colours[1], colours[2])
    time.sleep(1)

  RGBLED.rgb_clear()
  print "Finished"

main()
#End
