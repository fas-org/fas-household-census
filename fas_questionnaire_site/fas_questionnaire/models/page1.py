from __future__ import unicode_literals

from django.db import models
from .household_models import Household
from .common import Caste, Occupation, Relationship


class Religion(models.Model):
    id = models.AutoField(primary_key=True)
    religion = models.CharField(db_column='Religion', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Religion'
    def __str__(self):
        return self.religion


class Education(models.Model):
    id = models.AutoField(primary_key=True)
    level = models.CharField(db_column='Level', max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Education'
    def __str__(self):
        return self.level


class TehsilOfBirth(models.Model):
    id = models.AutoField(primary_key=True)
    tehsil = models.CharField(db_column='Tehsil', max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Tehsil of Birth'
    def __str__(self):
        return self.tehsil


class HouseholdIntroduction(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    sample_number = models.CharField(max_length=50, db_column='Sample number', blank=True, null=True)
    os_rs_reason = models.CharField(max_length=50, db_column='Reason if OS not canvassed or if RS canvassed',
                                    blank=True, null=True)
    household_head_name = models.CharField(max_length=50, db_column='Name of head of household')
    sex = models.CharField(max_length=50, db_column='Sex')
    age = models.IntegerField(db_column='Age', blank=True, null=True)
    address = models.CharField(max_length=50, db_column='Address', blank=True, null=True)
    birth_village = models.CharField(max_length=50, db_column='Birth village', blank=True, null=True)
    birth_tehsil = models.CharField(max_length=100,db_column='Tehsil of birth', blank=True,
                                     null=True)
    birth_district = models.CharField(max_length=50, db_column='District of birth', blank=True, null=True)
    year_of_migration = models.IntegerField(db_column='Year of migration', blank=True, null=True)
    caste_tribe = models.CharField(max_length=100,db_column='Caste/tribe', blank=True, null=True)
    sc_st_others = models.CharField(db_column='If SC/ST?', max_length=50, blank=True, null=True)
    religion = models.CharField(max_length=100,db_column='Religion', blank=True, null=True)
    father_name = models.CharField(db_column="Father's name", max_length=50, blank=True, null=True)
    father_occupation = models.CharField(max_length=100,db_column="Father's occupation", blank=True, null=True)
    telephone_no = models.CharField(max_length=100,db_column='Telephone number', blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Introduction'


class HouseholdMembers(models.Model):
    id = models.AutoField(primary_key=True)
    sno = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    sex = models.CharField(max_length=50, db_column='Sex',blank=True,null=True)
    age = models.IntegerField(blank=True, null=True)
    age_unit = models.CharField(max_length=100,db_column='age_unit', blank=True, null=True)
    relationship = models.CharField(max_length=100,db_column='relationship',blank=True, null=True)
    marital_status = models.CharField(max_length=100,db_column='marital status',blank=True, null=True)
    primary_occupation = models.CharField(max_length=100,db_column='primary', blank=True,
                                           null=True)
    secondary_occupation = models.CharField(max_length=100,db_column='secondary',
                                             blank=True, null=True)
    tertiary_occupation = models.CharField(max_length=100,db_column='tertiary',
                                            blank=True, null=True)
    place_of_work = models.CharField(max_length=100,db_column='place_of_work',blank=True, null=True)
    literacy_status = models.CharField(max_length=100, db_column='literacy_status',
                                        blank=True, null=True)
    education_level = models.CharField(max_length=100,db_column='education_level',blank=True, null=True)
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
        verbose_name_plural = "literacy status"

    def __str__(self):
        return self.status


class BirthVillage(models.Model):
    villageName = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'birth_village'

    def __str__(self):
        return self.villageName


class BirthDistrict(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'birth_district'

    def __str__(self):
        return self.name


class SC_ST_others(models.Model):
    caste = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'sc_st_others'
        verbose_name_plural = 'SC/ST/others'
        verbose_name = 'SC/ST/others'

    def __str__(self):
        return self.caste


class MaritalStatus(models.Model):
    status = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'marital_status'
        verbose_name_plural = "marital status"

    def __str__(self):
        return self.status


class CalendarGranularity(models.Model):
    unit = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'calendar_granularity'

    def __str__(self):
        return self.unit
