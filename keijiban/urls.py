from django.conf.urls import url
from keijiban import views

urlpatterns = [
    url('^$', views.geo_form, name='geo_form'),
]
