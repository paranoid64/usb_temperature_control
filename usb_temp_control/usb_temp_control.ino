#include "TM1651.h"
#include <OneWire.h>
#include <DallasTemperature.h>

#define SENSOR_PIN 4 // the pin number connected to the DS18B20 data pin

#define CLK 3//pins definitions for TM1651 and can be changed to other ports       
#define DIO 2

TM1651 Display(CLK,DIO);

OneWire oneWire(SENSOR_PIN);         // setup a oneWire instance
DallasTemperature tempSensor(&oneWire); // pass oneWire to DallasTemperature library

float tempCelsius;    // temperature in Celsius
float tempFahrenheit; // temperature in Fahrenheit

void setup()
{
  Serial.begin(9600); // initialize serial
  tempSensor.begin(); // initialize the sensor
  Display.displaySet(2);//BRIGHT_TYPICAL = 2,BRIGHT_DARKEST = 0,BRIGHTEST = 7;
}
void loop()
{
 temp();
}

void temp()
{
  tempSensor.requestTemperatures();             // send the command to get temperatures
  tempCelsius = tempSensor.getTempCByIndex(0);  // read temperature in Celsius
  tempFahrenheit = tempCelsius * 9 / 5 + 32; // convert Celsius to Fahrenheit

  if(tempCelsius < 10){
    Display.displayNum(0, 0);
    Display.displayNum(1, tempCelsius);
    Display.displayNum(2, 17); // upper zero as °C
  } else if(tempCelsius < 100) {
    unsigned num = tempCelsius;
    unsigned e = num%10; //einer
    unsigned z = num/10; //zehner
    Display.displayNum(0, z);
    Display.displayNum(1, e);
    Display.displayNum(2, 17); // upper zero as °C
  } else {
    Display.displayInteger(tempCelsius);
  }

  //output json
  Serial.print("{\"Celsius\":\"");
  Serial.print(tempCelsius);
  Serial.print("\",");

  Serial.print("\"Fahrenheit\":\"");
  Serial.print(tempFahrenheit);
  Serial.print("\"");
  Serial.println("}");

  delay(500);
}
