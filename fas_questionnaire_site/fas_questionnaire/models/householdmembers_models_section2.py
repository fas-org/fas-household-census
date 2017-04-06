from __future__ import unicode_literals
from django.db import models


class HouseholdMembers(models.Model):
    name = models.CharField(max_length=45)
    sex = models.ForeignKey('Sex', models.DO_NOTHING, db_column='sex')
    age = models.IntegerField()
    age_unit = models.ForeignKey('CalendarGranularity', models.DO_NOTHING, db_column='age_unit')
    relationship = models.CharField(max_length=45)
    marital_status = models.CharField(max_length=100)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    place_of_work = models.CharField(max_length=45, blank=True, null=True)
    literacy_status = models.ForeignKey('LiteracyStatus', models.DO_NOTHING, db_column='literacy_status')
    education_level = models.CharField(max_length=45, blank=True, null=True)
    name_location_of_institution = models.CharField(max_length=255, blank=True, null=True)
    household = models.ForeignKey('Household', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'household_members'


class LiteracyStatus(models.Model):
    status = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'literacy_status'

    def __str__(self):
        return self.status


class CalendarGranularity(models.Model):
    unit = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'calendar_granularity'

    def __str__(self):
        return self.unit