#!/usr/bin/python
from __future__ import division
import RPi.GPIO as GPIO
import time
import signal
import datetime
import os
from subprocess import check_output, call, Popen
from config import *
import spidev



def draw_icon(layer, icon):
    Popen(PNGVIEWPATH + "/pngview -b 0 -l " + layer + " -x " + str(ICONX) + " -y " + str(ICONY) + " " + ICONPATH + "/" + icon + " &", cwd=os.path.dirname(os.path.realpath(__file__)), shell=True)

def change_icon(percent):
    if (ICON != 1):
        return

    draw_icon("3000" + percent, "battery" + percent + ".png")

    if (DEBUGMSG == 1):
        print("Changed battery icon to " + percent + "%")

    out = check_output("ps aux | grep pngview | awk '{ print $2 }'", shell=True)
    nums = out.split('\n')
    i = 0

    for num in nums:
        i += 1
        if (i == 1):
            call("sudo kill " + num, shell=True)
def end_process(signalnum = None, handler = None):
    GPIO.cleanup()
    call("sudo killall pngview", shell=True);
    exit(0)
    
signal.signal(signal.SIGTERM, end_process)
signal.signal(signal.SIGINT, end_process)

def bitstring(n):
    s = bin(n)[2:]
    return '0'*(8-len(s)) + s

##Read the value from the voltage divider using the MCP3002
##The value from here is multplied by 5 which is the number of resistors in the voltage divider and it should give you a number between 2 and 3 after multiplying
def read_it(adc_channel=0, spi_channel=0):
    conn = spidev.SpiDev(0, spi_channel)
    conn.max_speed_hz = 1200000 #1.2MHz
    cmd = 128
    if adc_channel:
        cmd +=32
    reply_bytes = conn.xfer2([cmd, 0])
    reply_bitstring = ''.join(bitstring(n) for n in reply_bytes)
    reply = reply_bitstring[5:15]
    return int(reply, 2) / 2**10

while True:
    m = 0
    for x in range(10):
       # y=read_it()
    
        x = read_it()
        time.sleep(0.1)
    #    print(x)
        m = m+ x
     
    avg = m/10
    ret = avg * 16.5
    #print((round(avg * 16.5, 2)))    
    status = 0

    ADC100 = 13.00
    ADC75 = 12.30
    ADC50 = 11.60
    ADC25 = 10.90
    ADC0 = 10.20

    draw_icon("299999", "blank.png")

    count = 0

    print (round(ret, 2))
    
    if (ret < ADC0):
        if (status != 0):
            change_icon("0")
            #change_led("red")

        status = 0
    elif (ret < ADC25):
        if (status != 25):
           # change_led("red")
            change_icon("25")

        status = 25
    elif (ret < ADC50):
        if (status != 50):
           # change_led("green")
            change_icon("50")

        status = 50
    elif (ret < ADC75):
        if (status != 75):
            #change_led("green")
            change_icon("75")

        status = 75
    else:
        if (status != 100):
           # change_led("green")
            change_icon("100")

        status = 100

    count += 1
    time.sleep(REFRESHRATE)


    

"""if __name__ == '__main__':
    while True:
        trial()"""