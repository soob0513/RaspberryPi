import picamera as pc
import time

for i in range(1,4) :
    camera = pc.PiCamera()
    camera.start_preview()    # 미리보기 
    time.sleep(5)
    camera.capture(f'image{i}.jpg')
    camera.stop_preview()
    camera.close()
    
# 선생님 풀이
camera = pc.PiCamera()
camera.start_preview()    # 미리보기 
time.sleep(5)
for i in range(3) :
    camera.capture('image{}.jpg'.format(i))
    time.sleep(1)
camera.stop_preview()
camera.close()
    
