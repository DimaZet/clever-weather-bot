import os

import requests

token = os.environ['GEOCODER_TOKEN']


def prepare(address: str) -> str:
    return address  # TODO


def decode(address: str) -> [str, str]:
    return requests.get(
        url='https://geocode-maps.yandex.ru/1.x',
        params={
            'format': 'json',
            'apikey': token,
            'geocode': prepare(address)
        }
    ).json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()


if __name__ == '__main__':
    r = decode('Москва+Льва+Толстого+16')
    print(r)
