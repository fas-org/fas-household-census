from __future__ import unicode_literals
from django.db import models
from .household_models import Household


class AssetCategory(models.Model):
    id = models.AutoField(primary_key=True)
    asset_category = models.CharField(db_column='Asset Category', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Asset Category'
    def __str__(self):
        return self.asset_category



class AssetType(models.Model):
    id = models.AutoField(primary_key=True)
    asset_category_id= models.ForeignKey(AssetCategory, db_column='Asset Category id', blank=True, null=True)
    asset_type = models.CharField(db_column='Asset Type', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Asset Type'
    def __str__(self):
        return self.asset_type



class AssetOwnership(models.Model):
    household = models.ForeignKey(Household, db_column='household')
    id = models.AutoField(primary_key=True)
    type_of_asset = models.ForeignKey(AssetType, db_column='Type of asset', blank=True, null=True)
    number_of_assets_owned = models.IntegerField(db_column='Number of assets owned', default=0)
    value_of_assets = models.IntegerField(db_column='Value of assets', default=0)

    class Meta:
        managed = True
        db_table = 'Asset Ownership'

class AssetLandRegistration(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, db_column='household')
    land_registered_details = models.TextField(db_column='land registered details', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Asset Land Registration'