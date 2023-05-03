# -*- coding: utf-8 -*-
"""
Created on Wed May  3 14:48:15 2023

@author: ifreedom
"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]