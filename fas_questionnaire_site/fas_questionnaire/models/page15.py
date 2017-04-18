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
from .page1 import HouseholdMembers


class LongTermWorkers(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    worker_name = models.ForeignKey(HouseholdMembers, models.DO_NOTHING, db_column='Name of worker')
    employer_name = models.CharField(max_length=100, db_column='Name of employer', blank=True, null=True)
    residence_village = models.CharField(max_length=100, db_column='Village of residence', blank=True, null=True)
    caste = models.CharField(max_length=100, db_column='Caste', blank=True, null=True)
    occupation = models.CharField(max_length=100, db_column='Occupation', blank=True, null=True)
    land_owned = models.FloatField(db_column='Land owned', blank=True, null=True)
    land_leased_in = models.FloatField(db_column='Land leased/mort in', blank=True, null=True)
    land_leased_out = models.FloatField(db_column='Land leased/mort out', blank=True, null=True)
    agricultural_labor = models.BooleanField(db_column='Agri-cultural labour', blank=True, null=True)
    operating_machines = models.BooleanField(db_column='Operating machines', blank=True, null=True)
    tending_animals = models.BooleanField(db_column='Tending animals', blank=True, null=True)
    non_agri_business = models.BooleanField(db_column='Non-agricultural businesses', blank=True, null=True)
    domestic_work = models.BooleanField(db_column='Domestic work', blank=True, null=True)
    other_activities = models.CharField(max_length=50, db_column='Other business activities', blank=True, null=True)
    months_employed = models.FloatField(db_column='Number of months for which employed last year', blank=True, null=True)
    earning_cash = models.FloatField(db_column='Earnings-cash', blank=True, null=True)
    earning_kind = models.CharField(max_length=50, db_column='Earnings-kind', blank=True, null=True)
    comments = models.CharField(max_length=250, db_column='Comments', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'For long-term workers'


class NonAgricultureWorkers(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    worker_name = models.ForeignKey(HouseholdMembers, models.DO_NOTHING, db_column='Name of worker')
    sex = models.ForeignKey('Sex', models.DO_NOTHING, db_column='Sex', blank=True, null=True)
    work_description = models.CharField(max_length=100, db_column='Description', blank=True, null=True)
    work_place = models.CharField(max_length=255, db_column='Place of work', blank=True, null=True)
    wage_form = models.CharField(max_length=50, db_column='Wage form', blank=True, null=True)
    labor_days = models.CharField(max_length=50, db_column='Labour days', blank=True, null=True)
    earning_cash = models.CharField(max_length=50, db_column='Earnings in cash', blank=True, null=True)
    earning_kind = models.CharField(max_length=50, db_column='Earnings in kind', blank=True, null=True)
    earning_total = models.CharField(max_length=50, db_column='Total Earnings', blank=True, null=True)
    comments = models.CharField(max_length=250, db_column='Comments', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Non Agricultural labouring out'
