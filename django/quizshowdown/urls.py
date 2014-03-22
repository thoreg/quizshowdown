# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

from quizshowdown.core import api_views
from quizshowdown.core.views import IndexView

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'categories', api_views.CategoryViewSet)
router.register(r'quizzes', api_views.QuizViewSet)
router.register(r'answers', api_views.AnswerViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', IndexView.as_view(), name='index'),
)
