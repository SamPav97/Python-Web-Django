from django.contrib import admin

from models_demos.web.models import Employee, Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


# This model is enabled in Django Admin.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass



