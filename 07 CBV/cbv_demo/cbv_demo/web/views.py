from django.views import generic as views
from django.urls import reverse_lazy, reverse

from django.http import HttpResponse
from django.shortcuts import render

from cbv_demo.web.models import Employee


class IndexViewWithTemplate(views.TemplateView):
    template_name = 'index.html'
    extra_context = {'title': 'Template view'}  # static context

    # Dynamic context
    def get_context_data(self, **kwargs):
        # Get `super`'s context
        context = super().get_context_data(**kwargs)

        # Add specific view stuff, one or more
        context['employees'] = Employee.objects.all()
        # context['form'] = MyForm()

        # Return the ready-to-use context
        return context


class IndexViewWithListView(views.ListView):
    context_object_name = 'employees'  # renames `object_list` to `employees`
    model = Employee
    template_name = 'index.html'  # web/employee_list.html
    extra_context = {'title': 'List view'}  # static context

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['pattern'] = self.__get_pattern()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        pattern = self.__get_pattern()

        if pattern:
            queryset = queryset.filter(first_name__icontains=pattern)

        return queryset

    def __get_pattern(self):
        pattern = self.request.GET.get('pattern', None)
        return pattern.lower() if pattern else None


class EmployeeDetailsView(views.DetailView):
    context_object_name = 'employee'  # renames `object` to `employee`
    model = Employee
    template_name = 'employees/details.html'


class EmployeeUpdateView(views.UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'employees/edit.html'
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        # if the employee to update is the same as the user logged in => continue
        return super().dispatch(request, *args, **kwargs)


class EmployeeCreateView(views.CreateView):
    template_name = 'employees/create.html'
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('index')
