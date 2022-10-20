from django.db import models

class User(models.Model):
    email = models.EmailField(verbose_name='이메일', unique=True)
    nickname = models.CharField(verbose_name='닉네임', max_length=8, null=False, unique=True)
    first_name = models.CharField(verbose_name='이름', max_length=5, null=False)
    last_name = models.CharField(verbose_name='성', max_length=5, null=False)
    phone = models.CharField(verbose_name='휴대폰', max_length=11, null=True, blank=True)

    class Meta:
        verbose_name = '유저'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email
