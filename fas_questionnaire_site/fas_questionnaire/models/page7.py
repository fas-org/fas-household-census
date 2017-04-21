from django.db import models


class InputUseManure(models.Model):
    id = models.AutoField(primary_key=True,unique=True, blank=True, null=True)  # This field type is a guess.
    household = models.ForeignKey('Household', models.DO_NOTHING, db_column='household', blank=True, null=True)
    crop_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    manure_type = models.CharField(max_length=50, blank=True, null=True)
    manure_home_qunatity = models.TextField(blank=True, null=True)  # This field type is a guess.
    manure_home_unit = models.CharField(max_length=50, blank=True, null=True)
    manure_home_value = models.TextField(blank=True, null=True)  # This field type is a guess.
    manure_purchased_quantity = models.TextField(blank=True, null=True)  # This field type is a guess.
    manure_purchased_unit = models.CharField(max_length=50, blank=True, null=True)
    manure_purchased_price = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'input_use_manure'


class InputUsePlantProtectionIrrigation(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey('Household', models.DO_NOTHING, db_column='household', blank=True, null=True)
    crop_code = models.FloatField(blank=True, null=True)  # This field type is a guess.
    plant_protection_quantity = models.FloatField(blank=True, null=True)  # This field type is a guess.
    plant_protection_price = models.FloatField(blank=True, null=True)  # This field type is a guess.
    irrigation_source = models.CharField(max_length=50, blank=True, null=True)
    irrigation_price = models.FloatField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'input_use_plant_protection_irrigation'


class InputUseFertiliser(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey('Household', models.DO_NOTHING, db_column='household', blank=True, null=True)
    crop_code = models.FloatField(blank=True, null=True)  # This field type is a guess.
    fertiliser_type = models.CharField(max_length=50, blank=True, null=True)
    fertiliser_quantity = models.FloatField(blank=True, null=True)  # This field type is a guess.
    fertiliser_price = models.FloatField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'input_use_fertiliser'


class InputUseSeeds(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey('Household', models.DO_NOTHING, db_column='household', blank=True, null=True)
    home_produced_quantity = models.FloatField(blank=True, null=True)  # This field type is a guess.
    home_produced_value = models.CharField(max_length=50,blank=True, null=True)  # This field type is a guess.
    purchased_quantity = models.FloatField(blank=True, null=True)  # This field type is a guess.
    purchased_price = models.FloatField(blank=True, null=True)  # This field type is a guess.
    crop_code = models.FloatField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'input_type_seeds'
