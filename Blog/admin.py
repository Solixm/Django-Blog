from django.contrib import admin
# from .models import Article, Category, Comment
from . import models


# admin.site.register(Article)
# admin.site.register(Category)
# admin.site.register(Comment)
class CommentInLine(admin.TabularInline):
    model = models.Comment


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "show_image")
    list_editable = ("author",)
    list_filter = ("status",)
    search_fields = ("title", "body")
    inlines = (CommentInLine,)


admin.site.register(models.Category)
admin.site.register(models.Comment)
admin.site.register(models.Message)
admin.site.register(models.like)
