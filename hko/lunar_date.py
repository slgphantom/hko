"""A module to retrieve lunar date data from Hong Kong Observatory"""

import json

import requests


BASE_URL = 'http://pda.weather.gov.hk/'
URL = 'locspc/android_data/lunar_date_uc.xml'


def lunar_date():

    """A function to retrieve lunar date data from Hong Kong Observatory"""

    response = {}
    try:
        data = json.loads(requests.get(BASE_URL + URL).content)
        response['result'] = data
        response['status'] = 1
    except IndexError:
        response['result'] = ''
        response['status'] = 2
    except requests.exceptions.RequestException:
        response['result'] = ''
        response['status'] = 5
    return response
