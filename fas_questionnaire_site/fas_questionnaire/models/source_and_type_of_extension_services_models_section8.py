# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from .household_models import Household
from django.db import models


class Extension(models.Model):
    type_of_advice_received_description = models.CharField(db_column='Type of advice received-description',
                                                           max_length=250, blank=True, null=True)
    from_whom_advice_received = models.ForeignKey('CultivationAdviser', models.DO_NOTHING,
                                                  db_column='From whom advice received', blank=True, null=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')

    class Meta:
        managed = True
        db_table = 'Extension'


class CultivationAdviser(models.Model):
    adviser = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Cultivation adviser'

    def __str__(self):
        return self.adviser


class InstitutionalSupportCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(db_column='Category name', max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Institutional support category'

    def __str__(self):
        return self.category_name


class InstitutionalSupport(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    category = models.ForeignKey('InstitutionalSupportCategory', models.DO_NOTHING, db_column='Category')
    name_of_institution = models.CharField(db_column='Name of Institution', max_length=100, blank=True, null=True)
    year_of_support = models.CharField(db_column='Year of support', max_length=50, blank=True, null=True)
    nature_of_support_or_purpose = models.CharField(db_column='Nature of support/purpose', max_length=100, blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=250, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Institutional support'


class InstitutionalSupportComments(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    institutional_support_comments = models.CharField(db_column='comments', max_length=250, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Institutional support comments'
