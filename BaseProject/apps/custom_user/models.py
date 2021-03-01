from django.contrib.auth.models import AbstractUser
from django.db import models
from stdimage import StdImageField
from django.core.validators import RegexValidator
from BaseProject.apps.Diary.models import Department

phone_regex = RegexValidator(regex=r'^\d{8,14}((,\d{8,14})?)*$',
                             message="El formato del teléfono debe ser: '9998888777', "
                                     "sin código de país. De 8-14 dígitos permitidos. "
                                     "Puede agregar más telefonos seperados por coma.")

class User(AbstractUser):
    TYPE = (
        ('Admin', 'Administrador'),
        ('Tec', 'Técnico'),
        ('Ventas', 'Ventas')
    )
    username = None
    email = models.EmailField(verbose_name='email address', unique=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última Actualización')
    avatar = StdImageField(upload_to='usuarios/',
                           variations={'perfil': {"width": 240, "height": 240, "crop": True},
                                       'thumbnail': {"width": 45, "height": 45, "crop": True}},
                           default="usuarios/avatar.png")
    address = models.TextField(blank=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=250, blank=True, verbose_name="Teléfono Celular")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    department = models.ForeignKey(
        Department, verbose_name="Departamento", on_delete=models.CASCADE,
        null=True, blank=True
    )

    def __str__(self):
        return '{}'.format(self.email)
