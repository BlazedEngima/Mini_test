import pytest
import sys
from weather import getGeoCode

def test_getGeoCode_valid_city():
    assert getGeoCode('Jakarta') == (-6.1753942, 106.827183)

def test_getGeoCode_invalid_city():
    with pytest.raises(ValueError):
        getGeoCode('InvalidCityName')