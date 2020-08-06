"""
@brief: fetch gadm data from server
"""

import requests
from ..config.config import base_url



def fetch_provinces():
    """fetch provinces by country gid
    :param gid_0: country id
    :type gid_0: str

    :return list {}
    :rtype: list
    """
    return requests.get(f"{base_url}/provinces")

def fetch_districts(gid_1):
    """fetch districts by province gid
    :param gid_1: province id
    :type gid_1: str

    :return list {}
    :rtype: list
    """
    return requests.get(f"{base_url}/districts/from-province/{gid_1}")

def fetch_communes(gid_2):
    """fetch communes by disitrct gid
    :param gid_2: district id
    :type gid_2: str

    :return list {}
    :rtype: list
    """
    return requests.get(f"{base_url}/communes/from-district/{gid_2}")
