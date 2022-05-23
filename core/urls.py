from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.homeViews, name='home'),
    path('contactus', views.contactUsView, name='contactus'),
    path('aboutus', views.aboutUsView, name='aboutus'),
    path('stuff', views.StuffView, name='stuff'),
]
