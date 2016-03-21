from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'qa.views.mainpage', name = 'mainpage'),
    url(r'^popular/?$', 'qa.views.popular'),
    url(r'^question\/(?P<question_id>\d*)\/?$', 'qa.views.question', name='question'),
    url(r'^ask/?$', 'qa.views.newquestion'),
    url(r'^newanswer/?$', 'qa.views.newanswer'),
    url(r'^createdata/?$', 'qa.views.createdata'),
    url(r'^login/$', 'django.contrib.auth.views.login',  {'template_name': 'admin/login.html'}),
    url(r'^logout/$', 'qa.views.logout',),
    url(r'^signup/?$', 'qa.views.signup'),
)
