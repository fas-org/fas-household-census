from __future__ import unicode_literals

from django.db import models
from .household_models import Household

class InformationOnInvestigators(models.Model):
    household=models.ForeignKey(Household,models.DO_NOTHING,db_column='household')
    name_of_investigator = models.CharField(db_column='Name of investigator', max_length=50, blank=True, null=True)
    date_of_interview = models.CharField(db_column='Date of interview', max_length=50, blank=True, null=True)
    time_taken = models.CharField(db_column='Time taken', max_length=50, blank=True, null=True)
    data_entry_by = models.CharField(db_column='Data entry by', max_length=100, blank=True, null=True)
    further_investigation = models.ForeignKey('YesOrNo',models.DO_NOTHING,db_column='Further investigation',blank=True,null=True)
    date_of_entry = models.CharField(db_column='Date of entry', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Information on Investigators'
