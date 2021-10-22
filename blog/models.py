from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    """
    Blog model contains information relating to each blog post
    """
    title = models.CharField(max_length=60, blank=False, null=False, unique=True)
    subheading1 = models.CharField(max_length=40, blank=True, null=True)
    para1 = models.TextField(blank=False, null=False, default="Paragraph 1")
    subheading2 = models.CharField(max_length=40, blank=True, null=True)
    para2 = models.TextField(blank=True, null=True)
    subheading3 = models.CharField(max_length=40, blank=True, null=True)
    para3 = models.TextField(blank=True, null=True)
    subheading4 = models.CharField(max_length=40, blank=True, null=True)
    para4 = models.TextField(blank=False, null=False, default="Paragraph 4")
    subheading5 = models.CharField(max_length=40, blank=True, null=True)
    para5 = models.TextField(blank=True, null=True)
    subheading6 = models.CharField(max_length=40, blank=True, null=True)
    para6 = models.TextField(blank=True, null=True)
    subheading7 = models.CharField(max_length=40, blank=True, null=True)
    para7 = models.TextField(blank=False, null=False, default="Paragraph 7")
    subheading8 = models.CharField(max_length=40, blank=True, null=True)
    para8 = models.TextField(blank=True, null=True)
    subheading9 = models.CharField(max_length=40, blank=True, null=True)
    para9 = models.TextField(blank=True, null=True)
    image1 = models.ImageField(null=True, blank=True)
    image_caption1 = models.CharField(max_length=40, blank=True, null=True)
    image2 = models.ImageField(null=True, blank=True)
    image_caption2 = models.CharField(max_length=40, blank=True, null=True)
    image3 = models.ImageField(null=True, blank=True)
    image_caption3 = models.CharField(max_length=40, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
