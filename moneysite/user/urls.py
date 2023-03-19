from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.login_page, name='logout'),
    path('', views.register_page, name='register')
]