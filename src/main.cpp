#include <HX711_ADC.h>

// Pin definitions
const int HX711_dout1 = 16;
const int HX711_dout2 = 17;
const int HX711_dout3 = 4;
const int HX711_sck = 18; // Shared SCK pin

// HX711 objects
HX711_ADC LoadCell1(HX711_dout1, HX711_sck);
HX711_ADC LoadCell2(HX711_dout2, HX711_sck);
HX711_ADC LoadCell3(HX711_dout3, HX711_sck);

void setup() {
  Serial.begin(115200);
  delay(10);
  Serial.println("Starting...");

  float calibrationValue = 696.0; // Calibration value

  // Initialize each HX711
  LoadCell1.begin();
  LoadCell2.begin();
  LoadCell3.begin();

  unsigned long stabilizingtime = 2000;
  boolean _tare = true; // Perform tare (zeroing) on startup

  LoadCell1.start(stabilizingtime, _tare);
  LoadCell2.start(stabilizingtime, _tare);
  LoadCell3.start(stabilizingtime, _tare);

  if (LoadCell1.getTareTimeoutFlag() || LoadCell2.getTareTimeoutFlag() || LoadCell3.getTareTimeoutFlag()) {
    Serial.println("Timeout, check wiring and pin designations");
    while (1);
  } else {
    LoadCell1.setCalFactor(calibrationValue);
    LoadCell2.setCalFactor(calibrationValue);
    LoadCell3.setCalFactor(calibrationValue);
    Serial.println("Startup is complete");
  }
}

void loop() {
  // Update sensor data
  LoadCell1.update();
  LoadCell2.update();
  LoadCell3.update();

  // Get timestamp
  unsigned long timestamp = millis();

  // Prepare the data string in CSV format
  String data = String(timestamp) + ", " +
                String(LoadCell1.getData()) + "," +
                String(LoadCell2.getData()) + "," +
                String(LoadCell3.getData())+ ";";

  // Print the data to the Serial Monitor
  Serial.println(data);

  // Short delay to avoid overwhelming the serial output
  delay(1);
}
