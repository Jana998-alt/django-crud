from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.base import Model
# Create your models here.

class Snack(models.Model):
    title = models.TextField(max_length= 64)
    purchaser = models.ForeignKey(to = get_user_model(), on_delete= models.CASCADE)
    description = models.TextField(max_length=256)