from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="کاربر")
    fathers_name = models.CharField(max_length=40, verbose_name="نام پدر")
    Melicode = models.CharField(max_length=10, unique=True, verbose_name="کدملی ")
    image = models.ImageField(upload_to='image/profile', blank=True, null=True, verbose_name="تصویر")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "نام کاریری"
        verbose_name_plural = "نام های کاربری"
