from django.db import models

# Thru this class we can access the employees table in the DB... Model fields == Class attributes


class Department(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return f'Id: {self.pk}; Name: {self.name}'


class Project(models.Model):
    name = models.CharField(max_length=30)
    code_name = models.CharField(
        max_length=10,
        unique=True
    )
    deadline = models.DateField()


class Employee(models.Model):
    first_name = models.CharField(
        max_length=30
    )

    review = models.TextField()

    years_of_experience = models.IntegerField()

    level = models.CharField(
        max_length=3,
        choices=(
            ('jr', 'Junior'),
            ('reg', 'Regular')
        )
    )

    age = models.IntegerField()

    email = models.EmailField(
        default="sam@gmail.com",
        unique=True,
    )

    is_full_time = models.BooleanField(
        null=True,
    )

    # These below are kind of automatic meta-data that gets a field. They can also be manual.

    # This will automatically set on creation.
    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    # This will automatically save on each update.
    updated_on = models.DateTimeField(
        auto_now=True,
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )

    projects = models.ManyToManyField(
        Project,
        related_name='employees',
    )

    @property
    def fullname(self):
        return f'{self.first_name}'

    def __str__(self):
        return f'Id: {self.pk}; Name: {self.fullname}'


class EmployeesProjects(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.RESTRICT)
    project_id = models.ForeignKey(Project, on_delete=models.RESTRICT)

    date_joined = models.DateField(
        auto_now_add=True,
    )
    # Additional info


'''
Django ORM (Object-Relational-Mapping) - Translates Python code into SQL
'''