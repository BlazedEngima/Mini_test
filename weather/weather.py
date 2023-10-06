import config
import datetime
import requests
from collections import defaultdict

api_key = config.api_key


def getGeoCode(city):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}'

    response = requests.get(url)

    if response.status_code != 200:
        print('Error fetching city lat lon')
        return

    data = response.json()
    lat = data[0]['lat']
    lon = data[0]['lon']

    return lat, lon

def getDay(date):
    return datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

def print_dict(data):
    for key, value in data.items():
        date = key.strftime('%a, %d %b %Y')
        print(f'{date}: {value:.2f}\xb0C')

if __name__ == "__main__":
    city = 'Jakarta'
    count = 5
    units = 'metric'

    lat, lon = getGeoCode(city)

    url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={units}&appid={api_key}'
    response = requests.get(url)

    if response.status_code != 200:
        print('Error fetching weather data')

    data = response.json()

    temp_avg = defaultdict(lambda: 0)
    counter = defaultdict(lambda: 0)

    for time in data['list']:
        day = getDay(time['dt_txt'])

        if day.weekday() == datetime.date.today().weekday():
            continue

        temp = time['main']['temp']

        counter[day.date()] += 1
        temp_avg[day.date()] += temp
        
    
    for key in temp_avg.keys():
        temp_avg[key] /= counter[key]

    print('Weather Forecast:')
    print_dict(temp_avg)
