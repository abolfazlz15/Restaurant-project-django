from django.urls import path
from . import views

app_name = 'foods'
urlpatterns = [
    path('menu', views.menuView, name='menu'),
]