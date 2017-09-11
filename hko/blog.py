"""A module to retrieve blog data from Hong Kong Observatory"""

import json

import requests


BASE_URL = 'http://www.weather.gov.hk/'
URL = 'forecaster_blog/json/blog_json_uc.xml'


def blog():

    """A function to retrieve blog data from Hong Kong Observatory"""

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
