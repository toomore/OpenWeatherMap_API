# -*- coding:utf8 -*-
import requests
import setting
from urlparse import urljoin

VERSION = '2.5'
API_URL = 'http://api.openweathermap.org/'
WEATHER_URL = urljoin(API_URL, 'data/%s/weather' % VERSION)
FORECAST_URL = urljoin(API_URL, 'data/%s/forecast' % VERSION)
HISTORY_URL = urljoin(API_URL, 'data/%s/history/city' % VERSION)


class OpenWeatherMapAPI(object):
    APPID = ''

    def __init__(self, appid):
        OpenWeatherMapAPI.APPID = appid

    @classmethod
    def _requests(cls, path, **kwargs):
        if 'units' not in kwargs:
            kwargs['units'] = 'metric'

        if 'lang' not in kwargs:
            kwargs['lang'] = 'zh_tw'

        result = requests.get(path, params=kwargs,
                headers={'x-api-key': cls.APPID})
        return result.json()

    @classmethod
    def get_weather(cls, **kwargs):
        '''Get current weather data.
           wiki: http://bugs.openweathermap.org/projects/api/wiki/Api_2_5_weather
        '''
        return cls._requests(WEATHER_URL, **kwargs)

    @classmethod
    def get_forecast(cls, **kwargs):
        ''' Get forecast data.
            wiki: http://bugs.openweathermap.org/projects/api/wiki/Api_2_5_forecast
        '''
        return cls._requests(FORECAST_URL, **kwargs)

    @classmethod
    def get_history(cls, **kwargs):
        ''' Get city History
            wiki: http://bugs.openweathermap.org/projects/api/wiki/Api_2_5_history
        '''
        return cls._requests(HISTORY_URL, **kwargs)

if __name__ == '__main__':
    from pprint import pprint
    #pprint(OpenWeatherMapAPI(setting.APPID).get_weather(q='kaohsiung'))
    openweathermapapi = OpenWeatherMapAPI(setting.APPID)
    pprint(openweathermapapi.get_weather(id=1673820))
    pprint(OpenWeatherMapAPI.get_weather(id=1673820))
    pprint(openweathermapapi.get_forecast(id=1673820))
    pprint(openweathermapapi.get_history(id=1673820, type='hour'))
