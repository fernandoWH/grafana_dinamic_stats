# Granafa - InfluxDB - Telegraf - Python

Stats with Grafana, Plotly and Google Charts, in Python

Se usará Ubuntu 18.04 para el ejemplo

__1 Instalación y configuración de Influx DB__

Crear el directorio stats_test

    mkdir ~/Documentos/stats_test
    
1.1 Ubicate en el directorio donde deseas trabajar
    
    cd ~/Documentos/stats_test

1.2 Descarga y descomprime los archivos binarios necesarios para Grafana

    wget https://dl.influxdata.com/influxdb/releases/influxdb-1.8.1_linux_amd64.tar.gz
    tar xvfz influxdb-1.8.1_linux_amd64.tar.gz

1.3 Iniciar InfluxDB
    
    cd influxdb-1.8.1-1/usr/bin
    ./influxd
__2 Instalación y configuracion de telegraf__
    
Abrir nueva terminal *

2.1 Ubicate en el directorio donde deseas trabajar
    
    cd ~/Documentos/stats_test

2.2 Descarga y descomprime los archivos binarios necesarios para Grafana

    wget https://dl.influxdata.com/telegraf/releases/telegraf-1.15.2_linux_amd64.tar.gz
    tar xf telegraf-1.15.2_linux_amd64.tar.gz
    
2.3 Archivo de configuración
  Ingresamos al siguiente repositorio de los datos descomprimidos y creamos un archivo telefraf.conf, con lo siguientes comandos, donde suaremos los plugins input cpu, mem y disk y plugins output influxdb
    
    cd telegraf-1.15.2/usr/bin
    ./telegraf -sample-config -input-filter cpu:mem:disk:net -output-filter influxdb > telegraf.conf
 
 Ya que tenemos el archivo telegraf.conf solo nos queda iniciar telegraf
 
    ./telegraf --config telegraf.conf

__3 Intalación y configuracion de Grafana__

3.1 Ubicate en el directorio donde deseas trabajar
    
    cd ~/Documentos/stats_test

3.2 Clona grafana

    git clone https://github.com/fernandoWH/personal_grafana.git
    tar -zxvf grafana-7.1.3.linux-amd64.tar.gz
    
3.3 Inicia el grafana-server
    
    cd personal_grafana/grafana/bin
    ./grafana-server

3.4 Habrá iniciado grafana en el puerto 3000, ingresa a tu ip:3000 (127.0.0.1:3000) en tu navegador
  el usuario y contraseña inicial es:
  user: admin
  password: admin
  

__4 Configuracion Grafana HTTPS__

4.1 Ingrese al directorio **conf** y abra el archivo defaults.ini
    
    cd ~/Documentos/stats_test/personal_grafana/grafana/conf/
    sudo nano defaults.ini
    
4.2 Modifica lo siguiente
 
    [auth.anonymous]
    # enable anonymous access
    enabled = true

    # set cookie SameSite attribute. defaults to `lax`. can be set to "lax", "strict", "none" and "disabled"
    cookie_samesite = disabled
    
    # set to true if you want to allow browsers to render Grafana in a <frame>, <iframe>, <embed> or <object>. default is false.
    allow_embedding = true
    
    
4.3 Agregar Grafana e Influxdb a systemctl

   Agregaremos Grafana e InfluxDB a systemctl para tener un mejor manejo de estos
   
4.3.1 Crea un archivo demonio para grafana

    cd /etc/systemd/system/
    sudo nano grafana.service
    
