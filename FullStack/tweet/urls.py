
from django.urls import path
from . import views
from .views import serve_protected_image
app_name = 'tweet'  # Define the app namespace

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('post/<int:tweet_id>/', views.tweet_detail, name='tweet_detail'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('protected_media/<path:filename>/', views.serve_protected_image, name='protected_image'),

]
