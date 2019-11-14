from django.db import models

class Intro(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="self_image/", blank=True)

