print('Importing Parts')
# Import statements for the functions used in the prediction
import csvDataGather as csv
import sqlDataHandler as sql
import weatherPredictor as wp
import arimaTrainer as at
import averager as avg
import rowMaker as row
import sys
import datetime

# Assignment of arrays and variables
print('Assigning Variables')
season = 23
progress_indicator = 0
i = 0
prevDate = 0

print('Assigning Arrays')
data = [[],[],[],[]]
forecastFinal, avgAdder = [], []
sendData = [[],[],[],[]]
avgData = [[],[],[], []]
x=0

print('Initializing Done, Starting Infinite Loop')
while True:
	# Time stamps to compare, to make sure everything runs once/day
	now = datetime.datetime.now().time()
	time = now.replace(hour=0, minute=30, second=0)
	endTime = now.replace(hour=0, minute=35,second=0)
	
	if prevDate is not datetime.datetime.today().date() and now > time and now < endTime:
		# Two empty lines and timestamp for when the loop main starts.
		# Debug use only
		print()
		print()
		print('Loop Start Recorded At: ', now)
		
		# Part of the loop to retrieve data from SQL server
		sql.DataRetreiver(data, 1)
		avg.Averaging(data, avgData)
			
		# Loop for making predictions.
		for i in range(0, 3):
			sendData[i] = wp.Prediction(avgData[i], season, i)
		
		print('Building final send data')
		sendData.append([])
		for j in range(1,15):
			sendData[3].append(datetime.datetime.today().date() + 
			datetime.timedelta(days=j))
		
		forecastFinal = row.RowMaker(sendData)
		date = datetime.datetime.strptime(avgData[3][-1], '%Y-%m-%d')
		avgAdder = [date, "%.2f" % avgData[0][-1], 
					"%.2f" % avgData[1][-1], "%.2f" % avgData[2][-1]]
		
		# Send the Data to the sql server
		print('Building Done. Sending data to SQL Server', date)
		sql.DataSender(avgAdder, 2)
		sql.DataSender(forecastFinal, 3)
		
		# Two empty lines and timestamp for when the loop main finishes.
		# Debug use only
		print()
		print()
		now = datetime.datetime.now().time()
		print('Loop Ending Recorded At:', now)
		pervDate = datetime.datetime.today().date()
