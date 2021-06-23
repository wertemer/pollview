from django.contrib import admin
from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
	path('poll/',views.poll, name='poll'),
	path('poll/CompletePoll/', views.CompletePoll, name="complete"),
	path('poll/listusers/', views.listusers, name='listusers'),
	path('poll/results/',views.results,name='results'),
	path('', views.index),
]
