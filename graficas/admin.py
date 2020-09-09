# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from graficas.models import Empresa, GrafanaData, GrafanaDB

# Register your models here.


class EmpresaAdmin(admin.ModelAdmin):
    model = Empresa
    search_fields = ('nombre', 'slug')
    list_display = ('nombre',)
    prepopulated_fields = {"slug": ("nombre",)}


admin.site.register(Empresa, EmpresaAdmin)


class GrafanaDataAdmin(admin.ModelAdmin):
    model = GrafanaData
    search_fields = ('id_org', 'id')
    list_display = ('id_org',)


admin.site.register(GrafanaData, GrafanaDataAdmin)


class GrafanaDashBoardsAdmin(admin.ModelAdmin):
    model = GrafanaDB
    search_fields = ('empresa',)
    list_display = ('uuid_db','empresa',)
    raw_id_fields = ['empresa']


admin.site.register(GrafanaDB, GrafanaDashBoardsAdmin)