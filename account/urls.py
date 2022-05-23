from  django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('login', views.loginView, name='login'),
    path('register', views.registerView, name='register'),
    path('editprofile', views.editProfile, name='editprofile'),
    path('logout', views.logoutView, name='logout'),
]