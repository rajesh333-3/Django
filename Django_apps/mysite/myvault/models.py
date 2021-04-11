from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Credentials(models.Model):
    app_name = models.CharField(max_length=30)
    username= models.CharField(max_length=50)
    password= models.CharField(max_length=50)
    description= models.CharField(max_length=200)
    last_updated=models.DateTimeField('Date of last update')
    def __str__(self):
        return self.app_name
