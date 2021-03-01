from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .decorators import AllowedUsersView
from .models import User
from django.urls import reverse_lazy


class CreateUsersView(AllowedUsersView, CreateView):
    template_name = "register_user.html"
    model = User
    fields = [
        "email", "groups", "department", "address",
        "avatar", "password"
    ]
    allowed_roles = ["admin", ]
    success_url = reverse_lazy('custom_user:list_user')


class ListUsersView(AllowedUsersView, ListView):
    template_name = "user_form.html"
    model = User
    fields = "__all__"
    allowed_roles = ["admin", "simple_user"]
