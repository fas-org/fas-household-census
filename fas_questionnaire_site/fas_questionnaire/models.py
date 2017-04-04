# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Household(models.Model):
    id = models.AutoField(primary_key=True)
    village = models.CharField(max_length=45)
    household_number = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'household'
        unique_together = (('id', 'village', 'household_number'),)


class HouseholdIntroduction(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    household_head_name = models.CharField(max_length=45)
    sex = models.ForeignKey('Sex', models.DO_NOTHING, db_column='sex')
    age = models.IntegerField()
    caste_tribe = models.CharField(max_length=45)
    religion = models.CharField(max_length=45)
    birth_village_tehsil = models.CharField(max_length=200)
    year_of_migration = models.IntegerField(blank=True, null=True)
    father_name = models.CharField(max_length=45)
    father_occupation = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=500)
    telephone_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'household_introduction'


class Sex(models.Model):
    id = models.AutoField(primary_key=True)
    sex = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = True
        db_table = 'sex'

    def __str__(self):
        return self.sex


class Buyer(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    caste = models.CharField(max_length=45, blank=True, null=True)
    occupations = models.CharField(max_length=45, blank=True, null=True)
    place_of_residence = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'buyer'


class LandBought(models.Model):
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    year_of_purchase = models.IntegerField(blank=True, null=True)
    extent = models.CharField(max_length=50, blank=True, null=True)
    type_of_land = models.ForeignKey('LandType', models.DO_NOTHING, db_column='type_of_land', blank=True, null=True)
    seller = models.ForeignKey('Seller', models.DO_NOTHING, db_column='seller', blank=True, null=True)
    price_of_land = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'land_bought'


class LandSold(models.Model):
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    year_of_sale = models.IntegerField(blank=True, null=True)
    extent = models.CharField(max_length=50, blank=True, null=True)
    type_of_land = models.ForeignKey('LandType', models.DO_NOTHING, db_column='type_of_land', blank=True, null=True)
    buyer = models.ForeignKey(Buyer, models.DO_NOTHING, db_column='buyer', blank=True, null=True)
    price_of_land = models.IntegerField(blank=True, null=True)
    reasons_for_sale = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'land_sold'


class LandType(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'land_type'


class Seller(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    caste = models.CharField(max_length=45, blank=True, null=True)
    occupations = models.CharField(max_length=45, blank=True, null=True)
    place_of_residence = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'seller'
