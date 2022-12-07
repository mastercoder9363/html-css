from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=255)
    rasm = models.CharField(max_length=255)
    categories = models.TextField()
    tags = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

