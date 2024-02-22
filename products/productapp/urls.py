from django.urls import path
from .views import create_api,details_api

urlpatterns = [
    path('add/', create_api),
    path('show/<int:pk>/', details_api)
]

