import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import datetime

def DataRetreiver(wtData, pointer):
	try:
		print('Retreiving Data')
		connection = mysql.connector.connect(host=ADDRESS,
						     database='db',
						     user='user',
						     password='password')

		if pointer == 1:
			mySql_insert_query = """SELECT * FROM Historical"""
			cursor = connection.cursor()
			cursor.execute(mySql_insert_query)
			records = cursor.fetchall()
		
			for row in records:
				wtData[0].append(row[3])
				wtData[1].append(row[4])
				wtData[2].append(row[5])
				wtData[3].append(row[1])
		
		if pointer == 2:
			mySql_insert_query = """SELECT idDevice2, DATE(Date2), 
			HOUR(Date2), DATE(Date3), HOUR(Date3), Temp2, Temp3, AirP2, 
			AirP3, Humid2, Humid3 FROM Device2 JOIN 
			Device3 on Device2.idDevice2 = Device3.idDevice3
            ORDER BY idDevice2 DESC LIMIT 1"""
			
			cursor = connection.cursor()
			cursor.execute(mySql_insert_query)
			records = cursor.fetchall()
		
			for row in records:
				wtData[0].append(row[0])
				wtData[1].append(row[1])
				wtData[2].append(row[2])
				wtData[3].append(row[3])
				wtData[4].append(row[4])
				wtData[5].append(row[5])
				wtData[6].append(row[6])
				wtData[7].append(row[7])
				wtData[8].append(row[8])
				wtData[9].append(row[9])
				wtData[10].append(row[10])
				#wtData[11].append(row[11])
		
		return wtData

	except mysql.connector.Error as error:
		print("Failed to retreive record ".format(error))

	finally:
		if (connection.is_connected()):
			connection.close()
			cursor.close()
			print('Data Retreived')
			print("MySQL connection is closed")
			
			
def DataSender(data, indicator):
	try:
		connection = mysql.connector.connect(host=ADDRESS,
						     database='db',
						     user='user',
						     password='password')
		
		if indicator == 1:
			for row in data:
				mySql_insert_query = """INSERT INTO Historical  
									  (Date, Time, TempH, AirPH, HumidH) 
									   VALUES (%s, %s, %s, %s, %s) """
				records_to_insert = [(row[0], row[1], 
									  row[2], row[3], row[4])]
				

				cursor = connection.cursor()
				cursor.executemany(mySql_insert_query, records_to_insert)
				connection.commit()

		if indicator == 2:
			mySql_insert_query = """INSERT INTO HistoricalWeb  
								   (Date, Temp, AirP, Humid) 
								   VALUES (%s, %s, %s, %s) """
			records_to_insert = [(data[0], data[1], data[2], data[3])]
			
			cursor = connection.cursor()
			cursor.executemany(mySql_insert_query, records_to_insert)
			connection.commit()

		if indicator == 3:
			for row in data:
				mySql_insert_query = """INSERT INTO Ennuste  
									   (Date, Temp, AirP, Humid) 
									   VALUES (%s, %s, %s, %s) """
				records_to_insert = [(row[0], row[1],
									  row[2], row[3])]

				cursor = connection.cursor()
				cursor.executemany(mySql_insert_query, records_to_insert)
				connection.commit()
		
		if indicator == 4:
			mySql_insert_query = """INSERT INTO Current  
								   (Date, CurTemp, CurAirP, CurAirHumid) 
								   VALUES (%s, %s, %s, %s) """
			records_to_insert = [(datetime.datetime.today(), data[0],
								  data[1], data[2])]

			cursor = connection.cursor()
			cursor.executemany(mySql_insert_query, records_to_insert)
			connection.commit()
			
			mySql_insert_query = """INSERT INTO Historical  
								   (Date, Time, TempH, AirPH, HumidH) 
								   VALUES (%s, %s, %s, %s, %s) """
			records_to_insert = [(datetime.datetime.now().date(),
								  datetime.datetime.now().time(),
								  data[0], data[1], data[2])]

			cursor = connection.cursor()
			cursor.executemany(mySql_insert_query, records_to_insert)
			connection.commit()

	except mysql.connector.Error as error:
		print("Failed to insert record to table {}".format(error))

	finally:
		if (connection.is_connected()):
			cursor.close()
			connection.close()
			print("MySQL connection is closed")
