from django.db import models

from account.models import User

class Category(models.Model):
    category_name = models.CharField(verbose_name='카테고리', max_length=10)

    class Meta:
        verbose_name = '카테고리명'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category_name

class Board(models.Model):
    user = models.ForeignKey(User, verbose_name='유저', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='카테고리', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='제목', max_length=10)
    content = models.TextField(verbose_name='내용')

    class Meta:
        verbose_name = '게시글'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
