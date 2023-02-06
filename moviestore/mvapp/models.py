from django.db import models

class Movie(models.Model):
    name=models.CharField(max_length=40)
    image=models.ImageField(upload_to='pics')
    desc=models.TextField()
    year=models.IntegerField()

    def __str__(self):
        return self.name

