from django.shortcuts import render, redirect
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
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_volid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверно заполнена'
    form = ArticleForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'moneys/create.html', data)
