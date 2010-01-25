# -*- coding: UTF-8 -*-
import models

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def redirect(request, url):
    su = get_object_or_404(models.ShortUrl, pk=url)
    ctx = {
        'title': su.title,
        'url': su.url,
    }
    return render_to_response('surl/redirect.html', ctx, context_instance = RequestContext(request))
