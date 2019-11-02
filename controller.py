from time import sleep
from gpiozero import CPUTemperature
import RPi.GPIO as GPIO

pin = 18 # The pin ID, edit here to change it
toggleON = 60 # The temperature in Celsius after which we turn on the fan
toggleOFF = 50 # The temperature in Celsius after which we turn off the fan

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setwarnings(False)
    return()
def getCPUTemp():
    cpuTemp = CPUTemperature().temperature
    return cpuTemp
def fan(on):
    GPIO.output(pin, on)
    return()
def checkTemp():
    cpuTemp = getCPUTemp()
    #print cpuTemp
    if cpuTemp>toggleON:
        fan(True)
    elif cpuTemp < toggleOFF:
        fan(False)
    return()
try:
    setup()
    while True:
        checkTemp()
        sleep(5) # Read the temperature every 5 sec, increase or decrease this limit if you want
except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt
    GPIO.cleanup() # resets all GPIO ports used by this program