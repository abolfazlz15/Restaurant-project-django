from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('category/<slug:slug>', views.categoryDetail, name='category_detail'),
    path('detail/<slug:slug>', views.articleDetail, name='article_detail'),
    path('', views.ArticleList.as_view(), name='article_list'),
    path('search/', views.searchDetail, name='search')
]
