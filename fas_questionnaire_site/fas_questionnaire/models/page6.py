# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

from fas_questionnaire.models.common import Units, Month, YesOrNo, Crop
from .household_models import Household
from .page5 import CroppingPatternAndCropSchedule


class MarketingAgencies(models.Model):
    id = models.AutoField(primary_key=True)
    marketing_agency = models.CharField(db_column='Marketing Agency', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Marketing Agencies'

    def __str__(self):
        return self.marketing_agency


class WhereMarketed(models.Model):
    id = models.AutoField(primary_key=True)
    place_of_market = models.CharField(db_column='place of market', max_length=100, blank=True,
                                       null=True)

    class Meta:
        managed = True
        db_table = 'Where Marketed'

    def __str__(self):
        return self.place_of_market


class ModeOfTransport(models.Model):
    id = models.AutoField(primary_key=True)
    mode = models.CharField(db_column='mode', max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Mode Of Transport'

    def __str__(self):
        return self.mode


class Production(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    crop_number_first_digit = models.ForeignKey(CroppingPatternAndCropSchedule, models.DO_NOTHING,db_column='first digit',to_field= 'crop_number_first_digit',related_name='production_crop_number_first_digit',null=True, blank=True)
    crop_number_second_digit = models.ForeignKey(CroppingPatternAndCropSchedule, models.DO_NOTHING,db_column='second digit', to_field='crop_number_second_digit',related_name='production_crop_number_second_digit',null=True, blank=True)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, blank=True, null=True)

    production_main_product = models.FloatField(db_column='Production, main product', blank=True, null=True)
    unit_main_production = models.ForeignKey(Units, models.DO_NOTHING,db_column='Unit, production',blank=True, null=True,
                                             related_name='unit_main_production')
    unit_by_production = models.ForeignKey(Units, models.DO_NOTHING,db_column='Unit, by production' ,blank=True, null=True,
                                           related_name='unit_by_production')
    production_by_product = models.CharField(db_column='Production, by product', max_length=50, blank=True, null=True)

    consumption_main_product = models.FloatField(db_column='Consumption, main product', blank=True, null=True)
    unit_main_consumption = models.ForeignKey(Units, models.DO_NOTHING,db_column='Unit, main consumption', blank=True, null=True,
                                              related_name="unit_main_consumption")
    unit_by_consumption = models.ForeignKey(Units, models.DO_NOTHING,db_column='Unit, by consumption', blank=True, null=True,
                                            related_name='unit_by_consumption')
    consumption_by_product = models.CharField(db_column='Consumption, by product', max_length=50, blank=True, null=True)

    rent_and_wages_main_product = models.FloatField(db_column='Rent and Wages, main product', blank=True, null=True)
    unit_main_rent_and_wages = models.ForeignKey(Units, models.DO_NOTHING,db_column='Unit, main rent and wages', blank=True, null=True,
                                                 related_name="unit_main_rent_and_wages")
    unit_by_rent_and_wages = models.ForeignKey(Units,models.DO_NOTHING, db_column='Unit, by rent and wages', blank=True, null=True,
                                               related_name='unit_by_rent_and_wages')
    rent_and_wages_by_product = models.CharField(db_column='rent and wages, by product', max_length=50, blank=True,
                                                 null=True)

    comments = models.CharField(db_column='Comments', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'production'


class SalesOfProduction(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    crop_number_first_digit = models.FloatField(db_column='first digit', null=True, blank=True)
    crop_number_second_digit = models.FloatField(db_column='second digit', null=True, blank=True)

    sale_number = models.FloatField(db_column='Sale number', blank=True, null=True)
    commodity_sold = models.CharField(db_column='Commodity sold', max_length=50, blank=True, null=True)
    quantity = models.FloatField(db_column='Quantity', blank=True, null=True)
    unit_of_quantity = models.ForeignKey(Units,models.DO_NOTHING, db_column='Unit of quantity', blank=True, null=True,
                                         related_name='unit_of_quantity')
    month_of_disposal = models.ForeignKey(Month, models.DO_NOTHING, db_column='Month of disposal', blank=True,
                                          null=True)
    price = models.FloatField(db_column='Price', blank=True, null=True)
    unit_of_price = models.ForeignKey(Units,models.DO_NOTHING, db_column='Unit of price', blank=True, null=True,
                                      related_name='unit_of_price')
    where_marketed = models.ForeignKey(WhereMarketed, models.DO_NOTHING, db_column='Where marketed', blank=True,
                                       null=True)
    marketing_agency = models.ForeignKey(MarketingAgencies, models.DO_NOTHING, db_column='Marketing agency',
                                         max_length=50, blank=True, null=True)
    if_price_determined_in_advance = models.ForeignKey(YesOrNo, models.DO_NOTHING,
                                                       db_column='If price determined in advance', blank=True,
                                                       null=True)
    comments = models.CharField(db_column='Comments', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sales of production'
