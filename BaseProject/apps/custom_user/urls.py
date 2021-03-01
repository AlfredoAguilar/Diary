from django.urls import path
from .views import CreateUsersView

app_name = 'custom_user'

urlpatterns = [
    path('create/', CreateUsersView.as_view(), name="create_user"),
]
