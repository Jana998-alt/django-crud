from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.base import Model
from django.urls import reverse
# Create your models here.

class Snack(models.Model):
    title = models.TextField(max_length= 64)
    purchaser = models.ForeignKey(to = get_user_model(), on_delete= models.CASCADE)
    description = models.TextField(max_length=256)


    def get_absolute_url(self):
        return reverse('DetailView', args=[self.id])

    