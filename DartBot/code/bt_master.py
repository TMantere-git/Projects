import serial
import timeport = serial.Serial("/dev/rfcomm0", baudrate=9600)
 
# reading and writing data from and to arduino serially.                                      
# rfcomm0 -> this could be differentwhile True:
	
	rcv = port.readline()
	if rcv:
	   print(rcv)

	#   sudo rfcomm connect hci0 AA:BB:CC:DD:EE:FF (osoite)
