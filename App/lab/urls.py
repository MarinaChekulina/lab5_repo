from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^model_row$', views.model_row, name='model_row'),
    url(r'^sales$', views.sales, name='sales'),
    url(r'^address$', views.address, name='address'),
    ]

# urlpatterns = [
#     url(r'^$', views.main, name='main')
#     ]