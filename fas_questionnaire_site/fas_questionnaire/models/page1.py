from __future__ import unicode_literals

from django.db import models
from .household_models import Household
from .common import PlaceOfWork


class HouseholdIntroduction(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    sample_number = models.CharField(max_length=50, db_column='Sample number', blank=True, null=True)
    os_rs_reason = models.CharField(max_length=50, db_column='Reason if OS not canvassed or if RS canvassed', blank=True, null=True)
    household_head_name = models.CharField(max_length=50, db_column='Name of head of household')
    sex = models.ForeignKey('Sex', models.DO_NOTHING, db_column='Sex')
    age = models.IntegerField(db_column='Age', blank=True, null=True)
    address = models.CharField(max_length=50, db_column='Address', blank=True, null=True)
    birth_village = models.CharField(max_length=50, db_column='Village of birth', blank=True, null=True)
    birth_tehsil = models.CharField(max_length=50, db_column='Tehsil of birth', blank=True, null=True)
    birth_district = models.CharField(max_length=50, db_column='District of birth', blank=True, null=True)
    year_of_migration = models.IntegerField(db_column='Year of migration', blank=True, null=True)
    caste_tribe = models.CharField(db_column='Caste/tribe', max_length=50, blank=True, null=True)
    sc_st = models.CharField(db_column='If SC/ST?', max_length=50, blank=True, null=True)
    religion = models.CharField(db_column='Religion',max_length=50, blank=True, null=True)
    father_name = models.CharField(db_column="Father's name",max_length=50, blank=True, null=True)
    father_occupation = models.CharField(db_column="Father's occupation",max_length=50, blank=True, null=True)
    telephone_no = models.IntegerField(db_column='Telephone number', blank=True, null=True)
    comments = models.CharField(db_column='Comments',max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Introduction'


class HouseholdMembers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    sex = models.ForeignKey('Sex', models.DO_NOTHING, db_column='sex', blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    age_unit = models.ForeignKey('CalendarGranularity', on_delete=models.CASCADE, blank=True, null=True)
    relationship = models.CharField(max_length=45, blank=True, null=True)
    marital_status =  models.ForeignKey('MaritalStatus', on_delete=models.CASCADE, blank=True, null=True)
    primary_occupation = models.CharField(max_length=100, blank=True, null=True)
    secondary_occupation = models.CharField(max_length=100, blank=True, null=True)
    tertiary_occupation = models.CharField(max_length=100, blank=True, null=True)
    place_of_work = models.ForeignKey('PlaceOfWork', on_delete=models.CASCADE, blank=True, null=True)
    literacy_status = models.ForeignKey('LiteracyStatus', on_delete=models.CASCADE, db_column='literacy_status', blank=True, null=True)
    education_level = models.CharField(max_length=45, blank=True, null=True)
    years_of_schooling = models.IntegerField(blank=True, null=True)
    name_location_of_institution = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    household = models.ForeignKey('Household', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'household_members'

    def __str__(self):
        return self.name


class LiteracyStatus(models.Model):
    status = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'literacy_status'

    def __str__(self):
        return self.status


class MaritalStatus(models.Model):
    status = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'marital_status'

    def __str__(self):
        return self.status


class CalendarGranularity(models.Model):
    unit = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'calendar_granularity'

    def __str__(self):
        return self.unit
