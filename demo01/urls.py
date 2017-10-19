# -*- coding: utf-8 -*-

from django.conf.urls import url

from demo01.views import FirstView

urlpatterns = [
    url(r'^first/$', FirstView.as_view(), name="first_view"),
]
