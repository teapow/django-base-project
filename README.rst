===========
django-base
===========

``django-base`` is a working Django project that can be used as a starting
point for new projects. It includes a couple of default applications that
should prove useful for most new projects, as well as some tools to ensure
code quality/standards are maintained going forwards.


Quick-start
===========

1. Fork this project.

2. Install requirements: ``pip install -r requirements.txt``.

3. Copy ``project/local_settings.example.py`` to ``project/local_settings.py``.

4. (Optional) Edit your ``project/local_settings.py`` as desired.

5. Make migrations: ``python manage.py makemigrations simple_authentication``.

6. Apply migrations: ``python manage.py migrate``.

7. Run the development server: ``python manage.py runserver``.


Included tools
==============

The following applications are installed by default:

* ``django-simple-authentication`` (`teapow/django-simple-authentication`_)

* ``django-simple-pages`` (`teapow/django-simple-pages`_)

.. _teapow/django-simple-authentication: http://github.com/teapow/django-simple-authentication
.. _teapow/django-simple-pages: http://github.com/teapow/django-simple-pages


To help guarantee coding standards going forward, the following tools are
installed:

* ``flake8``

  * ``flake8-docstrings``

  * ``flake8-per-file-ignores``

  * ``flake8-quotes``


Usage with Docker
=================

Included within this repo is a production-ready ``docker-compose.yaml`` file
that runs the Django project (via uWSGI), served by NGINX with a PostgreSQL
database backend.

The ``docker-entrypoint.sh`` script will perform the application's setup
automatically by:

1. Generating any migrations for the pre-installed apps (specifically
   ``django-simple-authentication``), if necessary.

2. Applying any outstanding database migrations.

3. Gathering ``static`` files.


Building the image
------------------

Build with the following command from the root of the project:

``docker build . --tag=<repo>/<image>:latest``


Running within Docker
---------------------

Modify ``docker-compose.yaml``, changing the ``services > uwsgi > image``
value to match the name of the image that you built above. Then, from the
root of the project, run ``docker-compose up -d``.

You should then be able to access the application at http://localhost/admin.


Creating a superuser
--------------------

You can create a superuser account with the following command (assuming you've
run the application using ``docker-compose``):

``docker exec -it site_uwsgi_1 python manage.py createsuperuser``

Then, enter your email and set a password as prompted.


Credits / Useful resources
==========================

The Docker setup within this project was written taking inspiration from the
following sources:

* https://wsvincent.com/django-docker-postgresql/

* https://ruddra.com/2016/11/02/serve-static-files-by-nginx-from-django-using-docker/

* https://github.com/dockerfiles/django-uwsgi-nginx
