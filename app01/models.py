from django.db import models

# Create your models here.


class UserType(models.Model):
    caption = models.CharField(max_length=32)


class UserGroup(models.Model):
    name = models.CharField(max_length=32)

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField()
    user_type = models.ForeignKey(to='UserType',to_field='id')
    u2g = models.ManyToManyField(UserGroup)


class Category(models.Model):
    caption = models.CharField(max_length=32)

class ArticleType(models.Model):
    caption = models.CharField(max_length=32)

class Article(models.Model):
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    article_type = models.ForeignKey(ArticleType)