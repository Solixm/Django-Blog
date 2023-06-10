from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from Blog.forms import ContactUSform, MessageForm
from Blog.models import Article, Category, Comment, Message, like


# def article_detail(request, slug):
#     article = Article.objects.get(slug=slug)
#     if request.method == 'POST':
#         parent_id = request.POST.get('parent_id')
#         body = request.POST.get('body')
#         Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)
#
#         # if request.user.like.filter(article__slug=slug , user_id=request.user.id).exists():
#         #     is_true = request.user.like.all()
#         #     is_true = True
#         # else:
#         #     article['is_true'] = False
#
#     return render(request, 'Blog/article-details.html', context={'article': article,})

class ArticleDetailView(DetailView):
    model = Article
    template_name = "Blog/article-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.like.filter(article__slug=self.object.slug, user_id=self.request.user.id).exists():
            context['is_liked'] = True
        else:
            context['is_liked'] = False
        return context


def article_post(request):
    article = Article.objects.all()
    page_number = request.GET.get('page')
    print(page_number)
    paginator = Paginator(article, 1)
    object_list = paginator.get_page(page_number)
    return render(request, 'Blog/article-post.html', context={'article': object_list})


def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    article = category.articles.all()
    return render(request, 'Blog/article-post.html', context={'article': article})


def search(request):
    q = request.GET.get('q')
    article = Article.objects.filter(title__icontains=q)
    page = request.GET.get('page')
    paginator = Paginator(article, 1)
    object_list = paginator.get_page(page)
    return render(request, 'Blog/article-post.html', {'article': object_list})


def contact_us(request):
    if request.method == "POST":
        # form = ContactUSform(request.POST)
        form = MessageForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)  # در اینجا قرم ذخیره نمیشود
            instance.age += 5
            instance.save()
        # title = form.cleaned_data.get('title')
        # text = form.cleaned_data.get('text')
        # age = form.cleaned_data.get('age')
        # email = form.cleaned_data.get('email')
        # Message.objects.create(title=title, text=text, email=email, age=age)
        # print(form.cleaned_data['text'])
        # return redirect('home:home')

    else:
        form = MessageForm()
    return render(request, "Blog/contact.html", {'form': form})


def about_us(request):
    return render(request, "Blog/about_us.html", {})


def article_like(request, slug, pk):
    try:
        article_like = like.objects.get(article__slug=slug, user_id=request.user.id)
        article_like.delete()
        return JsonResponse({"response": "unliked"})
    except:
        like.objects.create(article_id=pk, user_id=request.user.id)
        return JsonResponse({"response": "liked"})

