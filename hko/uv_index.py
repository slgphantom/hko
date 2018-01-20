# encoding=utf8

"""A module to retrieve uv index data from Hong Kong Observatory"""

import requests


BASE_URL = 'http://pda.weather.gov.hk/'
URL_TC = 'locspc/android_data/fuvc.xml'
URL_EN = 'locspc/android_data/fuve.xml'


def uv_index(lang='UC'):

    """A function to retrieve uv index data from Hong Kong Observatory"""

    response = {}
    if lang in ['UC', 'EN']:
        try:
            if lang == 'UC':
                data = requests.get(BASE_URL + URL_TC).content.decode('utf8')
                data_1 = data.split(u'的最高紫外線指數大約是')
                response['result'] = {}
                response['result']['date'] = data_1[0]
                response['result']['max_uv_index'] = data_1[1].split(u'，強度屬於')[0]
                response['result']['intensity'] = data_1[1].split(u'，強度屬於')[1][:-1]
                response['status'] = 1
            if lang == 'EN':
                data = requests.get(BASE_URL + URL_EN).content.decode('utf8')
                data_1 = data.replace('The maximum UV Index for ', '')\
                             .replace(' will be about ', ',')\
                             .replace('. The intensity of UV radiation wll be ', ',')[:-1]
                data_2 = data_1.split(',')
                response['result'] = {}
                response['result']['date'] = data_2[0]
                response['result']['max_uv_index'] = data_2[1]
                response['result']['intensity'] = data_2[2]
                response['status'] = 1
        except IndexError:
            if data:
                response['result'] = data
                response['status'] = 4
            else:
                response['result'] = ''
                response['status'] = 2
        except requests.exceptions.RequestException:
            response['result'] = ''
            response['status'] = 5
    else:
        response['result'] = ''
        response['status'] = 0
    return response
