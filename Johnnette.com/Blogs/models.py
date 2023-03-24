from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse






# Create your models here.


class Author(models.Model):
    author_name=models.CharField(max_length=150)
    author_image=models.ImageField(upload_to="Blog/Author's Image")

    def __str__(self):
        return self.author_name




class Article(models.Model):
    author=models.ForeignKey(Author,on_delete=models.CASCADE,default=None)
    title=models.CharField(max_length=500)
    date=models.DateField(blank=True)
    thumbnail_image=models.ImageField(upload_to="Blog/Artical/Thumbnail", blank=True, null=True)
    cover_image=models.ImageField(upload_to="Blog/Artical/Cover Images", blank=True, null=True)
    content=RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.title