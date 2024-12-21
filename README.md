# Proyecto Gimnasio

Este proyecto es una aplicación web de un gimnasio. Permite acceder a información sobre actividades, socios y sucursales, y realizar operaciones como buscar y agregar socios, actividades y sucursales.

## Funcionalidades
- Página de Inicio: 
Visualiza la información principal del gimnasio.

- Socios
Ver eventos exclusivos para socios.
Agregar un socio y su información.
Buscar un socio por nombre o dni.

Ejemplo busqueda de socios ya inscriptos: ingresar alguno de los siguientes nombres: Ruben, Gabriela, Marina, Adriana, Esteban.

- Actividades
Ver las actividades disponibles en el gimnasio.
Buscar actividades por nombre.
Agregar actividades para el gimnasio.

Ejemplo de busqueda de actividades: ingresar alguno de los siguientes nombres: zumba, crosfitt, flexibilidad, funcional. boxeo, pilates, hiit

- Sucursales
Ver las sucursales del gimnasio por nombre y dirección.
Buscar sucursales por nombre.
Agregar nuevas sucursales.

Ejemplo de busqueda de sucursales: nueva cordoba, cerro, general paz, barrio jardin

## Gestión de Usuarios
- Creación de un superusuario para la gestión de la plataforma.
- Configuración de un grupo de administradores para controlar los permisos de los usuarios.

## Tecnologías Usadas
- Python 3.10.5
- Django 4.2
- Pipenv

## Instalación
- Clonación del repositorio
git clone  <URL del repositorio>

- Creación del entorno virtual
1. Instala pipenv si no lo tienes instalado: pip install pipenv
2. Crea un entorno virtual con Python 3.10.5: pipenv --python 3.10.5
3. Activa el entorno virtual: pipenv shell
4. Instala las dependencias del proyecto: pipenv install -r requirements.txt

## Servidor
python manage.py runserver
El proyecto estará disponible en http://127.0.0.1:8000.

link del video Youtube https://youtu.be/FLVnMAG_Ans?si=SYEKY9LCl92SWaf8


