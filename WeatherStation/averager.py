# Simple averaging function, which averages the data from one day
# and saves it to a new array

def Averaging(data, avgData):
	temp = []
	j=0

	for i in range(0, 3):
		for r in range(0, len(data[i])):
			temp.append(data[i][r])
			if j == 24:
				avg = sum(temp)/24
				avgData[i].append(avg)
				avgData[3].append(data[3][r])
				temp = []
				j=0
			j = j+1
	return avgData
