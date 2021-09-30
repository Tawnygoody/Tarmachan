from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=60, blank=False, null=False, unique=True)
    para1 = models.TextField(blank=False, null=False)
    para2 = models.TextField(blank=True, null=True)
    para3 = models.TextField(blank=True, null=True)
    image1 = models.ImageField(null=False, blank=False)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
