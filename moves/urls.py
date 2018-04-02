from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
	path('', views.movelist, name='movelist'),
	# path('<slug:dex>/', views.detail, name='detail'),
]
