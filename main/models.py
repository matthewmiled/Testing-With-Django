from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    intro = models.TextField()
    content = models.TextField()
    author = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title

    


