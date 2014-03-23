# -*- coding:utf8 -*-
import requests
import setting
from urlparse import urljoin


class OpenWeatherMapAPI(object):
    VERSION = '2.5'
    API_URL = 'http://api.openweathermap.org/'
    WEATHER_URL = urljoin(API_URL, 'data/%s/weather' % VERSION)
    FORECAST_URL = urljoin(API_URL, 'data/%s/forecast' % VERSION)

    def __init__(self, appid):
        self.appid = appid

    def _requests(self, path, **kwargs):
        if 'units' not in kwargs:
            kwargs['units'] = 'metric'

        if 'lang' not in kwargs:
            kwargs['lang'] = 'zh_tw'

        result = requests.get(path, params=kwargs,
                headers={'x-api-key': self.appid})
        return result.json()

    def get_weather(self, **kwargs):
        return self._requests(self.WEATHER_URL, **kwargs)

    def get_forecast(self, **kwargs):
        return self._requests(self.FORECAST_URL, **kwargs)

if __name__ == '__main__':
    from pprint import pprint
    #pprint(OpenWeatherMapAPI(setting.APPID).get_weather(q='kaohsiung'))
    pprint(OpenWeatherMapAPI(setting.APPID).get_weather(id=1673820))
    pprint(OpenWeatherMapAPI(setting.APPID).get_forecast(id=1673820))
