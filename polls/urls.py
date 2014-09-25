from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    url(r'^$','polls.views.home',name='home',view='polls.views.dec'),
    url(r'^yes', 'polls.views.index', name='index'),
    # url(r'^mysite/', include('mysite.foo.urls')),

)
