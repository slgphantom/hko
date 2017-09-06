# HKO
A package to retrieve weather data from the Hong Kong Observatory.
Data (private api endpoints) obtained through capturing the traffic of the HKO app and web, and extracting the apk file etc.
<br>

## Installating required packages
`pip install -r requirements.txt`
<br>

## Usage
Every function (request) will return a `dict`, whereas `result` and `status` will be the keys of the returning `dict`, for example:

    >>> import pprint
    >>> from hko import astro
    >>> pp = pprint.PrettyPrinter(indent=4).pprint
    >>> pp(astro())
    {   'result': {   'date': '20170906',
                      'moonrise': '1844',
                      'moonset': '0550',
                      'sunrise': '0607',
                      'sunset': '1836'},
        'status': 1}
<br>

## Functions List
Functions | Number of Arguments | Type of Argument | Arguments Supported | Default Arguments 
:---: | :---: | :---: | :---: | :---: 
`astro()` | 0 | / | / | / 
`blog()` | 0 | / | / | / 
`earthquake()` | 1 | `str` | ['UC', 'EN'] | 'UC'
`local_weather()` | 2 | `float`, `float` | [lat], [lng] | / 
`lunar_date()` | 0 | / | / | / 
`major_city_forecast()` | 1 | `str` | ['UC', 'EN'] | 'UC'
`marine_forecast()` | 1 | `str` | ['UC', 'EN'] | 'UC'
`rainfall_nowcast()` | 2 | `float`, `float` | [lat], [lng] | / 
`regional_weather()` | 0 | / | / | / 
`serval_days_weather_forecast()` | 1 | `str` | ['UC', 'EN'] | 'UC'
`south_china_coastal_waters()` | 1 | `str` | ['UC', 'EN'] | 'UC'
`tide()` | 0 | / | / | / 
`uv_index()` | 1 | `str` | ['UC', 'EN'] | 'UC'
`weather_warning()` | 1 | `str` | ['UC', 'EN'] | 'UC'
<br>

## Status Code
Status | Meaning
:---: | :---:
0 | Request Invalid
1 | Request Success
2 | Request Valid, But Server Returns Error
3 | Requested Location Not Inside Hong Kong
4 | Requested Data Not Yet Available
<br>

## Coding Style
- Following [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Checked by the `pylint`
<br>

## TODO
- unifying the time/date format (perhaps adding a `timestamp` field in returned `dict`)
- `major_city_forecast()` --> accept `place` as an argument
- support more functions 
<br>

## Contributions
We welcome any contributions which fulfilled the coding style
