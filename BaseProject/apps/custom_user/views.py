from django.views.generic.edit import CreateView
from .decorators import AllowedUsersView
from .models import Department


class CreateUsersView(AllowedUsersView, CreateView):
    template_name = "user_form.html"
    model = Department
    fields = "__all__"
    allowed_roles = ["admin", "simple_user"]

