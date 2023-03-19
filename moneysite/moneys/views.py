from django.shortcuts import render
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView

def moneys_home(request):
    moneys = Article.objects.all()
    return render(request, 'moneys/moneys_home.html', {'moneys': moneys})


class NewsDetailView(DetailView):
    model = Article
    template_name = 'moneys/details_view.html'
    context_object_name = 'Article'


def create(request):
    form = ArticleForm()

    data = {
        'form': form
    }

    return render(request, 'moneys/create.html', data)
