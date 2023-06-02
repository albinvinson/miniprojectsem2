from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration',views.registration,name='registration'),
    path('login',views.login,name='login'),
    path('booking',views.booking,name='booking'),
    path('home',views.home,name='home'),
    path('logout',views.logout,name='logout')
]
