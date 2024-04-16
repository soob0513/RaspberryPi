import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
gp.setup(18, gp.OUT)
gp.setup(19, gp.OUT)
gp.setup(20, gp.OUT)

try :
    while True :
        gp.output(18, 1)
        time.sleep(0.5)
        gp.output(18,0)
        time.sleep(0.5)
        gp.output(19, 1)
        time.sleep(0.5)
        gp.output(19,0)
        time.sleep(0.5)
        gp.output(20, 1)
        time.sleep(0.5)
        gp.output(20,0)
        time.sleep(0.5)
except KeyboardInterrupt:
    gp.cleanup()