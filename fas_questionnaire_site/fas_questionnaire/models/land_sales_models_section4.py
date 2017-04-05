# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from .household_models import Household


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
    buyer = models.ForeignKey(Buyer, models.DO_NOTHING, db_column='buyer')
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

    def __str__(self):
        return self.type


class Seller(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    caste = models.CharField(max_length=45, blank=True, null=True)
    occupations = models.CharField(max_length=45, blank=True, null=True)
    place_of_residence = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'seller'
