from django.db import models


class OtherCosts(models.Model):
    item = models.CharField(max_length=50, blank=True)
    amount_spent = models.IntegerField(blank=True, null=True)
    month_of_payment = models.ForeignKey('Month',db_column="month_of_payment", max_length=50, blank=True, null=True)
    comments = models.CharField(max_length=200, blank=True, null=True)
    record_type = models.PositiveSmallIntegerField(default=0)
    household = models.ForeignKey('Household', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'other_costs_of_agriculture'


class OtherCostsItems(models.Model):
    item = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'other_costs_items'


class PaymentsToManagersAndLongTermWorkers(models.Model):
    name_of_worker = models.CharField(max_length=100, blank=True, null=True)
    household = models.ForeignKey('Household', models.DO_NOTHING, db_column='household', blank=True, null=True)
    sex = models.ForeignKey('Sex', models.DO_NOTHING, db_column='sex', blank=True, null=True)
    caste = models.ForeignKey('Caste', models.DO_NOTHING, db_column='caste', blank=True, null=True)
    since_when_employed = models.CharField(max_length=100, blank=True, null=True)
    number_of_months_employed_last_year = models.FloatField(blank=True, null=True)  # This field type is a guess.
    payment_in_cash = models.IntegerField(blank=True, null=True)  # This field type is a guess.
    payment_in_kind = models.CharField(max_length=100, blank=True, null=True)
    agricultural_labour = models.NullBooleanField()
    operating_agricultural_machinery = models.NullBooleanField()
    tending_animals = models.NullBooleanField()
    non_agricultural_businesses = models.NullBooleanField()
    domestic_work = models.NullBooleanField()
    activities_others = models.CharField(max_length=100, blank=True, null=True)
    id = models.AutoField(primary_key=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'payments_to_managers_and_long_term_workers'


class EmployManagerOrLongTermWorker(models.Model):
    employ_manager = models.NullBooleanField(null=True, blank=True)
    employ_long_term_worker = models.NullBooleanField(null=True, blank=True)
    household = models.ForeignKey('Household', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'employ_manager_or_long_term_worker'
