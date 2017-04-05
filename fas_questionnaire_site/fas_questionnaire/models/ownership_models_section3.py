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


class IrrigationFlow(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'irrigation_flow'


class IrrigationOwnership(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'irrigation_ownership'


class IrrigationSource(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'irrigation_source'


class CurrentOwnershipHolding(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    land_type = models.ForeignKey(LandType, models.DO_NOTHING, db_column='land_type', blank=True, null=True)
    extent_owned_land = models.IntegerField(blank=True, null=True)
    acquisition_mode = models.ForeignKey('AcquisitionMode', models.DO_NOTHING, db_column='acquisition_mode', blank=True, null=True)
    irrigation_source = models.ForeignKey('IrrigationSource', models.DO_NOTHING, db_column='irrigation_source', blank=True, null=True)
    irrigation_flow = models.ForeignKey('IrrigationFlow', models.DO_NOTHING, db_column='irrigation_flow', blank=True, null=True)
    irrigation_ownership = models.ForeignKey('IrrigationOwnership', models.DO_NOTHING, db_column='irrigation_ownership', blank=True, null=True)
    value = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'current_ownership_holding'
