from django.urls import path
from . import views


urlpatterns = [
    path('', views.moneys_home, name='moneys_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='moneys-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='moneys-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='moneys-delete')
]
