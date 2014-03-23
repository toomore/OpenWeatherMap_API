# -*- coding:utf8 -*-
import requests
from urlparse import urljoin


class OpenWeatherMapAPI(object):
    VERSION = '2.5'
    API_URL = 'http://api.openweathermap.org/'
    WEATHER_URL = urljoin(API_URL, 'data/%s/weather' % VERSION)

    def _requests(self, path, **kwargs):
        result = requests.get(path, params=kwargs)
        return result.json()

    def get_weather(self, **kwargs):
        return self._requests(self.WEATHER_URL, **kwargs)

if __name__ == '__main__':
    from pprint import pprint
    pprint(OpenWeatherMapAPI().get_weather(q='kaohsiung'))
