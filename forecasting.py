import os

import requests

token = os.environ['WEATHER_TOKEN']


def get_weather(lat: float, lon: float, offset: int) -> (int, int):
    day = requests.get(
        url='https://api.weather.yandex.ru/v1/forecast',
        params={
            'lat': lat,
            'lon': lon
        },
        headers={
            'X-Yandex-API-Key': token
        }
    ).json()['forecasts'][offset]['day']['day']
    return day['temp_avg'], day['feels_like']


if __name__ == '__main__':
    avg, feels = get_weather(55.45, 37.37, 1)
    print(avg, feels)
