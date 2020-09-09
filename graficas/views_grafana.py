# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import uuid
import requests
import random

from django.shortcuts import render

from graficas.forms.forms_graficas import EmpresaForm
from graficas.models import Empresa, GrafanaData, GrafanaDB
from graficas.utils import data_dashboard
from monitoreo import settings

# Create your views here.

def api_grafana(request):
    empresa = Empresa.objects.first()
    form_empresa = EmpresaForm(initial={'empresa': empresa})
    if request.method == 'POST':
        form_empresa = EmpresaForm(request.POST)
        empresa_id = form_empresa.data.get('empresa')
        empresa = Empresa.objects.get(id=empresa_id)
    grafana_data = GrafanaData.objects.all()
    # Verificamos si tenemos en base de datos token admin, dashboar, etc, para crear una base de datos en Grafana
    if not grafana_data:
        grafana_data = obtener_token_grafana()
    else:
        grafana_data = grafana_data[0]
    grafana_db = GrafanaDB.objects.filter(empresa=empresa)
    # Verificamos si la empresa ya tiene una base de datos en Grafana
    if not grafana_db:
        grafana_db = obtener_db_grafana(empresa, grafana_data)
    else:
        grafana_db = grafana_db[0]
    url = grafana_data.url
    uuid_db = grafana_db.uuid_db

    url = settings.URL_GRAFANA+url+'?theme=light&var-empresa='+str(uuid_db)
    return render(request, 'api_grafana.html', {'url': url, 'form_empresa': form_empresa})


def obtener_token_grafana():
    errores = []
    headers_obtener_token_grafana = {
        "Content-Type": "application/json",
    }
    id_organizacion = 1
    data_add_admin = {"loginOrEmail": "admin", "role": "Admin"}
    data_add_admin = json.dumps(data_add_admin)
    # Agregamos un Usuario administrador a Grafana en la organizacion 1
    response_add_admin = requests.post(url=settings.URL_GRAFANA_ADMIN+'/api/orgs/'+ str(id_organizacion)+'/users',
                                       data=data_add_admin, headers=headers_obtener_token_grafana)
    # Si ya existe usuario admin o se creo entra en este if
    if response_add_admin.status_code == 200 or response_add_admin.status_code == 409:
        response = json.loads(response_add_admin.text)
        data_key_admin = {"name": "keyadmin", "role": "Admin"}
        data_key_viewer = {"name": "keyviewer", "role": "Viewer"}
        data_key_admin = json.dumps(data_key_admin)
        data_key_viewer = json.dumps(data_key_viewer)
        # Creamos un token Admin en Grafana para poder crear bases de datos y demas
        response_key_admin = requests.post(url=settings.URL_GRAFANA_ADMIN+'/api/auth/keys',
                                           data=data_key_admin, headers=headers_obtener_token_grafana)
        # Creamos un token Viewer en Grafana
        response_key_viewer = requests.post(url=settings.URL_GRAFANA_ADMIN+'/api/auth/keys',
                                            data=data_key_viewer, headers=headers_obtener_token_grafana)
        response_key_admin = json.loads(response_key_admin.text)
        response_key_viewer = json.loads(response_key_viewer.text)
        token_admin = response_key_admin['key']
        token_viewer = response_key_viewer['key']

        # Crearemos el dashboard, los panel y variables de grafana
        authorization = 'Bearer ' + token_admin
        data_create_new_dashboard = data_dashboard

        headers_grafana = {
            "Authorization": authorization,
            "Content-Type": "application/json",
        }
        data_create_new_dashboard = json.dumps(data_create_new_dashboard)
        response_create_dashboard = requests.post(url=settings.URL_GRAFANA+'/api/dashboards/db',
                                                  data=data_create_new_dashboard, headers=headers_grafana)
        if response_create_dashboard.status_code == 200:
            # Guardamos la informacion necesaria para crear bases de datos en Grafana
            response = json.loads(response_create_dashboard.text)
            id_dashboard = response['id']
            uuid_dashboard = response['uid']
            version_dashboard = int(response['version'])
            url = response['url']
            grafana_data = GrafanaData()
            grafana_data.id_org = id_organizacion
            grafana_data.token_admin = token_admin
            grafana_data.token_viewer = token_viewer
            grafana_data.uuid_dashboard = uuid_dashboard
            grafana_data.id_dashboard = id_dashboard
            grafana_data.url = url
            grafana_data.title = "Server Status"
            grafana_data.version = version_dashboard + 1
            grafana_data.save()

            return grafana_data

    else:
        errores.appen(response_add_admin.text)
        return None

def obtener_db_grafana(empresa, grafana_data):
    token_admin = grafana_data.token_admin
    authorization = 'Bearer ' + token_admin
    headers_grafana = {
        "Authorization": authorization,
        "Content-Type": "application/json",
    }

    # Toma una base de datos Random por ahora
    bd_disponibles = settings.BD_DISPONIBLES
    bd = random.choice(bd_disponibles)
    uuid_db = uuid.uuid4()
    data_db = {
        "name": str(uuid_db),
        "type": "influxdb",
        "typeLogoUrl": "public/app/plugins/datasource/influxdb/img/influxdb_logo.svg",
        "access": "proxy",
        "url": settings.URL_INFLUXDB,
        "password": "",
        "user": "",
        "database": str(bd),
        "basicAuth": False,
        "isDefault": False,
        "jsonData": {},
        "readOnly": False
    }
    data_db = json.dumps(data_db)
    # Crea una base de datos
    response_db = requests.post(url=settings.URL_GRAFANA+'/api/datasources', data=data_db, headers=headers_grafana)
    if response_db.status_code == 200:
        # Guardamos uuid y nombre en influx de la base de datos
        grafana_db = GrafanaDB()
        grafana_db.uuid_db = uuid_db
        grafana_db.empresa = empresa
        grafana_db.db_name = bd
        grafana_db.save()
        return grafana_db
    else:
        return None