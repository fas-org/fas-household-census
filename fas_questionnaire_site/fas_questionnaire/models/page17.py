from __future__ import unicode_literals

from django.db import models
from .household_models import Household
from .page1 import HouseholdMembers


class IncomeFromSalaries(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    worker_name = models.ForeignKey(HouseholdMembers, models.DO_NOTHING, db_column='Name of worker')
    description_of_work = models.CharField(max_length=100, db_column='Description of work', blank=True, null=True)
    place_of_work = models.CharField(max_length=50, db_column='Place of work', blank=True, null=True)
    annual_income = models.FloatField(db_column='Annual Income', default=0, null=True)
    comments = models.CharField(max_length=200, db_column='Comments', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Income from salaries artisan earnings'


class IncomeFromOtherBusinessActivities(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    name_of_worker = models.ForeignKey(HouseholdMembers, models.DO_NOTHING, db_column='Name of worker')
    description_of_work = models.CharField(db_column='Description of work', max_length=50, blank=True, null=True)
    place_of_work = models.CharField(db_column='Place of work', max_length=50, blank=True, null=True)
    production_and_sale = models.CharField(db_column='Production and sale', max_length=50, blank=True, null=True)
    cost_of_material_inputs = models.CharField(db_column='Cost of material inputs', max_length=50, blank=True,
                                               null=True)
    wages_and_salaries_paid = models.CharField(db_column='Wages and salaries paid', max_length=50, blank=True,
                                               null=True)
    rents_paid = models.CharField(db_column='Rents paid', max_length=50, blank=True, null=True)
    any_other_costs = models.CharField(db_column='Any other costs', max_length=50, blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=250, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Income from other business activities'
