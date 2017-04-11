from django.db import models


class OtherCosts(models.Model):
    item = models.CharField(max_length=50, blank=True)
    amount_spent = models.IntegerField(blank=True, null=True)
    month_of_payment = models.CharField(max_length=50, blank=True, null=True)
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
