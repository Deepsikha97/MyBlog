from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=250)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now())
    published_date=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})


class Comments(models.Model):
    post=models.ForeignKey('blog.Post',on_delete=models.CASCADE,related_name='comments')
    author=models.CharField(max_length=250)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now())
    approved_comments=models.BooleanField(default=False)

    def approve(self):
        self.approved_comments=True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")
