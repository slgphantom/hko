"""A module to retrieve rainfall nowcast data from Hong Kong Observatory"""

import json
import pkg_resources
import re
from operator import itemgetter

import requests

from hko.distance_calculation import distance_calculation


with open(pkg_resources.resource_filename(__name__, 'assets/rainfall_nowcast_mapping.json')) as f:
    MAPPING = json.load(f)
BASE_URL = 'http://pda.weather.gov.hk/'


def rainfall_nowcast(lat, lng):

    """A function to retrieve rainfall nowcast data from Hong Kong Observatory"""

    response = {}
    if isinstance(lat, float) and isinstance(lng, float) and\
       -90 <= lat <= 90 and -180 <= lng <= 180:
        temp_dict = MAPPING
        for i in temp_dict:
            distance = distance_calculation(lat, lng, float(i['lat']), float(i['lng']))
            i['dis'] = distance
        newlist = sorted(temp_dict, key=itemgetter('dis'))
        if newlist[0]['dis'] > 10:
            response['result'] = ''
            response['status'] = 3
            return response
        lat_2 = newlist[0]['lat']
        lng_2 = newlist[0]['lng']
        try:
            url = 'locspc/android_data/rainfallnowcast/{}_{}.xml'.format(float(lat_2), float(lng_2))
            data = requests.get(BASE_URL + url).content
            data2 = re.split('[@#]', data.decode('utf-8'))
            temp = {}
            temp['0-30'] = {'from_time': data2[0], 'to_time': data2[2], 'value': data2[1]}
            temp['30-60'] = {'from_time': data2[2], 'to_time': data2[4], 'value': data2[3]}
            temp['60-90'] = {'from_time': data2[4], 'to_time': data2[6], 'value': data2[5]}
            temp['90-120'] = {'from_time': data2[6], 'to_time': data2[8], 'value': data2[7]}
            temp['description_en'] = data2[9]
            temp['description_tc'] = data2[10]
            temp['description_sc'] = data2[11]
            response['result'] = temp
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
