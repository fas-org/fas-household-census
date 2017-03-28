from django.db import models


class Household(models.Model):
    Household_number = models.IntegerField
    head_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    age = models.IntegerField
    caste = models.CharField(max_length=40)
    religion = models.CharField(max_length=40)
    birth_village = models.CharField(max_length=100)
    year_of_migration = models.DateField
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    address = models.TextField
    telephone = models.CharField(max_length=10)

