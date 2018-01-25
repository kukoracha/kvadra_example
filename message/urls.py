from django.conf.urls import url, include
from message import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'addtext/$', views.addtext, name='addtext'),
    url(r'uploadtext/$', views.uploadtext),
    url(r'gettext/$', views.gettext),
]