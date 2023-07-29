from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4
import os
from django.utils.timezone import now
# Create your models here.


class User(AbstractUser):
    pass


class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.category_name}"


accepted_ext = ["gif", "png", "jpg", "jpeg", "webp"]


def path_and_rename(instance, filename):
    upload_to = 'image'
    ext = filename.split('.')[-1]
    if ext not in accepted_ext:
        ext = "jpg"
    # get filename
    if instance.filename:
        filename = instance.filename
        while (Image.objects.filter(filename=filename).exists()):
            ud = '_'+uuid4().hex
            filename = '{}.{}'.format(
                instance.filename.split('.')[0]+ud[0:9], ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Image(models.Model):
    filename = models.CharField(max_length=200, blank=True, null=False)
    img = models.ImageField(upload_to=path_and_rename)

    def __str__(self):
        return f"{self.img.url}"


class LastActivityRecord(models.Model):
    last_activity = models.DateTimeField(default=now)


class Post(models.Model):
    title = models.CharField(max_length=100)
    suffix = models.CharField(max_length=100, default="")
    author = models.CharField(max_length=100)
    category = models.ManyToManyField(
        Category, blank=True, related_name="category")
    introduction = models.CharField(max_length=2000, blank=True)
    content = models.TextField()
    views = models.IntegerField(default=0)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(
        auto_now_add=True, blank=True, null=False)
    hidden = models.BooleanField(default=False, blank=False)
    priority = models.IntegerField(default=5, blank=False)
    wordCount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id} {self.title}"
