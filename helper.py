from decoder import Decoder
from forecasting import Weather


class Helper:
    decoder = Decoder()
    weather = Weather()

    def complex_forecast_on_tomorrow(self, address: str) -> str:
        coords = self.decoder.decode(address)
        forecast = self.weather.get_weather(**coords)
        return "avg temperature is {}, feels like {}".format(forecast['temp_avg'], forecast['feels_like'])


if __name__ == "__main__":
    r = Helper().complex_forecast_on_tomorrow('Москва Льва Толстого 16')
    print(r)
