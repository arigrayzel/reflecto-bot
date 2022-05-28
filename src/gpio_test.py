import R64.GPIO as GPIO
import time

def angle_to_dc(angle):
    min_angle = 0.0
    max_angle = 180.0
    min_T = 0.0
    max_T = 10.0
    T = (max_angle-angle)/(max_angle-min_angle)*(max_T-min_T) + min_T
    return T


GPIO.setmode(GPIO.BOARD)
pin = 16
GPIO.cleanup(pin)


GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 50)

p.start(1)

while True:
    p.ChangeDutyCycle(angle_to_dc(90))
    time.sleep(1)
    '''
    for angle in range(0,180,5):
        p.ChangeDutyCycle(angle_to_dc(angle))
        time.sleep(0.2)
    for angle in range(180,0,-5):
        p.ChangeDutyCycle(angle_to_dc(angle))
        time.sleep(0.2)
'''

