from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class employee(models.Model):
    ID=models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=255)
    email_address = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    gender = models.CharField(max_length=10)
    manager= models.CharField(max_length=50)
    mob_no = models.CharField(max_length=15)
    role = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    
#Create empTask 
    
class empTask(models.Model):
    employee_name = models.CharField(max_length=255)
    employee_ID=models.BigIntegerField(primary_key=True,default=True)
    gender = models.CharField(max_length=10)
    mob_no = models.CharField(max_length=15)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    deadline = models.DateField()
    completion_date = models.DateField(null=True, blank=True)
    task_name = models.CharField(max_length=255)  # New field for the task name
    location = models.CharField(max_length=255)  # New field for the employee locatio
    task_status = models.TextField(null=True, blank=True)
    

#this is only fake attendance(django)
class attendance(models.Model):
    ID=models.BigIntegerField(primary_key=True,default=True)
    employee_name = models.CharField(max_length=255)  # Employee's name
    mobile_number = models.CharField(max_length=15)  # Employee's mobile number
    employee_role = models.CharField(max_length=100)  # Employee's role
    gender = models.CharField(max_length=10)  # Employee's gender
    date = models.DateField()  # Date of attendance
    attendance_status = models.CharField(max_length=50)  # Status of attendance (e.g., Present, Absent)
    location = models.CharField(max_length=255)  # Location of the employee
    image= models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    
    
    #create atten views

class atten(models.Model):
    ID=models.BigIntegerField(primary_key=True,default=True)
    employee_name = models.CharField(max_length=255)  # Employee's name
    mobile_no = models.CharField(max_length=15)  # Employee's mobile number
    employee_role = models.CharField(max_length=100)  # Employee's role
    gender = models.CharField(max_length=10)  # Employee's gender
    date = models.DateField()  # Date of attendance
    attendance_status = models.CharField(max_length=50)  # Status of attendance (e.g., Present, Absent)
    location = models.CharField(max_length=255)  # Location of the employee
    image= models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    
    
    
    #MarkManualAttendance

class MarkManualAttendance(models.Model):
    
    employee_name = models.CharField(max_length=255)  # Employee's name   
    ID=models.BigIntegerField(primary_key=True,default=True)
    date = models.DateField()  # Date of attendance
    attendance_status = models.CharField(max_length=50)  # Status of attendance (e.g., Present, Absent)
    location = models.CharField(max_length=255)  # Location of the employee
    notes = models.TextField(null=True, blank=True)  # Additional notes or comments
    
class LeaveAttendance(models.Model):
    ID = models.BigIntegerField(primary_key=True)  # Explicitly define ID as the primary key
    employee_name = models.CharField(max_length=255)  # Employee's name
    mobile_no = models.CharField(max_length=15)   # Employee's mobile number
    role = models.CharField(max_length=100)            # Employee's role
    gender = models.CharField(max_length=10)            # Employee's gender
    from_date = models.DateField()                      # Start date of the leave
    till_date = models.DateField()                      # End date of the leave
    total_leave= models.IntegerField()            # Total number of leave days
    reason = models.TextField(null=True, blank=True)   # Reason for the leave (optional)
   
   
class VisitShop(models.Model):
    ID = models.BigIntegerField(primary_key=True)
    employee_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    shop_name = models.CharField(max_length=255)
    shop_address = models.TextField()
    visiting_datetime = models.DateTimeField()
    reason_for_visit = models.TextField()
    image = models.ImageField(upload_to='visit_images/')
    
class OrderInvoice(models.Model):
    employee_name = models.CharField(max_length=255)
    ID = models.BigIntegerField(primary_key=True) 
    customer_name = models.CharField(max_length=255)
    customer_address = models.TextField()  # Use TextField for potentially long addresses
    order_date = models.DateField()  # Use DateField for the date without time
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()  # Use PositiveIntegerField for non-negative numbers
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # DecimalField for monetary values


class Expense(models.Model):
    # Define the fields for the Expense model
    ID = models.BigIntegerField(primary_key=True)  # Automatically incremented ID
    employee_name = models.CharField(max_length=255)  # Name of the employee incurring the expense
    expense_type = models.CharField(max_length=255)  # Type of the expense (e.g., Travel, Supplies, etc.)
    expense_description = models.TextField()  # Detailed description of the expense
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount of the expense
    date = models.DateField()  # Date of the expense
    upload_bill = models.FileField(upload_to='bills/')  # FileField for uploading the bill
        
    
