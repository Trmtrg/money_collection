from django.shortcuts import render
from .models import Article
from .forms import ArticleForm


def moneys_home(request):
    moneys = Article.objects.all()
    return render(request, 'moneys/moneys_home.html', {'moneys': moneys})


def create(request):
    form = ArticleForm()

    data = {
        'form': form
    }

    return render(request, 'moneys/create.html', data)
