# Import the SQL data handler
import sqlDataHandler as sql

# Assign variables
data = [[], [], [], [], [], [], [], [], [], [], []]
avgs = []
prevID = 0

while True:
	# Retrieve the data from the SQL server
	sql.DataRetreiver(data, 2)
	print(data)
	# If statements to check if averaging is needed
	# and that all data is current
	if prevID is not data[0][0]:
		if data[1][0] == data[3][0]:
			if data[1][0] == data[3][0]:
				# Averaging Statements
				avgTemp = (data[5][0] + data[6][0])/2
				avgAirP = (data[7][0] + data[8][0])/2
				avgHumid = (data[9][0] + data[10][0])/2
				
				# Assign the data to send
				# and send it with SQL data handler
				avgs = [avgTemp, avgAirP, avgHumid]
				sql.DataSender(avgs, 4)
				
				# Assign new value for prevID to make sure no duplicates
				# are sent
				prevID = data[0][0]

	# Reset all values and debug print
	avgs = []
	data = [[], [], [], [], [], [], [], [], [], [], []]
	print('Waiting for new data')
