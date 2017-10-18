from django.conf.urls import url, include
from note import views

urlpatterns = (
    url(r'^note/', views.note, name='note'),
)