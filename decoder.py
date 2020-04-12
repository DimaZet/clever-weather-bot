import os

import requests


class Decoder:

    def __init__(self):
        self.token = os.environ['GEOCODER_TOKEN']

    def __prepare__(self, address: str) -> str:
        return address  # TODO

    def decode(self, address: str) -> dict:
        resp = requests.get(
            url='https://geocode-maps.yandex.ru/1.x',
            params={
                'format': 'json',
                'apikey': self.token,
                'geocode': self.__prepare__(address)
            }
        ).json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        pos = [float(x) for x in resp.split()]
        return {'lon': pos[0], 'lat': pos[1]}


if __name__ == '__main__':
    r = Decoder().decode('Москва+Льва+Толстого+16')
    print(r['lon'], r['lat'])
