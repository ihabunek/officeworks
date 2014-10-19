from django.contrib import admin
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    tax_no = models.CharField(max_length=20)
    address = models.TextField()

    class Meta:
        verbose_name_plural = "companies"

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    company = models.ForeignKey('Company')
    profession = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)

class Client(models.Model):
    name = models.TextField()
    company = models.ForeignKey('Company')
    tax_no = models.CharField(max_length=20)
    address = models.TextField()

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Client)
