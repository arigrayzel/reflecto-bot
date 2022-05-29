import time
import R64.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)


enable_pin = 18
coil_A_1_pin = 3
coil_A_2_pin = 5
coil_B_1_pin = 15
coil_B_2_pin = 16

pins = [enable_pin, coil_A_1_pin, coil_A_2_pin, coil_B_1_pin, coil_B_2_pin]
drive_pins = [coil_A_1_pin, coil_A_2_pin, coil_B_1_pin, coil_B_2_pin]
GPIO.setup(pins, GPIO.OUT)

def forward(delay, steps):
    i=0
    while i in range(0, steps):
        setStep(drive_pins, [1,0,1,0])
        time.sleep(delay)
        setStep(drive_pins, [0,1,1,0])
        time.sleep(delay)
        setStep(drive_pins, [0,1,0,1])
        time.sleep(delay)
        setStep(drive_pins, [1,0,0,1])
        time.sleep(delay)
        i += 1

def backwards(delay, steps):
    i=0
    while i in range(0, steps):
        setStep(drive_pins, [1,0,0,1])
        time.sleep(delay)
        setStep(drive_pins, [0,1,0,1])
        time.sleep(delay)
        setStep(drive_pins, [0,1,1,0])
        time.sleep(delay)
        setStep(drive_pins, [1,0,1,0])
        time.sleep(delay)
        i += 1

def setStep(pins, states):
    for i in range(len(pins)):
        GPIO.output(pins[i], states[i])
    

if __name__ == "__main__":
    GPIO.output(enable_pin, GPIO.HIGH)
    while True:
        forward(0.0,3000)
        print("steps executed!")
        time.sleep(2)
