from django.urls import path
from .views import CreateUsersView, ListUsersView

app_name = 'custom_user'

urlpatterns = [
    path('list/', ListUsersView.as_view(), name="list_user"),
    path('create/', CreateUsersView.as_view(), name="create_user"),
]
