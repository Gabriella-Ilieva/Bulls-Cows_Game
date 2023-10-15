from django.urls import path

from bulls_and_cows.players import views

urlpatterns = [
    path('register/', views.RegisterPlayerView.as_view(), name='register'),
    path('login/', views.LoginPlayerView.as_view(), name='login'),

]