"""A module to retrieve tide data from Hong Kong Observatory"""

import re

import requests


BASE_URL = 'http://pda.weather.gov.hk/'
URL = 'locspc/android_data/astro_tide.xml'


def tide():

    """A function to retrieve tide data from Hong Kong Observatory"""

    response = {}
    try:
        data = requests.get(BASE_URL + URL).content
        data2 = re.split('[@#]', data.decode('utf-8'))
        temp = {}
        temp['low_tide_1'] = {}
        temp['low_tide_2'] = {}
        temp['high_tide_1'] = {}
        temp['high_tide_2'] = {}
        temp['low_tide_1']['value'] = data2[4]
        temp['low_tide_1']['time'] = data2[5]
        temp['high_tide_1']['value'] = data2[6]
        temp['high_tide_1']['time'] = data2[7]
        temp['low_tide_2']['value'] = data2[8]
        temp['low_tide_2']['time'] = data2[9]
        temp['high_tide_2']['value'] = data2[10]
        temp['high_tide_2']['time'] = data2[11]
        temp['date'] = data2[12]
        response['result'] = temp
        response['status'] = 1
    except IndexError:
        response['result'] = ''
        response['status'] = 2
    except requests.exceptions.RequestException:
        response['result'] = ''
        response['status'] = 5
    return response
