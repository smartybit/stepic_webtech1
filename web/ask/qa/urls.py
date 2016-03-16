from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'qa.views.mainpage'),
    url(r'^login/?$', 'qa.views.test'),
    url(r'^signup/?$', 'qa.views.test'),
    url(r'^question\/\d*\/?$', 'qa.views.test'),
    url(r'^ask/?$', 'qa.views.test'),
    url(r'^ask/\d*/popular/?$', 'qa.views.test'),
    url(r'^popular/?$', 'qa.views.test'),
    url(r'^new/?$', 'qa.views.test'),
)
