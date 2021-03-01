from .views import DiaryUsers, CreateDepartment, DepartmentsList
from django.conf.urls import url
from django.urls import path, re_path

app_name = 'Diary'

urlpatterns = [
    path('diary/', DiaryUsers.as_view(template_name="ex_i18n.html"), name="ex_i18n"),
    path('registry/', CreateDepartment.as_view(), name='registry'),
    path('diaryview/', DepartmentsList.as_view(), name='diaryview'),

]
