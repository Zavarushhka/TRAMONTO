from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='index'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('login/', views.login, name='login'),
    path('love/', views.love, name='love'),
    path('love/', views.list_users, name='list-users'),
    path('love/', views.like_block_view, name='like-like'),
    path('love/liked/', views.like, name='liked'),
    path('', views.get_order, name='order'),
]