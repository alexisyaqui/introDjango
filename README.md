# Introduccion a django

=> creamos la carpeta donde se va alojar el proyecto ..introDjango
=> dentro de la carpeta creado mi introDjango
    creamos nuestro entorno de trabajo para django
        python -m venv entorno
    
    levantamos nuestro entorno de trabajo desde la terminal de linux o winwdow
        source env/bin/activate


=> creamos nuestro proyecto de DJANGO  
    django-admin startproject settings 

=> nos dirigimos a la carpeta settings (cd settings)
    creamos nuestra aplicacion con el comando
    python manage.py startapp blog

=> instalamos django-environ con el siguiente comando
    pip install django-environ

=> para proteger nuestra llave secreta de django
    creamos un archivo llamado .env dento de la carpeta settings
    dentro ay un archivo llamado settings.py y buscamos donde dice SECRETE_KEY

=> dentro del archivo .env pegamos la llave llamada SECRETE_KEY y quitamos solo ''
    SECRET_KEY=django-insecure-v4nz=m0svz*qbp$wb)g**o&gi!s&b1n4sa0+j5ok+o=p=5z=3#

=> configuramos la variable SECRET_KEY
    SECRET_KEY=os.enviroment.get('SECRET_KEY')
    
=> copiamos DEBUG=TRUE al archivo .env 
    configuramos la variable DEBUG=TRUE
        DEBUG=os.enviroment.get('DEBUR')


=> configuracion de templates
    importamos import os 

    import os
    'DIRS': [os.path.join(BASE_DIR, 'templates')],


=> creamos nuestro modelo en el archivo models.py de nuestra app blog
    





=> en nuestra app blog en el archivo views.py creamos nuestra vista en clases


=> dentro de la app blog creamos nuestra un archivo con el nombre urls.py
    configuramos nuestra urls
    from django.urls import path, include
    from .views import *

    urlpatterns = [
        path('inicio/', HomeView.as_view(), name="inicio")
    ]


=> en el archivo urls.py esta en la carpeta settngs incluimos nuestra app blog importamos include
    from django.urls import path, include

    urlpatterns = [
        path('', include('blog.urls')),
    ]


