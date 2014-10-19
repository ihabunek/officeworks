from django.db import models

class Trip(models.Model):
    date = models.DateField()
    duration = models.IntegerField()
    destination = models.CharField(max_length=255)
    employee = models.ForeignKey('company.Employee')
    client = models.ForeignKey('company.Client')
    purpose = models.TextField()

class TripReport(models.Model):
    pass

class Currency(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=255)

class Country(models.Model):
    name = models.TextField()
    allowance_currency = models.ForeignKey('Currency')
    allowance_amount = models.DecimalField(max_digits=8, decimal_places=2)

