"""A module to retrieve local weather data from Hong Kong Observatory"""

import json
import pkg_resources

from operator import itemgetter
import requests

from hko.distance_calculation import distance_calculation


with open(pkg_resources.resource_filename(__name__, 'assets/grid_location.json')) as f:
    GRID = json.load(f)
BASE_URL = 'http://pda.weather.gov.hk/'


def local_weather(lat, lng):

    """A function to retrieve local weather data from Hong Kong Observatory"""

    response = {}
    if isinstance(lat, float) and isinstance(lng, float) and\
       -90 <= lat <= 90 and -180 <= lng <= 180:
        temp_dict = GRID
        for i in temp_dict:
            distance = distance_calculation(lat, lng, float(i['lat']), float(i['lng']))
            i['dis'] = distance
        newlist = sorted(temp_dict, key=itemgetter('dis'))
        if newlist[0]['dis'] < 10:
            try:
                grid = newlist[0]['grid']
                url = 'locspc/android_data/gridData/{}_tc.xml'.format(grid)
                grid_data = json.loads(requests.get(BASE_URL + url).text)
                response['status'] = 1
                response['result'] = grid_data
                response['place'] = newlist[0]['name']
            except IndexError:
                response['result'] = ''
                response['status'] = 2
            except requests.exceptions.RequestException:
                response['result'] = ''
                response['status'] = 5
        else:
            response['result'] = ''
            response['status'] = 3
    else:
        response['result'] = ''
        response['status'] = 0
    return response
