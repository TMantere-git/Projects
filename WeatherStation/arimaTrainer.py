from pmdarima.arima import auto_arima
import matplotlib.pyplot as plt

# Local arrays used
train, test, x = [],[], []

def modelTraining(data, season, pointer):
	print('Data Received, Training')
	
	# This runs all possible ARIMA combinations until the most fitting
	# is found
	s_model = auto_arima(data, start_p=1, start_q=1, max_p=3, max_q=3,
						 m=season, start_P=0, seasonal=True, d=1, D=1, 
						 trace=True, error_action='ignore', 
						 suppress_warnings=True, stepwise=True)
						 
	print('Training Done')
	
	# Here the function writes the arima model to .txt file
	with open('Output'+ str(pointer) +'.txt', 'w') as txt_file:
		txt_file.write(str(s_model))
