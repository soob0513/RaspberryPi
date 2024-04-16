import RPi.GPIO as gp

gp.setmode(gp.BCM)
gp.setup(18, gp.OUT)

def led_on():
    gp.output(18, gp.HIGH)
    
def led_off() :
    gp.output(18, gp.HIGH)
    
def led_clean() :
    gp.cleanup()