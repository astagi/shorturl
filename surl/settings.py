# -*- coding: UTF-8 -*-
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse

try:
    GOOGLE_ANALYTICS = settings.SURL_GOOGLE_ANALYTICS
except AttributeError:
    raise ImproperlyConfigured('google analytics code not found')

ABSOLUTE_PREFIX_REDIRECT_SERVICE = getattr(settings, 'SURL_ABSOLUTE_PREFIX_REDIRECT_SERVICE', None)
ABSOLUTE_PREFIX_JSONP_SERVICE = getattr(settings, 'SURL_ABSOLUTE_PREFIX_JSONP_SERVICE', None)
