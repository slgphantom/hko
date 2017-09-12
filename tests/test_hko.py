"""A module to test the HKO package"""

import unittest

from hko import astro, blog, earthquake, local_weather, lunar_date,\
    major_city_forecast, marine_forecast, rainfall_nowcast,\
    regional_weather, serval_days_weather_forecast,\
    south_china_coastal_waters, tide, uv_index, weather_warning


HONG_KONG_LAT_LNG = 22.352493, 113.8474984
MACAU_LAT_LNG = 22.161817, 113.5001117
FUNCTIONS_WITH_LANG = [earthquake, major_city_forecast, marine_forecast,
                       serval_days_weather_forecast, south_china_coastal_waters,
                       uv_index, weather_warning]
FUNCTIONS_WITH_LAT_LNG = [local_weather, rainfall_nowcast]
FUNCTIONS_WITH_LANG_ST4 = set([uv_index])
FUNCTIONS_WITHOUT_ARGS = [astro, blog, lunar_date, regional_weather, tide]


class TestHKO(unittest.TestCase):

    """A class to test the HKO package"""

    def test_functions_with_lang(self):

        """A function to test functions with language"""

        for func in FUNCTIONS_WITH_LANG:
            self.assertEqual(func('XXX')['status'], 0)
            self.assertEqual(func(123.4)['status'], 0)
            ok_status = [1, 2, 4, 5] if func in FUNCTIONS_WITH_LANG_ST4 else [1, 2, 5]
            self.assertIn(func()['status'], ok_status)
            self.assertIn(func('UC')['status'], ok_status)
            self.assertIn(func('EN')['status'], ok_status)

    def test_functions_with_lat_lng(self):

        """A function to test functions with latitude and longitude"""

        for func in FUNCTIONS_WITH_LAT_LNG:
            self.assertEqual(func('XXX', 'XXX')['status'], 0)
            self.assertEqual(func(45.6, 'XXX')['status'], 0)
            self.assertEqual(func('XXX', 123.4)['status'], 0)
            self.assertEqual(func(90.1, 123.4)['status'], 0)
            self.assertEqual(func(-90.1, 123.4)['status'], 0)
            self.assertEqual(func(45.6, 180.1)['status'], 0)
            self.assertEqual(func(45.6, -180.1)['status'], 0)
            self.assertIn(func(*HONG_KONG_LAT_LNG)['status'], [1, 2, 5])
            self.assertEqual(func(*MACAU_LAT_LNG)['status'], 3)

    def test_functions_without_args(self):

        """A function to test functions without arguments"""

        for func in FUNCTIONS_WITHOUT_ARGS:
            self.assertIn(func()['status'], [1, 2, 5])


if __name__ == '__main__':
    unittest.main()
