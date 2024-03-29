from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True,null=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse("article", args=(str(self.id)))
        return reverse("home")


class Category(models.Model):
    name = models.CharField(max_length=244)

    class Meta:
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse("article", args=(str(self.id)))
        return reverse("home")

    