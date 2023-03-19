from django.urls import path
from . import views


urlpatterns = [
    path('', views.moneys_home, name='moneys_home'),
    path('create/', views.create, name='create')
]
