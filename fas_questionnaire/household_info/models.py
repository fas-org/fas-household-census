from django.db import models


class Household(models.Model):
    Household_number = models.IntegerField(primary_key=True, default=0)
    head_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    age = models.IntegerField(default=None)
    caste = models.CharField(max_length=40)
    religion = models.CharField(max_length=40)
    birth_village = models.CharField(max_length=100)
    year_of_migration = models.DateField(default=None)
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    address = models.TextField(default=None)
    telephone = models.CharField(max_length=10)


class HouseholdMembers(models.Model):
    Household_number = models.ForeignKey(Household, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    age = models.IntegerField(default=None)
    relationship = models.CharField(max_length=40)
    marital_status = models.CharField(max_length=40)
    occupation = models.CharField(max_length=100)
    place_of_work = models.CharField(max_length=100)
    literacy_status = models.CharField(max_length=40)
    education_level = models.CharField(max_length=40)
    enrolled_institution = models.CharField(max_length=100)
