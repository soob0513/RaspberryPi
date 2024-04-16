import picamera as pc

with pc.PiCamera() as camera :  # -> 마지막에 close() 안 적어도 됨 
# ==> camera = pc.Picamera()  -> 마지막에 close() 적어주어야 함 
    camera.resolution = (640, 480)
    camera.start_preview()
    camera.start_recording('video.h264')
    camera.wait_recording(5)
    camera.stop_recording()
    camera.stop_preview()