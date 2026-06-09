from django.urls import path,include
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('<int:id>/', views.individual, name="indi"),
    path('register', views.register, name='register'),
    path('registration/', views.registration, name='reg'),
    path('', views.login_view, name='login'),
    path('logged-in/', views.log, name='log'),
]
