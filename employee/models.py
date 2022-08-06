from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.CharField(primary_key=True, max_length=11, unique=True, default='0')
    name= models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    joining_date = models.DateField(auto_now_add=True)
    blood_group = models.CharField(max_length=10)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    emergency_phone = models.CharField(max_length=255, blank=True)
    relation = models.CharField(max_length=20)
    father_name= models.CharField(max_length=255)
    mother_name= models.CharField(max_length=255)
    spouse_name= models.CharField(max_length=255)
    permanent_address = models.CharField(max_length=255)
    present_address = models.CharField(max_length=255)
    gender = models.CharField(max_length=50)
    nid = models.CharField(max_length=20)
    tin = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.id} {self.name}'

class LeaveForm(models.Model):
    id = models.CharField(primary_key=True, max_length=11, unique=True, default='0')
    name= models.CharField(max_length=255)
    CHOICES = (('p', 'Paid'),
               ('u', 'Unpaid'),
            )
    name= models.CharField(max_length=255)
    leave_type = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    total_days = models.IntegerField()
    reason = models.CharField(max_length=20)
    paid = models.CharField(max_length=255, choices=CHOICES)
    status = models.CharField(max_length=20)
    reliever= models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id} {self.name} {self.paid}'

class L_DAY_COUNT(models.Model):
    id = models.CharField(primary_key=True, max_length=11, unique=True, default='0')
    name= models.CharField(max_length=255)
    name= models.CharField(max_length=255)
    leave_type = models.CharField(max_length=255)
    total_days = models.IntegerField()
    enjoying_days = models.IntegerField()
    remaining_days = models.IntegerField()

    def __str__(self):
        return f'{self.id} {self.leave_type}'
