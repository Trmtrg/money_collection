from django.shortcuts import render
from .models import Article


def moneys_home(request):
    moneys = Article.objects.all()
    return render(request, 'moneys/moneys_home.html', {'moneys': moneys})