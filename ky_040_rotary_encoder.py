#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
import threading

class Ky040RotaryEncoder:
  def __init__(self, name):
    self.name = name
    self.is_alive = False
    self.stop_event = threading.Event()
    self.rotary_pos = 0
    # Use ky-040 as rotary_encoder input
    # Use BCM GPIO mode
    # CLK/A -> 12
    # DT/B -> 16
    self.ro_a = 12
    self.ro_b = 16
    self.rotary_run = threading.Thread(target=self.rotary_running)

  def encoder_configure(self, ro_a, ro_b, set_pos):
    self.ro_a = ro_a
    self.ro_b = ro_b
    self.rotary_pos = set_pos
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.ro_a, GPIO.IN)
    GPIO.setup(self.ro_b, GPIO.IN)

  def curr_pos(self):
    return (self.rotary_pos)

  def set_pos(self, pos):
    self.rotary_pos = pos

  def rotary_running(self):
    aLastState = GPIO.input(self.ro_a)
    while True:
      aState = GPIO.input(self.ro_a)
      if (aState != aLastState):
        if (GPIO.input(self.ro_b) != aState):
          self.rotary_pos += 1
        else:
          self.rotary_pos -= 1
      aLastState = aState
      if (self.stop_event.isSet()):
        self.is_alive = False
        self.stop_event.clear()
        break

  def start_rotary(self):
    if (not self.is_alive):
      self.is_alive = True
      self.rotary_run.start()

  def stop_rotary(self):
    self.stop_event.set()
    self.rotary_run.join()

def main():
  print("Here we go! Press CTRL+C to exit")
  GPIO.setwarnings(False)
  GPIO.cleanup()

  rotary_encoder = Ky040RotaryEncoder("myRotary")
  rotary_encoder.encoder_configure(12, 16, 0)

  rotary_encoder.start_rotary()

  for i in range(10):
    sleep(1)
    print("Curr Pos: ", rotary_encoder.curr_pos())

  rotary_encoder.stop_rotary()
  print("rotary stop running: {}".format(rotary_encoder.is_alive))

if __name__=='__main__':
  main()
