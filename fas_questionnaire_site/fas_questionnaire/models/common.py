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


class Caste(models.Model):
    id = models.AutoField(primary_key=True)
    caste = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'caste'

    def __str__(self):
        return self.caste
