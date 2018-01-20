"""A module to calculate distance."""

from LatLon23 import LatLon


def distance_calculation(lat1, lng1, lat2, lng2):

    """A function to calculate distance."""

    return LatLon(lat1, lng1).distance(LatLon(lat2, lng2))
