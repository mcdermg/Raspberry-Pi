from picamera import PiCamera
from time import sleep
print("debug1")
camera = PiCamera()
print("debug2")
camera.start_preview()
print("debug3")
sleep(10)
print("debug4")
camera.stop_preview()
print("debug5")
