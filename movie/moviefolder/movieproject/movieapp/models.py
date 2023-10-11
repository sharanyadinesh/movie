from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=250)
    about=models.TextField()
    director=models.CharField(max_length=250)
    img=models.ImageField(upload_to="gallery")