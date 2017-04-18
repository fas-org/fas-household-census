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
from .common import Caste, Occupation, LandType
from .page3 import Registration


class InterestUsufruct(models.Model):
    id = models.AutoField(primary_key=True)
    interestusufruct = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'interestusufruct'

    def __str__(self):
        return self.interestusufruct

class SeasonalYearlyOther(models.Model):
    id = models.AutoField(primary_key=True)
    seasonalyearlyother = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'seasonal_yearly_other'

    def __str__(self):
        return self.seasonalyearlyother

class LandMortgagedIn(models.Model):
    id = models.AutoField(primary_key=True)
    household_number = models.ForeignKey(Household, models.DO_NOTHING,db_column='Household number')
    land_type = models.ForeignKey(LandType, models.DO_NOTHING, db_column='Land type', blank=True, null=True)
    extent = models.IntegerField(db_column='Extent', blank=True, null=True)
    name_of_mortgagor = models.CharField(db_column='Name of mortgagor', max_length=50, blank=True, null=True)
    caste_of_mortgagor = models.ForeignKey(Caste, models.DO_NOTHING, db_column='Caste of mortgagor', blank=True, null=True)
    occupation_of_mortgagor = models.ForeignKey(Occupation, models.DO_NOTHING, db_column='Occupation of mortgagor', blank=True, null=True)
    year_of_mortgage = models.CharField(db_column='Year of mortgage', max_length=50, blank=True, null=True)
    mortgage_period = models.CharField(db_column='Mortgage period', max_length=50, blank=True, null=True)
    mortgage_money = models.CharField(db_column='Mortgage money', max_length=50, blank=True, null=True)
    interest_usufruct = models.ForeignKey(InterestUsufruct, models.DO_NOTHING, db_column='Interest/usufruct', blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Land mortgaged in'

class LandMortgagedOut(models.Model):
    id = models.AutoField(primary_key=True)
    household_number = models.ForeignKey(Household, models.DO_NOTHING,db_column='Household number')
    land_type = models.ForeignKey(LandType, models.DO_NOTHING, db_column='Land type', blank=True, null=True)
    extent = models.IntegerField(db_column='Extent', blank=True, null=True)
    name_of_mortgagee = models.CharField(db_column='Name of mortgagee', max_length=50, blank=True, null=True)
    caste_of_mortgagee = models.ForeignKey(Caste, models.DO_NOTHING, db_column='Caste of mortgagee', blank=True, null=True)
    occupation_of_mortgagee = models.ForeignKey(Occupation, models.DO_NOTHING, db_column='Occupation of mortgagee', blank=True, null=True)
    year_of_mortgage = models.CharField(db_column='Year of mortgage', max_length=50, blank=True, null=True)
    mortgage_period = models.CharField(db_column='Mortgage period', max_length=50, blank=True, null=True)
    mortgage_money = models.CharField(db_column='Mortgage money', max_length=50, blank=True, null=True)
    interest_usufruct = models.ForeignKey(InterestUsufruct, models.DO_NOTHING, db_column='Interest/usufruct',blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Land mortgaged out'


class LandLeasedInOnShareRent(models.Model):
    id = models.AutoField(primary_key=True)
    household_number = models.ForeignKey(Household, models.DO_NOTHING,db_column='Household number')
    operational_plot_no = models.CharField(db_column='Operational plot no', max_length=50, blank=True, null=True)
    land_type = models.ForeignKey(LandType, models.DO_NOTHING, db_column='Land type', blank=True, null=True)
    extent = models.IntegerField(db_column='Extent', blank=True, null=True)
    name_of_lessor = models.CharField(db_column='Name of lessor', max_length=50, blank=True, null=True)
    caste_of_lessor = models.ForeignKey(Caste, models.DO_NOTHING, db_column='Caste of lessor', blank=True, null=True)
    occupation_of_lessor = models.CharField(db_column='Occupation of lessor', max_length=50, blank=True, null=True)
    registered_unregistered = models.ForeignKey(Registration, models.DO_NOTHING, db_column='Registered/unregistered', blank=True, null=True)
    #seasonal_yearly_other = models.CharField(db_column='Seasonal/yearly/other', max_length=50, blank=True, null=True)
    seasonal_yearly_other = models.ForeignKey(SeasonalYearlyOther, models.DO_NOTHING, db_column='Seasonal/yearly/other', blank=True, null=True)
    year_of_lease = models.CharField(db_column='Year of lease', max_length=50, blank=True, null=True)
    percentage_share_of_crop = models.CharField(db_column='Percentage share of crop', max_length=50, blank=True, null=True)
    quantity_share_of_crop = models.CharField(db_column='Quantity share of crop', max_length=50, blank=True, null=True)
    percentage_share_of_by_product = models.CharField(db_column='Percentage share of by-product', max_length=50, blank=True, null=True)
    quantity_share_in_by_product = models.CharField(db_column='Quantity share in by-product', max_length=50, blank=True, null=True)
    share_in_fym_field = models.CharField(db_column='Share in FYM percentage', max_length=50, blank=True, null=True)
    share_in_fym_quantity_field = models.CharField(db_column='Share in FYM (quantity)', max_length=50, blank=True, null=True)
    share_in_fertiliser_field = models.CharField(db_column='Share in fertiliser percentage', max_length=50, blank=True, null=True)
    share_in_fertiliser_quantity_field = models.CharField(db_column='Share in fertiliser (quantity)', max_length=50, blank=True, null=True)
    share_in_seed_field = models.CharField(db_column='Share in seed percentage', max_length=50, blank=True, null=True)
    share_in_seed_quantity_field = models.CharField(db_column='Share in seed (quantity)', max_length=50, blank=True, null=True)
    share_in_pesticide_field = models.CharField(db_column='Share in pesticide percentage', max_length=50, blank=True, null=True)
    share_in_pesticide_quantity_field = models.CharField(db_column='Share in pesticide (quantity)', max_length=50, blank=True, null=True)
    share_in_electricity_field = models.CharField(db_column='Share in electricity percentage', max_length=50, blank=True, null=True)
    share_in_electricity_quantity_field = models.CharField(db_column='Share in electricity (quantity)', max_length=50, blank=True, null=True)
    share_in_pumpset_field = models.CharField(db_column='Share in pumpset percentage', max_length=50, blank=True, null=True)
    share_in_pumpset_rs_field = models.CharField(db_column='Share in pumpset (Rs)', max_length=50, blank=True, null=True)
    share_in_labour_field = models.CharField(db_column='Share in labour percentage', max_length=50, blank=True, null=True)
    share_in_labour_quantity_field = models.CharField(db_column='Share in labour (quantity)', max_length=50, blank=True, null=True)
    share_in_irrigation_field = models.CharField(db_column='Share in irrigation percentage', max_length=50, blank=True, null=True)
    share_in_irrigation_rs_field = models.CharField(db_column='Share in irrigation (Rs)', max_length=50, blank=True, null=True)
    share_in_machinery_field = models.CharField(db_column='Share in machinery percentage', max_length=50, blank=True, null=True)
    share_in_machinery_quantity_field = models.CharField(db_column='Share in machinery (quantity)', max_length=50, blank=True, null=True)
    interest_free_loan_by_owner = models.CharField(db_column='Interest free loan by owner', max_length=50, blank=True, null=True)
    amount_of_other_loan = models.CharField(db_column='Amount of other loan', max_length=50, blank=True, null=True)
    interest_of_other_loan = models.CharField(db_column='Interest of other loan', max_length=50, blank=True, null=True)
    comment = models.CharField(db_column='Comment', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Land leased in on share rent'


class LandLeasedOutOnShareRent(models.Model):
    id = models.AutoField(primary_key=True)
    household_number = models.ForeignKey(Household, models.DO_NOTHING,db_column='Household number')
    ownership_plot_no = models.CharField(db_column='Ownership plot no', max_length=50,blank=True, null=True)
    land_type = models.ForeignKey(LandType, models.DO_NOTHING, db_column='Land type', blank=True, null=True)
    extent = models.IntegerField(db_column='Extent', blank=True, null=True)
    name_of_sharecropper = models.CharField(db_column='Name of sharecropper', max_length=50, blank=True, null=True)
    caste_of_sharecropper = models.ForeignKey(Caste, models.DO_NOTHING, db_column='Caste of sharecropper', blank=True, null=True)
    occupation_of_sharecropper = models.CharField(db_column='Occupation of sharecropper', max_length=50, blank=True, null=True)
    registered_unregistered = models.ForeignKey(Registration, models.DO_NOTHING, db_column='Registered/unregistered', blank=True, null=True)
    seasonal_annual_other = models.ForeignKey(SeasonalYearlyOther, models.DO_NOTHING, db_column='Seasonal, annual, other', blank=True, null=True)
    year_of_lease = models.CharField(db_column='Year of lease', max_length=50, blank=True, null=True)
    percentage_share_of_crop = models.CharField(db_column='Percentage share of crop', max_length=50, blank=True, null=True)
    quantity_share_of_crop = models.CharField(db_column='Quantity share of crop', max_length=255, blank=True, null=True)
    percentage_share_of_by_product = models.CharField(db_column='Percentage share of by-product', max_length=50, blank=True, null=True)
    quantity_share_of_by_product = models.CharField(db_column='Quantity share of by-product', max_length=50, blank=True, null=True)
    share_in_fym_field = models.CharField(db_column='Share in FYM percentage', max_length=50, blank=True, null=True)
    share_in_fym_rs_field = models.CharField(db_column='Share in FYM (Rs)', max_length=50, blank=True, null=True)
    share_in_fertiliser_field = models.CharField(db_column='Share in fertiliser percentage', max_length=50, blank=True, null=True)
    share_in_fertiliser_rs_field = models.CharField(db_column='Share in fertiliser (Rs)', max_length=50, blank=True, null=True)
    share_in_seed_field = models.CharField(db_column='Share in seed percentage', max_length=50, blank=True, null=True)
    share_in_seed_rs_field = models.CharField(db_column='Share in seed (Rs)', max_length=50, blank=True, null=True)
    share_in_pesticide_field = models.CharField(db_column='Share in pesticide percentage', max_length=50, blank=True, null=True)
    share_in_pesticide_rs_field = models.CharField(db_column='Share in pesticide (Rs)', max_length=50, blank=True, null=True)
    share_in_electricity_field = models.CharField(db_column='Share in electricity percentage', max_length=50, blank=True, null=True)
    share_in_electricity_rs_field = models.CharField(db_column='Share in electricity (Rs)', max_length=50, blank=True, null=True)
    share_in_pumpset_field = models.CharField(db_column='Share in pumpset percentage', max_length=50, blank=True, null=True)
    share_in_pumpset_rs_field = models.CharField(db_column='Share in pumpset (Rs)', max_length=50, blank=True, null=True)
    share_in_labour_field = models.CharField(db_column='Share in labour percentage', max_length=50, blank=True, null=True)
    share_in_labour_quantity_field = models.CharField(db_column='Share in labour (quantity)', max_length=50, blank=True, null=True)
    interest_free_loan_by_owner = models.CharField(db_column='Interest free loan by owner', max_length=50, blank=True, null=True)
    amount_of_other_loan = models.CharField(db_column='Amount of other loan', max_length=50, blank=True, null=True)
    interest_of_other_loan = models.CharField(db_column='Interest of other loan', max_length=50, blank=True, null=True)
    share_in_irrigation_field = models.CharField(db_column='Share in irrigation percentage', max_length=50, blank=True, null=True)
    share_in_irrigation_rs_field = models.CharField(db_column='Share in irrigation (Rs)', max_length=50, blank=True, null=True)
    share_in_machinery_field = models.CharField(db_column='Share in machinery percentage', max_length=50, blank=True, null=True)
    share_in_machinery_quantity_field = models.CharField(db_column='Share in machinery (quantity)', max_length=50, blank=True, null=True)
    comment = models.CharField(db_column='Comment', max_length=255, blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'Land leased out on share rent'



