from rest_framework import serializers
from  employeeapi.models import employee,empTask,attendance,atten,MarkManualAttendance,LeaveAttendance,VisitShop,OrderInvoice,Expense

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=employee
        fields=('ID','fullname','email_address', 'username' , 'password'  ,  'gender'  ,  'manager'   , 'mob_no' , 'role' ,  'profile_picture')
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model =empTask
        fields = (
            'employee_name',               # Primary key of the task
            'employee_ID',         # Foreign key to Employee model (adjust according to your needs)
            'gender',        # The name of the task
            'mob_no',         # The location associated with the task
            'role',           # Status of the task
            'start_date',       # Task start date
            'deadline',         # Task deadline
            'completion_date',  # The date when the task was completed
            'task_status', # Description of the task (optional)
        )
        
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = attendance
        fields = (
            'ID',                 
            'employee_name',       # Employee's name
            'mobile_number',       # Employee's mobile number
            'employee_role',       # Employee's role
            'gender',              # Employee's gender
            'date',                # Date of attendance
            'attendance_status',  # Status of attendance
            'location',            # Location of the employee
            'image',               # Optional image field
        )
class attenSerializer(serializers.ModelSerializer):
    class Meta:
        model = atten
        fields = (
            'ID',              
            'employee_name',       # Employee's name
            'mobile_number',       # Employee's mobile number
            'role',       # Employee's role
            'gender',              # Employee's gender
            'date',                # Date of attendance
            'attendance_status',  # Status of attendance
            'location',            # Location of the employee
            'image',               # Optional image field
        )


class MarkManualAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkManualAttendance
        fields = (
            'ID',                 # Primary key (ID) of the attendance record
            'employee_name',      # Employee's name
            'date',               # Date of attendance
            'attendance_status', # Status of attendance (e.g., Present, Absent)
            'location',           # Location of the employee
            'notes',              # Additional notes or comments
        )
        
        
class LeaveAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveAttendance
        fields = (
            'ID',                # Custom primary key
            'employee_name',     # Employee's name
            'mobile_no',     # Employee's mobile number
            'role',              # Employee's role
            'gender',            # Employee's gender
            'from_date',         # Start date of the leave
            'till_date',         # End date of the leave
            'total_leave',       # Total number of leave days
            'reason',            # reason for leave
        )
    
    #Create seralizer for visit shop
    
class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitShop
        fields = [
            'ID',
            'employee_name',
            'role',
            'shop_name',
            'shop_address',
            'visiting_datetime',
            'reason_for_visit',
            'image'
        ]
        
    #serializer for invoice
class OrderInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInvoice
        fields = [
          
            'employee_name',
            'ID',
            'customer_name',
            'customer_address',
            'order_date',
            'product_name',
            'quantity',
            'total_amount'
        ]
        
class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            'ID',
            'employee_name',
            'expense_type',
            'expense_description',
            'amount',
            'date',
            'upload_bill'
        ]
        