from django.db import models

# Create your models here.

class News(models.Model):

    id = models.PositiveIntegerField(primary_key=True)

    title = models.CharField('Article title', max_length=255)

    image = models.ImageField(blank=True,upload_to="static/images")

    filename = models.CharField(max_length=200)

    description = models.CharField('Article description', max_length=500)

    content = models.CharField('Article content', max_length=5000)

    link = models.CharField('Article origin link', max_length=500)
