from __future__ import unicode_literals
from django.db import models
from .household_models import Household


class DescriptionOfAssets(models.Model):
    id = models.AutoField(primary_key=True)
    asset_name = models.CharField(db_column='asset name', max_length= 100,blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Description of assets'

    def __str__(self):
        return self.asset_name


class Month(models.Model):
    id = models.AutoField(primary_key=True)
    month = models.CharField(db_column='Month',max_length=100)

    class Meta:
        managed = True
        db_table = 'Month'

    def __str__(self):
        return self.month


class AcquisitionAndLossOfMajorAssets(models.Model):
    household = models.ForeignKey(Household, db_column='household')
    id = models.AutoField(primary_key=True)
    serial_no = models.IntegerField(db_column='Serial no')
    description_of_asset = models.ForeignKey(DescriptionOfAssets,db_column='Description of asset',blank=True)
    month_of_sale = models.ForeignKey(Month, db_column='Month of sale')
    price_received = models.FloatField(db_column='Price received', blank=True, null=True)
    month_of_purchase = models.ForeignKey(Month, db_column='Month of purchase')
    price_paid = models.FloatField(db_column='Price paid', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Acquisition and loss of major assets'
