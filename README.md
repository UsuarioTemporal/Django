# **Django**

## **¿Qué es Django ?**

- Es un framework web programado en python , gratuito y libre.
- Su nombre viene dado en alusión al guitarrista de jazz Django Reinhardt

## **¿Quienes los usan?**

- Mozilla
- Pinterest
- Instagram
- Bitbucket
- El diario de Washington Times

> Promueve la filosofía del desarrollo ágil y extensible, aplicado al principio DRY (don't repeat yourself)

### **Algunas de sus caracteristicas más importantes son :**

- un sistema basado en componentes reutilizables , las 'apps'
- Un mapeador ORM(Object Relational Mapping) para manejar registros de la BD
- Un panel de adminstrador extensible ya creado
- Un potente sistema de platillas extensible con herencia
- Usa el patron de arquitectura MVT (ModelViewTemplate)

## **Creando entornos virtuales de python con miniconda**

```sh
    $ conda create -n py372 python=3.7.2
```

```sh
	$ pip install virtualenv
	$ mkdir trydjango
	$ cd trydjango
	$ virtualenv -p python3 .
	$ source bin/activate
	( trydjango ) $ pip install django==2.2.7
	( trydjango ) $ django-admin
	( trydjango ) $ mkdir src
	( trydjango ) $ cd src && django-admin startproject trydjango && python manage.py runserver
```

```sh
 	$ python3 manage.py makemigrations
	$ python3 manage.py migrate
	$ # python3 manage.py shell
	$ # python3 manage.py createsuperuser
	$ # python3 manage.py startapp nombre-del-componente
```


```sh
	(trydjango) ➜  trydjango git:(master) ✗ python3 manage.py shell
	Python 3.6.8 (default, Oct  7 2019, 12:59:55) 
	[GCC 8.3.0] on linux
	Type "help", "copyright", "credits" or "license" for more information.
	(InteractiveConsole)
	>>> from products.models import Product
	>>> Product.objects.all()
	<QuerySet []>
	>>> Product.objects.create(title='New Product',description='something',price='12.4')
	<Product: Product object (1)>
	>>>
```
