import RPi.GPIO as GPIO 
import time

POWER_PIN = 11
PIN = 7
LATENCY =  1                                    # needs to be at least 1 to work
interval = 1
POWER_DELAY = 1

DEBUG = False

GPIO.setwarnings(DEBUG)

GPIO.setmode(GPIO.BOARD)                        ## Use board pin numbering 

GPIO.setup(PIN, GPIO.OUT)                   ## Setup GPIO Pin PIN to OUT 
GPIO.setup(POWER_PIN, GPIO.OUT)             ## Setup GPIO Pin PIN to OUT 

output = False

### Sets power #############################
def power (mode):
    GPIO.output(POWER_PIN, mode) 
    time.sleep(POWER_DELAY)

def power_off ():
    if DEBUG:
        print("Powering OFF")
    power(False)

def power_on ():
    if DEBUG:
        print("Powering ON")
    power(True) 

def power_cycle ():
    power_off()
    power_on()


### Sets light level from 0 to 3 ###########
def setlevel(level):
    level = min(level, 3)
    level = max(level, 0)

    if DEBUG:
        print("Setting power ", level)

    power_cycle()
    for i in range(level):
        if DEBUG:
            print("Tap")
        GPIO.output(PIN, True) 
        time.sleep(LATENCY/2)
        GPIO.output(PIN, False) 
        time.sleep(LATENCY/2)

    if level > 0:
        GPIO.output(PIN, True) 
    time.sleep(LATENCY)

    return


### MAIN TEST LOOP ###
def test ():
    print("Testing...")

    power_off()
    while True: 
        power_on()              # turn on

        if DEBUG:
            print("OFF")
        setlevel(0)
        time.sleep(interval) 

        if DEBUG:
            print("LEVEL 1")
        setlevel(1)
        time.sleep(interval) 

        if DEBUG:
            print("LEVEL 2")
        setlevel(2)
        time.sleep(interval) 

        if DEBUG:
            print("LEVEL 3")
        setlevel(3)
        time.sleep(interval) 

        if DEBUG:
            print("LEVEL 2")
        setlevel(2)
        time.sleep(interval) 

        if DEBUG:
            print("LEVEL 1")
        setlevel(1)
        time.sleep(interval) 

        power_off()             # turn off
        time.sleep(5) 

if __name__ == '__main__':
    test()
