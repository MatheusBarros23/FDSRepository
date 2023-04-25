from django.db import models

class Filme(models.Model):
    title = models.CharField(max_length=100)
