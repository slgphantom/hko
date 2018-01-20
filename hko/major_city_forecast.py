"""A module to retrieve major cities weather forecast data from Hong Kong Observatory"""

import requests


BASE_URL = 'http://pda.weather.gov.hk/'
URL_ASIA_UC = 'locspc/android_data/asis_wwic.xml'
URL_ASIA_EN = 'locspc/android_data/asis_wwi.xml'
URL_AFRICA_UC = 'locspc/android_data/africa_wwic.xml'
URL_AFRICA_EN = 'locspc/android_data/africa_wwi.xml'
URL_AUSTRALIASOUTHPACIFIC_UC = 'locspc/android_data/australia_south_pacific_wwic.xml'
URL_AUSTRALIASOUTHPACIFIC_EN = 'locspc/android_data/australia_south_pacific_wwi.xml'
URL_EUROPE_UC = 'locspc/android_data/europe_wwic.xml'
URL_EUROPE_EN = 'locspc/android_data/europe_wwi.xml'
URL_NORTHCENTRALAMERICA_UC = 'locspc/android_data/north_central_america_wwic.xml'
URL_NORTHCENTRALAMERICA_EN = 'locspc/android_data/north_central_america_wwi.xml'
URL_SOUTHAMERICA_UC = 'locspc/android_data/south_america_wwic.xml'
URL_SOUTHAMERICA_EN = 'locspc/android_data/south_america_wwi.xml'


def asia(lang='UC'):

    """A function to retrieve major Asian cities weather forecast data from Hong Kong Observatory"""

    response = []
    if lang == 'UC':
        data = requests.get(BASE_URL + URL_ASIA_UC)
    if lang == 'EN':
        data = requests.get(BASE_URL + URL_ASIA_EN)
    data.encoding = 'utf8'
    data2 = data.text.split('@')
    for i in data2:
        temp = i.split('#')
        temp_dict = {}
        temp_dict['place'] = temp[0]
        temp_dict['mintemp'] = temp[1]
        temp_dict['maxtemp'] = temp[2]
        temp_dict['status'] = temp[3]
        temp_dict['photo'] = temp[4]
        response.append(temp_dict)
    return response


def africa(lang='UC'):

    """A function to retrieve major African cities weather forecast
    data from Hong Kong Observatory"""

    response = []
    if lang == 'UC':
        data = requests.get(BASE_URL + URL_AFRICA_UC)
    if lang == 'EN':
        data = requests.get(BASE_URL + URL_AFRICA_EN)
    data.encoding = 'utf8'
    data2 = data.text.split('@')
    for i in data2:
        temp = i.split('#')
        temp_dict = {}
        temp_dict['place'] = temp[0]
        temp_dict['mintemp'] = temp[1]
        temp_dict['maxtemp'] = temp[2]
        temp_dict['status'] = temp[3]
        temp_dict['photo'] = temp[4]
        response.append(temp_dict)
    return response


def australia_south_pacific(lang='UC'):

    """A function to retrieve major Australian and South Pacific cities weather forecast
    data from Hong Kong Observatory"""

    response = []
    if lang == 'UC':
        data = requests.get(BASE_URL + URL_AUSTRALIASOUTHPACIFIC_UC)
    if lang == 'EN':
        data = requests.get(BASE_URL + URL_AUSTRALIASOUTHPACIFIC_EN)
    data.encoding = 'utf8'
    data2 = data.text.split('@')
    for i in data2:
        temp = i.split('#')
        temp_dict = {}
        temp_dict['place'] = temp[0]
        temp_dict['mintemp'] = temp[1]
        temp_dict['maxtemp'] = temp[2]
        temp_dict['status'] = temp[3]
        temp_dict['photo'] = temp[4]
        response.append(temp_dict)
    return response


def europe(lang='UC'):

    """A function to retrieve major European cities weather forecast
    data from Hong Kong Observatory"""

    response = []
    if lang == 'UC':
        data = requests.get(BASE_URL + URL_EUROPE_UC)
    if lang == 'EN':
        data = requests.get(BASE_URL + URL_EUROPE_EN)
    data.encoding = 'utf8'
    data2 = data.text.split('@')
    for i in data2:
        temp = i.split('#')
        temp_dict = {}
        temp_dict['place'] = temp[0]
        temp_dict['mintemp'] = temp[1]
        temp_dict['maxtemp'] = temp[2]
        temp_dict['status'] = temp[3]
        temp_dict['photo'] = temp[4]
        response.append(temp_dict)
    return response


def north_central_america(lang='UC'):

    """A function to retrieve major North and Central American cities weather forecast
    data from Hong Kong Observatory"""

    response = []
    if lang == 'UC':
        data = requests.get(BASE_URL + URL_NORTHCENTRALAMERICA_UC)
    if lang == 'EN':
        data = requests.get(BASE_URL + URL_NORTHCENTRALAMERICA_EN)
    data.encoding = 'utf8'
    data2 = data.text.split('@')
    for i in data2:
        temp = i.split('#')
        temp_dict = {}
        temp_dict['place'] = temp[0]
        temp_dict['mintemp'] = temp[1]
        temp_dict['maxtemp'] = temp[2]
        temp_dict['status'] = temp[3]
        temp_dict['photo'] = temp[4]
        response.append(temp_dict)
    return response


def south_america(lang='UC'):

    """A function to retrieve major South American cities weather forecast
    data from Hong Kong Observatory"""

    response = []
    if lang == 'UC':
        data = requests.get(BASE_URL + URL_SOUTHAMERICA_UC)
    if lang == 'EN':
        data = requests.get(BASE_URL + URL_SOUTHAMERICA_EN)
    data.encoding = 'utf8'
    data2 = data.text.split('@')
    for i in data2:
        temp = i.split('#')
        temp_dict = {}
        temp_dict['place'] = temp[0]
        temp_dict['mintemp'] = temp[1]
        temp_dict['maxtemp'] = temp[2]
        temp_dict['status'] = temp[3]
        temp_dict['photo'] = temp[4]
        response.append(temp_dict)
    return response


def major_city_forecast(lang='UC'):

    """A function to retrieve major cities weather forecast data from Hong Kong Observatory"""

    response = {}
    if lang in ['UC', 'EN']:
        try:
            response['result'] = {}
            response['result']['Asia'] = asia(lang)
            response['result']['Africa'] = africa(lang)
            response['result']['AustraliaSouthPacific'] = australia_south_pacific(lang)
            response['result']['Europe'] = europe(lang)
            response['result']['NorthCentralAmerica'] = north_central_america(lang)
            response['result']['SouthAmerica'] = south_america(lang)
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
