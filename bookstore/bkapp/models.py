from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=20)
    img=models.ImageField(upload_to='media')
    desc=models.TextField()
    author=models.CharField(max_length=20)

    def __str__(self):
        return self.name

