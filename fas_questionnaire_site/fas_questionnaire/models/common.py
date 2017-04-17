from django.db import models


class Crop(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'crop'

    def __str__(self):
        return self.name


class PlaceOfWork(models.Model):
    place = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'place_of_work'

    def __str__(self):
        return self.place
