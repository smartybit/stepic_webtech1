from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'qa.views.mainpage'),
    url(r'^popular/?$', 'qa.views.popular'),
    url(r'^question\/(?P<question_id>\d*)\/?$', 'qa.views.question'),
    url(r'^createdata/?$', 'qa.views.createdata'),
    url(r'^login/?$', 'qa.views.test'),
    url(r'^signup/?$', 'qa.views.test'),
)
