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


class IncomeFromStateAndCommonPropertyResources(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    crop_number_first_digit = models.FloatField(db_column='Crop number first digit', blank=True, null=True)
    crop_number_second_digit = models.FloatField(db_column='Crop number second digit', blank=True, null=True)
    sale_number = models.FloatField(db_column='Sale number', blank=True, null=True)
    item_collected = models.CharField(db_column='Item collected', max_length=50, blank=True, null=True)
    name_of_worker = models.CharField(db_column='Name of worker', max_length=50, blank=True, null=True)
    number_of_days_over_the_last_year = models.FloatField(db_column='Number of days over the last year', blank=True, null=True)
    commodity_sold = models.CharField(db_column='Commodity sold', max_length=50, blank=True, null=True)
    month_of_disposal = models.CharField(db_column='Month of disposal', max_length=50, blank=True, null=True)
    quantity_sold = models.FloatField(db_column='Quantity sold', blank=True, null=True)
    unit_of_quantity_consumed = models.CharField(db_column='Unit of quantity consumed', max_length=50, blank=True, null=True)
    price = models.FloatField(db_column='Price', blank=True, null=True)
    unit_of_price = models.CharField(db_column='Unit of price', max_length=50, blank=True, null=True)
    where_marketed = models.CharField(db_column='Where marketed', max_length=50, blank=True, null=True)
    marketing_agency = models.CharField(db_column='Marketing agency', max_length=50, blank=True, null=True)
    if_price_determined_in_advance = models.CharField(db_column='If price determined in advance', max_length=50, blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=250, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Income from state and common property resources'


class FreedomOfEmploymentQuestions(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    your_household_work_more_for_one_particular_employer = models.CharField(
        db_column='Your household work more for one particular employer', max_length=250, blank=True, null=True)
    members_of_your_family_free_to_work_for_wages_for_an_employer_of_their_choice = models.CharField(db_column='free to work for wages '
                                                                                                               'for an employer of their '
                                                                                                               'choice', max_length=250,
                                                                                                     blank=True, null=True)
    does_any_person_in_the_family_provide_unpaid_under_paid_labour_field = models.CharField(db_column='Does any person in the family '
                                                                                                      'provide unpaid/under-paid labour '
                                                                                                      '', max_length=250, blank=True,
                                                                                            null=True)
    is_your_household_obliged_to_perform_any_traditional_caste_duties = models.CharField(db_column='household obliged to perform '
                                                                                                   'any traditional caste duties',
                                                                                         max_length=250, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'freedom of employment questions'


class AgriculturalOrNonAgriculturalLabourServices(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    name_of_worker = models.CharField(db_column='Name of worker', max_length=50, blank=True, null=True)
    name_of_employer = models.CharField(db_column='Name of employer', max_length=50, blank=True, null=True)
    caste_of_employer = models.CharField(db_column='caste of employer', max_length=50, blank=True, null=True)
    land_owned_by_employer = models.FloatField(db_column='Land owned by employer', blank=True, null=True)
    type_of_obligation = models.CharField(db_column='Type of obligation', max_length=50, blank=True, null=True)
    description_of_task = models.CharField(db_column='Description of task', max_length=50, blank=True, null=True)
    labour_days_worked_annually = models.FloatField(db_column='Labour days worked annually', blank=True, null=True)
    hours_of_work = models.FloatField(db_column='Hours of work', blank=True, null=True)
    payment = models.FloatField(db_column='Payment', blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Agricultural or non-agricultural labour services'
