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


class LabourDaysEmployedInAgriculturalOperations(models.Model):

    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    crop = models.CharField(max_length=100, blank=True, null=True)
    crop_clean = models.CharField(db_column='Crop clean', max_length=250, blank=True, null=True)
    extent = models.FloatField(db_column='Extent', blank=True, null=True)
    tenurial_status = models.CharField(db_column='Tenurial status', max_length=50, blank=True, null=True)
    operation = models.CharField(db_column='Operation', max_length=255, blank=True, null=True)
    operation_clean = models.CharField(db_column='Operation clean', max_length=250, blank=True, null=True)
    operation_first_digit = models.IntegerField(db_column='Operation first digit', blank=True, null=True)
    operation_second_digit = models.IntegerField(db_column='Operation second digit', blank=True, null=True)
    operation_third_digit = models.IntegerField(db_column='Operation third digit', blank=True, null=True)
    operation_forth_digit = models.IntegerField(db_column='Operation forth digit', blank=True, null=True)
    family_labour_days_men = models.FloatField(db_column='Family labour days -men', blank=True, null=True)
    family_labour_days_women = models.FloatField(db_column='Family labour days-women', blank=True, null=True)
    family_labour_days_children = models.FloatField(db_column='Family labour days-children', blank=True, null=True)
    family_work_hours_men = models.FloatField(db_column='Family work hours-men', blank=True, null=True)
    family_work_hours_women = models.FloatField(db_column='Family work hours-women', blank=True, null=True)
    family_work_hours_children = models.FloatField(db_column='Family work hours-children', blank=True, null=True)
    daily_labour_days_men = models.FloatField(db_column='Daily labour days-men', blank=True, null=True)
    daily_labour_days_women = models.FloatField(db_column='Daily labour days-women', blank=True, null=True)
    daily_labour_days_children = models.FloatField(db_column='Daily labour days-children', blank=True, null=True)
    daily_work_hours_men = models.FloatField(db_column='Daily work hours-men', blank=True, null=True)
    daily_work_hours_women = models.FloatField(db_column='Daily work hours-women', blank=True, null=True)
    daily_work_hours_children = models.FloatField(db_column='Daily work hours-children', blank=True, null=True)
    daily_wages_male = models.CharField(db_column='Daily wages-male', max_length=50, blank=True, null=True)
    daily_wages_women = models.CharField(db_column='Daily wages-women', max_length=50, blank=True, null=True)
    daily_wages_children = models.CharField(db_column='Daily wages-children', max_length=50, blank=True, null=True)
    meal_daily_men = models.CharField(db_column='Meal daily-men', max_length=50, blank=True, null=True)
    meal_daily_women = models.CharField(db_column='Meal daily-women', max_length=50, blank=True, null=True)
    meal_daily_children = models.CharField(db_column='Meal daily-children', max_length=50, blank=True, null=True)
    exchange_labour_days_men = models.FloatField(db_column='Exchange labour days-men', blank=True, null=True)
    exchange_labour_days_women = models.FloatField(db_column='Exchange labour days-women', blank=True, null=True)
    exchange_labour_days_children = models.FloatField(db_column='Exchange labour days-children', blank=True, null=True)
    exchange_labour_hours_men = models.FloatField(db_column='Exchange labour hours-men', blank=True, null=True)
    exchange_labour_hours_women = models.FloatField(db_column='Exchange labour hours-women', blank=True, null=True)
    exchange_labour_hours_children = models.FloatField(db_column='Exchange labour hours-children', blank=True, null=True)
    meal_exchange_men = models.CharField(db_column='Meal exchange-men', max_length=50, blank=True, null=True)
    meal_exchange_women = models.CharField(db_column='Meal exchange-women', max_length=50, blank=True, null=True)
    meal_exchange_children = models.CharField(db_column='Meal exchange-children', max_length=50, blank=True, null=True)
    long_term_labour_days_men = models.FloatField(db_column='Long term labour days-men', blank=True, null=True)
    long_term_labour_days_women = models.FloatField(db_column='Long term labour days-women', blank=True, null=True)
    long_term_labour_days_children = models.FloatField(db_column='Long term labour days-children', blank=True, null=True)
    long_term_work_hrs_men = models.FloatField(db_column='Long term work hrs-men', blank=True, null=True)
    long_term_work_hrs_women = models.FloatField(db_column='Long term work hrs-women', blank=True, null=True)
    long_term_work_hrs_children = models.FloatField(db_column='Long term work hrs-children', blank=True, null=True)
    meal_long_term_men = models.CharField(db_column='Meal long term-men', max_length=50, blank=True, null=True)
    meal_long_term_women = models.CharField(db_column='Meal long term-women', max_length=50, blank=True, null=True)
    meal_long_term_children = models.CharField(db_column='Meal long term-children', max_length=50, blank=True, null=True)
    piece_rate_payment_cash = models.FloatField(db_column='Piece rate payment - cash', blank=True, null=True)
    piece_rate_payment_kind = models.CharField(db_column='Piece rate payment - kind', max_length=50, blank=True, null=True)
    machine_labour_hours = models.FloatField(db_column='Machine labour hours', blank=True, null=True)
    machine_labour_payment = models.CharField(db_column='Machine labour payment', max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Labour days employed in agricultural operations'
