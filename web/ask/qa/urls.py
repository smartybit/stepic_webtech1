from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'qa.views.test'),
    url(r'^login/?$', 'qa.views.test'),
    url(r'^signup/?$', 'qa.views.test'),
    url(r'^question\/\d*\/?$', 'qa.views.test'),
    url(r'^ask/?$', 'qa.views.test'),
    url(r'^popilar/?$', 'qa.views.test'),
    url(r'^new/?$', 'qa.views.test'),
)
