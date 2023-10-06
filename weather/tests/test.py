import pytest
import sys
from weather import getGeoCode

def test_getGeoCode_valid_city():
    assert getGeoCode('Jakarta') == (-6.2146, 106.8451)

def test_getGeoCode_invalid_city():
    assert getGeoCode('InvalidCityName') is None