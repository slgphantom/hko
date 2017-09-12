"""A module to retrieve astro data from Hong Kong Observatory"""

import json

import requests
import xmltodict


BASE_URL = 'http://pda.weather.gov.hk/'
URL_UC = 'locspc/android_data/earthquake/eq_app_uc.xml'
URL_EN = 'locspc/android_data/earthquake/eq_app_e.xml'


def earthquake(lang='UC'):

    """A function to retrieve astro data from Hong Kong Observatory"""

    response = {}
    if lang in ['UC', 'EN']:
        try:
            if lang == 'UC':
                data = requests.get(BASE_URL + URL_UC)
            if lang == 'EN':
                data = requests.get(BASE_URL + URL_EN)
            data.encoding = 'utf8'
            data = json.loads(json.dumps(xmltodict.parse(data.text)))
            response['result'] = data
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
