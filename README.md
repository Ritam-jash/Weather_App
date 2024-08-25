# Weather Application

This is a simple weather application built using Python and Flask that fetches weather data from the OpenWeatherMap API. The application allows users to get weather information by entering a city name or by using geolocation features.

## Features

- Fetch weather data by entering a city name.
- Use geolocation to fetch weather data based on the user's current location.
- Provide user feedback during the geolocation process.
- Default location feature to display weather for a predefined city if geolocation is unavailable or denied.
- Display detailed weather information, including temperature, description, humidity, and wind speed.

## Project Structure

```plaintext
weather-app/
│
├── app.py                # The main Flask application file
├── requirements.txt      # List of Python dependencies
├── templates/
│   └── base.html         # Base template for the web pages
│   └── index.html        # Main template displaying the weather data
├── static/
│   └── style.css         # Stylesheet for the application
├── README.md             # Project documentation
└── .gitignore            # Files and directories to ignore in Git