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


Clase 19 - Creación de la Aplicación 'Products' con Formularios en Django
--------------------------------------------------------------
1. crear forms.py en <app_folder>/
2. crear un formulario para el modelo Producto, en forma de clase, y se le dan los mismos atributos que al modelo (ver)
3. crear metodo .guardar() en el formulario (ver)
4. crear vista (ver 2 atributos) para el formulario, y url para la vista. Crear un html con una linea de texto simple (ver)
5. verificar url /productos/agregar
6. para renderizar el formulario en la vista, basta agregar al html
	{{ form.as_p }}
7. volver a verificar url /productos/agregar, se ve el formulario, el cual al inspeccionarlo tiene los campos del formulario dentro de etiquetas <p>
8. agregar boton de tipo -submit- al html
	<button type="submit">Agregar</button>
9. volver a verificar url /productos/agregar, se ve el boton. El html hasta este momento solo tiene 3 lineas
	Aca aparecera el formulario para agregar un producto
	{{ form.as_p }}
	<button type="submit">Agregar</button>
10. poner "accion" al formulario en el html, por medio del nombre asignado a la url. Al mismo tiempo, la accion debe tener el metodo "post" (ver html)
11. al intentar agregar un producto a traves del formulario del html, se tiene un error Forbidden 403
	CSRF verification failed. Request aborted.
12. agregar tag al html con csrf_token 
	{% csrf_token %}
13. al intentar de nuevo agregar el producto en html, nuevo error
	No URL to redirect to. Provide a success_url.
14. agregar nuevo atributo -success_url- a la vista (ver)
15. al intentar de nuevo agregar el producto en html, funciona, pero para que el producto se agregue efectivamente a la db es necesario usar el metodo .guardar() en la vista (ver)
16. la vista hasta ahora tenia 3 lineas de 3 atributos. Se le agregan las siguientes 3: 
    def form_valid(self, form):
        form.guardar()
        return super().form_valid(form)
17. se verifica en la dbshell como existe el nuevo producto

tarea: agregar producto con foto, y hacer que el success_url lleve a un listado de productos
'''''
a. se crean vistas de clase cbv y funcion fbv para listar los productos en un template. Se crea html, se agregan urls
b. nuevos html, view y url cumplen el mismo objetivo que a. pero el html acomoda en una tabla y tiene el atributo "foto". Como poner la foto? 


Clase 20 - Integracion de TailwindCSS en Django
-----------------------------------------------
Se muestra como hacer la anterior tarea con herramientas de html para una vista tipo marketplace del listado de productos. Aun sin mostrar como administrar imagenes en el proyecto


Clase 21 - Django Admin
-----------------------
- introduccion al admin
- modelos en el admin
- static() en urls para administracion de imagenes

1. crear superuser para el admin de django
	./manage.py create superuser
2. ya se puede acceder desde http://127.0.0.1:8000/admin/
3. crear clase en <app-folder>/admin.py para agregar los modelos al admin. Basta con las siguientes lineas para ver "Productos" en el admin
	from .models import Producto
	class ProductoAdmin(admin.ModelAdmin):
	    modelo = Producto
	admin.site.register(Producto, ProductoAdmin)
4. para agregar campos al modelo en admin, poner el siguiente atributo en la clase
	list_display = ['nombre', 'precio', "disponible"]
5. para agregar campos de busqueda
	search_fields = ['nombre', 'precio']
6. se prueba poner imagen a un producto en el admin, lo cual crea automaticamente la carpeta
	<project-folder>/logos
dentro de esta carpeta está la imagen subida. La url (*) ahora muestra un "link roto" a la imagen
	http://127.0.0.1:8000/productos/lista_cbv_tabla
7. en <project-folder>/urls.py agregar
	from django.conf.urls.static import static
	from django.conf import settings
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
con esto ya se muestra la imagen en la url (*)
	
tarea: agregar campo "fecha de creacion" al modelo Producto, mostrar en listado y admin
'''''
1. agregar atributo al modelo
	creacion = models.DateTimeField(auto_now_add=True, verbose_name="creacion")
2. makemigrations y migrate
3. modificar la tabla en el html (*) y la clase en admin.py
	list_display = ['nombre', 'precio', "disponible", "creacion"]  
	readonly_fields = ('creacion',) 
el atributo -readonly_fields- es una tupla, y es necesario para ver el campo dentro del admin en /change/


Clase 22 - Manejo de Sesiones en Django
---------------------------------------
- administracion de usuarios
- bastante estilo para html (no implementado) 

1. crear nueva aplicacion
	./manage.py startapp usuarios
2. agregar a INSTALLED_APPS en settings.py
3. crear usuarios/templates/usuarios/login.html
4. crear usuarios/urls.py y poner alli unas urls asociadas a views built-in en django para usuarios (ver)
	from django.contrib.auth.views import LoginView
	urlpatterns = [
    		path('login/', LoginView.as_view(template_name='usuarios/login.html'), name='login'),
	]
5. en urlpatterns de <project_folder>/urls.py poner 
	path("usuarios/", include("usuarios.urls"))
6. la url ya funciona. Poner lo siguiente en el html mostrara un formulario de login
	<form action="" >
	    {{ form.as_p }}
	    <button type="submit">Loguearse</button>
	</form>
5. para que funcione el login, el html debe ser
	<form action="" method="POST">
	    {% csrf_token %}
	    {{ form.as_p }}
	    <button type="submit">Loguearse</button>
	</form>
y agregar en <project_folder>/settings.py al final
	LOGIN_REDIRECT_URL = "url_name_lista_productos_cbv_tabla"
donde se usa el "name" de la url a la que se desea llegar luego del login

tarea: implementar LogoutView
'''''
la implementacion de LogoutView consiste en crear una url que ejecule la accion, no necesariamente requiere un template (html). La opcion de deslogueo puede ser mostrada siempre que el usuario este logueado i.e. user.is_authenticated = True

1. en usuarios/urls.py, importar LogoutView desde el mismo origen de LoginView y crear url de logout
	path('logout/', LogoutView.as_view(), name='logout')
2. crear <main_folder>/templates/base.html y agregar BASE_DIR / "templates" a TEMPLATES/DIRS en settings.py (ver html, ver settings)
3. en particular, /templates/base.html tiene en su header
        {% if user.is_authenticated %}
            <form method="post" action="{% url 'logout' %}">
                {% csrf_token %}
                Hola, {{ user.username }}! <button type="submit"> Log out </button>
            </form>               
        {% else %}
            Hola, anónimo! <a href="/usuarios/login/"> <button type="submit"> Loguearse </button> </a>
        {% endif %}
las condiciones de logueo y deslogueo segun user.is_authenticated

extra:
1. se estableció /templates/base.html como home, agregando a //urls.py
	path("", TemplateView.as_view(template_name='base.html'), name='base'),
2. se extendio el layout desde base.html para /productos/lista_cbv_tabla
3. algunas modificaciones de estilo en .../usuarios/login.html
