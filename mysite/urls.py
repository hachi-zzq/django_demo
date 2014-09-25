from django.conf.urls import patterns, include, url
import polls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$','polls.views.home',name='home'),

)
