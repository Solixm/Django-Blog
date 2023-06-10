from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # path('detail/<slug:slug>', views.article_detail, name="article_detail"),
    path('detail/<slug:slug>', views.ArticleDetailView.as_view(), name="article_detail"),
    path('Post', views.article_post, name="article_post"),
    path('category/<int:pk>', views.category_detail, name="category_detail"),
    path('search', views.search, name="search"),
    path('contact_us', views.contact_us, name="contact_us"),
    path('about_us', views.about_us, name="about_us"),
    path('like/<slug:slug>/<int:pk>', views.article_like, name="article_like"),

]
