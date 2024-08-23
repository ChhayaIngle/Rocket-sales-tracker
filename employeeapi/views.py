from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from employeeapi.models import employee,empTask,attendance,atten,MarkManualAttendance,LeaveAttendance,VisitShop,OrderInvoice,Expense
from employeeapi.serializers import employeeSerializer,TaskSerializer,AttendanceSerializer,attenSerializer,MarkManualAttendanceSerializer,LeaveAttendanceSerializer,VisitSerializer,OrderInvoiceSerializer,ExpenseSerializer
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def employeeApi(request, id=None):  # Use 'id=None' to allow it to be optional
    if request.method == 'GET':
        if id is not None:
            try:
                # Retrieve a specific employee if ID is provided
                employee_instance = employee.objects.get(ID=id)
                employee_serializer = employeeSerializer(employee_instance)
                return Response(employee_serializer.data)
            except employee.DoesNotExist:
                return Response({"message": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Retrieve all employees if no ID is provided
            employees = employee.objects.all()
            employee_serializer = employeeSerializer(employees, many=True)
            return Response(employee_serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        employee_serializer = employeeSerializer(data=data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return Response({"message": "Added Successfully"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to Add", "errors": employee_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        data = request.data
        try:
            employee_instance = employee.objects.get(ID=data.get('ID'))
        except employee.DoesNotExist:
            return Response({"message": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        employee_serializer = employeeSerializer(employee_instance, data=data, partial=True)  # partial=True for partial updates
        if employee_serializer.is_valid():
            employee_serializer.save()
            return Response({"message": "Updated Successfully"}, status=status.HTTP_200_OK)
        return Response({"message": "Failed to Update", "errors": employee_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            employee_instance = employee.objects.get(ID=id)
            employee_instance.delete()
            return Response({"message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
        except employee.DoesNotExist:
            return Response({"message": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

            
#adding task views api

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def taskApi(request, id=None):
    if request.method == 'GET':
        if id is not None:
            try:
                task_instance = empTask.objects.get(ID=id)
                task_serializer = TaskSerializer(task_instance)
                return Response(task_serializer.data)
            except empTask.DoesNotExist:
                return Response({"message": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            tasks = empTask.objects.all()
            task_serializer = TaskSerializer(tasks, many=True)
            return Response(task_serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        task_serializer = TaskSerializer(data=data)
        if task_serializer.is_valid():
            task_serializer.save()
            return Response({"message": "Added Successfully"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to Add", "errors": task_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    '''elif request.method == 'PUT':
        data = request.data
        try:
            task_instance = Task.objects.get(ID=data.get('id'))
        except Task.DoesNotExist:
            return Response({"message": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        task_serializer = TaskSerializer(task_instance, data=data, partial=True)
        if task_serializer.is_valid():
            task_serializer.save()
            return Response({"message": "Updated Successfully"}, status=status.HTTP_200_OK)
        return Response({"message": "Failed to Update", "errors": task_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            task_instance = Task.objects.get(id=id)
            task_instance.delete()
            return Response({"message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response({"message": "Task not found"}, status=status.HTTP_404_NOT_FOUND)'''
            
         # adding attendance api
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def attendanceApi(request, id=None):
    if request.method == 'GET':
        if id is not None:
            try:
                attendance_instance = attendance.objects.get(id=id)
                attendance_serializer = AttendanceSerializer(attendance_instance)
                return Response(attendance_serializer.data)
            except attendance.DoesNotExist:
                return Response({"message": "Attendance record not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            attendances = attendance.objects.all()
            attendance_serializer = AttendanceSerializer(attendances, many=True)
            return Response(attendance_serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        attendance_serializer = AttendanceSerializer(data=data)
        if attendance_serializer.is_valid():
            attendance_serializer.save()
            return Response({"message": "Added Successfully"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to Add", "errors": attendance_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        data = request.data
        try:
            attendance_instance = attendance.objects.get(id=data.get('id'))
        except attendance.DoesNotExist:
            return Response({"message": "Attendance record not found"}, status=status.HTTP_404_NOT_FOUND)

        attendance_serializer = AttendanceSerializer(attendance_instance, data=data, partial=True)
        if attendance_serializer.is_valid():
            attendance_serializer.save()
            return Response({"message": "Updated Successfully"}, status=status.HTTP_200_OK)
        return Response({"message": "Failed to Update", "errors": attendance_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            attendance_instance = attendance.objects.get(id=id)
            attendance_instance.delete()
            return Response({"message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
        except attendance.DoesNotExist:
            return Response({"message": "Attendance record not found"}, status=status.HTTP_404_NOT_FOUND)

# atten api again becoz failed to migrate
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def attenApi(request, id=None):
    if request.method == 'GET':
        if id is not None:
            try:
                atten_instance = atten.objects.get(ID=id)  # Use ID for filtering
                atten_serializer = attenSerializer(atten_instance)
                return Response(atten_serializer.data)
            except atten.DoesNotExist:
                return Response({"message": "Attendance record not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            atten_records = atten.objects.all()
            atten_serializer = attenSerializer(atten_records, many=True)
            return Response(atten_serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        atten_serializer = attenSerializer(data=data)
        if atten_serializer.is_valid():
            atten_serializer.save()
            return Response({"message": "Added Successfully"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to Add", "errors": atten_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        data = request.data
        try:
            atten_instance = atten.objects.get(ID=data.get('ID'))  # Use ID for filtering
        except atten.DoesNotExist:
            return Response({"message": "Attendance record not found"}, status=status.HTTP_404_NOT_FOUND)

        atten_serializer = attenSerializer(atten_instance, data=data, partial=True)
        if atten_serializer.is_valid():
            atten_serializer.save()
            return Response({"message": "Updated Successfully"}, status=status.HTTP_200_OK)
        return Response({"message": "Failed to Update", "errors": atten_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            atten_instance = atten.objects.get(ID=id)  # Use ID for filtering
            atten_instance.delete()
            return Response({"message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
        except atten.DoesNotExist:
            return Response({"message": "Attendance record not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
#MarkManualAttendance
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def mark_manual_attendance_api(request, id=None):
    if request.method == 'GET':
        if id is not None:
            try:
                # Retrieve a single record by ID
                attendance_instance = MarkManualAttendance.objects.get(ID=id)
                serializer = MarkManualAttendanceSerializer(attendance_instance)
                return Response(serializer.data)
            except MarkManualAttendance.DoesNotExist:
                return Response({"message": "Attendance record not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Retrieve all records
            attendance_records = MarkManualAttendance.objects.all()
            serializer = MarkManualAttendanceSerializer(attendance_records, many=True)
            return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = MarkManualAttendanceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Added Successfully"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to Add", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        data = request.data
        try:
            # Update an existing record by ID
            attendance_instance = MarkManualAttendance.objects.get(ID=data.get('ID'))
        except MarkManualAttendance.DoesNotExist:
            return Response({"message": "Attendance record not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = MarkManualAttendanceSerializer(attendance_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Updated Successfully"}, status=status.HTTP_200_OK)
        return Response({"message": "Failed to Update", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            # Delete an existing record by ID
            attendance_instance = MarkManualAttendance.objects.get(ID=id)
            attendance_instance.delete()
            return Response({"message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
        except MarkManualAttendance.DoesNotExist:
            return Response({"message": "Attendance record not found"}, status=status.HTTP_404_NOT_FOUND)

  
 #Leaveapplication manage
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def leave_attendance_api(request, ID=None):
    if request.method == 'GET':
        if ID is not None:
            try:
                # Retrieve a single record by ID
                leave_instance = LeaveAttendance.objects.get(ID=ID)
                serializer = LeaveAttendanceSerializer(leave_instance)
                return Response(serializer.data)
            except LeaveAttendance.DoesNotExist:
                return Response({"message": "Leave application not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Retrieve all records
            leave_records = LeaveAttendance.objects.all()
            serializer = LeaveAttendanceSerializer(leave_records, many=True)
            return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = LeaveAttendanceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Leave application added successfully"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to add leave application", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        data = request.data
        try:
            # Update an existing record by ID
            leave_instance = LeaveAttendance.objects.get(ID=data.get('ID'))
        except LeaveAttendance.DoesNotExist:
            return Response({"message": "Leave application not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = LeaveAttendanceSerializer(leave_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Leave application updated successfully"}, status=status.HTTP_200_OK)
        return Response({"message": "Failed to update leave application", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            # Delete an existing record by ID
            leave_instance = LeaveAttendance.objects.get(ID=ID)
            leave_instance.delete()
            return Response({"message": "Leave application deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except LeaveAttendance.DoesNotExist:
            return Response({"message": "Leave application not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
# visitshop api calling methods
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def visit_api(request, ID=None):
    if request.method == 'GET':
        if ID is not None:
            try:
                # Retrieve a single record by ID
                visit_instance = VisitShop.objects.get(ID=ID)
                serializer = VisitSerializer(visit_instance)
                return Response(serializer.data)
            except VisitShop.DoesNotExist:
                return Response({"message": "Visit record not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Retrieve all records
            visit_records = VisitShop.objects.all()
            serializer = VisitSerializer(visit_records, many=True)
            return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = VisitSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Visit record added successfully"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to add visit record", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        data = request.data
        try:
            # Update an existing record by ID
            visit_instance = VisitShop.objects.get(id=ID)
        except VisitShop.DoesNotExist:
            return Response({"message": "Visit record not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = VisitSerializer(visit_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Visit record updated successfully"}, status=status.HTTP_200_OK)
        return Response({"message": "Failed to update visit record", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            # Delete an existing record by ID
            visit_instance = VisitShop.objects.get(id=ID)
            visit_instance.delete()
            return Response({"message": "Visit record deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except VisitShop.DoesNotExist:
            return Response({"message": "Visit record not found"}, status=status.HTTP_404_NOT_FOUND)
        
    #Order Invoice.py
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def order_invoice_api(request, ID=None):
    if request.method == 'GET':
        if ID is not None:
            try:
                # Retrieve a single record by ID
                order_invoice_instance = OrderInvoice.objects.get(ID=ID)
                serializer = OrderInvoiceSerializer(order_invoice_instance)
                return Response(serializer.data)
            except OrderInvoice.DoesNotExist:
                return Response({"message": "Order invoice not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Retrieve all records
            order_invoices = OrderInvoice.objects.all()
            serializer = OrderInvoiceSerializer(order_invoices, many=True)
            return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = OrderInvoiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Order invoice added successfully"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to add order invoice", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        data = request.data
        try:
            # Update an existing record by ID
            order_invoice_instance = OrderInvoice.objects.get(ID=ID)
        except OrderInvoice.DoesNotExist:
            return Response({"message": "Order invoice not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderInvoiceSerializer(order_invoice_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Order invoice updated successfully"}, status=status.HTTP_200_OK)
        return Response({"message": "Failed to update order invoice", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            # Delete an existing record by ID
            order_invoice_instance = OrderInvoice.objects.get(ID=ID)
            order_invoice_instance.delete()
            return Response({"message": "Order invoice deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except OrderInvoice.DoesNotExist:
            return Response({"message": "Order invoice not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
        
# views.py file for expense

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def expense_api(request, ID=None):
    if request.method == 'GET':
        if ID is not None:
            try:
                # Retrieve a single record by ID
                expense_instance = Expense.objects.get(ID=ID)
                serializer = ExpenseSerializer(expense_instance)
                return Response(serializer.data)
            except Expense.DoesNotExist:
                return Response({"message": "Expense not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Retrieve all records
            expenses = Expense.objects.all()
            serializer = ExpenseSerializer(expenses, many=True)
            return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = ExpenseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Expense added successfully"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to add expense", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        data = request.data
        try:
            # Update an existing record by ID
            expense_instance = Expense.objects.get(ID=ID)
        except Expense.DoesNotExist:
            return Response({"message": "Expense not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ExpenseSerializer(expense_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Expense updated successfully"}, status=status.HTTP_200_OK)
        return Response({"message": "Failed to update expense", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            # Delete an existing record by ID
            expense_instance = Expense.objects.get(ID=ID)
            expense_instance.delete()
            return Response({"message": "Expense deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Expense.DoesNotExist:
            return Response({"message": "Expense not found"}, status=status.HTTP_404_NOT_FOUND)