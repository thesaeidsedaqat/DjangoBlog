import time
from django.db import models
from accounts.models import CustomUser


class Post(models.Model):
    title = models.CharField(max_length=255)
    excerpt = models.TextField()
    body = models.TextField()
    date = models.DateTimeField(default=time.strftime("%Y-%m-%d %H:%M", time.localtime()))
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
