from django.shortcuts import render

# forecast/views.py

import pickle
import joblib
from django.shortcuts import render
import pandas as pd

# Load the model once so it's available for all requests
with open('forecast/model/arima_model.pkl', 'rb') as model_file:
    model = joblib.load(model_file)

def home(request):
    return render(request, 'forecast/home.html')  # Display input form

def forecast(request):
    if request.method == 'POST':
        days = int(request.POST['days'])  # Retrieve days input from form
        
        # Generate forecast using the ARIMA model
        forecast_values = model.forecast(steps=days)
        
        # Prepare data for rendering in table and chart
        forecast_df = pd.DataFrame({
            'Day': range(1, days + 1),
            'Forecast': forecast_values
        })
        
        table_data = forecast_df.to_dict('records')  # Convert to table format
        chart_data = {
            'days': forecast_df['Day'].tolist(),
            'forecast_values': forecast_df['Forecast'].tolist()
        }
        
        return render(request, 'forecast/result.html', {
            'days': days,
            'forecast_data': table_data,
            'chart_data': chart_data
        })
