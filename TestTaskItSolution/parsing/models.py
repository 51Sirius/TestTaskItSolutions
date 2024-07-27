from django.db import models


class Advert(models.Model):
    title = models.CharField(max_length=255)
    reference_id = models.BigIntegerField()
    author = models.CharField(max_length=255)
    views_count = models.IntegerField()
    position = models.IntegerField()