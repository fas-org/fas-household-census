from __future__ import unicode_literals

from django.db import models
from .household_models import Household



class CommentsAndInformationOnInvestigators(models.Model):
    household=models.ForeignKey(Household,models.DO_NOTHING,db_column='household')
    comments_observations = models.TextField(db_column='comments/observations', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    name_of_investigator = models.CharField(db_column='Name of investigator', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_of_interview = models.CharField(db_column='Date of interview', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    time_taken = models.CharField(db_column='Time taken', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_entry_by = models.CharField(db_column='Data entry by', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    further_investigation = models.CharField(db_column='Further investigation', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_of_entry = models.CharField(db_column='Date of entry', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'Comments and Information on Investigators'