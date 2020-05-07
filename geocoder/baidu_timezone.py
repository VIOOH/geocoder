#!/usr/bin/python
# coding: utf8
from __future__ import absolute_import

import logging
from geocoder.location import Location
from geocoder.base import OneResult
from geocoder.baidu import BaiduQuery


class BaiduTimezoneResult(OneResult):
    @property
    def ok(self):
        return bool(self.timeZoneId)

    @property
    def timeZoneId(self):
        return self.raw.get('timezone_id')

    @property
    def rawOffset(self):
        return self.raw.get('raw_offset')

    @property
    def dstOffset(self):
        return self.raw.get('dst_offset')


class BaiduTimezone(BaiduQuery):
    """
    Baidu Geocoding API
    ===================
    Baidu Maps Geocoding API is a free open the API, the default quota
    one million times / day.

    Params
    ------
    :param location: Your search location you want geocoded.
    :param key: Baidu API key.
    :param referer: Baidu API referer website.

    References
    ----------
    API Documentation: http://developer.baidu.com/map
    Get Baidu Key: http://lbsyun.baidu.com/apiconsole/key
    """
    provider = 'baidu'
    method = 'timezone'

    _URL = 'http://api.map.baidu.com/timezone/v1/'
    _RESULT_CLASS = BaiduTimezoneResult

    def _build_params(self, location, provider_key, **kwargs):
        location = Location(location)
        params = {
            'location': str(location),
            'ret_coordtype': kwargs.get('coordtype', 'wgs84ll'),
            'output': 'json',
            'ak': provider_key
        }
        if ('lang_code' in kwargs):
            params['accept-language'] = kwargs['lang_code']

        return params

    def _adapt_results(self, json_response):
        return [json_response]


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = BaiduTimezone("39.983424,116.32298", key='')
    g.debug()
