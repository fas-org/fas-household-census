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
    crop_code = models.IntegerField(null=False)
    manure_type = models.CharField(max_length=50, blank=True, null=True)
    manure_home_quantity = models.TextField(blank=True, null=True)
    manure_home_unit = models.CharField(max_length=50, blank=True, null=True)
    manure_home_value = models.TextField(blank=True, null=True)
    manure_purchased_quantity = models.TextField(blank=True, null=True)
    manure_purchased_unit = models.CharField(max_length=50, blank=True, null=True)
    manure_purchased_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'input_use_manure'


class InputUsePlantProtectionIrrigation(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey('Household', models.DO_NOTHING, db_column='household', blank=True, null=True)
    crop_code = models.IntegerField(null=False)
    plant_protection_quantity = models.FloatField(blank=True, null=True)
    plant_protection_price = models.FloatField(blank=True, null=True)
    irrigation_source = models.CharField(max_length=50, blank=True, null=True)
    irrigation_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'input_use_plant_protection_irrigation'


class InputUseFertiliser(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey('Household', models.DO_NOTHING, db_column='household', blank=True, null=True)
    crop_code = models.IntegerField(null=False)
    fertiliser_type = models.CharField(max_length=50, blank=True, null=True)
    fertiliser_quantity = models.FloatField(blank=True, null=True)
    fertiliser_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'input_use_fertiliser'


class InputUseSeeds(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey('Household', models.DO_NOTHING, db_column='household', blank=True, null=True)
    home_produced_quantity = models.FloatField(blank=True, null=True)
    home_produced_value = models.CharField(max_length=50, blank=True, null=True)
    purchased_quantity = models.FloatField(blank=True, null=True)
    purchased_price = models.FloatField(blank=True, null=True)
    crop_code = models.IntegerField(null=False)

    class Meta:
        managed = True
        db_table = 'input_type_seeds'
