#pip install pyserial

import json
import serial
import time
import subprocess
import os, signal

ser = serial.Serial('/dev/ttyUSB0', 9600)
miner_status = 0
xmrig = "/home/mlausch/xmrig"

def kill(task):

    try:
        # iterating through each instance of the process
        for line in os.popen("ps ax | grep " + task + " | grep -v grep"):
            fields = line.split()

            # extracting Process ID from the output
            pid = fields[0]

            # terminating process
            os.kill(int(pid), signal.SIGKILL)
        print("Process Successfully terminated")
    except:
        print("Error Encountered while running script")

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

                if temperatur > 22 and miner_status == 1:
                    miner_status=0
                    print(f'temperatur is {temperatur} °C, turn off miner now')
                    print ("hiveos miner stop")
                    kill("xmrig.sh")
                    kill("xmrig")
                    subprocess.check_call(['miner', 'stop'])

                if temperatur <= 18 and miner_status == 0:
                    miner_status=1
                    print(f'temperatur is {temperatur} °C, turn on miner now')
                    print ("hiveos miner start")
                    subprocess.check_call(['miner', 'start'])
                    subprocess.Popen(['sh', 'xmrig.sh' ], cwd = xmrig)


            except Exception as e:
                print(e)
                pass


ser.close()
