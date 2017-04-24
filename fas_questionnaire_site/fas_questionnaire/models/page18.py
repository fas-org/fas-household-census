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
    serial_no = models.IntegerField(db_column='Serial no',blank=True,null=True)
    description_of_asset = models.ForeignKey(DescriptionOfAssets,db_column='Description of asset',blank=True,null=True)
    month_of_sale = models.ForeignKey(Month, db_column='Month of sale',blank=True,null=True)
    price_received = models.FloatField(db_column='Price received', blank=True, null=True)
    month_of_purchase = models.ForeignKey(Month, db_column='Month of purchase',blank=True,null=True)
    price_paid = models.FloatField(db_column='Price paid', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Acquisition and loss of major assets'


class ForChildrenOfAge616Years(models.Model):
    household = models.ForeignKey(Household, db_column='household')
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  
    whether_enrolled_in_eductional_institution_currently = models.NullBooleanField(db_column='Whether enrolled in eductional institution currently')  
    no_of_days_missed_school = models.IntegerField(db_column='No of days missed school', blank=True, null=True)  
    period_missed_school = models.CharField(db_column='period missed school', max_length=50, blank=True, null=True)  
    reason_for_missing_school = models.CharField(db_column='Reason for missing school', max_length=200, blank=True, null=True)  
    whether_ever_enrolled_in_school = models.NullBooleanField(db_column='Whether ever enrolled in school')  
    age_at_which_withdrawn = models.CharField(db_column='Age at which withdrawn', max_length=50, blank=True, null=True)  
    reasons_for_droppingout = models.CharField(db_column='reasons for droppingout', max_length=300, blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'For children of age 6-16 years'