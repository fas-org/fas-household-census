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

class LandLeasedInOnFixedRent(models.Model):
    id = models.AutoField(primary_key=True)
    household_number = models.ForeignKey(Household, models.DO_NOTHING,db_column='Household number')
    plot_no = models.IntegerField(db_column='Plot no', blank=True, null=True)
    land_type = models.CharField(db_column='Land type', max_length=50, blank=True, null=True)
    extent = models.TextField(db_column='Extent', blank=True, null=True)
    name_of_lessor = models.CharField(db_column='Name of lessor', max_length=50, blank=True, null=True)
    caste_of_lessor = models.CharField(db_column='Caste of lessor', max_length=50, blank=True, null=True)
    occupation_of_lessor = models.CharField(db_column='Occupation of lessor', max_length=50, blank=True, null=True)
    registered_unregistered = models.CharField(db_column='Registered/unregistered', max_length=50, blank=True, null=True)
    type_of_contract = models.CharField(db_column='Type of contract', max_length=50, blank=True, null=True)
    since_when_leased_in = models.CharField(db_column='Since when leased in', max_length=50, blank=True, null=True)
    annual_rent_in_cash = models.CharField(db_column='Annual rent in cash', max_length=50, blank=True, null=True)
    annual_rent_in_kind = models.CharField(db_column='Annual rent in kind', max_length=50, blank=True, null=True)
    interest_free_borrowing = models.CharField(db_column='Interest free borrowing', max_length=50, blank=True, null=True)
    loan_with_interest = models.CharField(db_column='Loan with interest', max_length=50, blank=True, null=True)
    further_interest_payment_on_rent = models.CharField(db_column='Further interest payment on rent', max_length=50, blank=True, null=True)
    qty_of_hay_taken_by_owner = models.CharField(db_column='Qty of hay taken by owner', max_length=50, blank=True, null=True)
    value_of_manure_provided_by_owner = models.CharField(db_column='Value of manure provided by owner', max_length=50, blank=True, null=True)
    value_of_fertiliser_provided_by_owner = models.CharField(db_column='Value of fertiliser provided by owner', max_length=50, blank=True, null
    =True)
    value_of_seed_provided_by_owner = models.CharField(db_column='Value of seed provided by owner', max_length=50, blank=True, null=True)
    value_of_pesticide_provided_by_owner = models.CharField(db_column='Value of pesticide provided by owner', max_length=50, blank=True, null
    =True)
    value_of_electricity_provided_by_owner = models.CharField(db_column='Value of electricity provided by owner', max_length=50, blank=True, null=True)
    if_pumpset_provided_by_owner = models.CharField(db_column='If pumpset provided by owner', max_length=50, blank=True, null=True)
    if_irrigation_provided_by_owner = models.CharField(db_column='If irrigation provided by owner', max_length=50, blank=True, null=True)
    if_machinery_provided_by_owner = models.CharField(db_column='If machinery provided by owner', max_length=50, blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Land leased in on fixed rent'



class LandLeasedOutOnFixedRent(models.Model):
    id = models.AutoField(primary_key=True)
    household_number = models.ForeignKey(Household, models.DO_NOTHING,db_column='Household number')
    ownership_plot_no = models.TextField(db_column='Ownership plot no', blank=True, null=True)
    land_type = models.CharField(db_column='Land type', max_length=50, blank=True, null=True)
    extent = models.TextField(db_column='Extent', blank=True, null=True)
    name_of_lessee = models.CharField(db_column='Name of lessee', max_length=50, blank=True, null=True)
    caste_of_lessee = models.CharField(db_column='Caste of lessee', max_length=50, blank=True, null=True)
    occupation_of_lessee = models.CharField(db_column='Occupation of lessee', max_length=50, blank=True, null=True)
    registered_unregistered = models.CharField(db_column='Registered/unregistered', max_length=50, blank=True, null=True)
    type_of_contract = models.CharField(db_column='Type of contract', max_length=50, blank=True, null=True)
    since_when_leased_out = models.CharField(db_column='Since when leased out', max_length=50, blank=True, null=True)
    annual_rent_in_cash = models.CharField(db_column='Annual rent in cash', max_length=50, blank=True, null=True)
    annual_rent_in_kind = models.CharField(db_column='Annual rent in kind', max_length=50, blank=True, null=True)
    interest_free_loan_given = models.CharField(db_column='Interest free loan given', max_length=50, blank=True, null=True)
    loan_with_interest_given = models.CharField(db_column='Loan with interest given', max_length=50, blank=True, null=True)
    further_interest_on_rent = models.CharField(db_column='Further interest on rent', max_length=50, blank=True, null=True)
    qty_of_hay_taken = models.CharField(db_column='Qty of hay taken', max_length=50, blank=True, null=True)
    value_of_manure_provided_by_you = models.CharField(db_column='Value of manure provided by you', max_length=50, blank=True, null=True)
    value_of_fertiliser_provided_by_you = models.CharField(db_column='Value of fertiliser provided by you', max_length=50, blank=True, null
    =True)
    value_of_seed_provided_by_you = models.CharField(db_column='Value of seed provided by you', max_length=50, blank=True, null=True)
    value_of_pesticide_provided_by_you = models.CharField(db_column='Value of pesticide provided by you', max_length=50, blank=True, null=True)

    value_of_electricity_paid_for_by_you = models.CharField(db_column='Value of electricity paid for by you', max_length=50, blank=True, null=True)
    if_you_provided_the_pumpset = models.CharField(db_column='If you provided the pumpset', max_length=50, blank=True, null=True)
    if_irrigation_provided_by_owner = models.CharField(db_column='If irrigation provided by owner', max_length=50, blank=True, null=True)
    if_machinery_provided_by_owner = models.CharField(db_column='If machinery provided by owner', max_length=50, blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Land leased out on fixed rent'



class LandMortgagedIn(models.Model):
    id = models.AutoField(primary_key=True)
    household_number = models.ForeignKey(Household, models.DO_NOTHING,db_column='Household number')
    land_type = models.CharField(db_column='Land type', max_length=50, blank=True, null=True)
    extent = models.IntegerField(db_column='Extent', blank=True, null=True)
    name_of_mortgagor = models.CharField(db_column='Name of mortgagor', max_length=50, blank=True, null=True)
    caste_of_mortgagor = models.CharField(db_column='Caste of mortgagor', max_length=50, blank=True, null=True)
    occupation_of_mortgagor = models.CharField(db_column='Occupation of mortgagor', max_length=50, blank=True, null=True)
    year_of_mortgage = models.CharField(db_column='Year of mortgage', max_length=50, blank=True, null=True)
    mortgage_period = models.CharField(db_column='Mortgage period', max_length=50, blank=True, null=True)
    mortgage_money = models.CharField(db_column='Mortgage money', max_length=50, blank=True, null=True)
    interest_usufruct = models.CharField(db_column='Interest/usufruct', max_length=50, blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Land mortgaged in'

class LandMortgagedOut(models.Model):
    id = models.AutoField(primary_key=True)
    household_number = models.ForeignKey(Household, models.DO_NOTHING,db_column='Household number')
    land_type = models.CharField(db_column='Land type', max_length=50, blank=True, null=True)
    extent = models.IntegerField(db_column='Extent', blank=True, null=True)
    name_of_mortgagee = models.CharField(db_column='Name of mortgagee', max_length=50, blank=True, null=True)
    caste_of_mortgagee = models.CharField(db_column='Caste of mortgagee', max_length=50, blank=True, null=True)
    occupation_of_mortgagee = models.CharField(db_column='Occupation of mortgagee', max_length=50, blank=True, null=True)
    year_of_mortgage = models.CharField(db_column='Year of mortgage', max_length=50, blank=True, null=True)
    mortgage_period = models.CharField(db_column='Mortgage period', max_length=50, blank=True, null=True)
    mortgage_money = models.CharField(db_column='Mortgage money', max_length=50, blank=True, null=True)
    interest_usufruct = models.CharField(db_column='Interest/usufruct', max_length=50, blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Land mortgaged out'


class LandLeasedInOnShareRent(models.Model):
    id = models.AutoField(primary_key=True)
    household_number = models.ForeignKey(Household, models.DO_NOTHING,db_column='Household number')
    operational_plot_no = models.TextField(db_column='Operational plot no', blank=True, null=True)
    land_type = models.CharField(db_column='Land type', max_length=50, blank=True, null=True)
    extent = models.TextField(db_column='Extent', blank=True, null=True)
    name_of_lessor = models.CharField(db_column='Name of lessor', max_length=50, blank=True, null=True)
    caste_of_lessor = models.CharField(db_column='Caste of lessor', max_length=50, blank=True, null=True)
    occupation_of_lessor = models.CharField(db_column='Occupation of lessor', max_length=50, blank=True, null=True)
    registered_unregistered = models.CharField(db_column='Registered/unregistered', max_length=50, blank=True, null=True)
    seasonal_yearly_other = models.CharField(db_column='Seasonal/yearly/other', max_length=50, blank=True, null=True)
    year_of_lease = models.CharField(db_column='Year of lease', max_length=50, blank=True, null=True)
    percentage_share_of_crop = models.CharField(db_column='Percentage share of crop', max_length=50, blank=True, null=True)
    quantity_share_of_crop = models.CharField(db_column='Quantity share of crop', max_length=50, blank=True, null=True)
    percentage_share_of_by_product = models.CharField(db_column='Percentage share of by-product', max_length=50, blank=True, null=True)
    quantity_share_in_by_product = models.CharField(db_column='Quantity share in by-product', max_length=50, blank=True, null=True)
    share_in_fym_field = models.CharField(db_column='Share in FYM (%)', max_length=50, blank=True, null=True)
    share_in_fym_quantity_field = models.CharField(db_column='Share in FYM (quantity)', max_length=50, blank=True, null=True)
    share_in_fertiliser_field = models.CharField(db_column='Share in fertiliser (%)', max_length=50, blank=True, null=True)
    share_in_fertiliser_quantity_field = models.CharField(db_column='Share in fertiliser (quantity)', max_length=50, blank=True, null=True)
    share_in_seed_field = models.CharField(db_column='Share in seed (%)', max_length=50, blank=True, null=True)
    share_in_seed_quantity_field = models.CharField(db_column='Share in seed (quantity)', max_length=50, blank=True, null=True)
    share_in_pesticide_field = models.CharField(db_column='Share in pesticide (%)', max_length=50, blank=True, null=True)
    share_in_pesticide_quantity_field = models.CharField(db_column='Share in pesticide (quantity)', max_length=50, blank=True, null=True)
    share_in_electricity_field = models.CharField(db_column='Share in electricity (%)', max_length=50, blank=True, null=True)
    share_in_electricity_quantity_field = models.CharField(db_column='Share in electricity (quantity)', max_length=50, blank=True, null=True)
    share_in_pumpset_field = models.CharField(db_column='Share in pumpset (%)', max_length=50, blank=True, null=True)
    share_in_pumpset_rs_field = models.CharField(db_column='Share in pumpset (Rs)', max_length=50, blank=True, null=True)
    share_in_labour_field = models.CharField(db_column='Share in labour (%)', max_length=50, blank=True, null=True)
    share_in_labour_quantity_field = models.CharField(db_column='Share in labour (quantity)', max_length=50, blank=True, null=True)
    interest_free_loan_by_owner = models.CharField(db_column='Interest free loan by owner', max_length=50, blank=True, null=True)
    amount_of_other_loan = models.CharField(db_column='Amount of other loan', max_length=50, blank=True, null=True)
    interest_of_other_loan = models.CharField(db_column='Interest of other loan', max_length=50, blank=True, null=True)
    share_in_irrigation_field = models.CharField(db_column='Share in irrigation (%)', max_length=50, blank=True, null=True)
    share_in_irrigation_rs_field = models.CharField(db_column='Share in irrigation (Rs)', max_length=50, blank=True, null=True)
    share_in_machinery_field = models.CharField(db_column='Share in machinery (%)', max_length=50, blank=True, null=True)
    share_in_machinery_quantity_field = models.CharField(db_column='Share in machinery (quantity)', max_length=50, blank=True, null=True)
    comment = models.CharField(db_column='Comment', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Land leased in on share rent'


class LandLeasedOutOnShareRent(models.Model):
    id = models.AutoField(primary_key=True)
    household_number = models.ForeignKey(Household, models.DO_NOTHING,db_column='Household number')
    ownership_plot_no = models.TextField(db_column='Ownership plot no', blank=True, null=True)
    land_type = models.CharField(db_column='Land type', max_length=50, blank=True, null=True)
    extent = models.TextField(db_column='Extent', blank=True, null=True)
    name_of_sharecropper = models.CharField(db_column='Name of sharecropper', max_length=50, blank=True, null=True)
    caste_of_sharecropper = models.CharField(db_column='Caste of sharecropper', max_length=50, blank=True, null=True)
    occupation_of_sharecropper = models.CharField(db_column='Occupation of sharecropper', max_length=50, blank=True, null=True)
    registered_unregistered = models.CharField(db_column='Registered/unregistered', max_length=50, blank=True, null=True)
    seasonal_annual_other = models.CharField(db_column='Seasonal, annual, other', max_length=50, blank=True, null=True)
    year_of_lease = models.CharField(db_column='Year of lease', max_length=50, blank=True, null=True)
    percentage_share_of_crop = models.CharField(db_column='Percentage share of crop', max_length=50, blank=True, null=True)
    quantity_share_of_crop = models.CharField(db_column='Quantity share of crop', max_length=255, blank=True, null=True)
    percentage_share_of_by_product = models.CharField(db_column='Percentage share of by-product', max_length=50, blank=True, null=True)
    quantity_share_of_by_product = models.CharField(db_column='Quantity share of by-product', max_length=50, blank=True, null=True)
    share_in_fym_field = models.CharField(db_column='Share in FYM (%)', max_length=50, blank=True, null=True)
    share_in_fym_rs_field = models.CharField(db_column='Share in FYM (Rs)', max_length=50, blank=True, null=True)
    share_in_fertiliser_field = models.CharField(db_column='Share in fertiliser (%)', max_length=50, blank=True, null=True)
    share_in_fertiliser_rs_field = models.CharField(db_column='Share in fertiliser (Rs)', max_length=50, blank=True, null=True)
    share_in_seed_field = models.CharField(db_column='Share in seed (%)', max_length=50, blank=True, null=True)
    share_in_seed_rs_field = models.CharField(db_column='Share in seed (Rs)', max_length=50, blank=True, null=True)
    share_in_pesticide_field = models.CharField(db_column='Share in pesticide (%)', max_length=50, blank=True, null=True)
    share_in_pesticide_rs_field = models.CharField(db_column='Share in pesticide (Rs)', max_length=50, blank=True, null=True)
    share_in_electricity_field = models.CharField(db_column='Share in electricity (%)', max_length=50, blank=True, null=True)
    share_in_electricity_rs_field = models.CharField(db_column='Share in electricity (Rs)', max_length=50, blank=True, null=True)
    share_in_pumpset_field = models.CharField(db_column='Share in pumpset (%)', max_length=50, blank=True, null=True)
    share_in_pumpset_rs_field = models.CharField(db_column='Share in pumpset (Rs)', max_length=50, blank=True, null=True)
    share_in_labour_field = models.CharField(db_column='Share in labour (%)', max_length=50, blank=True, null=True)
    share_in_labour_quantity_field = models.CharField(db_column='Share in labour (quantity)', max_length=50, blank=True, null=True)
    interest_free_loan_by_owner = models.CharField(db_column='Interest free loan by owner', max_length=50, blank=True, null=True)
    amount_of_other_loan = models.CharField(db_column='Amount of other loan', max_length=50, blank=True, null=True)
    interest_of_other_loan = models.CharField(db_column='Interest of other loan', max_length=50, blank=True, null=True)
    share_in_irrigation_field = models.CharField(db_column='Share in irrigation (%)', max_length=50, blank=True, null=True)
    share_in_irrigation_rs_field = models.CharField(db_column='Share in irrigation (Rs)', max_length=50, blank=True, null=True)
    share_in_machinery_field = models.CharField(db_column='Share in machinery (%)', max_length=50, blank=True, null=True)
    share_in_machinery_quantity_field = models.CharField(db_column='Share in machinery (quantity)', max_length=50, blank=True, null=True)
    comment = models.CharField(db_column='Comment', max_length=255, blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'Land leased out on share rent'

