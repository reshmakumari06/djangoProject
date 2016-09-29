from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.notif_list, name='notif_list'),
]