import os

import requests


class Weather:

    def __init__(self):
        self.__token__ = os.environ['WEATHER_TOKEN']

    def get_weather(self, lat: float = 0, lon: float = 0, offset: int = 1) -> (int, int):
        r = requests.get(
            url='https://api.weather.yandex.ru/v1/forecast',
            params={
                'lat': lat,
                'lon': lon
            },
            headers={
                'X-Yandex-API-Key': self.__token__
            }
        )
        day = r.json()['forecasts'][offset]['parts']['day']
        return day['temp_avg'], day['feels_like']


if __name__ == '__main__':
    avg, feels = Weather().get_weather(55.45, 37.37, 1)
    print(avg, feels)
