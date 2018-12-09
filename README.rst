===========
django-base
===========

``django-base`` is a working Django project that can be used as a starting
point for new projects. It includes a couple of default applications that
should prove useful for most new projects, as well as some tools to ensure
code quality/standards are maintained going forwards.


Quick-start
===========

1. Clone or fork this project.

2. Install requirements: ``pip install -r requirements-dev.txt``.

3. Copy ``project/settings/local.example.py`` to ``project/settings/local.py``.

4. (Optional) Edit your ``project/local_settings.py`` as desired.

5. Set: ``DJANGO_SETTINGS_MODULE=project.settings.local``.

6. Make migrations: ``python manage.py makemigrations simple_authentication``.

7. Apply migrations: ``python manage.py migrate``.

8. Run the development server: ``python manage.py runserver``.


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
