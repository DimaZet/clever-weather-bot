from decoderclient import DecoderClient
from forecasting import WeatherClient


class ForecastingService:
    decoder = DecoderClient()
    weather = WeatherClient()

    def complex_forecast_on_tomorrow(self, address: str) -> str:
        coords = self.decoder.decode(address)
        forecast = self.weather.get_weather(**coords)
        return "avg temperature is {}, feels like {}".format(forecast['temp_avg'], forecast['feels_like'])


if __name__ == "__main__":
    r = ForecastingService().complex_forecast_on_tomorrow('Москва Льва Толстого 16')
    print(r)
