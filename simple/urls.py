from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:id>/', views.individual, name="indi"),
    path('register/', views.register, name='re'),
    path('registration/', views.registration, name='reg'),
    path('login/', views.login, name='login'),
    path('logged-in/', views.log, name='log'),
]
