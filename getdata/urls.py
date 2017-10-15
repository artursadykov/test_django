from django.conf.urls import url, include
from getdata import views

urlpatterns = (
    url(r'^getdata/', views.getdata, name='getdata'),
)