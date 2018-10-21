from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.text


class Comment(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField()
    post_id = models.IntegerField(default=0)

    def __str__(self):
        return self.comment
