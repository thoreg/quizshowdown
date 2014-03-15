from django.conf.urls import patterns, include, url

from django.contrib import admin

from quizshowdown.core.views import IndexView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quizshowdown.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', IndexView.as_view(), name='index'),
)
