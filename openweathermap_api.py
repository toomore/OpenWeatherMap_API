# -*- coding:utf8 -*-
import requests

class OpenWeatherMapAPI(object):

    def _requests(self, path, **kwargs):
        result = requests.get(path, params=kwargs)
        return result.json()

if __name__ == '__main__':
    from pprint import pprint
    pprint(OpenWeatherMapAPI()._requests('http://api.openweathermap.org/data/2.5/weather',
            q='kaohsiung'))
