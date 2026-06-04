from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index),
    path('' , views.welcome_view),
    path('search', views.search),
    path('article/<int:article_id>', views.read_article),
    path('article/<str:username>', views.author_profile),
    path('payment', views.payment),

]
