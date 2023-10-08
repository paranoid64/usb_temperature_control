# exsample for Hive OS
# This script turn on the miner on

#pip3 install pyserial

import json
import serial
import time
import subprocess
import os, signal

ser = serial.Serial('/dev/ttyUSB0', 9600)
miner_status = 1 #the miner starts automatically in hive os, so there must be 1 here.

turn_on = 18 #°C
turn_off = 22 #°C

while (True):
    if (ser.inWaiting() > 0):

        time.sleep(0.5)
        data = (ser.readline().decode('ascii')).strip("\r\n")

        #{"Celsius":"30.37","Fahrenheit":"86.68"}
        #print(data)

        if data:
            temperatur = 0

            try:
                json_str = json.loads(data)
                temperatur = int(float(json_str["Celsius"]))

                if temperatur > turn_off and miner_status == 1:
                    miner_status=0
                    print(f'temperatur is {temperatur} °C, turn off miner now')
                    print ("hiveos miner stop")
                    subprocess.check_call(['miner', 'stop'])

                if temperatur <= turn_on and miner_status == 0:
                    miner_status=1
                    print(f'temperatur is {temperatur} °C, turn on miner now')
                    print ("hiveos miner start")
                    subprocess.check_call(['miner', 'start'])

            except Exception as e:
                print(e)
                pass

ser.close()
