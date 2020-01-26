#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include <MySQL_Connection.h>
#include <MySQL_Cursor.h>
#include <ESP8266WiFi.h>
#include <NTPClient.h>
#include <WiFiUdp.h>

Adafruit_BME280 bme;

const long utcOffset = 7200;

float temperature, pressure, humidity;
int hours, minutes, seconds;

bool state = 1;

WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "europe.pool.ntp.org", utcOffset);

WiFiClient client;
MySQL_Connection conn((Client *)&client);

IPAddress server_addr();  // IP of the MySQL *server* here
char mysqluser[] = " ";              // MySQL user login username
char mysqlpassword[] = " ";        // MySQL user login password
const char *ssid =  " ";     // replace with your wifi ssid and wpa2 key
const char *pass =  " ";

char INSERT_SQL[] = "INSERT INTO projekti.Device1 (Temp1,AirP1,Humid1) VALUES ('%.1f', '%.1f', '%.0f')";
char query[128];

void setup() {
  Serial.begin(115200);
  
  unsigned status;
  
  
  WiFi.begin(ssid, pass); 
       while (WiFi.status() != WL_CONNECTED) 
          {
            delay(500);
            Serial.print(".");
          }
      Serial.println("");
      Serial.println("WiFi connected");
      
      status = bme.begin(0x76);  
          if (!status) {
            Serial.println("Sensoria ei löydy");
            Serial.print("SensorID: 0x"); 
            Serial.println(bme.sensorID(),16);
            while (1);
            }
            
  while (!Serial); // wait for serial port to connect
  Serial.println("Connecting...");
  if (conn.connect(server_addr, 3306, mysqluser, mysqlpassword)) {
    delay(1000);
  }
  else {
    Serial.println("Connection failed.");
    }
  timeClient.begin();
}

void loop() {

  while(!timeClient.update()) {
    timeClient.forceUpdate();
  }

  hours = timeClient.getHours();
  minutes = timeClient.getMinutes();
  seconds = timeClient.getSeconds();

  if(state == 1) {
    if(minutes < 5) {

      temperature = bme.readTemperature();
      pressure = bme.readPressure() / 100.0F;
      humidity = bme.readHumidity();

      sprintf(query, INSERT_SQL, temperature, pressure, humidity);
      
      MySQL_Cursor *cur_mem = new MySQL_Cursor(&conn);
  
      cur_mem->execute(query);
      Serial.println(query);
      Serial.print(hours);
      Serial.print(":");
      Serial.print(minutes);
      Serial.print(":");
      Serial.println(seconds);
      
      delete cur_mem;

      state = 0;
    }
  }
  if (minutes > 5)
  {
    state = 1;
  }

  //Serial.println(timeClient.getFormattedTime());*/

  delay(5000);

}
