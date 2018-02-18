"""A module to test the HKO package"""

import socket
import unittest

from requests.exceptions import RequestException


def guard(*_, **__):

    """A function to replace socket.socket"""

    raise RequestException("This is a virtual error.")


if __name__ == '__main__':
    socket.socket = guard
    unittest.main('tests.test_hko')
