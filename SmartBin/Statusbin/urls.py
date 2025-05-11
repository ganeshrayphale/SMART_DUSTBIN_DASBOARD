from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('unlock/<int:bin_id>/', views.unlock_bin, name='unlock_bin'),
]
