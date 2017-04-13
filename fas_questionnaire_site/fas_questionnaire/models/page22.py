from __future__ import unicode_literals

from django.db import models
from .household_models import Household



class InvestigationNeeded(models.Model):
    id = models.AutoField(primary_key=True)
    instivigation_needed = models.CharField(db_column='Instivigation Needed',max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'investigation needed'
    def __str__(self):
        return str(self.instivigation_needed)

class CommentsAndInformationOnInvestigators(models.Model):
    household=models.ForeignKey(Household,models.DO_NOTHING,db_column='household')
    comments_observations = models.TextField(db_column='comments/observations', blank=True, null=True)
    name_of_investigator = models.CharField(db_column='Name of investigator', max_length=50, blank=True, null=True)
    date_of_interview = models.CharField(db_column='Date of interview', max_length=50, blank=True, null=True)
    time_taken = models.CharField(db_column='Time taken', max_length=50, blank=True, null=True)
    data_entry_by = models.CharField(db_column='Data entry by', max_length=100, blank=True, null=True)
    further_investigation = models.ForeignKey(InvestigationNeeded,models.DO_NOTHING,db_column='Further investigation',blank=True,null=True)
    date_of_entry = models.CharField(db_column='Date of entry', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Comments and Information on Investigators'
