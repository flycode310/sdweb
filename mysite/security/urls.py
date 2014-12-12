from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	url(r'^$', views.show_main),
	url(r'^upload/', views.upload),
)