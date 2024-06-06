#include <MQ135.h>

// Create an instance of the MQ135 sensor
MQ135 mq135(A0);

// Set your fresh air baseline (Sensor Zero)
const int sensorZero = 400;

// Set the threshold for flame detection (adjust as needed)
const float flameThreshold = 500; // Example threshold value

void setup() {
    Serial.begin(115200);
}

void loop() {
    // Read the raw sensor value
    int co2read = analogRead(A0);

    // Print the CO2 value to the serial monitor
    Serial.print("CO2 (PPM): ");
    Serial.println(co2read);

    // Check if CO2 concentration exceeds the flame threshold
    if (co2read > flameThreshold) {
        Serial.println("Fire detected!");
        
    }else{ Serial.println("No Fire detected!");
      }

    delay(2000);
}
