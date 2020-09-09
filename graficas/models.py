# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Empresa(models.Model):
    slug = models.SlugField(unique=True)
    nombre = models.CharField(max_length=80, unique=True)

    def __unicode__(self):
        return u'{0}'.format(self.nombre)

class GrafanaData(models.Model):
    token_admin = models.CharField(max_length=100,  blank=True)
    token_viewer = models.CharField(max_length=100,  blank=True)  # Opcional
    id_org = models.IntegerField(null=True)
    uuid_dashboard = models.CharField(max_length=80, unique=True, null=True, blank=True)
    id_dashboard = models.IntegerField(null=True, blank=True),
    url = models.CharField(max_length=150, unique=True, blank=True, null=True)
    title = models.CharField(max_length=80, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)


class GrafanaDB(models.Model):
    uuid_db = models.UUIDField()
    db_name = models.CharField(max_length=100, default='telegraf')
    empresa = models.ForeignKey(Empresa, related_name='_dashboard', null=True)