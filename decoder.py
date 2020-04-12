import os

import requests

token = os.environ['GEOCODER_TOKEN']


def prepare(address: str) -> str:
    return address  # TODO


def decode(address: str) -> dict:
    resp = requests.get(
        url='https://geocode-maps.yandex.ru/1.x',
        params={
            'format': 'json',
            'apikey': token,
            'geocode': prepare(address)
        }
    ).json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    pos = [float(x) for x in resp.split()]
    return {'lon': pos[0], 'lat': pos[1]}


if __name__ == '__main__':
    r = decode('Москва+Льва+Толстого+16')
    print(r['lon'], r['lat'])
