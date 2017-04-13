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
from .ownership_section3 import IrrigationFlow


class OwnershipType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Ownership Type'

    def __str__(self):
        return self.type


class WellType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Well Type'

    def __str__(self):
        return self.type


class PowerSource(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Power Source'

    def __str__(self):
        return self.source


class NatureExchange(models.Model):
    id = models.AutoField(primary_key=True)
    exchange = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Nature of Exchange'

    def __str__(self):
        return self.exchange


class OwnershipWellsTubewells(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    ownership_type = models.ForeignKey('OwnershipType', models.DO_NOTHING, db_column='Type of Ownership', blank=True, null=True)
    year_when_installed = models.IntegerField(db_column='Year when installed', blank=True, null=True)
    present_depth = models.IntegerField(db_column='Present Depth', blank=True, null=True)
    original_depth = models.IntegerField(db_column='Original Depth', blank=True, null=True)
    type = models.ForeignKey(WellType, models.DO_NOTHING, db_column='Type', blank=True, null=True)
    power_source = models.ForeignKey(PowerSource, models.DO_NOTHING, db_column='Source of Power', blank=True, null=True)
    installation_cost = models.IntegerField(db_column='Cost of installation', blank=True, null=True)
    finance_source = models.IntegerField(db_column='Source of finance', blank=True, null=True)
    expenses_last_year = models.IntegerField(db_column='Maintenance expenses last year', blank=True, null=True)
    irrigation_crop = models.CharField(max_length=50, db_column='Irrigation Crop', blank=True, null=True)
    irrigation_sale_area = models.IntegerField(db_column='Irrigation Sale Area', blank=True, null=True)
    irrigation_revenue = models.IntegerField(db_column='Irrigation Revenue', blank=True, null=True)
    exchange_nature = models.ForeignKey(NatureExchange, models.DO_NOTHING, db_column='Nature Exchange', blank=True, null=True)
    irrigation_land_extent = models.IntegerField(db_column='Irrigation Land Extent', blank=True, null=True)
    comments = models.CharField(max_length=250, db_column='Comments', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Ownership Wells'


class ProductionMeans(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Means of Production'

    def __str__(self):
        return self.type


class SpecifiedProductionMeans(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    irrigation_item_code = models.ForeignKey(IrrigationFlow, models.DO_NOTHING, db_column='Irrigation item code', blank=True, null=True)
    production_item_code = models.ForeignKey(ProductionMeans, models.DO_NOTHING, db_column='Production item code', blank=True, null=True)
    ownership_number = models.IntegerField(db_column='Ownership Number', blank=True, null=True)
    year_of_purchase = models.IntegerField(db_column='Year of Purchase', blank=True, null=True)
    price_paid = models.IntegerField(db_column='Year when installed', blank=True, null=True)
    subsidy_received = models.IntegerField(db_column='Subsidy received', blank=True, null=True)
    present_value = models.IntegerField(db_column='Present Value', blank=True, null=True)
    maintenance_charges = models.IntegerField(db_column='Maintenance charges', blank=True, null=True)
    rental_earnings = models.IntegerField(db_column='Rental earnings', blank=True, null=True)
    rental_earnings_units = models.CharField(max_length=50, db_column='Rental earning units', blank=True, null=True)
    comments = models.CharField(max_length=250, db_column='Comments', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Specified Means of Production'
