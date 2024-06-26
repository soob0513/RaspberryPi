# 초음파 센서 
import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
trig = 23
echo = 24
gp.setup(trig, gp.OUT)
gp.setup(echo, gp.IN)


try :
    while True :
        gp.output(trig, gp.LOW)
        time.sleep(0.5)
        gp.output(trig, gp.HIGH)
        time.sleep(0.0001)
        gp.output(trig, gp.LOW)
        while gp.input(echo) == 0:
            start = time.time()        # 현재 시간 출력
        while gp.input(echo) == 1:
            end = time.time()
        duration = end - start
        distance = duration * 34000/2    # 초음파 센서 나누기 2
        distance = round(distance, 2)
        print(f'Distance : {distance}cm')

except KeyboardInterrupt:
    gp.cleanup()