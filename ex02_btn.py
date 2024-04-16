import RPi.GPIO as gp

gp.setmode(gp.BCM)
gp.setup(21, gp.IN)
gp.setup(18, gp.OUT)

# try:
#     while True:
#         btn = gp.input(21)
#         print(btn)
# except KeyboardInterrupt :
#     gp.cleanup()

try:
    while True :
        # gp.output(18, gp.LOW)
        btn = gp.input(21)
        # gp.output(18, btn)
        
        if btn == 1 :
            gp.output(18, gp.HIGH)
            print(btn)
        else :
            gp.output(18, gp.LOW)
            print(btn)
    
except KeyboardInterrupt:
    gp.cleanup()