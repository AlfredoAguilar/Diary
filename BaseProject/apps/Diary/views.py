from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from BaseProject.apps.custom_user.decorators import AllowedUsersView
from BaseProject.apps.custom_user.models import User
from .models import Department
from django.urls import reverse_lazy
from django.db.models import Q


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
    success_url = reverse_lazy('Diary:diaryview')


class DepartmentsList(AllowedUsersView, ListView):
    model = Department
    template_name = 'listAllDepartment.html'
    fields = "__all__"
    allowed_roles = ["admin", "simple_user"]


class SearchResultsView(AllowedUsersView, ListView):
    model = Department
    template_name = 'listAllDepartment.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            queryset = Department.objects.filter(name_department__icontains=query)
        else:
            queryset = Department.objects.all()
        return queryset

    allowed_roles = ["admin", "simple_user"]
