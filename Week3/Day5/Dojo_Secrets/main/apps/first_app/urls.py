from django.conf.urls import url
from . import views         

urlpatterns = [
	url(r'^$', views.index),
	url(r'^secrets$', views.secrets),
	url(r'^create$', views.create),
	url(r'^logout$', views.logout),
	url(r'^popular$', views.popular),
	url(r'^display$', views.display),
	url(r'^delete/(?P<id>\d+)$', views.delete),
	url(r'^like/(?P<id>\d+)$', views.like),
]