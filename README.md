# Projects

Here is a compilation of projects I have been part of.

### ![1. Dartbot](DartBot)

Dartbot is a device that uses OpenGL to track a target and shoot a dart on it at a right distance. The target is taught to it using Haar Cascade. For moving it uses 4 DC motors, for target acquiring 2 servo motors, and for shooting the dart 2 dc motors and a solenoid. At a heart of the device lies a Raspberry Pi 3b and for camera it uses a regular Raspberry Pi camera.

Dartbot was part of a Amazing Robots competition hosted by Finnish TIETOTEKNIIKAN JA ELEKTRONIIKAN SEURA or SOCIETY OF INFORMATION TECHNOLOGY AND ELECTRONICS in which the robot came on the 4th position out of 10 competitors.

[Link to a News article about the competition](https://www.mikrobitti.fi/neuvot/robotit-kisasivat-messukeskuksessa-10-000-euron-voittopotti-tuli-ylivertaisella-teknisella-toteutuksella/60490a0f-0bc4-4c8e-a108-126306718576) (only in Finnish)

![Dartbot](/DartBot/Dartbot.png)

Picture of the Device


### ![2. Weatherstation](/Weatherstation)

Weatherstation is simple multidevice weather monitoring system. It uses multiple similar stations that are made of Adafruit Feather Huzzah ESP8266 boards with bme280 sensors to measure temperature, air pressure and air humidity. These measurements are then uploaded on a mySQL database every hour where they can be accessed by a website showing the data in raw form as well as in a graph.

Station-program runs on linux server that is self built, configurated and managed. On the server program does averaging of the measurements and a prediction of the weather using SARIMA model.


![WeatherStation](/WeatherStation/WeatherStation.png)
Website layout

### ![3. Snake Game](/SnakeGame)

Basic snake type game using c#. To run the program run SnakeGame.exe from SnakeGame/bin/Release/publish/

Aim of the project was to learn some basic game-programming on C#

### ![4. TankkaajaPro](/TankkaajaPro)

TankkaajaPro is a self made android application to track car fueling statistics like kilometers driven, gas price, etc.
Application is done using dart and kotlin.
Application uses python api on a self made server to add and read data from mySQL database.

The aim of the project was to learn how to do android programming.

### 5 More to come...
