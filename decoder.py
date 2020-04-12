import os

import requests


class DecoderClient:

    def __init__(self):
        self.__token__ = os.environ['GEOCODER_TOKEN']

    def __prepare__(self, address: str) -> str:
        return address  # TODO

    def decode(self, address: str) -> dict:
        resp = requests.get(
            url='https://geocode-maps.yandex.ru/1.x',
            params={
                'format': 'json',
                'apikey': self.__token__,
                'geocode': self.__prepare__(address)
            }
        ).json()

        if resp['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData']['found'] == '0':
            raise ValueError('wrong address')

        point = resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        pos = [float(x) for x in point.split()]
        return {'lon': pos[0], 'lat': pos[1]}


if __name__ == '__main__':
    r = DecoderClient().decode('Москва+Льва+Толстого+16')
    print(r['lon'], r['lat'])
