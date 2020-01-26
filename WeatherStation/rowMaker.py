# Simple function to create neat little rows for use in MySQL functions.
# Each row contains one point of data for each type and timestamp.

returnData = []

def RowMaker(data):
	for x in range(0, len(data[0])):
		temp1 = float(data[0][x])
		temp2 = float(data[1][x])
		temp3 = float(data[2][x])
		temp4 = data[3][x]
		row = [temp4, "%.2f" % temp1, "%.2f" % temp2, "%.2f" % temp3]
		returnData.append(row)
	return returnData
