# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

from fas_questionnaire.models.common import Units, Month, YesOrNo
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


class ProductionAndSales(models.Model):
    id = models.AutoField(primary_key=True)
    crop_serial_no = models.ForeignKey(CroppingPatternAndCropSchedule, models.DO_NOTHING, db_column='crop serial no',
                                       null=True, blank=True)
    crop = models.ForeignKey('Crop', on_delete=models.CASCADE, blank=True, null=True)
    sales_of_main_product_transportation_mode = models.ForeignKey(ModeOfTransport,models.DO_NOTHING,db_column='sales of main product transportation mode',
                                                                  blank=True, null=True)
    sales_of_main_product_transportation_cost = models.CharField(db_column='sales of main product transportation cost',
                                                                 max_length=50, blank=True, null=True)
    sales_of_main_product_other_marketing_costs = models.CharField(
        db_column='sales of main product other marketing costs', max_length=50, blank=True, null=True)
    sales_of_by_product_amt = models.CharField(db_column='sales of by product amt', max_length=50, blank=True,
                                               null=True)
    sales_of_by_product_price = models.CharField(db_column='sales of by product price', max_length=50, blank=True,
                                                 null=True)
    quantity_of_main_product_used_for_payment = models.CharField(db_column='quantity of main product used for payment',
                                                                 max_length=50, blank=True, null=True)
    quantity_of_by_product_used_for_payment = models.CharField(db_column='quantity of by product used for payment',
                                                               max_length=50, blank=True, null=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    crop_number_first_digit = models.FloatField(db_column='Crop number first digit', blank=True, null=True)
    crop_number_second_digit = models.FloatField(db_column='Crop number second digit', blank=True, null=True)
    sale_number = models.FloatField(db_column='Sale number', blank=True, null=True)
    commodity_sold = models.CharField(db_column='Commodity sold', max_length=50, blank=True, null=True)
    month_of_disposal = models.ForeignKey(Month, models.DO_NOTHING, db_column='Month of disposal', blank=True,
                                          null=True)
    quantity = models.FloatField(db_column='Quantity', blank=True, null=True)
    unit_of_quantity = models.ForeignKey(Units, db_column='Unit of quantity', blank=True, null=True,
                                         related_name='unit_of_quantity')
    price = models.FloatField(db_column='Price', blank=True, null=True)
    unit_of_price = models.ForeignKey(Units, db_column='Unit of price', blank=True, null=True,
                                      related_name='unit_of_price')
    where_marketed = models.ForeignKey(WhereMarketed, models.DO_NOTHING, db_column='Where marketed', blank=True,
                                       null=True)
    marketing_agency = models.ForeignKey(MarketingAgencies, models.DO_NOTHING, db_column='Marketing agency',
                                         max_length=50, blank=True, null=True)
    marketing_agency_value = models.CharField(db_column='marketing agency value', max_length=50, blank=True, null=True)
    if_price_determined_in_advance = models.ForeignKey(YesOrNo, models.DO_NOTHING,
                                                       db_column='If price determined in advance', blank=True,
                                                       null=True)
    comments = models.CharField(db_column='Comments', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'production and sales'
