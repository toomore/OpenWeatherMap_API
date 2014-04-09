# -*- coding:utf8 -*-
''' OpenWeatherMapAPI '''
import cStringIO
import csv
import os
import requests
import setting
from urlparse import urljoin

VERSION = '2.5'
API_URL = 'http://api.openweathermap.org/'
WEATHER_URL = urljoin(API_URL, 'data/%s/weather' % VERSION)
FORECAST_URL = urljoin(API_URL, 'data/%s/forecast' % VERSION)
HISTORY_URL = urljoin(API_URL, 'data/%s/history/city' % VERSION)
COUNTRY_LIST_URL = 'http://openweathermap.org/help/city_list.txt'


class OpenWeatherMapAPI(object):
    ''' OpenWeatherMapAPI '''
    APPID = ''

    def __init__(self, appid):
        OpenWeatherMapAPI.APPID = appid

    @classmethod
    def _requests(cls, path, **kwargs):
        ''' Fetch data. '''
        if 'units' not in kwargs:
            kwargs['units'] = 'metric'

        if 'lang' not in kwargs:
            kwargs['lang'] = 'zh_tw'


        result = requests.get(path, params=kwargs,
                headers={'x-api-key': cls.APPID})

        if 'notjson' in kwargs:
            return result.content

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

    @classmethod
    def get_country_list(cls, keyby=None):
        ''' Get country list
            city list: http://openweathermap.org/help/city_list.txt
            ['id', 'nm', 'lat', 'lon', 'countryCode']
        '''
        if not os.path.isfile('./city_list.txt'):
            with open('./city_list.txt', 'w+') as files:
                files.write(cls._requests(COUNTRY_LIST_URL, notjson=True))

        with open('./city_list.txt', 'r+') as files:
            csv_files = csv.reader(files, delimiter='\t')

            result = {}
            csv_files.next()
            if keyby:
                if keyby is not 'countryCode':
                    key_no = {'id': 0, 'nm': 1, 'lat': 2, 'lon': 3, 'countryCode': 4}
                    result = {i[key_no[keyby]]: i for i in csv_files}
                else:
                    for i in csv_files:
                        result.setdefault(i[4], [])
                        result[i[4]].append(i)
            else:
                result = {i[1]: i for i in csv_files}

        return result

if __name__ == '__main__':
    from pprint import pprint
    #pprint(OpenWeatherMapAPI(setting.APPID).get_weather(q='kaohsiung'))
    OPEN_WEATHER_MAPAPI = OpenWeatherMapAPI(setting.APPID)
    #pprint(OPEN_WEATHER_MAPAPI.get_weather(id=1673820))
    #pprint(OpenWeatherMapAPI.get_weather(id=1673820))
    #pprint(OPEN_WEATHER_MAPAPI.get_forecast(id=1673820))
    #pprint(OPEN_WEATHER_MAPAPI.get_history(id=1673820, type='hour'))
    pprint(OpenWeatherMapAPI.get_country_list()['Kaohsiung'])
    pprint(OpenWeatherMapAPI.get_country_list('countryCode')['TW'])
