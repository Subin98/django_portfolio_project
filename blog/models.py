from django.db import models


class blog(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    image=models.ImageField(upload_to='blog/images')
    url=models.URLField(blank=True)
    date=models.DateField()
