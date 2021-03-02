from django.db import models


class Department(models.Model):
    name_department = models.CharField(verbose_name='Nombre', max_length=30, unique=True)
    office_number = models.PositiveSmallIntegerField(verbose_name='Numero de Oficina')
    floor_number = models.PositiveSmallIntegerField(verbose_name='Numero de piso')

    def __str__(self):
        return '{}'.format(self.name_department)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
