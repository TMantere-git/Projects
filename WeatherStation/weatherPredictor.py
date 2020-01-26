import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

def Prediction(data, season, pointer):
	# Locally used arrays and variables.
	test, train, x, tempData = [], [], [], []
	h = 13
	
	print('Training Done, modelling')
	
	# Assign correct ARIMA model based on the data given.
	# This is achieved by reading the pointer, given by the main part
	# of the code
	if pointer == 0:
		order1 = (2, 1, 1)
		order2 = (2, 1, 2, season)
		
	elif pointer == 1:
		order1 = (1, 1, 2)
		order2 = (1, 1, 1, season)
		
	elif pointer == 2:
		order1 = (2, 1, 1)
		order2 = (0, 1, 1, season)
	
	# Save model into a variable, using orders given above.
	# Additional rules available, but not needed for current use
	model = sm.tsa.SARIMAX(data, order=order1,
						   seasonal_order=order2,
						   enforce_invertibility=False, 
						   enforce_stationarity=False)
	

	print('Model Done, Predicting')
	
	# Fit the model, and make a prediction from data.
	# The length of prediction array is changed by changeing variable h
	model_fit = model.fit(disp = False)
	output = model_fit.predict(start = len(data), end = len(data)+h)
	
	print('Prediction Done, Output = ', output)
	return output
