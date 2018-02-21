from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^demo0/$', views.demo0),
    url(r'^demo1/$', views.demo1),
]
