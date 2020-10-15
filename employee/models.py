from django.db import models


class Employee(models.Model):
    """
    Employee model : model for Employees
    """
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    designation = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name


class Address(models.Model):
    """
    Address model : Table for Employee Addresses
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    address_choices = [('Present address', 'Present address'), ('Permanent address', 'Permanent address'),
                       ('Office address', 'Office address')]

    address_type = models.CharField(max_length=50, choices=address_choices)
    address_line_1 = models.CharField(max_length=500, null=False, blank=False)
    address_line_2 = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=100, null=False, blank=False)
    pin = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return self.address_line_1
