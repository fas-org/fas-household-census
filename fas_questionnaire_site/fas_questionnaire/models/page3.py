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
from .common import LandType, Caste, Units


class Registration(models.Model):
    id = models.AutoField(primary_key=True)
    registration = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'registration'

    def __str__(self):
        return self.registration


class TypeOfContract(models.Model):
    id = models.AutoField(primary_key=True)
    type_of_contract = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'type_of_contract'

    def __str__(self):
        return self.type_of_contract


class LandLeasedInOnFixedRent(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    plot_no = models.IntegerField(db_column='Plot no', blank=True, null=True)
    land_type = models.CharField(max_length=100, db_column='Land type', blank=True, null=True)
    extent = models.IntegerField(db_column='Extent', blank=True, null=True)
    unit_of_extent = models.ForeignKey(Units, models.DO_NOTHING, db_column='unit of extent', blank=True, null=True)
    name_of_lessor = models.CharField(db_column='Name of lessor', max_length=50, blank=True, null=True)
    caste_of_lessor = models.CharField(max_length=100,db_column='Caste of lessor', blank=True, null=True)
    occupation_of_lessor = models.CharField(db_column='Occupation of lessor', max_length=50, blank=True, null=True)
    registered_unregistered = models.CharField(max_length=100,db_column='Registered/unregistered',
                                                blank=True, null=True)
    type_of_contract = models.CharField(max_length=100,db_column='Type of contract', blank=True,
                                         null=True)
    since_when_leased_in = models.CharField(db_column='Since when leased in', max_length=50, blank=True, null=True)
    annual_rent_in_cash = models.CharField(db_column='Annual rent in cash', max_length=50, blank=True, null=True)
    annual_rent_in_kind = models.CharField(db_column='Annual rent in kind', max_length=50, blank=True, null=True)
    interest_free_borrowing = models.CharField(db_column='Interest free borrowing', max_length=50, blank=True,
                                               null=True)
    loan_with_interest = models.CharField(db_column='Loan with interest', max_length=50, blank=True, null=True)
    further_interest_payment_on_rent = models.CharField(db_column='Further interest payment on rent', max_length=50,
                                                        blank=True, null=True)
    qty_of_hay_taken_by_owner = models.CharField(db_column='Qty of hay taken by owner', max_length=50, blank=True,
                                                 null=True)
    value_of_manure_provided_by_owner = models.CharField(db_column='Value of manure provided by owner', max_length=50,
                                                         blank=True, null=True)
    value_of_fertiliser_provided_by_owner = models.CharField(db_column='Value of fertiliser provided by owner',
                                                             max_length=50, blank=True, null
                                                             =True)
    value_of_seed_provided_by_owner = models.CharField(db_column='Value of seed provided by owner', max_length=50,
                                                       blank=True, null=True)
    value_of_pesticide_provided_by_owner = models.CharField(db_column='Value of pesticide provided by owner',
                                                            max_length=50, blank=True, null
                                                            =True)
    value_of_electricity_provided_by_owner = models.CharField(db_column='Value of electricity provided by owner',
                                                              max_length=50, blank=True, null=True)
    if_pumpset_provided_by_owner = models.CharField(db_column='If pumpset provided by owner', max_length=50, blank=True,
                                                    null=True)
    if_irrigation_provided_by_owner = models.CharField(db_column='If irrigation provided by owner', max_length=50,
                                                       blank=True, null=True)
    if_machinery_provided_by_owner = models.CharField(db_column='If machinery provided by owner', max_length=50,
                                                      blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Land leased in on fixed rent'


class LandLeasedOutOnFixedRent(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    ownership_plot_no = models.IntegerField(db_column='Ownership plot no', blank=True, null=True)
    land_type = models.CharField(max_length=100, db_column='Land type', blank=True, null=True)
    extent = models.IntegerField(db_column='Extent', blank=True, null=True)
    unit_of_extent = models.ForeignKey(Units, models.DO_NOTHING, db_column='unit of extent', blank=True, null=True)
    name_of_lessee = models.CharField(db_column='Name of lessee', max_length=50, blank=True, null=True)
    caste_of_lessee = models.CharField(max_length=100,db_column='Caste of lessee', blank=True, null=True)
    occupation_of_lessee = models.CharField(db_column='Occupation of lessee', max_length=50, blank=True, null=True)
    registered_unregistered = models.CharField(max_length=100, db_column='Registered/unregistered',
                                                blank=True, null=True)
    type_of_contract = models.CharField(max_length=100, db_column='Type of contract', blank=True,
                                         null=True)
    since_when_leased_out = models.CharField(db_column='Since when leased out', max_length=50, blank=True, null=True)
    annual_rent_in_cash = models.CharField(db_column='Annual rent in cash', max_length=50, blank=True, null=True)
    annual_rent_in_kind = models.CharField(db_column='Annual rent in kind', max_length=50, blank=True, null=True)
    interest_free_loan_given = models.CharField(db_column='Interest free loan given', max_length=50, blank=True,
                                                null=True)
    loan_with_interest_given = models.CharField(db_column='Loan with interest given', max_length=50, blank=True,
                                                null=True)
    further_interest_on_rent = models.CharField(db_column='Further interest on rent', max_length=50, blank=True,
                                                null=True)
    qty_of_hay_taken = models.CharField(db_column='Qty of hay taken', max_length=50, blank=True, null=True)
    value_of_manure_provided_by_you = models.CharField(db_column='Value of manure provided by you', max_length=50,
                                                       blank=True, null=True)
    value_of_fertiliser_provided_by_you = models.CharField(db_column='Value of fertiliser provided by you',
                                                           max_length=50, blank=True, null
                                                           =True)
    value_of_seed_provided_by_you = models.CharField(db_column='Value of seed provided by you', max_length=50,
                                                     blank=True, null=True)
    value_of_pesticide_provided_by_you = models.CharField(db_column='Value of pesticide provided by you', max_length=50,
                                                          blank=True, null=True)

    value_of_electricity_paid_for_by_you = models.CharField(db_column='Value of electricity paid for by you',
                                                            max_length=50, blank=True, null=True)
    if_you_provided_the_pumpset = models.CharField(db_column='If you provided the pumpset', max_length=50, blank=True,
                                                   null=True)
    if_irrigation_provided_by_owner = models.CharField(db_column='If irrigation provided by owner', max_length=50,
                                                       blank=True, null=True)
    if_machinery_provided_by_owner = models.CharField(db_column='If machinery provided by owner', max_length=50,
                                                      blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Land leased out on fixed rent'
