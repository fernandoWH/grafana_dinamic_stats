"""monitoreo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from graficas.views import info_datos_server, info_datos_server_google
from graficas.views_grafana import api_grafana

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', api_grafana, name='graficas_grafana'),
    url(r'^graficas-plotly$', info_datos_server, name='graficas_plotly'),
    url(r'^graficas-google$', info_datos_server_google, name='graficas_google'),

]

