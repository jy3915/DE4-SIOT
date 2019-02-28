#include <M5Stack.h>
#include "DHT12.h"
#include <Wire.h>     //The DHT12 uses I2C comunication.
DHT12 dht12;          //Preset scale CELSIUS and ID 0x5c.

void setup() {
  M5.begin();
  Wire.begin();
}

void loop() {
  //Read temperature with preset scale.
  M5.Lcd.print("Temperatura: ");
  Serial.print(dht12.readTemperature());
  M5.Lcd.print(dht12.readTemperature());

  delay(3600000);
}
