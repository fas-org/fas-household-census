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
from .land_sales_models_section4 import LandType


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
    source = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'irrigation_source'

    def __str__(self):
        return self.source


class CurrentOwnershipHolding(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    ownership_plot_no = models.FloatField(db_column='Ownership plot no', blank=True, null=True)
    land_type = models.ForeignKey(LandType, models.DO_NOTHING, db_column='Land type', blank=True, null=True)
    extent_owned_land = models.FloatField(db_column='Extent of owned land', blank=True, null=True)
    acquisition_mode = models.ForeignKey('AcquisitionMode', models.DO_NOTHING, db_column='acquisition_mode', blank=True, null=True)
    irrigation_source = models.ForeignKey('IrrigationSource', models.DO_NOTHING, db_column='Irrigation source', blank=True, null=True)
    irrigation_flow = models.ForeignKey('IrrigationFlow', models.DO_NOTHING, db_column='Irrigation lift', blank=True, null=True)
    irrigation_ownership = models.ForeignKey('IrrigationOwnership', models.DO_NOTHING, db_column='Irrigation ownership', blank=True, null=True)
    value = models.FloatField(db_column='Value', blank=True, null=True)
    comments = models.CharField(max_length=50, db_column='Comments', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Current ownership holding'
