# USB Temperature Control

## Description
An Arduino NANO that outputs the current temperature as JSON in Celsius and Fahrenheit via USB-Seria.
This JSON can then be used in another programming language for your own projects. E.g. if it is 24° C in the room, the PC should shut down.

This is an example of what a JSON looks like:

```
{"Celsius":"30.37","Fahrenheit":"86.68"}
```

## Install Firmeware to Arduino NANO
Download this projekt folder and extract to e.g.: /home/user/Desktop/usb_temp_control
Now run the Arduino IDE and open usb_temp_control.ino

Install the DallasTemperature Lib from Arduino IDE -> tools -> library

Now you have to set the board at Tools to Arduino Nano and at port your COM1 port or at Linux mostly /dev/ttyUSB0
There are 2 bootloaders, one old and one new. You have to try out which bootloader is the right one.

Click the Verify button and than the Upload button.

## Connect hardware
I use a DS18B20 with cable. You should also use the 4.7 K ohm resistor.
Please google how to connect the dalles.
It is important that you either connect the data pin to D4 or if it is a different digital pin, this must be changed in the variable SENSOR_PIN.

I use a display from a Gotek floppy emulator. But this is optional. no display is necessary.

Clock pin is D3
DIO is D2

## 3D printer data
is in the folder "3D_Printer_Files"
As program is used SketchUp.
