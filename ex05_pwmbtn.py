import RPi.GPIO as gp

gp.setmode(gp.BCM)
gp.setup(18, gp.OUT)
gp.setup(21, gp.IN)

check = True
cnt = 0
p = gp.PWM(18, 500)
p.start(0)

try:
    while True :
        btn = gp.input(21)
        if btn == 1 :
            if check == True :
                cnt +=1
                check = False
        else :
            check = True
        
#       if cnt %3 == 1 :
#           p.ChangeDutyCycle(50)
#       elif cnt%3 == 2 :
#           p.ChangeDutyCycle(100)
#       else :
#           p.ChangeDutyCycle(0)

        if cnt == 1:
            p.ChangeDutyCycle(50)
        elif cnt == 2 :
            p.ChangeDutyCycle(100)
        else :
            p.ChangeDutyCycle(0)
            cnt = 0;
            
except KeyboardInterrupt:
    gp.cleanup()
