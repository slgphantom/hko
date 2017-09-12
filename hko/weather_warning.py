"""A module to retrieve weather warning data from Hong Kong Observatory"""

import json

import requests


BASE_URL = 'http://www.weather.gov.hk/'
URL_UC = 'wxinfo/json/warnsumc.xml'
URL_EN = 'wxinfo/json/warnsum.xml'


def weather_warning(lang='UC'):

    """A function to retrieve weather warning data from Hong Kong Observatory"""

    response = {}
    if lang in ['UC', 'EN']:
        try:
            if lang == 'UC':
                data = requests.get(BASE_URL + URL_UC)
            if lang == 'EN':
                data = requests.get(BASE_URL + URL_EN)
            data_2 = json.loads(data.text.replace('var weather_warning_summary = ', '')[:-2] + '}')
            response['result'] = data_2
            response['status'] = 1
        except IndexError:
            response['result'] = ''
            response['status'] = 2
        except requests.exceptions.RequestException:
            response['result'] = ''
            response['status'] = 5
    else:
        response['result'] = ''
        response['status'] = 0
    return response
