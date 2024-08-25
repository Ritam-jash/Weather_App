from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)


API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Default location: New York City coordinates
DEFAULT_LAT = '40.7128'
DEFAULT_LON = '-74.0060'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None

    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            params = {
                'q': city,
                'appid': API_KEY,
                'units': 'metric'  # For Celsius
            }
            response = requests.get(BASE_URL, params=params)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                weather_data = {'error': 'City not found'}

    # Handle geolocation-based weather fetching
    elif request.args.get('lat') and request.args.get('lon'):
        latitude = request.args.get('lat', DEFAULT_LAT)
        longitude = request.args.get('lon', DEFAULT_LON)

        params = {
            'lat': latitude,
            'lon': longitude,
            'appid': API_KEY,
            'units': 'metric'  # For Celsius
        }
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {'error': 'Location not found'}

    # Fallback to default location if no parameters are provided
    else:
        params = {
            'lat': DEFAULT_LAT,
            'lon': DEFAULT_LON,
            'appid': API_KEY,
            'units': 'metric'  # For Celsius
        }
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {'error': 'Location not found'}

    return render_template('index.html', weather=weather_data)


if __name__ == '__main__':
    app.run(debug=True)

    