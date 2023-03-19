from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .models import Article
from .forms import ArticleForm

def moneys_home(request):
    moneys = Article.objects.all()
    return render(request, 'moneys/moneys_home.html', {'moneys': moneys})


class NewsDetailView(DetailView):
    model = Article
    template_name = 'moneys/details_view.html'
    context_object_name = 'Article'


def create(request):
    error = ''
    form = ArticleForm()

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверно заполнена'

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'moneys/create.html', data)
