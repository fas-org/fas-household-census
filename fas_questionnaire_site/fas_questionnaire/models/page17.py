from __future__ import unicode_literals

from django.db import models

from fas_questionnaire.models.common import Sex
from fas_questionnaire.models.common import Units
from .household_models import Household
from .page1 import HouseholdMembers


class IncomeFromSalaries(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    worker_name = models.ForeignKey(HouseholdMembers, models.DO_NOTHING, db_column='Name of worker')
    description_of_work = models.CharField(max_length=100, db_column='Description of work', blank=True, null=True)
    place_of_work = models.CharField(max_length=50, db_column='Place of work', blank=True, null=True)
    annual_income = models.FloatField(db_column='Annual Income', default=0, null=True)
    comments = models.CharField(max_length=200, db_column='Comments', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Income from salaries artisan earnings'


class IncomeFromOtherBusinessActivities(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    name_of_worker = models.ForeignKey(HouseholdMembers, models.DO_NOTHING, db_column='Name of worker')
    description_of_work = models.CharField(db_column='Description of work', max_length=50, blank=True, null=True)
    place_of_work = models.CharField(db_column='Place of work', max_length=50, blank=True, null=True)
    production_and_sale = models.CharField(db_column='Production and sale', max_length=50, blank=True, null=True)
    cost_of_material_inputs = models.CharField(db_column='Cost of material inputs', max_length=50, blank=True,
                                               null=True)
    wages_and_salaries_paid = models.CharField(db_column='Wages and salaries paid', max_length=50, blank=True,
                                               null=True)
    rents_paid = models.CharField(db_column='Rents paid', max_length=50, blank=True, null=True)
    any_other_costs = models.CharField(db_column='Any other costs', max_length=50, blank=True, null=True)
    comments = models.CharField(db_column='Comments', max_length=250, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Income from other business activities'


class AnimalCattleType(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'Animal cattle type'

    def __str__(self):
        return self.type


class AnimalTypes(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'Animal Types'

    def __str__(self):
        return self.name


class AnimalResoursesInventory(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    type = models.ForeignKey(AnimalTypes, models.DO_NOTHING, db_column='Type', blank=True, null=True)
    sex = models.ForeignKey(Sex, models.DO_NOTHING, db_column='sex', blank=True, null=True)
    cattle_type = models.ForeignKey(AnimalCattleType, models.DO_NOTHING, db_column='Cattle type', blank=True, null=True)
    breed = models.CharField(db_column='Breed', max_length=50, blank=True, null=True)
    no = models.IntegerField(db_column='No', blank=True, null=True)
    age = models.IntegerField(db_column='Age', blank=True, null=True)
    total_present_value = models.IntegerField(db_column='Total present valuse', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Animal Resourses Inventory'


class FeedType(models.Model):
    id = models.AutoField(primary_key=True)
    feed_name = models.CharField(db_column='feed name', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Feed Type'

    def __str__(self):
        return self.feed_name


class FeedSource(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.CharField(db_column='source', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Feed Source'

    def __str__(self):
        return self.source


class AnimalResourcesFeed(models.Model):
    id = models.AutoField(primary_key=True)
    type_of_feed = models.ForeignKey(FeedType, db_column='Type of Feed', blank=True, null=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    source = models.ForeignKey(FeedSource, models.DO_NOTHING, db_column='Feed Source', blank=True, null=True)
    qty = models.IntegerField(db_column='QTY', blank=True, null=True)
    value = models.IntegerField(db_column='Value', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Animal Resources Feed'


class ItemType(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(db_column='item', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Item Type'

    def __str__(self):
        return self.item


class OtherExpenditure(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    item = models.ForeignKey(ItemType, db_column='Item Name', blank=True, null=True)
    expenditure = models.IntegerField(db_column='Expenditure', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'other Expenditure'


class ProductType(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(db_column='product name', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Product Type'

    def __str__(self):
        return self.product_name


class OutputAndIncome(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING, db_column='household')
    product = models.ForeignKey(ProductType, db_column='product', blank=True, null=True)
    production = models.IntegerField(db_column='production', blank=True, null=True)
    production_unit = models.ForeignKey(Units, db_column='production_unit', null=True, blank=True,related_name="%(class)s_production_unit")
    sale = models.IntegerField(db_column='sale', blank=True, null=True)
    sale_unit = models.ForeignKey(Units, db_column='sale_unit', null=True, blank=True,related_name="%(class)s_sale_unit")
    price = models.IntegerField(db_column='price', blank=True, null=True)
    price_unit = models.ForeignKey(Units, db_column='price_unit', null=True, blank=True,related_name="%(class)s_price_unit")

    class Meta:
        managed = True
        db_table = 'Output and Income'
