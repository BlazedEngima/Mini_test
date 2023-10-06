import config # Secret file that stores api_key
import datetime
import requests
from collections import defaultdict

api_key = config.api_key

# Function to use the geocode API call from openweather map to get lat, lon of cities
def getGeoCode(city):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}'

    response = requests.get(url)

    if response.status_code != 200:
        print('Error fetching city lat lon')
        return

    try:
        data = response.json()
    except ValueError:
        raise ValueError('No JSON returned')

    if not data:
        raise ValueError('No content in JSON data')

    lat = data[0]['lat']
    lon = data[0]['lon']

    return lat, lon


# Function to get transform a string with the current date to a datetime object
def getDay(date):
    return datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

# Helper function to print out dictionary value in a proper string format
def print_dict(data):
    for key, value in data.items():
        date = key.strftime('%a, %d %b %Y')
        print(f'{date}: {value:.2f}\xb0C')

# Driver code
if __name__ == "__main__":
    # Get proper city and units 
    city = 'Jakarta'
    units = 'metric'

    # Get lat, lon of the city
    lat, lon = getGeoCode(city)

    # Query the openweathermap api to get the weather data forecast for the next 5 days in 3 hour intervals
    url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={units}&appid={api_key}'
    response = requests.get(url)

    # Error handling
    if response.status_code != 200:
        print('Error fetching weather data')

    data = response.json()

    # Storage for temperature and day counts
    temp_avg = defaultdict(lambda: 0)
    counter = defaultdict(lambda: 0)

    # Add temperature of the same days (excluding today) 
    for time in data['list']:
        day = getDay(time['dt_txt'])

        if day.weekday() == datetime.date.today().weekday():
            continue

        temp = time['main']['temp']

        counter[day.date()] += 1
        temp_avg[day.date()] += temp
        
    
    # Get the temperature average
    for key in temp_avg.keys():
        temp_avg[key] /= counter[key]

    # Print the result
    print('Weather Forecast:')
    print_dict(temp_avg)
