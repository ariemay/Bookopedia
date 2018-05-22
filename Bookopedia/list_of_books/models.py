from datetime import datetime
from django.db import models
from django.urls import reverse
# Create your models here.


def content_file_name(instance, filename):
    return '/'.join(['images/', datetime.now().strftime("%Y/%m/%d"), filename])

class Type(models.Model):
    type_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse("types:type_of_book", kwargs={"slug": self.slug})

    def __str__(self):
        return self.type_name

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    date_published = models.DateTimeField(auto_now=False, auto_now_add=True)
    number_of_pages = models.IntegerField(blank=True, null=True)
    type_of_book = models.ForeignKey(Type, default="", on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=200)
    image_file = models.ImageField(upload_to=content_file_name, default='')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_absolute_url(self):
        return reverse("book:book_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
