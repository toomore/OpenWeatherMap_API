# -*- coding:utf8 -*-
import requests
import setting
from urlparse import urljoin


class OpenWeatherMapAPI(object):
    VERSION = '2.5'
    API_URL = 'http://api.openweathermap.org/'
    WEATHER_URL = urljoin(API_URL, 'data/%s/weather' % VERSION)
    FORECAST_URL = urljoin(API_URL, 'data/%s/forecast' % VERSION)
    HISTORY_URL = urljoin(API_URL, 'data/%s/history/city' % VERSION)

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
        '''Get current weather data.
           wiki: http://bugs.openweathermap.org/projects/api/wiki/Api_2_5_weather
        '''
        return self._requests(self.WEATHER_URL, **kwargs)

    def get_forecast(self, **kwargs):
        ''' Get forecast data.
            wiki: http://bugs.openweathermap.org/projects/api/wiki/Api_2_5_forecast
        '''
        return self._requests(self.FORECAST_URL, **kwargs)

    def get_history(self, **kwargs):
        ''' Get city History
            wiki: http://bugs.openweathermap.org/projects/api/wiki/Api_2_5_history
        '''
        return self._requests(self.HISTORY_URL, **kwargs)

if __name__ == '__main__':
    from pprint import pprint
    #pprint(OpenWeatherMapAPI(setting.APPID).get_weather(q='kaohsiung'))
    openweathermapapi = OpenWeatherMapAPI(setting.APPID)
    pprint(openweathermapapi.get_weather(id=1673820))
    pprint(openweathermapapi.get_forecast(id=1673820))
    pprint(openweathermapapi.get_history(id=1673820, type='hour'))
