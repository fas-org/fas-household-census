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
from .common import LandType, Caste, Occupation


class AcquisitionMode(models.Model):
    id = models.AutoField(primary_key=True)
    acquisition = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'acquisition_mode'

    def __str__(self):
        return self.acquisition


class IrrigationFlow(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'irrigation_flow'

    def __str__(self):
        return self.type


class IrrigationOwnership(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'irrigation_ownership'

    def __str__(self):
        return self.owner


class IrrigationSource(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=100,unique=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'irrigation_source'

    def __str__(self):
        return self.source


class CurrentOwnershipHolding(models.Model):
    id = models.AutoField(primary_key=True)
    sno = models.PositiveIntegerField(blank=True, null=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    land_type = models.CharField(max_length=100,db_column='Land type', blank=True, null=True)
    extent_owned_land = models.CharField(max_length=100,db_column='Extent of owned land', blank=True, null=True)
    acquisition_mode = models.CharField(max_length=100,db_column='acquisition_mode', blank=True,
                                         null=True)
    irrigation_source = models.CharField(max_length=100,db_column='Irrigation source',
                                          blank=True, null=True)
    irrigation_flow = models.CharField(max_length=100, db_column='Irrigation lift', blank=True,
                                        null=True)
    irrigation_ownership = models.CharField(max_length=100, db_column='Irrigation ownership',
                                             blank=True, null=True)
    value = models.FloatField(db_column='Value', blank=True, null=True)
    comments = models.CharField(max_length=50, db_column='Comments', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Current ownership holding'


class HomesteadComponents(models.Model):
    id = models.AutoField(primary_key=True)
    components = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Homestead Components'

    def __str__(self):
        return self.components


class HomesteadArea(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    sno = models.PositiveIntegerField(blank=True, null=True)
    components = models.CharField(max_length=100, db_column='Components', blank=True,
                                   null=True)
    area = models.CharField(max_length=100, db_column='Area', blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Homestead Area'


class LandPurchased(models.Model):
    id = models.AutoField(primary_key=True)
    sno = models.PositiveIntegerField(blank=True, null=True)
    household = models.ForeignKey(Household, models.DO_NOTHING,
                                  db_column='household')
    year_of_purchase = models.CharField(max_length=100, db_column='Year of purchase',
                                           blank=True, null=True)
    extent_of_land_bought = models.CharField(max_length=100,db_column='Extent of land bought',
                                              blank=True, null=True)
    type_of_land_purchased = models.CharField(max_length=100,
                                               db_column='Type of land',
                                               blank=True, null=True)
    name_of_seller = models.CharField(db_column='Name of seller',
                                      max_length=50, blank=True, null=True)
    caste_of_seller = models.CharField(max_length=100,db_column='Caste of seller',
                                        blank=True, null=True)
    occupation_of_seller = models.CharField(max_length=100, db_column='Occupation of seller',
                                             blank=True,
                                             null=True)
    place_of_residence = models.CharField(
        db_column='Place of residence of seller', max_length=50, blank=True,
        null=True)
    price_of_land_purchased = models.IntegerField(db_column='Price of land',
                                                  blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Land bought'


class LandSold(models.Model):
    id = models.AutoField(primary_key=True)
    sno = models.PositiveIntegerField(blank=True, null=True)
    household = models.ForeignKey(Household, models.DO_NOTHING,
                                  db_column='household')
    year_of_sale = models.CharField(max_length=100,db_column='Year of sale', blank=True,
                                       null=True)
    extent_of_land_sold = models.CharField(max_length=100,db_column='Extent of land sold',
                                            blank=True, null=True)
    type_of_land_sold = models.CharField(max_length=100,
                                          db_column='Type of land', blank=True,
                                          null=True)
    name_of_buyer = models.CharField(db_column='Name of buyer', max_length=50,
                                     blank=True, null=True)
    caste_of_buyer = models.CharField(max_length=100,db_column='Caste of buyer',
                                       blank=True, null=True)
    occupation_of_buyer = models.CharField(max_length=100, db_column='Occupation of buyer', blank=True,
                                            null=True)
    place_of_residence = models.CharField(
        db_column='Place of residence of buyer', max_length=50, blank=True,
        null=True)
    price_of_land_sold = models.IntegerField(db_column='Price of land',
                                             blank=True, null=True)
    reasons_for_sale = models.CharField(db_column='Reasons for sale',
                                        max_length=250, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Land sold'


class PlaceOfResidence(models.Model):
    place = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'place_of_residence'

    def __str__(self):
        return self.place