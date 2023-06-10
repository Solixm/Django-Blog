from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.utils.text import slugify


# ManyToOne
# ManyToMany
# OneToOne


# cascade
# set null


# set difficult

# do nothing


class Category(models.Model):
    title = models.CharField(max_length=40, verbose_name="عنوان")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


# class ArticleManager(models.Manager):
# edit class object
# def counter(self):
#     return len(self.all())
#
# def published(self):
#     return self.filter(published=True)
# def get_queryset(self):
#     return super(ArticleManager, self).get_queryset().filter(status=True)


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles", verbose_name="نوبسنده")
    category = models.ManyToManyField(Category, related_name="articles", verbose_name="دسته بندی")
    slug = models.SlugField(blank=True, unique=True, verbose_name="اسلاگ")
    title = models.CharField(max_length=70, verbose_name="عنوان")
    body = models.TextField(verbose_name="بدنه متن")
    image = models.ImageField(upload_to="image/article", verbose_name="تصویر")
    created = models.DateTimeField(auto_now_add=True, verbose_name="زمان تولید")
    updated = models.DateTimeField(auto_now=True, verbose_name="زمان ویرایش")
    floatfield = models.FloatField(default=1, verbose_name="فیلد اعداد")
    myfile = models.FileField(upload_to='test', null=True, blank=True, verbose_name="فایل")
    status = models.BooleanField(default=True, verbose_name="وضعیت")
    published = models.BooleanField(default=True, verbose_name="انتشار")

    # objects = models.Model()
    # custom_objects = ArticleManager()

    # class Meta:
    #     ordering = ('-created', '-updated')

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Article, self).save()

    class Meta:
        ordering = ('-created', '-updated')
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[self.slug])

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" height="50px" width="60px">')
        else:
            format_html('<h2>تصویری وجود ندارد</h2>')

    def __str__(self):
        return f"{self.title} - {self.body[:20]}"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name="نوبسنده")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name="کاربر")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replied', blank=True, null=True,
                               verbose_name="ارث بری ")
    body = models.TextField(verbose_name="بدنه متن")
    created = models.DateTimeField(auto_now_add=True, verbose_name="زمان تولید")

    def __str__(self):
        return self.body[:20]

    class Meta:
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"


class Message(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    text = models.TextField(verbose_name="بدنه متن")
    age = models.IntegerField(default=0, verbose_name="سن")
    email = models.EmailField(verbose_name="ایمیل")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="زمان تولید")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"


class like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر", related_name="like")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="like", verbose_name="مقاله")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.article.title}"

    class Meta:
        verbose_name = "لایک"
        verbose_name_plural = "لایک ها"
        ordering = ('-created',)
