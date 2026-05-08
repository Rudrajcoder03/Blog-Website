from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('register/', views.register, name='register'),  # ✅ ADD THIS
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('like/<int:id>/', views.like_post, name='like_post'),
    path('profile/', views.profile, name='profile'),
    path('update/<int:id>/', views.update_post, name='update_post'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
]