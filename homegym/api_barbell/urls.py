from django.urls import path
from .views import barbell_list

urlpatterns = [
    path('barbell/', barbell_list)
]
