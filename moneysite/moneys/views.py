from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView

from .forms import ArticleForm
from .models import Article


def moneys_home(request):
    moneys = Article.objects.all()

    p = Paginator(moneys, 3)
    page = request.GET.get('page')
# Работает
    try:
        articles = p.page(page)
    except PageNotAnInteger:
        articles = p.page(1)
    except EmptyPage:
        articles = p.page(p.num_pages)

# Не работает
    # if not PageNotAnInteger:
    #     articles = p.page(1)
    # elif not EmptyPage:
    #     articles = p.page(p.num_pages)
    # else:
    #     articles = p.page(page)

    return render(request, 'moneys/moneys_home.html', {'moneys': moneys, 'articles': articles})


class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'moneys/create.html'
    form_class = ArticleForm
    success_url = '..'


class NewsDeleteView(DeleteView):
    model = Article
    success_url = '/moneys/'
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

