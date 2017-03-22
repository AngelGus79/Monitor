from __future__ import unicode_literals

from django.db import models


class Miembro(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.TextField(max_length=100)
    edad = models.IntegerField(max_length=150)
    idWeareble = models.IntegerField()


class Medicamento(models.Model):
    descripcion = models.CharField(max_length=100)


class Grupo(models.Model):
    idMedicamento = models.IntegerField()
    horaInicial = models.DateTimeField()
    periodo = models.IntegerField()
    dosis = models.FloatField()
    miembro = models.ForeignKey(Miembro)
    medicamento = models.ForeignKey(Medicamento)
