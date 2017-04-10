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


class HouseholdIntroduction(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    sample_number = models.CharField(max_length=50, db_column='Sample number', blank=True, null=True)
    os_rs_reason = models.CharField(max_length=50, db_column='Reason if OS not canvassed or if RS canvassed', blank=True, null=True)
    household_head_name = models.CharField(max_length=50, db_column='Name of head of household')
    sex = models.ForeignKey('Sex', models.DO_NOTHING, db_column='Sex')
    age = models.IntegerField(db_column='Age', blank=True, null=True)
    address = models.CharField(max_length=50, db_column='Address')
    birth_village = models.CharField(max_length=50, db_column='Village of birth')
    birth_tehsil = models.CharField(max_length=50, db_column='Tehsil of birth', blank=True, null=True)
    birth_district = models.CharField(max_length=50, db_column='District of birth', blank=True, null=True)
    year_of_migration = models.FloatField(db_column='Year of migration', blank=True, null=True)
    caste_tribe = models.CharField(db_column='Caste/tribe', max_length=50)
    sc_st = models.CharField(db_column='If SC/ST?', max_length=50)
    religion = models.CharField(db_column='Religion',max_length=50)
    father_name = models.CharField(db_column="Father's name",max_length=50)
    father_occupation = models.CharField(db_column="Father's occupation",max_length=50, blank=True, null=True)
    telephone_no = models.IntegerField(db_column='Telephone number', blank=True, null=True)
    comments = models.CharField(db_column='Comments',max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Introduction'



class Sex(models.Model):
    id = models.AutoField(primary_key=True)
    sex = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = True
        db_table = 'sex'

    def __str__(self):
        return self.sex
