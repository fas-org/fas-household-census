# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Household(models.Model):
    id = models.AutoField(primary_key=True)
    village = models.ForeignKey('Village', models.DO_NOTHING, db_column='village')
    household_number = models.CharField(max_length=45, db_column='household number')
    is_submitted = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'household'
        unique_together = ('village', 'household_number')


class Village(models.Model):
    id = models.AutoField(primary_key=True)
    village = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = True
        db_table = 'village'

    def __str__(self):
        return self.village
