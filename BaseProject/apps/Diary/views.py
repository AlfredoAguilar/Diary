from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from BaseProject.apps.custom_user.decorators import AllowedUsersView
from BaseProject.apps.custom_user.models import User
from .models import Department
from django.urls import reverse_lazy


class DiaryUsers(TemplateView):
    template_name = "diary.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['registered_users'] = User.objects.all()
        return context


class CreateDepartment(AllowedUsersView, CreateView):
    model = Department
    fields = "__all__"
    template_name = 'registry_department.html'
    allowed_roles = ["admin", ]
    success_url = reverse_lazy('custom_user:list_user')


class DepartmentsList(AllowedUsersView, ListView):
    model = Department
    template_name = 'listAllDepartment.html'
    fields = "__all__"
    allowed_roles = ["admin", "simple_user"]
