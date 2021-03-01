from django.views.generic import TemplateView
from BaseProject.apps.custom_user.models import User


class DiaryUsers(TemplateView):
    template_name = "diary.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['registered_users'] = User.objects.all()
        return context
