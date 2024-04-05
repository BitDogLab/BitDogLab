import time
from machine import Pin

time.sleep(5)

onboard = Pin("LED", Pin.OUT, value=0)

for i in range(0, 40000):
  onboard.on()
  time.sleep(0.025)
  onboard.off()
  time.sleep(0.025)