from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('details_view/', views.details_view, name='details_view')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
