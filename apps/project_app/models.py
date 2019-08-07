from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
class Employee(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    employee_address = models.EmailField(max_length = 255)
    phone_number = models.CharField(max_length = 255)
    employee_email = models.EmailField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    product_name = models.CharField(max_length = 255)
    barcode_number = models.CharField(max_length = 255)
    employees_p = models.ForeignKey(Employee, related_name ="products")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
class Vehicle (models.Model):
    year = models.DateField()
    make = models.CharField(max_length = 255)
    model = models.CharField(max_length = 255)
    vin= models.IntegerField()
    employees_v = models.ForeignKey(Employee, related_name="vehicles")
    stock_number = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
