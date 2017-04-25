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


class Institution(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Institution'

    def __str__(self):
        return self.name


class SupportNature(models.Model):
    id = models.AutoField(primary_key=True)
    support = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Support Nature'

    def __str__(self):
        return self.support


class Month(models.Model):
    id = models.AutoField(primary_key=True)
    month = models.CharField(db_column='Month',max_length=100)

    class Meta:
        managed = True
        db_table = 'Month'

    def __str__(self):
        return self.month


class Relationship(models.Model):
    id = models.AutoField(primary_key=True)
    relationship = models.CharField(db_column='Relationship', max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Relationship'
