from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import permission_required

from .models import Article
from .forms import ArticleForm


def moneys_home(request):
    moneys = Article.objects.all()

    p = Paginator(Article.objects.all(), 2)
    page = request.GET.get('page')

    try:
        articles = p.page(page)
    except PageNotAnInteger:
        articles = p.page(1)
    except EmptyPage:
        articles = p.page(p.num_pages)

    return render(request, 'moneys/moneys_home.html', {'moneys': moneys, 'articles': articles})


class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'moneys/create.html'
    form_class = ArticleForm


class NewsDeleteView(DetailView):
    model = Article
    success_url = '/moneys/moneys_home'
    template_name = 'moneys/moneys-delete.html'


class NewsDetailView(DetailView):
    model = Article
    template_name = 'moneys/details_view.html'
    context_object_name = 'Article'


@permission_required('moneys.add_article')
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
