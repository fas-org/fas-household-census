from django.db import models


class OtherCosts(models.Model):
    id = models.AutoField(primary_key=True)  # This field type is a guess.
    item = models.CharField(max_length=50, blank=True)
    amount_spent = models.IntegerField(blank=True, null=True)
    month_of_payment = models.CharField(db_column="month_of_payment", max_length=50, blank=True, null=True)
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
        verbose_name_plural = 'other costs items'

    def __str__(self):
        return self.item

class PaymentsToManagersAndLongTermWorkers(models.Model):
    name_of_worker = models.IntegerField(blank=True, null=True)
    household = models.ForeignKey('Household', models.DO_NOTHING, db_column='household', blank=True, null=True)
    sex = models.CharField( max_length=100,db_column='sex', blank=True, null=True)
    caste = models.CharField(max_length=100,db_column='caste', blank=True, null=True)
    since_when_employed = models.CharField(max_length=100, blank=True, null=True)
    number_of_months_employed_last_year = models.FloatField(blank=True, null=True)  # This field type is a guess.
    payment_in_cash = models.IntegerField(blank=True, null=True)  # This field type is a guess.
    payment_in_kind = models.CharField(max_length=100, blank=True, null=True)
    agricultural_labour =  models.CharField(max_length=100, blank=True, null=True)
    operating_agricultural_machinery = models.CharField(max_length=100, blank=True, null=True)
    tending_animals =  models.CharField(max_length=100, blank=True, null=True)
    non_agricultural_businesses =  models.CharField(max_length=100, blank=True, null=True)
    domestic_work =  models.CharField(max_length=100, blank=True, null=True)
    activities_others = models.CharField(max_length=100, blank=True, null=True)
    id = models.AutoField(primary_key=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'payments_to_managers_and_long_term_workers'


class EmployManagerOrLongTermWorker(models.Model):
    employ_manager = models.CharField(max_length=100,db_column='employ_manager',null=True, blank=True)
    employ_long_term_worker = models.CharField(max_length=100,db_column='employ_long_term_worker',null=True, blank=True)
    household = models.ForeignKey('Household', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'employ_manager_or_long_term_worker'
