from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('<int:id>/', views.individual, name="indi"),
    path('register', views.register, name='register'),
    path('registration/', views.registration, name='reg'),
    path('', views.login_view, name='login'),
    path('logged-in/', views.log, name='log'),
    path('enter/', views.entry, name='entry'),
    path('ent/', views.ent, name='ent'),
]
