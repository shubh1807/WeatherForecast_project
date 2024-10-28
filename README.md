# Weather Forecasting Application

This is a Django web application that predicts average temperature forecasts for a specified number of days using an ARIMA model.

## Features
- Input the number of days for the temperature forecast.
- Displays the forecast in a table and graph format.

## Setup Instructions
1. Clone the repository.
2. Install dependencies using Pipenv.
3. Run the Django server using python manage.py runserver command

## Forecasting Model
This app uses an ARIMA model which is trained on time series data.
Basically, We had temperature data with static behavior, and a ARIMA model is well-suited for this kind of data to be trained on
we have achieved a PDW value by using auto ARIMA function.


