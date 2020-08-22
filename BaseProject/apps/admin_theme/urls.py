from django.conf.urls import url
from django.urls import path, re_path
from django.views.generic import TemplateView
from .views import ExamplesTranslations
from django.contrib.auth.decorators import login_required

app_name = 'panel'

urlpatterns = [
    re_path(r'^$', login_required(TemplateView.as_view(template_name="example.html")), name="example"),
    path('translations/', ExamplesTranslations.as_view(template_name="ex_i18n.html"), name="ex_i18n"),
    url(r'^tables/$', TemplateView.as_view(template_name="tables.html"), name="tables"),
]
