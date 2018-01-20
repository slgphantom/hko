"""A module to retrieve astro data from Hong Kong Observatory"""

import re

import requests


BASE_URL = 'http://pda.weather.gov.hk/'
URL = 'locspc/android_data/astro_tide.xml'


def astro():

    """A function to retrieve astro data from Hong Kong Observatory"""

    response = {}
    try:
        data = requests.get(BASE_URL + URL).content
        data2 = re.split('[@#]', data.decode('utf-8'))
        temp = {}
        temp['sunrise'] = data2[0]
        temp['sunset'] = data2[1]
        temp['moonrise'] = data2[2]
        temp['moonset'] = data2[3]
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
