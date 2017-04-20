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
        db_table = 'Salaries artisan earnings other businesses'
