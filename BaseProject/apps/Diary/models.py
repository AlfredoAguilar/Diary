from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Deparment(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=30)
    office_number = models.IntegerField(verbose_name='Numero de Oficina')

class User(AbstractUser):
    is_reader = models.BooleanField(verbose_name='Es lector', default=False)
    is_admin = models.BooleanField(verbose_name='Es Administrador', default=False)
    department = models.ForeignKey(Deparment, on_delete=models.CASCADE)
    USERNAME_FIELD = 'email'
    def get_reader_profile(self):
        reader_profile = None
        if hasattr(self, 'readerprofile'):
            reader_profile = self.readerprofile
        return reader_profile

    def get_admin_profile(self):
        admin_profile = None
        if hasattr(self,'adminprofile'):
            admin_profile = self.adminprofile
        return admin_profile

    class Meta:
        db_table = 'employee'

class ReaderProfile(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(verbose_name='Activo', default=True)

class AdminProfile(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(verbose_name='Activo', default=True)