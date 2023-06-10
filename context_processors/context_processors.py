from Blog.models import Article
from Blog.models import Category


def recent_article(request):
    recent_article = Article.objects.order_by("-created")
    return {"recent_article": recent_article}


def category(request):
    category = Category.objects.all()
    return {"category": category}
