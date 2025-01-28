Curso de Django, main repo https://github.com/jjpereirab/django_t1

Clase 16 - Configuración del Proyectos en Django
------------------------------------------------
1. crear nuevo entorno virtual para nuevo proyecto
2. se instala django
	pip install Django
3. verificacion de extensiones django y python para vscode
4. crear nuevo proyecto, con .gitignore de https://www.toptal.com/developers/gitignore/
5. se hace 'pip freeze' para obtener la version de django, se agrega a un requirements.txt
	Django==5.1.5
6. se instala ipython pip install ipython y se mira su version (inicio del output luego del comando de instalacion) para agregar a requirements-dev.txt


Clase 17 - Creación del Modelo para la Aplicación 'Products' en Django
----------------------------------------------------------------------
1. nueva app "productos", agregarla a los settings del proyecto
2. crear modelo Producto dentro de la app productos, nuevo parametro verbose_name en los atributos del modelo (ver)
3. se verifica el interpretador de python en vscode, luego ctrl+p y >reload_window para tomar cambios (interesante, poco importante)
4. *** ver todos los atributos de este modelo creado (ver)


Clase 18 - Cómo Crear Migraciones de Datos en Django
----------------------------------------------------
1. al hacer ./manage.py makemigrations aparece un error debido a la falta de un paquete necesario para usar models.ImageField
	pip install Pillow
2. makemigrations y migrate
3. asegurar que la nueva dependencia esta agregada en requirements.txt

* recurso, Pillow administra caracteristicas sobre las imagenes
	https://pillow.readthedocs.io/en/stable/
	
tarea: views y urls para el nuevo modelo 
'''''
1. agregar productos.urls a path de <project_folder>/urls.py, como productos/
2. crear instancia del modelo Producto en ./manage.py shell
3. crear view que use parametro id para Producto. La vista es una funcion que retorna HttpResponse
	Producto.objects.get(id=kwargs['id'])
4. crear url en <app_folder>/urls.py y llamar la vista del producto, usando <int:id> en path
	path('<int:id>', vista_producto)
5. se verifica el funcionamiento de 
	http://127.0.0.1:8000/productos/1
	
