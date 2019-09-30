=============================
sql_debug
=============================


Requirements
-------------
sorl-thumbnail
django-cleanup

Installation
-------------

Install rest_thumbnail:

    pip install django-rest-thumbnail

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'rest_thumbnail',
        ...
    ]

Add sql_debug's URL patterns:

.. code-block:: python

    from rest_thumbnail import urls as rest_thumbnail_urls


    urlpatterns = [
        ...
        path('thumbnail/', include(rest_thumbnail_urls)),
        ...
    ]


Run migrate::

    python manage.py migrate

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
