# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('test-drill/', views.topics, name='test-drills'),
    path('start-test/', views.start_test, name='test-sessions'),
    path('', views.index, name='home'),
    

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
