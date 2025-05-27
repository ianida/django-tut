from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/<int:student_id>/', views.profile, name='profile'),
    path('all/', views.all_profiles, name='all_profiles'),
]
