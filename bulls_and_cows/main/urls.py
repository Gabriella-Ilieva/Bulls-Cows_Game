from django.urls import path
from bulls_and_cows.main.views import index

urlpatterns = [
    path('', index, name="index"),
]