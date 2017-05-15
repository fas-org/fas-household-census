from django.db import models


class ManureType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(db_column='manure_type', max_length=100, unique=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'manure_type'

    def __str__(self):
        return self.type


class FertilizerType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(db_column='manure_type', max_length=100, unique=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fertilizer_type'

    def __str__(self):
        return self.type


class InputUseManure(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey('Household', models.DO_NOTHING, db_column='household', blank=True, null=True)
    crop_code = models.IntegerField(blank=True, null=True)
    manure_type = models.CharField(max_length=100,blank=True, null=True)
    manure_home_quantity = models.FloatField(blank=True, null=True)
    manure_home_unit = models.CharField(max_length=100, blank=True, null=True)
    manure_home_value = models.FloatField(blank=True, null=True)
    manure_purchased_quantity = models.FloatField(blank=True, null=True)
    manure_purchased_unit = models.CharField(max_length=100, blank=True, null=True)
    manure_purchased_value = models.FloatField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'input_use_manure'


class InputUsePlantProtection(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey('Household', models.DO_NOTHING, db_column='household', blank=True, null=True)
    crop_code = models.IntegerField(blank=True, null=True)
    plant_protection_quantity = models.FloatField(blank=True, null=True)
    plant_protection_value = models.FloatField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'input_use_plant_protection'


class InputUseIrrigation(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey('Household', models.DO_NOTHING, db_column='household', blank=True, null=True)
    crop_code = models.IntegerField(blank=True, null=True)
    irrigation_source = models.CharField(max_length=100, blank=True, null=True)
    irrigation_cost = models.FloatField(blank=True, null=True)
    irrigation_unit_price = models.CharField(max_length=100, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'input_use_irrigation'


class InputUseFertiliser(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey('Household', models.DO_NOTHING, db_column='household', blank=True, null=True)
    crop_code = models.IntegerField(blank=True, null=True)
    fertiliser_type = models.CharField(max_length=100, blank=True, null=True)
    fertiliser_quantity = models.FloatField(blank=True, null=True)
    fertiliser_unit = models.CharField(max_length=100,blank=True, null=True)
    fertiliser_value = models.FloatField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'input_use_fertiliser'


class InputUseSeeds(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey('Household', models.DO_NOTHING, db_column='household', blank=True, null=True)
    crop_code_first_digit = models.IntegerField(blank=True, null=True)
    crop_code_second_digit = models.IntegerField(blank=True, null=True)
    home_produced_quantity = models.FloatField(blank=True, null=True)
    home_produced_unit = models.CharField(max_length=100, blank=True, null=True)
    home_produced_value = models.CharField(max_length=50, blank=True, null=True)
    purchased_quantity = models.FloatField(blank=True, null=True)
    purchased_unit = models.CharField(max_length=100, blank=True, null=True)
    purchased_value = models.FloatField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'input_type_seeds'
