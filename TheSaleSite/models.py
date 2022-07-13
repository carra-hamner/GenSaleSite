from django.db import models
from django.contrib.auth.models import User


class ListItem(models.Model):
    name = models.CharField(max_length=200)
    contact_email = models.EmailField()
    list_option = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name
