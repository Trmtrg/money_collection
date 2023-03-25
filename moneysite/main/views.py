from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def details_view(request):
    return render(request, 'moneys/moneys/details_view.html')
