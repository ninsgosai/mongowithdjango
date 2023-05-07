from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from EmployeeApp.models import *
from EmployeeApp.serializers import *

# Create your views here.
@csrf_exempt
def departmentApi(request,id=0):
    if request.method == "GET":
        departments = Departments.objects.all()
        department_serializer = DepartmentSerializer(departments,many=True)
        return JsonResponse(department_serializer.data,safe=False)
    elif request.method == "POST":
        dep_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=dep_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("saved succesfully",safe=False)
        return JsonResponse("Failed to add.")
    elif request.method == "PUT":
        dep_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=dep_data['DepartmentId'])
        department_serializer = DepartmentSerializer(department,data=dep_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Update succesfully",safe=False)
        return JsonResponse("Failed to update.")
    elif request.method == "DELETE":
        dep_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=dep_data['DepartmentId'])
        department.delete()
        return JsonResponse("Delete succesfully",safe=False)
    

@csrf_exempt
def employeeApi(request,id=0):
    if request.method == "GET":
        employee = Employee.objects.all()
        employee_serializer = EmployeeSerializer(employee,many=True)
        return JsonResponse(employee_serializer.data,safe=False)
    elif request.method == "POST":
        dep_data = JSONParser().parse(request)
        department_serializer = EmployeeSerializer(data=dep_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("saved succesfully",safe=False)
        return JsonResponse("Failed to add.")
    elif request.method == "PUT":
        dep_data = JSONParser().parse(request)
        department = Employee.objects.get(DepartmentId=dep_data['EmployeeId'])
        department_serializer = EmployeeSerializer(department,data=dep_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Update succesfully",safe=False)
        return JsonResponse("Failed to update.")
    elif request.method == "DELETE":
        dep_data = JSONParser().parse(request)
        department = Employee.objects.get(DepartmentId=dep_data['EmployeeId'])
        department.delete()
        return JsonResponse("Delete succesfully",safe=False)