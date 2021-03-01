from .views import DiaryUsers
from django.conf.urls import url
from django.urls import path, re_path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

app_name = 'panel'

urlpatterns = [
    path('diary/', DiaryUsers.as_view(template_name="ex_i18n.html"), name="ex_i18n"),
]
