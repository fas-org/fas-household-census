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


class Tenurial(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(db_column='tenurial status', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tenurial'
    def __str__(self):
        return self.status


class CroppingPatternAndCropSchedule(models.Model):
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    serial_no = models.IntegerField(db_column='serial no',primary_key=True)
    crop_number_first_digit = models.FloatField(db_column='Crop number first digit', blank=True, null=True)
    crop_number_second_digit = models.FloatField(db_column='Crop number second digit', blank=True, null=True)
    crop = models.CharField(db_column='Crop', max_length=50, blank=True, null=True)
    crop_clean = models.CharField(db_column='Crop clean', max_length=50, blank=True, null=True)
    variety = models.CharField(db_column='Variety', max_length=50, blank=True, null=True)
    tenurial_status = models.ForeignKey(Tenurial, models.DO_NOTHING, db_column='tenurial status')
    crop_homestead_land = models.CharField(db_column='Crop/ Homestead land', max_length=50, blank=True, null=True)
    extent = models.FloatField(db_column='Extent', blank=True, null=True)
    month_of_sowing = models.CharField(db_column='Month of sowing', max_length=50, blank=True, null=True)
    month_of_harvesting = models.CharField(db_column='Month of harvesting', max_length=50, blank=True, null=True)
    source_of_irrigation = models.CharField(db_column='Source of irrigation', max_length=50, blank=True, null=True)
    production_main_product = models.FloatField(db_column='Production, main product', blank=True, null=True)
    unit_production = models.CharField(db_column='Unit, production', max_length=50, blank=True, null=True)
    production_by_product = models.CharField(db_column='Production, by product', max_length=50, blank=True, null=True)
    consumption_main_product = models.FloatField(db_column='Consumption, main product', blank=True, null=True)
    unit_consumption = models.CharField(db_column='Unit, consumption', max_length=50, blank=True, null=True)
    consumption_by_product = models.CharField(db_column='Consumption, by product', max_length=50, blank=True, null=True)
    loans_advances_taken_from_buyer = models.CharField(db_column='Loans/advances taken from buyer', max_length=50,
                                                       blank=True, null=True)
    principal = models.FloatField(db_column='Principal', blank=True, null=True)
    interest_on_loans_advances = models.CharField(db_column='Interest on loans/advances', max_length=50, blank=True,
                                                  null=True)
    output_price_if_fixed_in_advance = models.FloatField(db_column='Output price, if fixed in advance', blank=True,
                                                         null=True)
    other_conditions = models.CharField(db_column='Other conditions', max_length=50, blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cropping pattern and crop schedule'

    def __str__(self):
        return str(self.serial_no)


class CroppingPatternAndCropScheduleComments(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    comments_notes = models.CharField(db_column='comments/notes', max_length=500, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cropping pattern and crop schedule comments'


class  ProductionAndSales(models.Model):
    crop_serial_no = models.ForeignKey(CroppingPatternAndCropSchedule, models.DO_NOTHING, db_column='crop serial no', null=True, blank=True)
    sales_of_main_product_transportation_mode = models.CharField(db_column='sales of main product transportation mode', max_length=50, blank=True, null=True)  
    sales_of_main_product_transportation_cost = models.CharField(db_column='sales of main product transportation cost', max_length=50, blank=True, null=True)  
    sales_of_main_product_other_marketing_costs = models.CharField(db_column='sales of main product other marketing costs', max_length=50, blank=True, null=True)  
    sales_of_by_product_amt = models.CharField(db_column='sales of by product amt', max_length=50, blank=True, null=True)  
    sales_of_by_product_price = models.CharField(db_column='sales of by product price', max_length=50, blank=True, null=True)  
    quantity_of_main_product_used_for_payment = models.CharField(db_column='quantity of main product used for payment', max_length=50, blank=True, null=True)  
    quantity_of_by_product_used_for_payment = models.CharField(db_column='quantity of by product used for payment', max_length=50, blank=True, null=True)  
    household= models.ForeignKey(Household,models.DO_NOTHING,db_column='household')
    crop_number_first_digit = models.FloatField(db_column='Crop number first digit', blank=True, null=True)  
    crop_number_second_digit = models.FloatField(db_column='Crop number second digit', blank=True, null=True)  
    sale_number = models.FloatField(db_column='Sale number', blank=True, null=True)  
    commodity_sold = models.CharField(db_column='Commodity sold', max_length=50, blank=True, null=True)  
    month_of_disposal = models.CharField(db_column='Month of disposal', max_length=50, blank=True, null=True)  
    quantity = models.FloatField(db_column='Quantity', blank=True, null=True)  
    unit_of_quantity = models.CharField(db_column='Unit of quantity', max_length=50, blank=True, null=True)  
    price = models.FloatField(db_column='Price', blank=True, null=True)  
    unit_of_price = models.CharField(db_column='Unit of price', max_length=50, blank=True, null=True)  
    where_marketed = models.CharField(db_column='Where marketed', max_length=50, blank=True, null=True)  
    marketing_agency = models.CharField(db_column='Marketing agency', max_length=50, blank=True, null=True)
    if_price_determined_in_advance = models.CharField(db_column='If price determined in advance', max_length=50, blank=True, null=True)  
    comments = models.CharField(db_column='Comments', max_length=50, blank=True, null=True)
    production_main_product = models.FloatField(db_column='Production, main product', blank=True, null=True)
    production_by_product = models.CharField(db_column='Production, by product', max_length=50, blank=True, null=True)
    consumption_main_product = models.FloatField(db_column='Consumption, main product', blank=True, null=True)
    consumption_by_product = models.CharField(db_column='Consumption, by product', max_length=50, blank=True, null=True)






    class Meta:
        managed = True
        db_table = 'production and sales'


