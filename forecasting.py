from decoder import DecoderClient
from weather import WeatherClient


class ForecastingService:
    decoder = DecoderClient()
    weather = WeatherClient()

    def complex_forecast_on_tomorrow(self, address: str) -> dict:
        coords = self.decoder.decode(address)
        forecast = self.weather.get_weather(**coords)
        c = forecast['condition']
        if self.__is_rainy__(c):
            forecast['take'] = 'umbrella'
        elif self.__is_snowy__(c):
            forecast['take'] = 'mittens'
        elif self.__is_sunny__(c):
            forecast['take'] = 'hat'
        else:
            forecast['take'] = 'good mood'
        return forecast

    @staticmethod
    def __is_rainy__(condition: str) -> bool:
        return condition in ['partly-cloudy-and-light-rain',
                             'partly-cloudy-and-rain',
                             'overcast-and-rain',
                             'overcast-thunderstorms-with-rain',
                             'cloudy-and-light-rain',
                             'overcast-and-light-rain',
                             'cloudy-and-rain',
                             'overcast-and-wet-snow']

    @staticmethod
    def __is_snowy__(condition: str) -> bool:
        return condition in ['partly-cloudy-and-light-snow',
                             'partly-cloudy-and-snow',
                             'overcast-and-snow',
                             'cloudy-and-light-snow',
                             'overcast-and-light-snow',
                             'cloudy-and-snow']

    @staticmethod
    def __is_sunny__(condition: str) -> bool:
        return condition in ['clear']


if __name__ == "__main__":
    r = ForecastingService().complex_forecast_on_tomorrow('Москва Льва Толстого 16')
    print(r)
