#define kytkin 4
#define ledi 9
#include <SoftwareSerial.h>
boolean asento = 0;
boolean viimeAsento = 0;
SoftwareSerial BT(14, 16); // RX, TX

void setup() {
  BT.begin(9600);
  pinMode(kytkin, INPUT);
  pinMode(ledi, OUTPUT);
  delay(1000);
}

void loop() {
  asento = digitalRead(kytkin);
  if (asento != viimeAsento) {
    if (asento == HIGH) {
      BT.println("ON");
      digitalWrite(ledi, HIGH);
    } else {
      BT.println("OFF");
      digitalWrite(ledi, LOW);
    }
    delay(200);
  }
  viimeAsento = asento;
}