4.3.2 Pegamos el siguiente contenido en grafana.service remplazando **/home/ubuntu/grafana2/grafana/bin/grafana-server**
por la ruta donde este el script grafana-server y **/home/ubuntu/grafana2/grafana/bin/** por la de el directorio donde este el script
    
    # ***grafana.service***
    [Unit]
    Description=Fork Grafana
    After=multi-user.target
    
    [Service]
    Type=simple
    ExecStart=/home/ubuntu/Documentos/stats_test/personal_grafana/grafana/bin/grafana-server
    User=root
    WorkingDirectory=/home/ubuntu/Documentos/stats_test/personal_grafana/grafana/bin/
    Restart=on-failure
    StandardOutput=syslog
    StandardError=syslog
    
    [Install]
    WantedBy=multi-user.target
 
4.3.3 Crear un archivo demonio para InfluxDB

    cd /etc/systemd/system/
    sudo nano influx.service
     
4.3.4 Pegamos el siguiente contenido en grafana.service remplazando **/home/ubuntu/monitoreo/influxdb-1.8.1-1/usr/bin/influxd**
por la ruta donde este el script grafana-server y **/home/ubuntu/monitoreo/influxdb-1.8.1-1/usr/bin/** por la de el directorio donde este el script
                                                                                                                          

    # ***influxdb.service***
    [Unit]
    Description=InfluxDB
    After=multi-user.target
    
    [Service]
    Type=simple
    ExecStart=/home/ubuntu/monitoreo/influxdb-1.8.1-1/usr/bin/influxd
    User=root
    WorkingDirectory=/home/ubuntu/monitoreo/influxdb-1.8.1-1/usr/bin/
    Restart=on-failure
    StandardOutput=syslog
    StandardError=syslog
    
    [Install]
    WantedBy=multi-user.target

4.3.5 Iniciamos InfluxDB y Grafana con systemctl (Si, previamente tienes corriendo grafana o influxdb, detenlos)
    
    sudo systemctl daemon-reload
    sudo systemctl enable grafana.service
    sudo systemctl start grafana.service
    sudo systemctl enable influx.service
    sudo systemctl start influx.service
    
__5__ Proxy con nginx

Necesitamos un proxy para procesar peticiones a nuestro servidor de Grafana

5.1 Instala nginx

    sudo apt update
    sudo apt install nginx

5.2 Crear archivo grafana

    sudo nano /etc/nginx/sites-available/grafana
    
5.3 Pegar lo siguiente

    server {
      listen      80;
      # listen      [::]:80 ipv6only=on;
      server_name localhost;
    
    
      location / {
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-Host $host;
                proxy_set_header X-Forwarded-Server $host;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_hide_header 'x-frame-options';
                proxy_set_header x-frame-options allowall;
    
                add_header Access-Control-Allow-Origin *;
                add_header 'Access-Control-Allow-Credentials: true' always;
                add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS' always;
                add_header 'Access-Control-Expose-Headers' 'Content-Type,Content-Length,Content-Range';
                add_header 'Access-Control-Allow-Headers'
                           'Accept,
                            Authorization,
                            Cache-Control,
                            Content-Type,
                            DNT,
                            If-Modified-Since,
                            Keep-Alive,
                            Origin,
                            User-Agent,
                            X-Requested-With' always;
    
                if ($request_method = 'OPTIONS') {
                  return 204;
                }
    
                proxy_pass http://localhost:3000/;
    
            }
    }

5.4 Vincular a sites-enabled

    sudo ln -s /etc/nginx/sites-available/grafana.conf /etc/nginx/sites-enabled
    
5.5 Verificar sintasix de nginx

    sudo nginx -t

5.6 Recargar nginx

    sudo service nginx reload
    
__6 Instalacion del proyecto Django__

6.1 Instalar postgresql, ngixn, pip, curl


    sudo apt update
    sudo apt install python-pip python-dev libpq-dev postgresql postgresql-contrib nginx curl   

6.2 Descargar el proyecto

    mkdir ~/Documentos/monitoreo_pyhton
    cd ~/Documentos/monitoreo_pyhton
    git clone https://github.com/fernandoWH/grafana_dinamic_stats.git
    
6.3 Crear entorno virtual

6.3.1 Descargar virtualenv

    sudo -H pip install --upgrade pip
    sudo -H pip install virtualenv

6.3.2 Crear entorno virtual

    virtualenv monitoreo
    source monitoreo/bin/activate
    
    
6.4 Instalar requirements.txt__
    
    cd grafana_dinamic_stats/
    pip install -r requirements.txt

6.55 Correr el proyecto__

    cd monitoreo
    ./manage.py runserver
    

# Accesos
django-admin

u: admin
p: admin123

