import csv

# CSV handler function which opens a file and saves its contents to an
# array.
kosteus, lampo, paine, kello, paiva = [],[],[],[],[]

def DataGather(tempData):
	# Path to the CSV file
	path = 'PATH-TO-FILE'
	
	# Open the CSV file, and select encoding if necessary
	with open(path + 'csv-1d86b714-353e-437e-a0de-9660eae7a0c4.csv', 'r') as f:
		reader = csv.reader(f, quoting=csv.QUOTE_ALL)
		
		# For loop to save the contents of the file to appropriate
		# arrays
		for row in reader:
			paiva.append(str(row[0]) + '-' + str(row[1]) + 
						 '-' + str(row[2]))
			kello.append(row[3])
			try:
				paine.append(float(row[4]))
				kosteus.append(float(row[5]))
				lampo.append(float(row[6]))
			except:
				continue
			row_print = [paiva[-1], kello[-1], lampo[-1], paine[-1], kosteus[-1]]
			tempData.append(row_print)
		
		# Return arrays
		return tempData
