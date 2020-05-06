import RPi.GPIO as GPIO
from gpiozero import LED, Button
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
button = Button(18)

print("Here we go! Press CTRL+C to exit")
led = GPIO.PWM(17, 50)  # channel=17 frequency=50Hz
try:
  while True:
    if button.is_pressed:
      led.start(0)
      for dc in range(0, 101, 5):
          led.ChangeDutyCycle(dc)
          sleep(0.1)
      for dc in range(100, -1, -5):
          led.ChangeDutyCycle(dc)
          sleep(0.1)
    else:
      led.stop()
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
  GPIO.cleanup() # cleanup all GPIO


