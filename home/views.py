from django.shortcuts import render
from Blog.models import Article


def home(request):
    article = Article.objects.all()
    recent_post = Article.objects.all().order_by('-created', '-updated')
    # article = Article.custom_objects.all()
    # print(Article.objects.counter())
    return render(request, 'home/index.html', context={'article': article, 'recent_post': recent_post})


def sidebar(request):
    data = {'name':'soheil'}
    return render(request, "includes/sidebar.html", data)
