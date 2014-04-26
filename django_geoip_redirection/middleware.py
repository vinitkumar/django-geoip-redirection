# -*- coding: utf-8 -*-
import pygeoip
from django.conf import settings
from django.http import HttpResponseRedirect


def get_country_request(ip_address):
    """
    Looks up the database to find out country of the incoming IP.
    """
    file_path = settings.PROJECT_ROOT + '/data/GeoIP.dat.dat'
    geo_object = pygeoip.GeoIP(file_path)
    country = geo_object.country_name_by_addr(ip_address)
    return country


class LocationMiddleWare(object):
    """
    Middleware to redirect user as per country returned by get_country_request
    """

    def process_request(self, request):
        """
        Process incoming requests
        """
        #NOTICE: This will make sure redirect loop is broken.
        # The list is same as the languages in your django settings
        if request.path[:4] in ["/en/", "/nl/", "/in/"]:
            return None
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            request.META['REMOTE_ADDR'] = request.META['HTTP_X_FORWARDED_FOR']
        ip_address = request.META['REMOTE_ADDR']
        country = get_country_request(ip_address)
        if country == "India":
            return HttpResponseRedirect('/in/')
        elif country == "Netherlands":
            return HttpResponseRedirect('/nl/')
        else:
            return HttpResponseRedirect('/en/')
        return None
