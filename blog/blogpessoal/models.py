from datetime import datetime
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    path = models.ImageField(upload_to="images/")
    date_create = models.DateTimeField(default=datetime.now, blank= True)