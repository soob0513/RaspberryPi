# 한 번 누르면 켜지고 다시 한 번 누르면 꺼지는 led 만들기 
import RPi.GPIO as gp

gp.setmode(gp.BCM)
gp.setup(18, gp.OUT)
gp.setup(21, gp.IN)

check = True
cnt = 0

try :
    while True : 
        btn = gp.input(21)
        if btn == 1:
            if check == True :
                cnt+=1
                check = False
        else :
            check = True
        
#       if cnt%2 == 1 :
#           gp.output(18, gp.HIGH)
#       else if cnt%2 == 0 :
#           gp.output(18, gp.LOW)

        gp.output(18, cnt%2)
        
except KeyboardInterrupt:
    gp.cleanup()
    