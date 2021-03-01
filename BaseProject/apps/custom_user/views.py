from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .decorators import AllowedUsersView
from .models import User


class CreateUsersView(AllowedUsersView, CreateView):
    template_name = "user_form.html"
    model = User
    fields = "__all__"
    allowed_roles = ["admin", ]


class ListUsersView(AllowedUsersView, ListView):
    template_name = "user_form.html"
    model = User
    fields = "__all__"
    allowed_roles = ["admin", "simple_user"]
