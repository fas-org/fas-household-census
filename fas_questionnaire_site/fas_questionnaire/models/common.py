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


class LandType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'land type'

    def __str__(self):
        return self.type


class Sex(models.Model):
    id = models.AutoField(primary_key=True)
    sex = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = True
        db_table = 'sex'

    def __str__(self):
        return self.sex


class Occupation(models.Model):
    id = models.AutoField(primary_key=True)
    occupation = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'occupation'

    def __str__(self):
        return self.occupation


class Caste(models.Model):
    id = models.AutoField(primary_key=True)
    caste = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'caste'

    def __str__(self):
        return self.caste


class Units(models.Model):
    id = models.AutoField(primary_key=True)
    unit = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'units'

    def __str__(self):
        return self.unit
