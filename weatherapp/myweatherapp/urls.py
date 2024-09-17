from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='myhome'),
    path('api-data/', views.fetch_data_from_api, name='fetch_api_data'),
]