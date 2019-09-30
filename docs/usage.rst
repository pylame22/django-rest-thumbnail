=====
Usage
=====

To use sql_debug in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'sql_debug.apps.SqlDebugConfig',
        ...
    )

Add sql_debug's URL patterns:

.. code-block:: python

    from sql_debug import urls as sql_debug_urls


    urlpatterns = [
        ...
        url(r'^', include(sql_debug_urls)),
        ...
    ]
