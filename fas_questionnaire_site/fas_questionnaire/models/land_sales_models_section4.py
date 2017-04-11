# This is an auto-generated Django model module. You'll have to do the
# following manually to clean this up: * Rearrange models' order * Make sure
#  each model has one field with primary_key=True * Make sure each
# ForeignKey has `on_delete` set to the desired behavior. * Remove `managed
# = False` lines if you wish to allow Django to create, modify, and delete
# the table Feel free to rename the models, but don't rename db_table values
#  or field names.
from __future__ import unicode_literals

from django.db import models
from .household_models import Household


class LandPurchasedComments(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    landpurchased_comments = models.CharField(db_column='comments', max_length=250, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Land Purchased Comments'


class LandType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'land type'

    def __str__(self):
        return self.type


class LandPurchased(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING,
                                  db_column='household')
    year_of_purchase = models.IntegerField(db_column='Year of purchase',
                                           blank=True, null=True)
    extent_of_land_bought = models.FloatField(db_column='Extent of land bought',
                                              blank=True, null=True)
    type_of_land_purchased = models.ForeignKey('LandType', models.DO_NOTHING,
                                               db_column='Type of land',
                                               blank=True, null=True)
    name_of_seller = models.CharField(db_column='Name of seller',
                                      max_length=50, blank=True, null=True)
    caste_of_seller = models.CharField(db_column='Caste of seller',
                                       max_length=50, blank=True, null=True)
    occupation_of_seller = models.CharField(db_column='Occupation of seller',
                                            max_length=50, blank=True,
                                            null=True)
    place_of_residence_of_seller = models.CharField(
        db_column='Place of residence of seller', max_length=50, blank=True,
        null=True)
    price_of_land_purchased = models.IntegerField(db_column='Price of land',
                                                  blank=True, null=True)
    purchase_transaction_number = models.FloatField(db_column='Purchase transaction number',
                                                    blank=True, null=True)
    comments = models.CharField(max_length=50, blank=True, null=True)
    landpurchased_comments = models.ForeignKey('LandPurchasedComments', models.DO_NOTHING,
                                               db_column='land purchased comments',
                                               blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Land bought'


class LandSold(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING,
                                  db_column='household')
    year_of_sale = models.IntegerField(db_column='Year of sale', blank=True,
                                       null=True)
    extent_of_land_sold = models.FloatField(db_column='Extent of land sold',
                                            blank=True, null=True)
    type_of_land_sold = models.ForeignKey('LandType', models.DO_NOTHING,
                                          db_column='Type of land', blank=True,
                                          null=True)
    name_of_buyer = models.CharField(db_column='Name of buyer', max_length=50,
                                     blank=True, null=True)
    caste_of_buyer = models.CharField(db_column='Caste of buyer',
                                      max_length=50, blank=True, null=True)
    occupation_of_buyer = models.CharField(db_column='Occupation of buyer',
                                           max_length=50, blank=True,
                                           null=True)
    place_of_residence_of_buyer = models.CharField(
        db_column='Place of residence of buyer', max_length=50, blank=True,
        null=True)
    price_of_land_sold = models.IntegerField(db_column='Price of land',
                                             blank=True, null=True)
    sale_transaction_number = models.FloatField(db_column='Sale transaction number',
                                                blank=True, null=True)
    reasons_for_sale = models.CharField(db_column='Reasons for sale',
                                        max_length=250, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Land sold'
