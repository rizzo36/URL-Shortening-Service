from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www).*', 'kirr.hostsconf.urls', name='wildcard'),
)

'''
In Zukunft kann es sein, dass man es wie in den neuen Versionen von Django aufrufen muss. 
Das wäre so:

from kirr.hostsconf import urls as redirect_urls

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www).*', redirect_urls, name='wildcard'),
)
'''