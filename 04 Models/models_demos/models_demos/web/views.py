from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from models_demos.web.models import Employee, Department


def index(request):
    employees = [e for e in Employee.objects.all() if e.department_id == 1]
    employees2 = Employee.objects.filter(department_id=1) \
        .order_by('first_name')

    # get must return a single object. Not more then one... and it does not return a promise but the object directly.
    # By promise I mean that get does not return a query set. Get is eager and acts even if unused.
    department = Department.objects.get(pk=1)
    context = {
        'employees': employees,
        'employees2': employees2,
        'department': department,
    }

    return render(request, 'index.html', context)


def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    print(employee)
    employee.delete()
    return redirect('index')
